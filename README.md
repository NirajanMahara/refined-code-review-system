# Refined Code Review System

A **Full Stack MVC-based code review tool** built to optimize the code review process at Refined Stack Co. This project integrates with GitHub, automates code analysis, and tracks code quality metrics.
Team members:

- **Nirajan Mahara**
- **Swetha Macha**
- **Muhammed Nihal Kunnath**

---

## Deliverables

This project fulfills the following deliverables:

1. **MVC Architecture**: Built using Flask (Python) for the backend and HTML templates for the frontend.
2. **Seamless VCS Integration**: GitHub webhooks for pull request-triggered code analysis.
3. **Automated Code Analysis**: Runs Pylint for Python code linting.
4. **Customizable Review Templates**: Supports basic and bug-fix review templates.
5. **Metrics Tracking**: Tracks and visualizes lint errors over time.

---

## Features

- **GitHub Integration**: Automatically analyzes code on pull requests.
- **Automated Linting**: Runs Pylint to detect code issues.
- **Review Templates**: Predefined templates for bug fixes and feature reviews.
- **Metrics Dashboard**: Displays lint error trends using a simple HTML table.

---

## Prerequisites

- Python 3.9+
- GitHub repository with webhook access
- [Ngrok](https://ngrok.com/) (for local testing)

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/NirajanMahara/refined-code-review-system.git
   cd refined-code-review-system
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file:
     ```env
     GITHUB_WEBHOOK_SECRET='your_secret_here'
     ```
   - Replace `your_secret_here` with a secure key (use `openssl rand -hex 32`).

---

## Running the Application

1. Start the Flask app:

   ```bash
   flask run
   ```

2. Expose your local server using ngrok:

   ```bash
   ngrok http 5000
   ```

3. Set up the GitHub webhook:

   - Go to your GitHub repository → **Settings** → **Webhooks** → **Add webhook**.
   - Set **Payload URL** to your ngrok URL + `/github-webhook` (e.g., `https://abc123.ngrok.io/github-webhook`).
   - Set **Secret** to match your `.env` file.
   - Select **Pull requests** under events.

4. Visit `http://localhost:5000` to submit a repository URL and view metrics.

---

## Project Structure

```
refined-code-review/
├── app.py                # Flask app (Controller)
├── models.py             # Database models (Model)
├── templates/            # HTML templates (View)
│   ├── index.html        # Submit review form
│   └── metrics.html      # Metrics dashboard
├── .env                  # Environment variables
└── requirements.txt      # Dependencies
```

## Deployment

1. **PythonAnywhere**:

   - Upload your project files.
   - Install dependencies in the virtual environment.
   - Configure the web app to run `app.py`.

2. **Heroku**:
   ```bash
   heroku create
   git push heroku main
   heroku config:set GITHUB_WEBHOOK_SECRET='your_secret_here'
   ```

---

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

---

## Acknowledgments

- Built with [Flask](https://flask.palletsprojects.com/).
- Inspired by Refined Stack Co.'s code review challenges.
