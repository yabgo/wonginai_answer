import base64

secret = "aWFuZ25vVzpOQU06RU5JTDp0YTpzdTpuaW9K"
answer = base64.b64decode(secret)
print(answer[::-1].decode())
