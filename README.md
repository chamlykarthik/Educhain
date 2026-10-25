
🎓 EduChain
Tamper-proof education certificates, verified in seconds.
A Python command-line prototype that combines SHA-256 hashing, a proof-of-work blockchain and a SQLite database to issue and verify academic certificates.

Show Image Show Image Show Image Show Image Show Image Show Image

</div>
💡 Why EduChain?
Fake degrees and edited marksheets are a real problem. Checking a certificate usually means emails, phone calls and waiting days for a reply.

EduChain makes this simple. When a college issues a certificate, the file's unique digital fingerprint (its SHA-256 hash) is saved in a database and locked into a blockchain block. Later, anyone can re-check the same file. If even one pixel was changed, the fingerprint no longer matches and the system flags it right away.

✨ Features
🏛️ University / College (Admin)	👩‍🎓 Student
Secure, password-protected admin login	Two-step login: password + biometric check
Register students with ID, name, password and biometric type	View your complete education history
Issue certificates (hash + issuer + type)	See the issuer, type and hash of every document
Verify any certificate file instantly	Confirm records against the blockchain
View the full blockchain	Browse the entire blockchain
Check whether the chain has been tampered with	See whether the chain is valid
⚙️ How It Works
Yes
No
📄 Certificate file
🔐 SHA-256 hash
🗄️ SQLite database
⛏️ Mine new block
🔗 Blockchain
📄 File to verify
🔐 Hash again
Matches stored hash?
✅ VERIFIED
❌ FAILED - documentmodified
Issue: the admin selects a certificate file and the system calculates its SHA-256 hash.
Store: the hash and details are saved in educhain.db.
Seal: a new block holding the certificate data is mined (proof-of-work, difficulty 3) and added to the chain.
Verify: the file is hashed again and compared with the stored value. A mismatch means it was altered.
Audit: the chain can be validated at any time by recomputing every block hash and checking each previous_hash link.
📁 Project Structure
text
EduChain/
├── main.py                   # 🚀 Entry point and main menu
├── admin_menu.py             # 🏛️ Admin / university menu
├── student_menu.py           # 👩‍🎓 Student portal menu
├── student_registration.py   # 📝 Register a new student
├── student_login.py          # 🔑 Password + biometric login
├── student_history.py        # 📚 Education history view
├── add_certificate.py        # ➕ Issue a certificate
├── verify_certificate.py     # ✅ Verify a certificate file
├── certificate_hash.py       # 🔐 SHA-256 file hashing
├── blockchain.py             # 🔗 Block and EduChain classes
├── database.py               # 🗄️ SQLite database layer
└── educhain.db               # 💾 Auto-created database
🚀 Getting Started
Requirements: Python 3.x. No external packages are needed, since everything uses the standard library.

bash
# 1. Clone the repository
git clone https://github.com/<your-username>/<your-repo>.git

# 2. Move into the project folder
cd <your-repo>

# 3. Run the application
python main.py
🔑 Default admin password: admin123

🧭 Quick Walkthrough
text
1. Main menu  →  1. University / College  →  enter admin password
2. Register student   →  ID, name, password, biometric type
3. Add certificate    →  student ID, file path, certificate type, issuer
4. Verify certificate →  student ID + file path  →  VERIFIED / FAILED
5. Logout  →  2. Student  →  password + biometric type
6. View Education History and the blockchain
🛠️ Tech Stack
Component	Technology
Language	Python 3
Database	SQLite (sqlite3)
Hashing	SHA-256 (hashlib)
Ledger	Custom proof-of-work blockchain
Interface	Command line
⚠️ Prototype Limitations
EduChain is built for learning and demonstration. Please be aware of the following before using it for anything real:

🔓 Plain-text passwords. Passwords are stored unhashed. Use bcrypt or Argon2 in a real system.
🔑 Hard-coded admin password. Move credentials to environment variables or a proper authentication system.
👆 Simulated biometrics. The biometric step is typed text, not a real fingerprint, face or retina sensor.
🧠 In-memory blockchain. The chain is recreated whenever the program starts, although certificate records stay in the database.
🌐 Single node. There is no network, consensus or peer replication.
🔮 Roadmap
 Persist the blockchain to disk or a database
 Secure password hashing
 Real biometric integration
 Web interface (Flask or React)
 Multi-node blockchain network
 QR-code certificate verification for employers
 Role-based access for multiple institutions
🤝 Contributing
Ideas and improvements are welcome! Fork the repo, create a branch, make your changes and open a pull request.

📄 License
This project is licensed under the MIT License. Add a LICENSE file to your repository to make it official.

<div align="center">
Built with ❤️ and Python

⭐ If you found this project useful, consider giving it a star!

</div>
Claude finished the response
