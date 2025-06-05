import ssl

# Create a secure SSL/TLS context with hostname verification enabled
ctx = ssl.create_default_context()

# Optionally, you can further customize the context
# For example, to disable specific TLS versions or ciphers
# ctx.options &= ~ssl.OP_NO_TLSv1_3
# ctx.set_ciphers("HIGH:!DH:!aNULL")

# Use the secure context for establishing SSL/TLS connections
# For example, with a HTTPS request
# import urllib.request
# with urllib.request.urlopen("https://example.com", context=ctx) as response:
#     data = response.read()