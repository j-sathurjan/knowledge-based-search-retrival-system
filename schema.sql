CREATE DATABASE document_db;

USE document_db;

CREATE TABLE documents (
    id INT AUTO_INCREMENT PRIMARY KEY,
    report_name VARCHAR(255) NOT NULL,
    report_type VARCHAR(50),
    additional_notes TEXT,
    pages INT,
    pdf_location VARCHAR(255)
);
