from flask import Blueprint, jsonify
from database import get_db_connection

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/get_dashboard_data', methods=['GET'])
def get_dashboard_data():
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

        response_data = {
            "blood_donations": blood_count,
            "organ_donations": organ_count,
            "accidents": accident_count
        }

        return jsonify(response_data), 200

    except Exception as e:
        print(f"Error fetching dashboard data: {e}")
        return jsonify({"error": "Failed to fetch data"}), 500
    finally:
        cursor.close()
        conn.close()
