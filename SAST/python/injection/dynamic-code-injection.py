# Remediated code:

from flask import request

@app.route("/")
def example():
    operation = request.args.get("operation")
    allowed_operations = ["add", "subtract", "multiply", "divide"]
    if operation in allowed_operations:
        if operation == "add":
            product_add()
        elif operation == "subtract":
            product_subtract()
        elif operation == "multiply":
            product_multiply()
        elif operation == "divide":
            product_divide()
    else:
        return "Invalid operation", 400
    return "OK"