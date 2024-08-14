Project Overview
This project demonstrates the implementation of a custom middleware in a Django application. Middleware allows you to process requests and responses globally across the application, 
enabling functionalities such as logging, authentication, and request modification.

File Structure
1. middleware/mid.py
Purpose:
This file contains the DemoMiddleware class.
The middleware processes incoming HTTP requests before they reach the view and processes outgoing HTTP responses before they are sent back to the client.
It can be customized to perform actions like logging request details, modifying request/response objects, or implementing custom authentication.
2. project1/settings.py
Purpose:
Configures the Django project settings, including:
Middleware: Registers the DemoMiddleware class here to ensure it is applied to all requests.

MIDDLEWARE = [
'middleware.mid.DemoMiddleware' #that is file path
......
]
