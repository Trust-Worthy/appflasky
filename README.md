# Flask Task Manager

This is a simple task management web application built with Flask, Flask-SQLAlchemy, and Flask-Scss. It allows users to create, view, update, and delete tasks. Task data is stored locally using SQLite.

## Features

- Create new tasks
- Display a list of tasks (ordered by creation time)
- Edit task content
- Delete tasks
- SCSS support using Flask-Scss
- UTC-based timestamps with `datetime.now(timezone.utc)`
- Clean and minimal structure for easy maintenance

## Requirements

- Python 3.8+
- pip

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/appflasky.git
```

### Install dependencies
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt
```

### Project Structure
```bash
.
├── app.py               # Main application file
├── templates/
│   ├── index.html       # Home page template
│   └── edit.html        # Edit task page template
├── static/
│   └── scss/            # SCSS stylesheets
├── database.db          # SQLite database (created automatically)
├── requirements.txt     # Python dependencies
└── README.md
```
