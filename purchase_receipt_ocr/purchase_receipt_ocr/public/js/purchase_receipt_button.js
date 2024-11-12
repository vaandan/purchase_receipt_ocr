frappe.ui.form.on('Purchase Receipt', {
    refresh(frm) {
        // Avoid duplicate buttons
        if (!frm.custom_buttons['OCR Scan']) {
            frm.add_custom_button(__('OCR Scan'), function() {
                openCameraModal(frm);
            });
        }
    }
});

function openCameraModal(frm) {
    let d = new frappe.ui.Dialog({
        title: 'Capture Material Label Image',
        fields: [
            { 
                fieldtype: 'HTML', 
                fieldname: 'camera_view', 
                label: 'Camera View' 
            }
        ],
        primary_action_label: 'Capture',
        primary_action() {
            captureImage(frm, d);
        },
        secondary_action_label: 'Cancel',
        onhide: () => {
            // Stop camera stream when dialog is closed
            let video = document.getElementById('video');
            if (video && video.srcObject) {
                video.srcObject.getTracks().forEach(track => track.stop());
            }
        }
    });

    d.fields_dict.camera_view.$wrapper.html(`
        <div class="camera-container">
            <video id="video" width="100%" autoplay></video>
            <canvas id="canvas" style="display:none;"></canvas>
            <div class="camera-overlay"></div>
        </div>
        <style>
            .camera-container { position: relative; }
            .camera-overlay {
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                border: 2px solid #4CAF50;
                pointer-events: none;
            }
        </style>
    `);

    initializeCamera(d);
}

function initializeCamera(dialog) {
    let video = document.getElementById('video');
    
    navigator.mediaDevices.getUserMedia({ 
        video: { 
            facingMode: 'environment',
            width: { ideal: 1920 },
            height: { ideal: 1080 }
        } 
    }).then(function(stream) {
        video.srcObject = stream;
    }).catch(function(error) {
        console.error("Camera error:", error);
        frappe.msgprint({
            title: __('Camera Error'),
            indicator: 'red',
            message: __('Unable to access camera. Please check camera permissions.')
        });
        dialog.hide();
    });
}

function captureImage(frm, dialog) {
    try {
        let video = document.getElementById('video');
        let canvas = document.getElementById('canvas');
        let context = canvas.getContext('2d');

        // Set canvas dimensions to match video
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        
        // Capture frame
        context.drawImage(video, 0, 0, canvas.width, canvas.height);
        let imageData = canvas.toDataURL('image/png');

        // Stop camera stream
        let stream = video.srcObject;
        if (stream) {
            stream.getTracks().forEach(track => track.stop());
        }

        // Show loading state
        frappe.show_progress(__('Processing'), 0.5, 1, 'Please wait');

        frappe.call({
            method: 'purchase_receipt_ocr.purchase_receipt_ocr.doctype.purchase_receipt.purchase_receipt.process_ocr',
            args: {
                image_data: imageData,
                receipt_name: frm.doc.name
            },
            callback: function(r) {
                frappe.hide_progress();
                if (r.message.status === "success") {
                    frappe.show_alert({
                        message: __('Label data extracted successfully'),
                        indicator: 'green'
                    });
                    frm.reload_doc();
                } else {
                    frappe.show_alert({
                        message: __('Error: ' + r.message.message),
                        indicator: 'red'
                    });
                }
            },
            error: function(r) {
                frappe.hide_progress();
                frappe.show_alert({
                    message: __('Failed to process image'),
                    indicator: 'red'
                });
            }
        });

        dialog.hide();
    } catch (error) {
        console.error("Capture error:", error);
        frappe.msgprint({
            title: __('Capture Error'),
            indicator: 'red',
            message: __('Failed to capture image: ' + error.message)
        });
    }
}