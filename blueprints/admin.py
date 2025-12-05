from flask import Blueprint, render_template, request, redirect, url_for, session, flash, jsonify
from database import get_db_connection
from functools import wraps
import hashlib

admin = Blueprint('admin', __name__)

# Admin credentials (in production, use environment variables and proper hashing)
ADMIN_CREDENTIALS = {}  # Store admin credentials in memory (in production, use database)

# Create a default admin account if none exists
def create_default_admin():
    if not ADMIN_CREDENTIALS:
        ADMIN_CREDENTIALS['admin'] = 'admin123'
        print("Default admin account created: username='admin', password='admin123'")

# Initialize default admin
create_default_admin()

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin_logged_in' not in session:
            return redirect(url_for('admin.login'))
        return f(*args, **kwargs)
    return decorated_function

@admin.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if not username or not password:
            flash('Username and password are required!', 'error')
        elif password != confirm_password:
            flash('Passwords do not match!', 'error')
        elif username in ADMIN_CREDENTIALS:
            flash('Username already exists!', 'error')
        else:
            ADMIN_CREDENTIALS[username] = password
            flash('Admin account created successfully! Please login.', 'success')
            return redirect(url_for('admin.login'))
    
    return render_template('admin/signup.html')

@admin.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username in ADMIN_CREDENTIALS and ADMIN_CREDENTIALS[username] == password:
            session['admin_logged_in'] = True
            session['admin_username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Invalid credentials!', 'error')
    
    return render_template('admin/login.html')

@admin.route('/logout')
def logout():
    session.pop('admin_logged_in', None)
    session.pop('admin_username', None)
    flash('Logged out successfully!', 'success')
    return redirect(url_for('general.home'))

@admin.route('/dashboard')
@admin_required
def dashboard():
    return render_template('admin/dashboard.html')

@admin.route('/api/stats')
@admin_required
def get_stats():
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500
    
    cursor = conn.cursor(dictionary=True)
    
    try:
        # Get blood donation count
        cursor.execute("SELECT COUNT(*) as count FROM blood_donation")
        blood_count = cursor.fetchone()['count']
        
        # Get organ donation count
        cursor.execute("SELECT COUNT(*) as count FROM organ_donation")
        organ_count = cursor.fetchone()['count']
        
        # Get accident count
        cursor.execute("SELECT COUNT(*) as count FROM accident_zone")
        accident_count = cursor.fetchone()['count']
        
        # Get blood request count
        cursor.execute("SELECT COUNT(*) as count FROM blood_request")
        blood_request_count = cursor.fetchone()['count']
        
        # Get organ request count
        cursor.execute("SELECT COUNT(*) as count FROM organ_request")
        organ_request_count = cursor.fetchone()['count']
        
        response_data = {
            "blood_donations": blood_count,
            "organ_donations": organ_count,
            "accidents": accident_count,
            "blood_requests": blood_request_count,
            "organ_requests": organ_request_count
        }
        
        return jsonify(response_data), 200
        
    except Exception as e:
        print(f"Error fetching stats: {e}")
        return jsonify({"error": "Failed to fetch data"}), 500
    finally:
        cursor.close()
        conn.close()

@admin.route('/api/blood_donations')
@admin_required
def get_blood_donations():
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500
    
    cursor = conn.cursor(dictionary=True)
    
    try:
        cursor.execute("SELECT * FROM blood_donation ORDER BY id DESC")
        donations = cursor.fetchall()
        return jsonify(donations), 200
        
    except Exception as e:
        print(f"Error fetching blood donations: {e}")
        return jsonify({"error": "Failed to fetch data"}), 500
    finally:
        cursor.close()
        conn.close()

@admin.route('/api/organ_donations')
@admin_required
def get_organ_donations():
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500
    
    cursor = conn.cursor(dictionary=True)
    
    try:
        cursor.execute("SELECT * FROM organ_donation ORDER BY id DESC")
        donations = cursor.fetchall()
        return jsonify(donations), 200
        
    except Exception as e:
        print(f"Error fetching organ donations: {e}")
        return jsonify({"error": "Failed to fetch data"}), 500
    finally:
        cursor.close()
        conn.close()

@admin.route('/api/accidents')
@admin_required
def get_accidents():
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500
    
    cursor = conn.cursor(dictionary=True)
    
    try:
        # First check if table exists and has data
        cursor.execute("SHOW TABLES LIKE 'accident_zone'")
        table_exists = cursor.fetchone()
        
        if not table_exists:
            return jsonify({"error": "Table 'accident_zone' does not exist"}), 500
        
        # Get table structure
        cursor.execute("DESCRIBE accident_zone")
        columns = cursor.fetchall()
        print(f"Table structure: {columns}")
        
        # Check if table has any data
        cursor.execute("SELECT COUNT(*) as count FROM accident_zone")
        count_result = cursor.fetchone()
        total_count = count_result['count'] if count_result else 0
        print(f"Total accidents in table: {total_count}")
        
        # Fetch accidents data with limit for debugging
        cursor.execute("SELECT * FROM accident_zone ORDER BY id DESC LIMIT 100")
        accidents = cursor.fetchall()
        print(f"Fetched {len(accidents)} accidents")
        
        # Log first accident for debugging
        if accidents:
            print(f"First accident data: {accidents[0]}")
        
        return jsonify(accidents), 200
        
    except Exception as e:
        print(f"Error fetching accidents: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

@admin.route('/api/blood_requests')
@admin_required
def get_blood_requests():
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500
    
    cursor = conn.cursor(dictionary=True)
    
    try:
        cursor.execute("SELECT * FROM blood_request ORDER BY id DESC")
        requests = cursor.fetchall()
        return jsonify(requests), 200
        
    except Exception as e:
        print(f"Error fetching blood requests: {e}")
        return jsonify({"error": "Failed to fetch data"}), 500
    finally:
        cursor.close()
        conn.close()

@admin.route('/api/organ_requests')
@admin_required
def get_organ_requests():
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500
    
    cursor = conn.cursor(dictionary=True)
    
    try:
        cursor.execute("SELECT * FROM organ_request ORDER BY id DESC")
        requests = cursor.fetchall()
        return jsonify(requests), 200
        
    except Exception as e:
        print(f"Error fetching organ requests: {e}")
        return jsonify({"error": "Failed to fetch data"}), 500
    finally:
        cursor.close()
        conn.close()
