from flask import request, escape

# /hello?username={{config}} will display the entire flask configuration and potential secrets
@app.route('/hello')
def hello():
    username = request.args.get('username', '')
    username = escape(username)
    template = f"<p>Hello {username}</p>"
    return render_template_string(template)