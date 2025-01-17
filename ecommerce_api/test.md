1 login test

 url: http://127.0.0.1:8000/api/token/

{
  "username": "becky",
  "password": "becky@123"
}


2 List Categories

url: http://127.0.0.1:8000/api/categories/



2.1 Create a New Category

url: http://127.0.0.1:8000/api/categories/

{
  "name": "Electronics"
}

3 List Products

url: http://127.0.0.1:8000/api/products/


3.1 Create a New Product

url: http://127.0.0.1:8000/api/products/


{
  "name": "Laptop",
  "description": "High-performance laptop",
  "price": 1200.50,
  "category_id": 1,
  "stock_quantity": 10,
  "image_url": "http://example.com/image.jpg"
}
