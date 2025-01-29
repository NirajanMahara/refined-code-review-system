from flask import Flask, render_template, request, redirect
from models import db, ReviewRequest, CodeMetric
import subprocess
import os
from flask import jsonify
import hmac
import hashlib

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviews.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_review():
    # Get form data
    repo_url = request.form['repo_url']
    template = request.form.get('template', 'basic')

    # Save to database
    new_review = ReviewRequest(repo_url=repo_url, template=template)
    db.session.add(new_review)
    db.session.commit()

    # Run pylint analysis
    result = subprocess.run(['pylint', repo_url], capture_output=True)
    error_count = result.stdout.decode().count('error')

    # Save metrics
    metric = CodeMetric(review_id=new_review.id, lint_errors=error_count)
    db.session.add(metric)
    db.session.commit()

    return redirect('/metrics')

@app.route('/metrics')
def show_metrics():
    metrics = CodeMetric.query.all()
    return render_template('metrics.html', metrics=metrics)


@app.route('/github-webhook', methods=['POST'])
def handle_github_webhook():
    # Verify HMAC signature
    signature = request.headers.get('X-Hub-Signature-256', '')
    secret = os.getenv('GITHUB_WEBHOOK_SECRET').encode()
    digest = hmac.new(secret, request.data, hashlib.sha256).hexdigest()
    
    if not hmac.compare_digest(f'sha256={digest}', signature):
        return jsonify({"error": "Invalid signature"}), 403

    # Handle pull request event
    payload = request.json
    if payload.get('pull_request'):
        repo_url = payload['repository']['clone_url']
        subprocess.Popen(['pylint', repo_url])  # Run in background
        
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)