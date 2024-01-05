

## Introduction

This app is a Django application that allows users to create their companies and perform CRUD operations with them in the database. There are 2 main entities in this app: Users and Companies. Each user is created through the Admin panel of the Django application and they have the typical user related fields such as: email, username, first name, last name etc. and they can be checked in the auth_user table in the database. Each company can be created by a user, they are saved in the database table myapp_company with the following fields: id, company_name, description, number_of_employees, owner. 


## Starting the app

To start the app run the following commands in terminal:

1. Clone the repository to your local machine.

2. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```
   And the application will be started on localhost:8000.

3. Run this command in terminal 
    ```
       python manage.py runserver 
    ```

## Local Testing

#### Creating a user

To create a new user open the Admin panel at http://127.0.0.1:8000/admin/ and login as the superuser to be able to manage the application. You can login using username: ina and password: ina ( they are the same for easier use). Then you can create the user.


#### Creating a token

As all endpoints are required to be protected, the user should generate a token, so that the app knows it's an authorized user trying to reach it. In order to generate the token I used Postman to send a request for token generation with the following format:


- **Method:** GET
- **URL:** `http://localhost:8000/api/token/`
- **Headers:**
  - `Content-Type: application/json`
- **Body:**
  ```json
    {
    "username": "ina2",
    "password": "ina12345"   
    }


After the token is provided you can use it to perform other actions on the app.

#### Creating a company

To create a new company you can simply send a POST request with the following format:

- **Method:** POST
- **URL:** `http://localhost:8000/api1/companies/`
- **Headers:**
  - `Content-Type: application/json`
  - `Authorization: Token 78235364761565108b81701a85cbdd2f8d5ed9d2`  <!-- provided token -->
- **Body:**
  ```json
  {
    "company_name": "Krofnite of Hrom",
    "description": "Bakery",
    "number_of_employees": 33
  }

With this the company will be created in the database and the user can access the information about it. Also, the user will receive a confirmation email if they provided an email when creating it in the Admin Panel. 

The other functionalities of the assignment can be tested in similar format.

#### Listing all companies for logged in user

To get all the companies registered by a user - less than 5, you can perform a GET request in this format:


- **Method:** GET
- **URL:** `http://localhost:8000/api1/companies/`
- **Headers:**
  - `Content-Type: application/json`
  - `Authorization: Token 78235364761565108b81701a85cbdd2f8d5ed9d2`  <!-- provided token -->


```json
{
    "count": 5,
    "next": "http://localhost:8000/api1/companies/?page=2",
    "previous": null,
    "results": [
        {
            "company_name": "Your Company Name",
            "description": "Your Company Description",
            "number_of_employees": 10
        },
        {
            "company_name": "Ina Inc",
            "description": "Best company in the world!!!",
            "number_of_employees": 1800
        },
        {
            "company_name": "Neon Nirvana",
            "description": "LED decorations",
            "number_of_employees": 2
        }
    ]
}
```

You can notice that there are only 3 companies per page, I set this low number on purpose, because the maximum number of companies created per user is 5, and this way it's easier to see how the pagination works. 



## Database

For the database I used a PostgresSQL database hosted on ElephantSQL. It can be accessed with the following connection:

- **Name:** Name of the set up, for example ElephantSQL
- **Host name/address:** `castor.db.elephantsql.com`
- **Port:** `5432`
- **Maintenance DB:** `vzovsduz`
- **Username:** `vzovsduz`
- **Password:** `kNW9PQOAXSGCDnfLOixMQ2mFqNvxtJHm`

Please keep in mind that because this is a free service and not very stable, I experienced that from time to time it lost connection. In that case you need to wait for a few seconds and try to perform the request again. Also keep in mind that when you connect to the server, there are quite a lot of databases and you have to scroll down to the one named vzovsduz.


