# hooks.py
app_name = "purchase_receipt_ocr"
app_title = "Purchase Receipt OCR"
app_publisher = "LMCP"
app_description = "OCR functionality for Purchase Receipts"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_license = "MIT"

# Include the JS for Purchase Receipt form
doctype_js = {
    "Purchase Receipt": "public/js/purchase_receipt_button.js"
}
app_include_js = "/assets/purchase_receipt_ocr/js/purchase_receipt_button.js"
# app_include_css = "/assets/purchase_receipt_ocr/css/your_styles.css"  # If any CSS exists

# Include JS files in the Purchase Receipt DocType
doctype_js = {
    "Purchase Receipt": "public/js/purchase_receipt_button.js"
}

# Add custom page templates for HTML

page_js = {"capture_image": "public/js/purchase_receipt_button.js"}
