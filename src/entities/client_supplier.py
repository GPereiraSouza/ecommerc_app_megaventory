class SupplierClient:
    def __init__(self, name, email, address, phone, type_):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        self.type = type_

    def to_dict(self):
        return {
            "SupplierClientName": self.name,
            "SupplierClientEmail": self.email,
            "SupplierClientShippingAddress1": self.address,
            "SupplierClientPhone1": self.phone,
            "SupplierClientType": self.type
        }
