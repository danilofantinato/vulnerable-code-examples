import python_jwt

# Generate a secure key
key = python_jwt.generate_key()

# Encode the JWT with a secure algorithm (e.g., HS256)
token = python_jwt.encode_jwt(payload, key, algorithm='HS256')

# Verify the JWT signature before processing
try:
    payload = python_jwt.verify_jwt(token, key, algorithms=['HS256'])
    python_jwt.process_jwt(payload)
except python_jwt.InvalidTokenError:
    # Handle invalid token
    pass