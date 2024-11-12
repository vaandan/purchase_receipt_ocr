from setuptools import setup, find_packages

setup(
    name="purchase_receipt_ocr",
    version="0.0.1",
    description="OCR functionality for Purchase Receipts",
    author="LMCP",
    author_email="support@logic-motive.com",
    packages=find_packages(),
    install_requires=[
        "pytesseract",
        "Pillow"
    ],
    
)
