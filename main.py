import base64

secret = "aWFuZ25vVzpOQU06RU5JTDp0YTpzdTpuaW9K"
answer = base64.b64decode(secret).decode()
final_answer = answer[::-1]

print(final_answer)
