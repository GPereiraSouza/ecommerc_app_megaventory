import requests
import logging

class MegaventoryAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.megaventory.com/v2017a"
        logging.basicConfig(level=logging.INFO)
    
    def post(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, json=data)
        
        if response.status_code != 200:
            logging.error(f"HTTP error occurred: {response.status_code} {response.reason}")
            logging.error(f"Response: {response.text}")
            return None
        
        response_json = response.json()
        if response_json['ResponseStatus']['ErrorCode'] != '0':
            logging.error(f"API error occurred: {response_json['ResponseStatus']['Message']}")
        else:
            logging.info(f"Successfully updated entity at {endpoint}")
            logging.info(f"Response: {response_json}")
        
        return response_json

    def update_product(self, product):
        if isinstance(product, dict):
            data = {
                "APIKEY": self.api_key,
                "mvProduct": product,
                "mvRecordAction": "Insert"
            }
            return self.post("Product/ProductUpdate", data)
        else:
            logging.error("Invalid product format. Expected dictionary.")
            return None

    def update_supplier_client(self, supplier_client):
        if isinstance(supplier_client, dict):
            data = {
                "APIKEY": self.api_key,
                "mvSupplierClient": supplier_client,
                "mvRecordAction": "Insert"
            }
            return self.post("SupplierClient/SupplierClientUpdate", data)
        else:
            logging.error("Invalid supplier/client format. Expected dictionary.")
            return None

    def update_inventory_location(self, inventory_location):
        if isinstance(inventory_location, dict):
            data = {
                "APIKEY": self.api_key,
                "mvInventoryLocation": inventory_location,
                "mvRecordAction": "Insert"
            }
            return self.post("InventoryLocation/InventoryLocationUpdate", data)
        else:
            logging.error("Invalid inventory location format. Expected dictionary.")
            return None

    def update_inventory_location_stock(self, inventory_location_stock):
        if isinstance(inventory_location_stock, dict):
            data = {
                "APIKEY": self.api_key,
                "mvProductStockAlertsAndSublocationsList": inventory_location_stock,
                "mvRecordAction": "Insert"
            }
            return self.post("InventoryLocationStock/InventoryLocationStockUpdate", data)
        else:
            logging.error("Invalid inventory location stock format. Expected dictionary.")
            return None
        
    def create_purchase_order(self, purchase_order):
        if isinstance(purchase_order, dict):
            data = {
                "APIKEY": self.api_key,
                "mvPurchaseOrder": purchase_order,
                "mvRecordAction": "Insert"
            }
            return self.post("PurchaseOrder/PurchaseOrderUpdate", data)
        else:
            logging.error("Invalid purchase order format. Expected dictionary.")
            return None

    def create_sales_order(self, sales_order):
        if isinstance(sales_order, dict):
            data = {
                "APIKEY": self.api_key,
                "mvSalesOrder": sales_order,
                "mvRecordAction": "Insert"
            }
            return self.post("SalesOrder/SalesOrderUpdate", data)
        else:
            logging.error("Invalid sales order format. Expected dictionary.")
            return None
