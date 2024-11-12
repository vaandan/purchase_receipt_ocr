import frappe
import base64
import io
from PIL import Image
import pytesseract

@frappe.whitelist()
def process_ocr(image_data, receipt_name):
    try:
        # Decode the Base64 image data
        image_data = image_data.split(",")[1]
        image = Image.open(io.BytesIO(base64.b64decode(image_data)))
        
        # Perform OCR on the image
        ocr_text = pytesseract.image_to_string(image)
        
        # Initialize variables for Batch No, Serial No, and Qty
        batch_no = serial_no = qty = None
        
        # Parse OCR text to find relevant fields
        lines = ocr_text.splitlines()
        for line in lines:
            line = line.strip().upper()  # Normalize text
            
            # Use regex for more robust matching
            if "LOT NO" in line:
                batch_no = re.search(r'LOT NO[:\s]*(\S+)', line)
                batch_no = batch_no.group(1) if batch_no else None
                
            elif "REEL NO" in line:
                serial_no = re.search(r'REEL NO[:\s]*(\S+)', line)
                serial_no = serial_no.group(1) if serial_no else None
                
            elif "WT" in line and "KGS" in line:
                qty = re.search(r'WT.*?KGS[:\s]*(\d+\.?\d*)', line)
                qty = qty.group(1) if qty else None

        # Validate extracted data and update the document
        if all([batch_no, serial_no, qty]):
            frappe.db.set_value("Purchase Receipt", receipt_name, {
                "batch_no": batch_no,
                "serial_no": serial_no,
                "qty": float(qty)
            })
            
            frappe.db.commit()
            return {"status": "success", "message": "Data processed successfully"}
        else:
            missing_fields = []
            if not batch_no: missing_fields.append("Batch No")
            if not serial_no: missing_fields.append("Serial No")
            if not qty: missing_fields.append("Quantity")
            
            return {
                "status": "error", 
                "message": f"Failed to extract: {', '.join(missing_fields)}"
            }
            
    except Exception as e:
        frappe.log_error(f"OCR Processing Error: {str(e)}")
        return {"status": "error", "message": f"Processing error: {str(e)}"}