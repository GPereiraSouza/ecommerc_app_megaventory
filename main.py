from src.megaventory_api import MegaventoryAPI
from src.entities.products import Product
from src.entities.client_supplier import SupplierClient
from src.entities.inventory_location import InventoryLocation
import logging

def main():
    api_key = "b539f4374f8b5962@m152705"
    api = MegaventoryAPI(api_key)
    
    # Example of product update
    product1 = Product("1112223", "Puma sneakers", 79.99, 35.99)
    product2 = Product("1112299", "New Balance sneakers", 89.99, 39.99)
    
    products = [product1.to_dict(), product2.to_dict()]
    
    for product in products:
        response = api.update_product(product)
        if response and response['ResponseStatus']['ErrorCode'] == '500':
            logging.info(f"Product {product['ProductSKU']} already exists. Skipping insert.")
    

    # Example of client/supplier creation
    client_supplier1 = SupplierClient(
        "Achilles",
        "achilles@exampletest.com",
        "Example 5, Athens",
        "9876543210",
        "Client"
    )
    client_supplier2 = SupplierClient(
        "Helen",
        "helen@exampletest.com",
        "Example 25, Athens",
        "9876543233",
        "Supplier"
    )
    clients_suppliers = [client_supplier1.to_dict(), client_supplier2.to_dict()]
    for client_supplier in clients_suppliers:
        response = api.update_supplier_client(client_supplier)
        if response and response['ResponseStatus']['ErrorCode'] == '500':
            logging.info(f"Supplier/Client {client_supplier['SupplierClientName']} already exists. Skipping insert.")

    # Example of inventory location update
    inventory_location1 = InventoryLocation(
        "1",
        "Demo",
        "Demo Project Location",
        "Example 25, Athens"
    )
    response = api.update_inventory_location(inventory_location1.to_dict())
    if response and response['ResponseStatus']['ErrorCode'] == '500':
        logging.info(f"Inventory location {inventory_location1.abbreviation} already exists. Skipping insert.")

    # Example of purchase order creation
    purchase_order = {
        "PurchaseOrderSupplierName": "Helen",
        "PurchaseOrderStatus": "Pending",
        "PurchaseOrderDetails": [
            {
                "PurchaseOrderRowProductSKU": "1112299",
                "PurchaseOrderRowQuantity": 20,
                "PurchaseOrderRowUnitPriceWithoutTaxOrDiscount": 39.99
            }
        ]
    }
    response = api.create_purchase_order(purchase_order)
    if response and response['ResponseStatus']['ErrorCode'] == '403':
        logging.error("The orders module is not enabled. Cannot create purchase order.")

    # Example of sales order creation
    sales_order = {
        "SalesOrderInventoryLocationID": "1",
        "SalesOrderClientName": "Achilles",
        "SalesOrderClientId": 0,
        "SalesOrderStatus": "Verified",
        "SalesOrderDetails": [
            {
                "SalesOrderRowProductSKU": "1112223",
                "SalesOrderRowQuantity": 10,
                "SalesOrderRowUnitPriceWithoutTaxOrDiscount": 79.99
            }
        ]
    }
    response = api.create_sales_order(sales_order)
    if response and response['ResponseStatus']['ErrorCode'] == '403':
        logging.error("The orders module is not enabled. Cannot create sales order.")
        
    # Example of updating inventory stock at inventory location
    inventory_stock_update = {
        "mvProductStockUpdateList": [
            {
                "ProductSKU": "1112223",
                "ProductQuantity": 15,
                "InventoryLocationID": 3409
            },
            {
                "ProductSKU": "1112299",
                "ProductQuantity": 30,
                "InventoryLocationID": 3409
            }
        ]
    }
    response = api.update_inventory_location_stock(inventory_stock_update)
    if response and response['ResponseStatus']['ErrorCode'] == '500':
        logging.info(f"Inventory location stock update for products already exists. Skipping insert.")

if __name__ == "__main__":
    main()
