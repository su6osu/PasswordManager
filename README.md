# SecurePassManager: A Secure Password Storage Tool 🔒🔑

## Project Overview

The **Password Manager** is a simple yet robust tool designed to help users securely store, manage, and retrieve their passwords. This tool provides a secure and user-friendly way to handle passwords without the need to remember every single one. By leveraging encryption techniques, it ensures that sensitive information is stored safely. 🛡️

## Features ⚡

- **Secure Password Storage**: Encrypts all passwords using industry-standard encryption algorithms to ensure data safety. 🔐
- **Password Generation**: Generates strong, random passwords to enhance account security. 🔄
- **User-Friendly Interface**: Choose between a **CLI (Command Line Interface)** or a **GUI (Graphical User Interface)** built with **Tkinter** for easy interaction. 💻🖱️
- **SQLite Database**: Stores encrypted passwords in a local **SQLite** database, providing quick access while maintaining security. 🗄️
- **Search and Retrieve**: Quickly search and retrieve stored passwords with a user-friendly search functionality. 🔍
- **Password Strength Indicator**: Helps ensure that users create passwords that are both complex and secure. 🔑

## Technologies Used ⚙️

- **Python**: The core language used to develop the application. 🐍
- **SQLite**: A lightweight, serverless database used to securely store user data. 🗄️
- **Cryptography**: Provides AES encryption to ensure the safe storage of passwords. 🔐
- **Tkinter**: A built-in Python library for creating graphical user interfaces (GUI). 🖥️
- **Argparse**: A library for building the command-line interface (CLI). 🛠️

## How It Works 🧑‍💻

1. **Encryption**: When a password is entered, it is encrypted using the **cryptography** library before being stored in the **SQLite** database. The encryption ensures that even if the database is accessed, the passwords remain unreadable without the correct decryption key. 🔒
   
2. **Password Storage**: The encrypted password, along with a unique identifier (such as the website name), is stored in the SQLite database for easy access. 🗃️

3. **Password Retrieval**: Users can retrieve stored passwords either through the **CLI** or **GUI**. Once the password is needed, the program decrypts it and displays it for the user. 🔓

4. **Password Generation**: The application provides a password generator that creates random, complex passwords, ensuring users follow best practices in password security. 🔑🎲

## Installation 📥

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/su6o/SecurePassManager.git
    ```

2. Navigate to the project directory:
    ```bash
    cd SecurePassManager
    ```

3. Install the required dependencies:
    ```bash
    pip3 install -r requirements.txt
    ```

4. Run the application:
    - For CLI:
      ```bash
      python3 password_manager.py
      ```
    - For GUI:
      ```bash
      python3 password_manager_gui.py
      ```

## Usage 🚀

- **CLI**: When using the command-line interface, users can add, view, and delete passwords by typing commands. The interface is simple and allows quick interaction for users familiar with the terminal. 💻
- **GUI**: The graphical interface allows users to add, view, search, and delete passwords through a window, providing a more intuitive experience. 🖱️

## Security Considerations 🔐

- **Encryption**: All passwords are encrypted with **AES** encryption before being stored in the database. 🛡️
- **Salting**: Salts are added to passwords before encryption to ensure unique, secure encryption for each password. 🧂
- **Master Password**: A master password is used to access the database, ensuring that the user is the only one who can unlock and view stored passwords. 🔑

## Why This Tool? 💡

With the rise of **data breaches** and **password theft**, it’s important to store passwords securely. Most people rely on simple, easily guessable passwords or reuse passwords across multiple sites, which can lead to catastrophic breaches. This **Password Manager** solves these issues by creating strong, unique passwords for every site and encrypting them for safe storage. 🔒

This tool is ideal for anyone looking for a **simple, secure**, and **self-hosted** password management solution that they can trust with their sensitive information. 🔑🛡️

---

### License 📄

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details. 📜
