# Django-POS-System

A Point of Sale web app for businesses built with Python and Django for learning purposes.

<a><img src="https://user-images.githubusercontent.com/95726794/212497770-a3e241e7-0c77-4573-9d22-8f0ae813e958.png" width="70%" heigth="70%"></a>
<br></br>
<a><img src="https://user-images.githubusercontent.com/95726794/212497784-80a48617-759c-4415-aa1c-4591b9892c3d.png" width="70%" heigth="70%"></a>

## Table of Contents:
- [Features](#features)
- [Screenshots](#screenshots)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Run it locally](#run-it-locally)
- [Contributing](#contributing)
- [License](#license)

## Screenshots
[Click Here](screenshots/README.md)

## Features
- Login Page with User authentication
- Dashboard Page with statistics and graphs
- DataTables with print, copy, CSV, and PDF buttons
- Categories and Products Management
- Clients Management
- Sales Management


## Tech Stack

- Frontend: HTML, CSS, JavaScript, Bootstrap, SweetAlert, DataTables
- Backend: Django, Python, Ajax, SQLite 

## Installation

### Prerequisites
- [Python 3.x](https://www.python.org/downloads/)
- [pip package manager](https://pip.pypa.io/en/stable/installation/)
- [git](https://git-scm.com/downloads)
  
#### Browser Compatibility Notice: Firefox NOT Supported ‼
#### Please Use Chrome or Edge Browsers ‼
    
  1. Clone or download the repository:

  ` git clone https://github.com/betofleitass/django-POS-system`

  2. Go to the project directory

  ` cd django_pos`

  3. Install dependencies:  
  ` pip install -r requirements.txt`
  
  5.  Update pip and setuptools  
  ` python -m pip install --upgrade pip setuptools`  
  
  6. Install MSYS2:
     
  ` Before seeing the video on how to install step-by-step progress.`
  
  ` MSYS2 Install Tutorials:`
  
  - Link: (https://www.youtube.com/watch?v=rUJFYOCbuDg&t=844s)
    
  - Link: (https://www.msys2.org/)

  7. Install GTK to create the PDF files:
     
   [Official documentation](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation)  
  
  8. Windows Users (IMPORTANT)‼:

     Only Windows 10/11 64-bit is supported ‼

     GTX3 2021 Installation and Automatically Path environment you need Recommended Install GTX3 2021: 
     Link: (https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases/download/2021-04-29/gtk3-runtime-3.24.29-2021-04-29-ts-win64.exe)

     you write in the terminal this ( weasyprint --info ) and you see no error and error any problems.
     Link: (https://www.cnblogs.com/melloliana/p/16098061.html)

     After installing GTK, you must add it to your system's Path environment variable. Follow these steps:

      - Assuming you installed GTK at:
        `C:\Program Files\GTK3-Runtime Win64\bin`  
        This will be the new variable that you need to add to Path.
        
      - Refer to this tutorial for detailed instructions on adding to the Path environment variable:
        [Tutorial add to the Path environment variable](https://helpdeskgeek.com/windows-10/add-windows-path-environment-variable/)  
    
      - If you encounter an error such as "cannot load library," refer to this documentation for troubleshooting:
        [Missing Library Error](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#missing-library)  
  
  10. Restart your computer: After you complete the steps above, you will need to restart your computer for the changes to take effect properly. ‼
  
## Run it locally
After restarting your computer

1. Go to the project directory: `cd django_point_of_sale`


2. Go to the django_pos folder: `cd django_pos`

3. Make database migrations:  
  `python manage.py makemigrations` and 
  `python manage.py migrate`

4. Create superuser `python manage.py createsuperuser` 
  
   with the following data, or with the data you prefer:
    - username: admin
    - password: admin
    - email: admin@admin

   and You can log in:
   - Name: zafir
   - Password: Zafir*123

6. Run the server: `python manage.py runserver`

7. Open a browser and go to: `http://127.0.0.1:8000/`

8. Login with your superuser credentials.
    

## Contributing

Contributions are always welcome!

- Fork this repository;

- Create a branch with your feature: `git checkout -b my-feature`;

- Commit your changes: `git commit -m "feat: my new feature"`;

- Push to your branch: `git push origin my-feature`.

## Authors

- [@zafirabdullah](https://github.com/Zafir547)

##  License

This project is under [MIT License.](https://choosealicense.com/licenses/mit/)

[Back to top ⬆️](#Django-POS-System)
