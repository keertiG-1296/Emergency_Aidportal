from flask import Blueprint, render_template, request, redirect, url_for
from models import BloodDonation, BloodRequest

# Create blueprint
blood = Blueprint('blood', __name__)

@blood.route('/blood_donation', methods=['GET', 'POST'])
def donate_blood():
    """
    Handle blood donation - both form display and submission
    """
    if request.method == 'POST':
        name = request.form.get('name')
        blood_group = request.form.get('blood_group')
        email = request.form.get('email')
        phone = request.form.get('phone')
        city = request.form.get('city')
        
        # Use model to save blood donation
        success = BloodDonation.create(name, blood_group, email, phone, city)
        
        if success:
            print("Form Data Received:", request.form)
            print("Redirecting to:", url_for('general.thank_you'))
            return redirect(url_for('general.thank_you'))
        else:
            print("Error in Blood Donation Form Submission")
            return "An error occurred. Please try again later."
    
    return render_template('blood_donation.html')

@blood.route('/blood_request', methods=['POST'])
def request_blood():
    """
    Handle blood request submission
    """
    patient_name = request.form.get('patient_name')
    blood_group = request.form.get('blood_group')
    contact = request.form.get('contact')
    hospital = request.form.get('hospital')
    
    # Use model to save blood request
    success = BloodRequest.create(patient_name, blood_group, contact, hospital)
    
    if success:
        print("Form Data Received:", request.form)
        print("Redirecting to:", url_for('general.thank_you'))
        return redirect(url_for('general.thank_you'))
    else:
        print("Error in Blood Request Form Submission")
        return "An error occurred. Please try again later."
