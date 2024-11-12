FROM frappe/erpnext-worker:version-15

# Install Tesseract and other dependencies
RUN apt-get update && \
    apt-get install -y tesseract-ocr && \
    pip install pytesseract Pillow && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . /app
RUN pip install -r /app/requirements.txt