app_name = "purchase_receipt_ocr"
app_title = "Purchase Receipt OCR"
app_publisher = "LMCP"
app_description = "OCR functionality for Purchase Receipts"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "support@logic-motive.com"
app_license = "MIT"

# Include JS files in the Purchase Receipt DocType
doctype_js = {
    "Purchase Receipt": "public/js/purchase_receipt_button.js"
}

# Add custom page templates for HTML

page_js = {"capture_image": "public/js/purchase_receipt_button.js"}


# # Scheduler events (if required)
# scheduler_events = {
#     "daily": [
#         "purchase_receipt_ocr.tasks.daily_task"
#     ]
# }

# Define any custom installations
def after_install():
    pass