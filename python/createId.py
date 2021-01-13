import string
import secrets

def createId(size=12):
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return "".join(secrets.choice(chars) for x in range(size))