from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class Admin(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password_hash = db.Column(db.String(128))

class VendorRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_name = db.Column(db.String(120))
    vendor_name = db.Column(db.String(120))
    description = db.Column(db.Text)
    upload_path = db.Column(db.String(300))
    status = db.Column(db.String(50), default='Pending')
    risk_score = db.Column(db.Integer)
    comments = db.Column(db.Text)
    risk_level = db.Column(db.String(20))
    risk_description = db.Column(db.Text)
    prevention = db.Column(db.Text)

class AuditLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    action = db.Column(db.String(100))
    actor = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
