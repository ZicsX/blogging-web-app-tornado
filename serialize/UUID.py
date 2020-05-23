import base64
import uuid
def get_uuid():
    id = base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)
    print("UUID = "+str(id))
    return id