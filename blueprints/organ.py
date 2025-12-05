from flask import Blueprint, render_template, request, redirect, url_for
from models import OrganDonation, OrganRequest

# Create blueprint
organ = Blueprint('organ', __name__)

@organ.route('/organ_donation', methods=['GET', 'POST'])
def donate_organ():
    """
    Handle organ donation - both form display and submission
    """
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        city = request.form.get('city')
        organ_type = request.form.get('organs')
        
        # Use model to save organ donation
        success = OrganDonation.create(name, organ_type, email, phone, city)
        
        if success:
            print("Form Data Received:", request.form)
            print("Redirecting to:", url_for('general.thank_you'))
            return redirect(url_for('general.thank_you'))
        else:
            print("Error in Organ Donation Form Submission")
            return "An error occurred. Please try again later."
    
    return render_template('organ_donation.html')

@organ.route('/organ_request', methods=['POST'])
def request_organ():
    """
    Handle organ request submission
    """
    patient_name = request.form.get('patient_name')
    organ_needed = request.form.get('organ_needed')
    contact = request.form.get('contact')
    hospital = request.form.get('hospital')
    
    # Use model to save organ request
    success = OrganRequest.create(patient_name, organ_needed, contact, hospital)
    
    if success:
        print("Form Data Received:", request.form)
        print("Redirecting to:", url_for('general.thank_you'))
        return redirect(url_for('general.thank_you'))
    else:
        print("Error in Organ Request Form Submission")
        return "An error occurred. Please try again later."
