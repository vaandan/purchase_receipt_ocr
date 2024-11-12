from setuptools import setup, find_packages

setup(
    name="purchase_receipt_ocr",
    version="0.0.1",
    description="OCR functionality for Purchase Receipts",
    author="LMCP",
    author_email="support@logic-motive.com",
    packages=find_packages(),
    install_requires=[
        "frappe",
        "pytesseract",
        "opencv-python",
        "Pillow"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Frappe",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.6"
)