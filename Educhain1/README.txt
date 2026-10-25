EDUCHAIN - FIXED RUNNABLE VERSION

Requirements:
- Python 3.x
- No external packages required

Run:
    python main.py

Admin password:
    admin123

Basic flow:
1. University / College
2. Login using admin123
3. Register a student
4. Logout
5. Student login
6. Enter the registered biometric type
7. View education history

To add a certificate:
1. Login as admin.
2. Select Add certificate.
3. Enter the Student ID.
4. Enter the path of an existing certificate file.
5. Enter certificate type and issuer.

Important:
- This prototype stores passwords as plain text. For a real application,
  passwords should be securely hashed.
- Biometric input here is only a simulation. It does not access a real
  fingerprint, face, or retina sensor.
- The blockchain is stored in memory for this prototype and is recreated
  when the program starts.
