frappe.ui.form.on('Purchase Receipt', {
    refresh: function(frm) {
        frm.add_custom_button(__('Capture Label Image'), function() {
            frappe.call({
                method: 'purchase_receipt_ocr.purchase_receipt_ocr.doctype.purchase_receipt.purchase_receipt.capture_image',
                callback: function(r) {
                    if (r.message) {
                        let captureWindow = window.open("/capture_image", "Capture Image", "width=800,height=600");
                    }
                }
            });
        });
    }
    
});
