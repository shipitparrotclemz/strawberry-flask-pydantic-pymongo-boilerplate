import os

# Connects to local mongo's `strawberry_farmers` database by default
MONGO_URL: str = os.getenv("MONGO_URL", "mongodb://localhost:27017/strawberry_farmers")
