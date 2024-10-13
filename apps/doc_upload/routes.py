from flask import Blueprint, render_template, request, redirect, url_for
import os
import PyPDF2
from database import db
from . import upload_bp

@upload_bp.route('/')
def index():
    return render_template('doc_upload/upload.html')

@upload_bp.route('/upload', methods=['POST'])
def upload_document():
    file = request.files['file']
    report_name = request.form['report_name']
    report_type = request.form['report_type']
    additional_notes = request.form['additional_notes']
    
    # Save the PDF file locally
    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)
    
    # Extract number of pages from PDF
    with open(file_path, 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)
        pages = len(pdf_reader.pages)
    
    # Store metadata in MySQL
    cursor = db.cursor()
    query = """INSERT INTO documents (report_name, report_type, additional_notes, pages, pdf_location)
                VALUES (%s, %s, %s, %s, %s)"""
    values = (report_name, report_type, additional_notes, pages, file_path)
    cursor.execute(query, values)
    db.commit()

    return  f"{file.filename} has been successfully uploaded."