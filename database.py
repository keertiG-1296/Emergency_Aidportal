import mysql.connector
from config import Config

def get_db_connection():
    """
    Create and return a MySQL database connection.
    """
    try:
        return mysql.connector.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME
        )
    except mysql.connector.Error as e:
        print(f"Database connection error: {e}")
        return None

def update_donation_count(donation_id):
    """
    Updates the count column in the donation table for a given donation ID.
    """
    db = get_db_connection()
    if db:
        try:
            cursor = db.cursor()
            cursor.execute("UPDATE donation SET count = count + 1 WHERE id = %s", (donation_id,))
            db.commit()  # Save the changes
            print(f"Donation count updated successfully for ID {donation_id}.")
        except mysql.connector.Error as e:
            print(f"Error updating donation count: {e}")
        finally:
            cursor.close()
            db.close()  # Close connection
    else:
        print("Failed to connect to the database.")

# Example usage
update_donation_count(1)  # Replace '1' with the actual ID
