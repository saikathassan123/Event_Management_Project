"""
Helper script to create .env file with your PostgreSQL password.
Run this script: python create_env_file.py
"""
import os

env_content = """# Django Settings
SECRET_KEY=django-insecure-&5qgin)4692r9c6@l)-((kkmi44b!s*w#%hcz)7d2ayu_g9q2p

# Database Configuration (PostgreSQL)
DB_NAME=Task_Management
DB_USER=postgres
DB_PASSWORD=123
DB_HOST=localhost
DB_PORT=5432

# Optional: Email Configuration
EMAIL_HOST=smtp.gmail.com
EMAIL_USE_TLS=True
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
"""

env_file_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(env_file_path):
    print(".env file already exists!")
    response = input("Do you want to overwrite it? (yes/no): ")
    if response.lower() != 'yes':
        print("Cancelled. .env file not modified.")
        exit()

try:
    with open(env_file_path, 'w') as f:
        f.write(env_content)
    print("SUCCESS: .env file created successfully!")
    print(f"Location: {env_file_path}")
    print("\nConfiguration:")
    print("   - Database: Task_Management")
    print("   - User: postgres")
    print("   - Password: 123")
    print("   - Host: localhost")
    print("   - Port: 5432")
except Exception as e:
    print(f"ERROR: Error creating .env file: {e}")
    print("\nPlease create .env file manually with the following content:")
    print("\n" + "="*50)
    print(env_content)
    print("="*50)
