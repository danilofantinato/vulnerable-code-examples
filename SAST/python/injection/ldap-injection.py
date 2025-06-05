# Remediated code:

from flask import request
import ldap
from ldap import filter

@app.route("/user")
def user():
    username = request.args.get('username')

    if not username:
        return "Username is required", 400

    # Sanitize the input using the ldap.filter.escape_filter_chars function
    sanitized_username = ldap.filter.escape_filter_chars(username)

    search_filter = "(&(objectClass=user)(uid=" + sanitized_username + "))"

    ldap_connection = ldap.initialize("ldap://localhost:389")
    try:
        user = ldap_connection.search_s("dc=example,dc=org", ldap.SCOPE_SUBTREE, search_filter)
        return user[0]
    except ldap.LDAPError as e:
        return f"LDAP error: {str(e)}", 500