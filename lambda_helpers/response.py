import json
class Response:
    def __init__(self,  status_code: int, body: dict):
        self.status_code = status_code
        self.body = body

    def to_json(self):
        return {'statusCode': self.status_code, 'body': json.dumps(self.body)}