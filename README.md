# Enterprise CRUD API with FastAPI and MongoDB

This is a simple enterprise-level CRUD API built with FastAPI and MongoDB. The API allows for basic CRUD operations on items in a MongoDB database. The application uses Pydantic for data validation and typing, and it features logging, configuration management, and error handling.

## Features

- **Create** an item
- **Read** an item by ID
- **Update** an item by ID
- **Delete** an item by ID
- Logging setup
- Configuration management using environment variables
- Exception handling for robustness

## Requirements

- Python 3.12.2+
- MongoDB
- FastAPI
- Pydantic (v2.x)
- Motor (async MongoDB driver)
- Uvicorn (ASGI server)
- `pydantic-settings` (for configuration)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/enterprise-crud-api.git
    cd enterprise-crud-api
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:

    Create a `.env` file in the root directory of the project with the following content:

    ```env
    MONGO_URI=mongodb://localhost:27017
    DATABASE_NAME=your_database_name
    ```

5. Run the application:

    ```bash
    uvicorn app.main:app --reload
    ```

    The application will be available at `http://127.0.0.1:8000`.

## API Endpoints

### Create Item

- **URL**: `/api/v1/items/`
- **Method**: `POST`
- **Request Payload**:
    ```json
    {
        "name": "Laptop",
        "description": "A high-performance laptop for gaming and work.",
        "price": 1500.00,
        "in_stock": true
    }
    ```
- **Response**: `201 Created`, returns the created item with an ID.

### Read Item

- **URL**: `/api/v1/items/{item_id}`
- **Method**: `GET`
- **URL Params**:
    - `item_id`: The ID of the item to retrieve.
- **Response**: `200 OK`, returns the item data.

### Update Item

- **URL**: `/api/v1/items/{item_id}`
- **Method**: `PUT`
- **URL Params**:
    - `item_id`: The ID of the item to update.
- **Request Payload**:
    ```json
    {
        "name": "Gaming Laptop",
        "price": 1600.00
    }
    ```
- **Response**: `200 OK`, returns the updated item.

### Delete Item

- **URL**: `/api/v1/items/{item_id}`
- **Method**: `DELETE`
- **URL Params**:
    - `item_id`: The ID of the item to delete.
- **Response**: `200 OK`, returns the deleted item.

## Testing

To run the tests, use the following command:

```bash
pytest
