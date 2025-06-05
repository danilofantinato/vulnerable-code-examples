def ping():
    host = request.args.get("host", "www.google.com")
    if not re.match(r'^[\w\.-]+$', host):
        return "Invalid host"
    try:
        subprocess.check_call(["ping", "-c", "1", host], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return "True"
    except subprocess.CalledProcessError:
        return "False"