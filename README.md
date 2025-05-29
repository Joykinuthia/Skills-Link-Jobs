# Skills-Link-Jobs CLI Application

## Overview
The Skills-Link-Jobs CLI application is a Python-based command-line tool designed to manage users, jobs, and applications using SQLAlchemy ORM. It provides functionalities for creating, viewing, and deleting records in a SQLite database.

## Features
- User Management:
  - Create users with hashed passwords.
  - View all users.
  - Delete users.
- Job Management:
  - Create jobs with detailed information.
  - View all jobs.
  - Delete jobs.
- Application Management:
  - Apply to jobs.
  - View all applications.
  - Delete applications.

## Prerequisites
- Python 3.8 or higher.
- Pipenv for managing dependencies.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Skills-Link-Jobs
   ```
2. Install dependencies:
   ```bash
   pipenv install
   ```

## Running the Application
1. Activate the virtual environment:
   ```bash
   pipenv shell
   ```
2. Run the application:
   ```bash
   python main.py
   ```

## Database Setup
The application uses a SQLite database (`skills_link_jobs.db`) located in the project root. The database schema is automatically initialized when the application starts.

## Usage
### User Management
- **Create User**: Enter username, email, password, user type, and skills.
- **View All Users**: Displays all users in a tabular format.
- **Delete User**: Deletes a user by ID.

### Job Management
- **Create Job**: Enter employer ID, job title, category, salary, and requirements.
- **View All Jobs**: Displays all jobs in a tabular format.
- **Delete Job**: Deletes a job by ID.

### Application Management
- **Apply to Job**: Enter job ID, seeker ID, and cover letter.
- **View All Applications**: Displays all applications in a tabular format.
- **Delete Application**: Deletes an application by ID.

## Development
### Project Structure
- `main.py`: Entry point for the application.
- `lib/`: Contains the core logic and modules.
  - `cli/`: CLI menus for user, job, and application management.
  - `database/`: Database setup and initialization.
  - `models/`: SQLAlchemy models for users, jobs, and applications.
  - `utils/`: Utility functions and validators.

### Adding Dependencies
To add new dependencies, update the `Pipfile` and run:
```bash
pipenv install
```
# Expanded README.md with examples of CLI interactions and explanations of SQLAlchemy ORM and bcrypt.
## Examples of CLI Interactions
### User Management
#### Create User
```bash
Enter username: Johnson Kamau
Enter email: johnson@example.com
Enter password: johnsonmay@123
Enter user type (seeker/employer): seeker
Enter skills: Python, SQL
User created successfully.
```
#### View All Users
```bash
+------+-----------+----------------------+--------+----------------+
|   ID | Username  | Email                | Type   | Skills         |
+======+===========+======================+========+================+
|    1 | Johnson Kamau  | johnson@example.com | seeker | Python, SQL    |
+------+-----------+----------------------+--------+----------------+
```
### Job Management
#### Create Job
```bash
Enter employer ID: 1
Enter employer name: ABC Corp
Enter job category: Tech
Enter job title: Python Developer
Enter job requirements: Python, SQLAlchemy, Team player
Enter salary: 120000
Job created successfully.
```
#### View All Jobs
```bash
+------+---------------+------------------+------------+----------+----------------------------------+----------+
|   ID | Employer ID   | Title            | Category   | Salary   | Requirements                      | Filled   |
+======+===============+==================+============+==========+==================================+==========+
|    1 | 1             | Python Developer | Tech       | 120000   | Python, SQLAlchemy, Team player  | False    |
+------+---------------+------------------+------------+----------+----------------------------------+----------+
```
### Application Management
#### Apply to Job
```bash
Enter job ID: 1
Enter seeker ID: 1
Enter resume: Resume.pdf
Enter cover letter (optional): Cover letter attached
Application created successfully.
```
#### View All Applications
```bash
+------+--------+-----------+----------------------+
|   ID | Job ID | Seeker ID | Cover Letter         |
+======+========+===========+======================+
|    1 | 1      | 1         | Cover letter attached|
+------+--------+-----------+----------------------+
```
## SQLAlchemy ORM and bcrypt
### SQLAlchemy ORM
SQLAlchemy is used to define models and manage database operations. It provides an abstraction layer for interacting with the SQLite database.
### bcrypt
bcrypt is used for secure password hashing, ensuring that user passwords are stored safely in the database.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Support
For issues or feature requests, please open an issue in the repository.

## Contributors
- Joyrose Kinuthia

## Acknowledgments
- SQLAlchemy for ORM.
- Pipenv for dependency management.
- Tabulate for CLI table formatting.
