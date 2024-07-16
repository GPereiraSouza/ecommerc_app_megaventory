from src.megaventory_api import MegaventoryAPI

import logging

def main():
    api_key = "b539f4374f8b5962@m152705"
    api = MegaventoryAPI(api_key)

    # Produtos
    products = [
        {
            "ProductSKU": "1112223",
            "ProductDescription": "Puma sneakers",
            "ProductSellingPrice": 79.99,
            "ProductPurchasePrice": 35.99
        },
        {
            "ProductSKU": "1112299",
            "ProductDescription": "New Balance sneakers",
            "ProductSellingPrice": 89.99,
            "ProductPurchasePrice": 39.99
        }
    ]
    for product in products:
        response = api.update_product(product)
        if response and response['ResponseStatus']['ErrorCode'] == '500':
            logging.info(f"Product {product['ProductSKU']} already exists. Skipping insert.")

    # Clientes e Fornecedores
    clients_suppliers = [
        {
            "SupplierClientName": "Achilles",
            "SupplierClientEmail": "achilles@exampletest.com",
            "SupplierClientShippingAddress1": "Example 5, Athens",
            "SupplierClientPhone1": "9876543210",
            "SupplierClientType": "Client"
        },
        {
            "SupplierClientName": "Helen",
            "SupplierClientEmail": "helen@exampletest.com",
            "SupplierClientShippingAddress1": "Example 6, Athens",
            "SupplierClientPhone1": "9876543233",
            "SupplierClientType": "Supplier"
        }
    ]
    for client_supplier in clients_suppliers:
        response = api.update_supplier_client(client_supplier)
        if response and response['ResponseStatus']['ErrorCode'] == '500':
            logging.info(f"Supplier/Client {client_supplier['SupplierClientName']} already exists. Skipping insert.")

    # Local de Inventário
    inventory_location = {
        "InventoryLocationAbbreviation": "Demo",
        "InventoryLocationName": "Demo Project Location",
        "InventoryLocationAddress": "Example 25, Athens"
    }
    api.update_inventory_location(inventory_location)

    # Pedido de Compra
    purchase_order = {
        "PurchaseOrderSupplierID": 6,  # ID do fornecedor Helen
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
        logging.error("O módulo de pedidos não está habilitado. Não é possível criar o pedido de compra.")

    # Pedido de Venda
    sales_order = {
        "SalesOrderClientID": 5,  # ID do cliente Achilles
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
        logging.error("O módulo de pedidos não está habilitado. Não é possível criar o pedido de venda.")

    # Atualização de Estoque no Inventário
    inventory_updates = [
        {
            "ProductSKU": "1112223",
            "InventoryLocationID": 1,  # ID do local de inventário
            "ProductStockQuantity": 15
        },
        {
            "ProductSKU": "1112299",
            "InventoryLocationID": 1,  # ID do local de inventário
            "ProductStockQuantity": 30
        }
    ]

    for update in inventory_updates:
        response = api.update_inventory_stock(update['ProductSKU'], update['InventoryLocationID'], update['ProductStockQuantity'])
        if response and response['ResponseStatus']['ErrorCode'] == '400':
            logging.error(f"Falha ao atualizar o estoque para {update['ProductSKU']}.")

if __name__ == "__main__":
    main()
