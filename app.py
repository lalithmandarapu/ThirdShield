from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
import os
from risk_engine import assess_risk
from models import db, VendorRequest

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vendors.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

def create_tables():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_vendor', methods=['POST'])
def submit_vendor():
    data = request.form
    file = request.files['document']
    filename = secure_filename(file.filename)
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(path)

    with open(path, 'r', errors='ignore') as f:
        content = f.read()
    risk_score = assess_risk(content)

    vendor = VendorRequest(
        employee_name=data['employee_name'],
        vendor_name=data['vendor_name'],
        description=data['description'],
        upload_path=path,
        risk_score=risk_score
    )
    db.session.add(vendor)
    db.session.commit()

    return jsonify({"message": "Vendor submitted successfully", "risk_score": risk_score})

@app.route('/dashboard')
def dashboard():
    vendors = VendorRequest.query.all()
    return render_template('dashboard.html', vendors=vendors)

@app.route('/review_vendor/<int:vendor_id>', methods=['POST'])
def review_vendor(vendor_id):
    vendor = VendorRequest.query.get(vendor_id)
    vendor.status = request.form['status']
    vendor.comments = request.form['comments']
    db.session.commit()
    return jsonify({"message": "Vendor reviewed"})

if __name__ == '__main__':
    app.run(debug=True)
