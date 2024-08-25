CREATE DATABASE IF NOT EXISTS pharmacys;
USE pharmacys;

CREATE TABLE inventory (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    item_code VARCHAR(50) NOT NULL,
    item_name VARCHAR(100) NOT NULL,
    uom VARCHAR(20) NOT NULL,
    warehouse VARCHAR(100) NOT NULL,
    purchase_price DECIMAL(10, 2) NOT NULL,
    sale_price DECIMAL(10, 2) NOT NULL,
    supplier_name VARCHAR(100),
    batch_number VARCHAR(50),
    expiration_date DATE,
    reorder_level INT DEFAULT 0,
    in_qty INT DEFAULT 0,
    out_qty INT DEFAULT 0,
    balance INT AS (in_qty - out_qty) STORED,
    remarks VARCHAR(255)
);
