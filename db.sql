CREATE TABLE IF NOT EXISTS `digikala_products`(
    `product_title` TEXT NOT NULL,
    `product_link` TEXT NOT NULL,
    `product_category` TEXT NOT NULL,
    `product_model` TEXT,
    `product_warranty` TEXT,
    `product_colors` TEXT,
    `product_overview` TEXT,
    `product_general_specifications` TEXT,
    `product_details_box` TEXT
) CHARACTER set utf8;