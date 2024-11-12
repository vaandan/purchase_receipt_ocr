frappe.ui.form.on('Purchase Receipt', {
    refresh(frm) {
        frm.add_custom_button(__('OCR Scan'), function() {
            openCameraModal(frm);
        });
    }
});

function openCameraModal(frm) {
    let d = new frappe.ui.Dialog({
        title: 'Capture Material Label Image',
        fields: [
            { fieldtype: 'HTML', fieldname: 'camera_view', label: 'Camera View' }
        ],
        primary_action_label: 'Capture',
        primary_action() {
            captureImage(frm, d);
        }
    });

    d.fields_dict.camera_view.$wrapper.html(`
        <video id="video" width="100%" autoplay></video>
        <canvas id="canvas" style="display:none;"></canvas>
    `);

    let video = document.getElementById('video');
    navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
        video.srcObject = stream;
    }).catch(function(error) {
        console.error("Error accessing camera: ", error);
        frappe.msgprint(__('Unable to access camera. Please check camera permissions.'));
        d.hide();
    });

    d.show();
}

function captureImage(frm, dialog) {
    let video = document.getElementById('video');
    let canvas = document.getElementById('canvas');
    let context = canvas.getContext('2d');

    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    context.drawImage(video, 0, 0, canvas.width, canvas.height);

    let imageData = canvas.toDataURL('image/png');

    let stream = video.srcObject;
    let tracks = stream.getTracks();
    tracks.forEach(track => track.stop());

    frappe.call({
        method: 'purchase_receipt_ocr.purchase_receipt_ocr.doctype.purchase_receipt.purchase_receipt.process_ocr',
        args: {
            image_data: imageData,
            receipt_name: frm.doc.name
        },
        callback: function(r) {
            if (r.message.status === "success") {
                frappe.msgprint(__('Label data has been extracted and populated successfully.'));
                frm.reload_doc();
            } else {
                frappe.msgprint(__('Error: ' + r.message.message));
            }
        }
    });

    dialog.hide();
}
