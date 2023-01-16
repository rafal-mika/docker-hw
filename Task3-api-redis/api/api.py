import os
from flask import Flask
from flask import request
from redis import Redis
from flask_api import status

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST")
redis_port = os.getenv("REDIS_PORT")

redis = Redis(host=redis_host,port=redis_port,charset='utf-8',decode_responses=True)

@app.get("/api/keys")
def get_keys():
    return {"keys":redis.keys('*')}

@app.get("/api/keys/<key>")
def get(key: str):
    value = redis.get(key)
    if value is None:
        return f"Key '{key}' not found...", status.HTTP_404_NOT_FOUND
    return {'key': key, 'value': value}

@app.post("/api/keys")
def create():
    request_data = request.get_json()
    key = request_data['key']
    value = request_data['value']
    if key is None or not bool(key.strip()) or value is None:
        return "\n\nInvalid data format. Please check your entry data...", status.HTTP_400_BAD_REQUEST
    
    set_result = redis.set(key,value,nx=True)
    return get(key) if set_result is not None else f"\n\nOperation was not performed. Key '{key}' already exists"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=5000)