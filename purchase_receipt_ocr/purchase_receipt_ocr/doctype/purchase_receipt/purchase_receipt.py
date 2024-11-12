import frappe
import base64
import re
from PIL import Image
import io
import pytesseract

@frappe.whitelist()
def process_ocr(image_data, receipt_name):
    # Decode the Base64 image data
    image_data = image_data.split(",")[1]
    image = Image.open(io.BytesIO(base64.b64decode(image_data)))
    
    # Perform OCR on the image
    ocr_text = pytesseract.image_to_string(image)
    
    # Initialize variables for Batch No, Serial No, and Qty
    batch_no = serial_no = qty = None
    
    # Parse OCR text to find relevant fields
    for line in ocr_text.splitlines():
        line = line.strip()
        
        # Check for Batch No (next to Lot No)
        if line.startswith("Lot No"):
            batch_no = line.split("Lot No")[1].replace(":", "").strip()
        
        # Check for Serial No (next to REEL No)
        elif line.startswith("REEL No"):
            serial_no = line.split("REEL No")[1].replace(":", "").strip()
        
        # Check for Qty (next to Wt (In Kgs))
        elif line.startswith("Wt (In Kgs)"):
            qty = line.split("Wt (In Kgs)")[1].replace(":", "").strip()

    # Validate extracted data and update the document
    if batch_no and serial_no and qty:
        frappe.db.set_value("Purchase Receipt", receipt_name, {
            "batch_no": batch_no,
            "serial_no": serial_no,
            "qty": qty
        })
        
        frappe.db.commit()
        return {"status": "success", "message": "Data processed successfully"}
    else:
        return {"status": "error", "message": "Failed to extract all required data"}
