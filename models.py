from database import db

class VendorRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_name = db.Column(db.String(100))
    vendor_name = db.Column(db.String(100))
    description = db.Column(db.Text)
    upload_path = db.Column(db.String(200))
    status = db.Column(db.String(20), default="Pending")
    risk_score = db.Column(db.Integer)
    comments = db.Column(db.Text)
