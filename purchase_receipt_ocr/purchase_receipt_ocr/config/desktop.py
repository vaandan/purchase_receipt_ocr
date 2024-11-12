# desktop.py
from frappe import _

def get_data():
    return [
        {
            "module_name": "Purchase Receipt OCR",
            "color": "grey",
            "icon": "octicon octicon-file-directory",
            "type": "module",
            "label": _("Purchase Receipt OCR"),
            "category": "Modules",  # Added category
            "description": _("OCR functionality for Purchase Receipts"),  # Added description
            "onboard_present": True,  # Added for onboarding
            "items": [  # Added items for quick access
                {
                    "type": "doctype",
                    "name": "Purchase Receipt",
                    "label": _("Purchase Receipt"),
                    "description": _("Process Purchase Receipts with OCR"),
                    "onboard": True,
                },
                # You can add more items here as needed
                # {
                #     "type": "page",
                #     "name": "capture-image",
                #     "label": _("Capture Image"),
                #     "description": _("Capture and process images for OCR"),
                # },
            ]
        }
    ]