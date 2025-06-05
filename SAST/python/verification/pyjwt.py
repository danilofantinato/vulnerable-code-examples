import jwt

# Verify the token signature
jwt.decode(token, key, algorithms=["HS256"])

# Alternatively, you can use the jwt.decode() function with the verify parameter set to True
# and provide the appropriate key and algorithm
jwt.decode(token, key, algorithms=["HS256"], verify=True)