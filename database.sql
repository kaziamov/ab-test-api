CREATE TABLE devices (
    device VARCHAR(255) PRIMARY KEY,
    created_at TIMESTAMP
);

ALTER TABLE devices
ADD COLUMN button_color VARCHAR(7);

ALTER TABLE devices
ADD COLUMN price INTEGER;