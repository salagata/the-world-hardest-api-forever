import base64
import json

# Cadena de ejemplo
original_texto = """{"Y29kZWxpbmVz":6,"aGlnaHBhcnNlYWJsZQ==":8,"bG93cGFyc2VhYmxl":8,"bWFjcGFyc2VhYmxl":8,"cmFtc2l6ZQ==":15,"bmFtZQ==":"pchav","cGFzc3dvcmQ=":1234}"""


def enc64(txt):
    return base64.b64encode(txt.encode()).decode()

def dec64(txt):
    return base64.b64decode(txt).decode()

print(json.loads(original_texto))