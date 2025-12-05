Clone the repository
```bash
git clone git@github.com:keertiG-1296/Emergency_Aidportal.git
or
git clone https://github.com/keertiG-1296/Emergency_Aidportal.git
```

Enter the project folder
``` bash
cd Emergency_Aidportal
```
Set up a Python virtual environment (optional but recommended)
```bash
python -m venv venv
```
Activate it:
Windows:
```bash
venv\Scripts\activate
```
Mac/Linux:
```bash
source venv/bin/activate
```
Install dependencies
```bash
pip install -r requirements.txt
```
Configure database
Open config.py and database.py

Update MySQL credentials (host, user, password, database)

Make sure the database exists:
```bash
CREATE DATABASE emergency_aid;
```
Run the project
``` bash
python main.py
```
