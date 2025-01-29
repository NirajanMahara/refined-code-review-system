from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ReviewRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    repo_url = db.Column(db.String(200), nullable=False)
    template = db.Column(db.String(50), default='basic')  # Simple template system

class CodeMetric(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    review_id = db.Column(db.Integer, db.ForeignKey('review_request.id'))
    lint_errors = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default=db.func.now())