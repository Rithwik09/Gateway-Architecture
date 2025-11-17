api-gateway-wars/
├── README.md
├── Makefile
├── .env
├── docker-compose.yml
├── compose.override.yml # optional: local dev overrides
├── services/
│ ├── user/
│ ├── app/
│ ├── __init__.py
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ ├── schemas.py
│ └── routes/
│ │    ├── __init__.py
│ │    └── users.py
│ ├── product/
│ │ ├── app/
│ │ │ ├── __init__.py
│ │ │ └── main.py
│ │ ├── requirements.txt
│ │ └── Dockerfile
│ └── order/
│ ├── app/
│ │ ├── __init__.py
│ │ └── main.py
│ ├── requirements.txt
│ └── Dockerfile
├── tests/
│ └── k6/
│ └── smoke.js # placeholder for Week 5
└── ops/
├── grafana/ # placeholders for Week 5
└── prometheus/


API list 
user: 
| Method   | Endpoint           | Description             |
| :------- | :----------------- | :---------------------- |
| `GET`    | `/health`          | Health check            |
| `GET`    | `/info`            | Service info + metadata |
| `GET`    | `/users`           | List all users          |
| `GET`    | `/users/{user_id}` | Get user by ID          |
| `POST`   | `/users`           | Create new user         |
| `PUT`    | `/users/{user_id}` | Update user info        |
| `DELETE` | `/users/{user_id}` | Delete a user           |


product :
| Method   | Endpoint                 | Description         |
| :------- | :----------------------- | :------------------ |
| `GET`    | `/health`                | Health check        |
| `GET`    | `/info`                  | Service info        |
| `GET`    | `/products`              | List all products   |
| `GET`    | `/products/{product_id}` | Get product details |
| `POST`   | `/products`              | Add a new product   |
| `PUT`    | `/products/{product_id}` | Update product info |
| `DELETE` | `/products/{product_id}` | Delete product      |

order:
| Method   | Endpoint             | Description                                        |
| :------- | :------------------- | :------------------------------------------------- |
| `GET`    | `/health`            | Health check                                       |
| `GET`    | `/info`              | Service info                                       |
| `GET`    | `/orders`            | List all orders                                    |
| `GET`    | `/orders/{order_id}` | Get specific order                                 |
| `POST`   | `/orders`            | Create new order *(calls User & Product services)* |
| `PUT`    | `/orders/{order_id}` | Update an order                                    |
| `DELETE` | `/orders/{order_id}` | Delete order                                       |
