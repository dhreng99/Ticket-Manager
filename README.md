# Ticket Manager Web Application

## Summary

The Ticket Manager is a web-based application designed to help organisations manage and track their assets efficiently. It provides a user-friendly interface for creating, updating, and viewing asset information, making it a valuable tool for IT departments, facilities management, or any team responsible for tracking assets.

## Features

- **Asset Management:** Easily create, update, and delete asset records.
- **User Roles:** Supports two user roles - admin and regular user - each with specific permissions.
- **User Authentication:** Users must register and log in to access the application.
- **Dashboard:** A clean and intuitive dashboard provides an overview of assets.
- **Responsive Design:** The application is responsive and works on various devices.

    ![image](https://github.com/dhreng99/Ticket-Manager/assets/101814652/e97197aa-faf9-4dd9-a723-cd932476a8a3)

## User Roles

- **Admin:** Administrators can perform all CRUD operations on IT assets, including creating, viewing, updating, and deleting records.
- **Regular User:** Regular users have the ability to add new IT assets and update the ones they've added.

## Dependencies

To run the Ticket Manager web application, you'll need the following dependencies:

- [Python](https://www.python.org/) (Version 3.6+)
- [Django](https://www.djangoproject.com/) (Version 3.0+)
- [SQLite](https://www.sqlite.org/) (or any other relational database)

You can install Python and the required packages using pip:

```bash
pip install -r requirements.txt
```
## Admin Login

Username - Admin

Password - Password123
=======

Password - Password123

## Database Schema

- **Asset:** Stores information about IT assets including name, description, purchase data and category.
  
            Attributes: 'id', 'name', 'description', 'purchase_date', 'category_id', 'user_id'

- **AssetCategory:** Contains asset category details.
  
            Attributes: 'id', 'name', 'description'

- **User:** Stores information about the user.

            Attributes: 'id', 'username', 'password', 'email', first_name', 'last_name', 'profile_picture', 'bio'
    
    ![image](https://github.com/dhreng99/Ticket-Manager/assets/101814652/e3e6eef6-87ac-480e-8aa4-b7c0885741c7)

## Development

Developed using the Scrum agile framework in order to efficiently manage the project, stay adaptable to changes, adhere to timelines, and ensure the delivery of a high-quality application. This included utilising GitHub projects and discussions to keep a track of tickets through the development cycle and Discussions in order to complete Sprint Retrospectives to reflect on successes and challenges. 

## Testing

The following tests were created prior to development in order to outline the requirements of the project and ensure that the main functionality worked correctly. This was done by specifying a test condition and then the required outcome from this. 
    ![image](https://github.com/dhreng99/Ticket-Manager/assets/101814652/969bc776-7c95-40b5-97d5-42b7c34f4da4)
    ![image](https://github.com/dhreng99/Ticket-Manager/assets/101814652/66b2f64e-321f-4140-b925-485df9184e0e)



