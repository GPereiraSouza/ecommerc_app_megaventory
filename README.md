Ecommerce Application with Megaventory Integration
This project demonstrates integration with the Megaventory API for managing products, clients, inventory locations, purchase orders, and sales orders in an ecommerce setting.

Dependencies
Ensure you have the following dependencies installed:

Python 3.x
Requests library (pip install requests)
Setup Instructions
Clone the Repository

bash
Copy code
git clone https://github.com/your-username/ecommerce_app_megaventory.git
cd ecommerce_app_megaventory
Install Dependencies

Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
API Key Setup

Obtain your Megaventory API key from Megaventory Dashboard.

Replace YOUR_API_KEY_HERE in main.py with your actual API key:

python
Copy code
api_key = "YOUR_API_KEY_HERE"
Run the Application

Execute the main script to see examples of API calls:

bash
Copy code
python main.py
Project Structure
The project directory structure is organized as follows:

css
Copy code
ecommerce_app_megaventory/
│
├── main.py
├── README.md
├── requirements.txt
└── src/
    ├── entities/
    │   ├── products.py
    │   ├── client_supplier.py
    │   └── inventory_location.py
    └── megaventory_api.py
main.py: Entry point of the application where examples of API interactions are demonstrated.
src/: Directory containing source code.
entities/: Modules defining product, client/supplier, and inventory location entities.
megaventory_api.py: Module containing the MegaventoryAPI class for API interactions.
Functionality
Product Update: Updates product information using the Megaventory API.
Client/Supplier Creation: Creates new clients or suppliers.
Inventory Location Update: Manages inventory locations.
Purchase Order Creation: Creates purchase orders for products.
Sales Order Creation: Creates sales orders for products.
Notes
Ensure proper internet connectivity and valid Megaventory API key for successful API interactions.
Check the logs (logs.log) for detailed information on API requests and responses.
