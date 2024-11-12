# desktop.py
from frappe import _

def get_data():
    return [
        {
            "module_name": "Purchase Receipt OCR",
            "color": "grey",
            "icon": "octicon octicon-file-directory",
            "type": "module",
            "label": _("Purchase Receipt OCR")
        }
    ]
