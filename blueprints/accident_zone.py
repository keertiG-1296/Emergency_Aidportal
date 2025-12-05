from flask import Blueprint, render_template, request, redirect, url_for
from models import AccidentReport

# Create blueprint
accident_zone = Blueprint('accident_zone', __name__)

@accident_zone.route('/accident_zone', methods=['GET', 'POST'])
def report_accident():
    """
    Handle accident zone reporting - both form display and submission
    """
    if request.method == 'POST':
        accident_location = request.form.get('accident_location')
        accident_description = request.form.get('accident_description')
        picture = request.files.get('accident_image')
        image_data = picture.read() if picture and picture.filename else None
        
        # Use model to save accident report
        success = AccidentReport.create(accident_location, accident_description, image_data)
        
        if success:
            print("Form Data Received:", request.form)
            print("Redirecting to:", url_for('general.thank_you'))
            return redirect(url_for('general.thank_you'))
        else:
            print("Error in Accident Report Submission")
            return "An error occurred. Please try again later."
    
    return render_template('accident_zone.html')
