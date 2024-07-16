class InventoryLocation:
    def __init__(self, id, abbreviation, name, address):
        self.id = id
        self.abbreviation = abbreviation
        self.name = name
        self.address = address

    def to_dict(self):
        return {
            "InventoryLocationID": self.id,
            "InventoryLocationAbbreviation": self.abbreviation,
            "InventoryLocationName": self.name,
            "InventoryLocationAddress": self.address
        }
