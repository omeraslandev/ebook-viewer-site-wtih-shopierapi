# Do You Want Your Shopier Customers to Read Your E-Book on Your Website? 🚀

This documentation provides information on how to run a web application built using Flask and covers the core functionalities of your project. I will guide you step-by-step based on my own experience. You can also see the live version of the project at [stayhard.com.tr](http://stayhard.com.tr).

## 🎯 Project Goal

This project aims to create a simple web application that allows users to purchase or read online books. Users log in via an email address, view books, and then buy or read them. Below, I will explain step-by-step how to run and customize the project. The core features of the project include:

  - User Login
  - Email Verification
  - Book Viewing
  - Book Purchase or Reading
  - Theme and Style Options

## 🚀 How to Run?

You can run and publish your project online by following these steps:

### Step 1️⃣: Create a Virtual Machine on Amazon EC2

Create a Windows virtual machine (Instance) on Amazon Web Services (AWS). This virtual machine will be used to host your project.

### Step 2️⃣: Connect to the Virtual Machine

Use an RDP (Remote Desktop Protocol) client to access the virtual machine. Also, decrypt the password in the .PEM file to gain access.

### Step 3️⃣: Upload Project Files

Copy the project from your local computer to your virtual machine. This step ensures that the files containing your project's source code are transferred to your virtual machine.

### Step 4️⃣: Python Installation

Install the latest version of Python on your virtual machine. This step is necessary for your Flask application to run.

### Step 5️⃣: Navigate to the Project Directory

Open the command prompt on your virtual machine and navigate to your project directory. For example:

```
cd ProjectPath
```

### Step 6️⃣: Run the Application

Use the following command to start your Flask application:

```
python main.py
```

This command will run your project on your local server, making it accessible via a specific IP address and port.

### Step 7️⃣: Provide Hosting Service

To expose your Flask application running on the virtual machine to the internet, use the IP address of your virtual machine. This will be a temporary URL for your project. For example, it might be an IP address like `http://51.20.1.29/`.

### Step 8️⃣: Use a Custom Domain

To achieve a more professional appearance, purchase a domain from hosting.com.tr or a similar domain provider. Then, you can run your project on a custom domain by pointing it to your virtual machine's IP address.

### Step 9️⃣: Customizations

Follow these steps to personalize the project:

#### 1\. Shopier API Keys

  - Replace `"Bearer API_KEY"` in the `main.py` file with your own **Shopier API key**.

#### 2\. SMTP Settings

  - Replace `"YOUR_GMAIL"` and `"YOUR_PASSWORD_OF_GMAIL"` with your own **Gmail address and password**. This is used for email verification processes.

#### 3\. Product IDs

  - In the `get_emails` function, replace `"YOUR_PRODUCT_ID"` with the **product IDs** you created in your Shopier account.

### Step 🔟: Go Live with the Project

Your project is now live\! You can use it by visiting your project's URL in your browser. For example, [stayhard.com.tr](http://stayhard.com.tr).

## 🔍 Main Functions of the Code

The main functions of the Python code within the project are as follows:

### `main.py` Functions

1.  **User Login and Session Management**

      - The `User` class is used to represent users.
      - The `load_user` function is used to load users by their IDs.
      - Session management is provided with `login_manager`.

2.  **Fetching Email Addresses from API**

      - The `get_emails` function retrieves customer email addresses from the API and stores them in the `customer_emails` list.

3.  **Home Page (`/`)**

      - The `main` function represents the home page and returns the `main.html` template.

4.  **Email Verification Process**

      - The `create_verification_code` function generates a random verification code.
      - The `send_code_to_mail` function sends the verification code to the user via email.

5.  **Book Viewing and Redirection**

      - The `login` function allows the user to log in to view books.
      - The `check_verification` function checks the user's verification code and redirects them to the books.

6.  **Book Pages**

      - The `firstbook` and `secondbook` functions allow the user to view the books.

### HTML Files Functions

1.  **`main.html`**: Contains the main page design. It presents a card design for the user to view books.

2.  **`login.html`**: Presents a form where the user can enter their email address.

3.  **`verification.html`**: Presents a form to enter the verification code.

4.  **`firstbook.html` and `secondbook.html`**: Contain the design of the book pages. They provide a view for users to read the books.

5.  **`error_page.html`**: Presents a page design showing errors and warnings.

## 🧰 Technologies and Libraries

  - **Flask**: A Python framework used for developing web applications.
  - **Flask-Login**: A Flask extension used for user session management.
  - **requests**: A Python module used for making API calls.
  - **smtplib and email**: Python modules used for email verification processes.
  - **HTML and CSS**: Basic web technologies used to create the user interface.

## 📁 File Directory

The project file directory is as follows:

```
- Bonus Project
    - static
        favicon.ico
        main.css
        pdf.css
        style.css
        pdf.js
        pdf.worker.js
    - templates
        error_page.html
        firstbook.html
        login.html
        main.html
        secondbook.html
        verification.html
    main.py
    README.md
```

## 📂 File Descriptions

  - `main.py`: The main file of the Flask application. It includes user login, email verification, book viewing, and redirection processes.

  - `static`: The folder containing static files such as style sheets and favicon.

  - `templates`: The folder containing the HTML templates for your Flask application.

## 🧑‍💻 Python Code Functions

The Python code within the project has the following functions:

  - User login and session management.
  - Email verification and email sending processes.
  - Viewing books using API.
  - User's book purchase or reading processes.
