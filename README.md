# Ecommerce Application with Megaventory Integration

This project showcases integration with the Megaventory API for managing products, clients, inventory locations, purchase orders, and sales orders within an ecommerce environment.

## Dependencies

Ensure you have the following dependencies installed:

- Python 3.x
- Requests library (`pip install requests`)

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/ecommerce_app_megaventory.git
   cd ecommerce_app_megaventory

2. **API Key Setup**

   Obtain your Megaventory API key from [Megaventory Dashboard](https://www.megaventory.com/login.aspx).
   
   Replace YOUR_API_KEY_HERE in main.py with your actual API key:
   
   ```python
   api_key = "YOUR_API_KEY_HERE"  # Replace with your Megaventory API key

3. **Run the Application**

   Execute the main script to see examples of API calls:
   
   ```bash
   python main.py
    
##Project Structure

The project directory structure is organized as follows:

```graphql
ecommerce_app_megaventory/
│
├── main.py         # Entry point of the application where examples of API interactions are demonstrated.
├── README.md       # This file provides project overview, setup instructions, and structure.
└── src/
    ├── entities/
    │   ├── products.py           # Module for defining product entity.
    │   ├── client_supplier.py    # Module for defining client and supplier entities.
    │   └── inventory_location.py   # Module for defining inventory location entity.
    └── megaventory_api.py       # Module containing the MegaventoryAPI class for API interactions.


```vbnet

## Additional Notes

- Make sure to replace placeholders like `YOUR_API_KEY_HERE` with actual values as per the instructions provided.
- For further details on each module's functionality and usage, refer to the respective source files in the `src/` directory.
