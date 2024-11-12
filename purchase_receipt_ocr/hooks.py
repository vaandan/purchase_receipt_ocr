# hooks.py (at root level: /purchase_receipt_ocr/hooks.py)
app_name = "purchase_receipt_ocr"
app_title = "Purchase Receipt OCR"
app_publisher = "LMCP"
app_description = "OCR functionality for Purchase Receipts"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "support@logic-motive.com"
app_license = "MIT"

# Includes in <head>
# ------------------
# app_include_css = "/assets/purchase_receipt_ocr/css/purchase_receipt_ocr.css"
app_include_js = "/assets/purchase_receipt_ocr/js/purchase_receipt_button.js"

# DocTypes
# --------
# Include js in doctype views
doctype_js = {
    "Purchase Receipt": "public/js/purchase_receipt_button.js"
}

# Custom page routes
# -----------------
page_js = {
    "capture_image": "public/js/purchase_receipt_button.js"
}

# Website
# -------
# website_route_rules = [
#     {"from_route": "/capture-image", "to_route": "pages/capture_image"},
# ]

# Installation
# -----------
after_install = "purchase_receipt_ocr.setup.install.after_install"

# Fixtures
# --------
# fixtures = [
#     {
#         "doctype": "Custom Field",
#         "filters": [
#             ["name", "in", [
#                 "Purchase Receipt-ocr_image",
#                 "Purchase Receipt-ocr_text"
#             ]]
#         ]
#     }
# ]

# Document Events
# --------------
# doc_events = {
#     "Purchase Receipt": {
#         "after_save": "purchase_receipt_ocr.purchase_receipt_ocr.doctype.purchase_receipt.purchase_receipt.process_ocr"
#     }
# }

# Scheduler Events
# ---------------
# scheduler_events = {
#     "daily": [
#         "purchase_receipt_ocr.tasks.daily"
#     ]
# }

# Permissions
# ----------
# permission_query_conditions = {
#     "Purchase Receipt": "purchase_receipt_ocr.permissions.get_permission_query_conditions"
# }