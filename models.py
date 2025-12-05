from database import get_db_connection

class AccidentReport:
    @staticmethod
    def create(accident_location, accident_description, image_data):
        """Create a new accident report"""
        try:
            db = get_db_connection()
            if not db:
                return {"status": "error", "message": "Database connection failed"}

            cursor = db.cursor()
            sql = "INSERT INTO accident_zone (accident_location, accident_description, accident_image) VALUES (%s, %s, %s)"
            cursor.execute(sql, (accident_location, accident_description, image_data))
            db.commit()
            return {"status": "success"}
        except Exception as e:
            print(f"Error creating accident report: {e}")
            return {"status": "error", "message": str(e)}
        finally:
            cursor.close()
            db.close()


class BloodDonation:
    @staticmethod
    def create(name, blood_group, email, phone, city):
        """Create a new blood donation record"""
        try:
            db = get_db_connection()
            if not db:
                return {"status": "error", "message": "Database connection failed"}

            cursor = db.cursor()
            sql = "INSERT INTO blood_donation (name, blood_group, email, phone, city) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (name, blood_group, email, phone, city))
            db.commit()
            return {"status": "success"}
        except Exception as e:
            print(f"Error creating blood donation: {e}")
            return {"status": "error", "message": str(e)}
        finally:
            cursor.close()
            db.close()


class BloodRequest:
    @staticmethod
    def create(patient_name, blood_group, contact, hospital):
        """Create a new blood request"""
        try:
            db = get_db_connection()
            if not db:
                return {"status": "error", "message": "Database connection failed"}

            cursor = db.cursor()
            sql = "INSERT INTO blood_request (patient_name, blood_group, contact, hospital) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (patient_name, blood_group, contact, hospital))
            db.commit()
            return {"status": "success"}
        except Exception as e:
            print(f"Error creating blood request: {e}")
            return {"status": "error", "message": str(e)}
        finally:
            cursor.close()
            db.close()


class OrganDonation:
    @staticmethod
    def create(name, organ_type, email, phone, city):
        """Create a new organ donation record"""
        try:
            db = get_db_connection()
            if not db:
                return {"status": "error", "message": "Database connection failed"}

            cursor = db.cursor()
            sql = "INSERT INTO organ_donation (name, organ_type, email, phone, city) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (name, organ_type, email, phone, city))
            db.commit()
            return {"status": "success"}
        except Exception as e:
            print(f"Error creating organ donation: {e}")
            return {"status": "error", "message": str(e)}
        finally:
            cursor.close()
            db.close()


class OrganRequest:
    @staticmethod
    def create(patient_name, organ_needed, contact, hospital):
        """Create a new organ request"""
        try:
            db = get_db_connection()
            if not db:
                return {"status": "error", "message": "Database connection failed"}

            cursor = db.cursor()
            sql = "INSERT INTO organ_request (patient_name, organ_needed, contact, hospital) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (patient_name, organ_needed, contact, hospital))
            db.commit()
            return {"status": "success"}
        except Exception as e:
            print(f"Error creating organ request: {e}")
            return {"status": "error", "message": str(e)}
        finally:
            cursor.close()
            db.close()


class EmergencyCases:
    @staticmethod
    def get_all():
        """Fetch all emergency aid cases from the database."""
        try:
            db = get_db_connection()
            if not db:
                return {"status": "error", "message": "Database connection failed"}

            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT * FROM emergency_cases")
            data = cursor.fetchall()
            return {"status": "success", "data": data}
        except Exception as e:
            print(f"Error fetching emergency cases: {e}")
            return {"status": "error", "message": str(e)}
        finally:
            cursor.close()
            db.close()
