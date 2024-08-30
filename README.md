# API Documentation

This API is built using Django and Django Rest Framework. Below are the available endpoints:

## User Endpoints
- **GET /users/**: List all users
- **GET /users/{id}/**: Retrieve a user by ID

## Menu Endpoints
- **GET /menu/**: List all menu items
- **GET /menu/{id}/**: Retrieve a menu item by ID
- **POST /menu-items/**: Create a new menu item
- **GET /menu-items/**: List all menu items
- **GET /menu-items/{id}/**: Retrieve a menu item by ID
- **PUT /menu-items/{id}/**: Update a menu item
- **DELETE /menu-items/{id}/**: Delete a menu item

## Booking Endpoints
- **GET /booking/**: List all bookings
- **POST /booking/**: Create a new booking
- **GET /booking/{id}/**: Retrieve a booking by ID
- **PUT /booking/{id}/**: Update a booking
- **DELETE /booking/{id}/**: Delete a booking

## Authentication
- **POST /api-token-auth/**: Obtain an authentication token

## Other Endpoints
- **GET /message/**: Test endpoint

## Note
Replace `{id}` with the actual ID of the resource you want to retrieve or update.
