import base64, uuid

class Utils:
	def gen64uuid():
		return base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)
