use pharmacys;

-- Example to insert more data into the table
INSERT INTO inventory (date, item_code, item_name, uom, warehouse, purchase_price, sale_price, supplier_name, batch_number, expiration_date, reorder_level, in_qty, out_qty, remarks)
VALUES 
('2024-08-25', 'A124', 'Ibuprofen 200mg Tablets', 'Box', 'Main Warehouse', 40.00, 60.00, 'XYZ Pharmaceuticals', 'B654321', '2025-07-15', 100, 200, 100, 'Initial Stock'),
('2024-08-26', 'A125', 'Amoxicillin 500mg Capsules', 'Bottle', 'Main Warehouse', 120.00, 180.00, 'HealthCare Suppliers', 'B789012', '2025-12-01', 50, 100, 20, 'Restocked'),
('2024-08-26', 'A126', 'Cough Syrup 100ml', 'Bottle', 'Main Warehouse', 25.00, 40.00, 'MedLife Inc.', 'B345678', '2024-11-30', 30, 60, 30, 'Restocked'),
('2024-08-27', 'A127', 'Vitamin C 500mg Tablets', 'Box', 'Secondary Warehouse', 35.00, 55.00, 'Nutrient Suppliers', 'B901234', '2026-01-10', 200, 300, 150, 'Initial Stock'),
('2024-08-27', 'A128', 'Antiseptic Liquid 500ml', 'Bottle', 'Secondary Warehouse', 45.00, 70.00, 'SafeMed', 'B112233', '2026-03-20', 60, 120, 60, 'Initial Stock');
