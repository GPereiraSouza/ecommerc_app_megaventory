class Product:
    def __init__(self, sku, description, selling_price, purchase_price):
        self.sku = sku
        self.description = description
        self.selling_price = selling_price
        self.purchase_price = purchase_price

    def to_dict(self):
        return {
            "ProductSKU": self.sku,
            "ProductDescription": self.description,
            "ProductSellingPrice": self.selling_price,
            "ProductPurchasePrice": self.purchase_price
        }
