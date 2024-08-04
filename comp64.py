import base64
import json


def enc64(txt):
    return base64.b64encode(txt.encode()).decode()

def dec64(txt):
    return base64.b64decode(txt).decode()

# Y29kZWxpbmVz: codelines: lineas de codigo
# cGFyc2Vjb3VudA==: parsecount: conteo de parse
# cmFtc2l6ZQ==: ramsize: tamaño de la ram
# dGVtcHJlZ2lzdGVy: tempregister: variables a usar
# dXNlcg==: user: usuario
# cGFzc3dvcmQ=: password:  contraseña
if __name__ == "__main__":
    original_texto = """{
    "Y29kZWxpbmVz": 5,
    "cGFyc2Vjb3VudA==": 16,
    "cmFtc2l6ZQ==": 50,
    "dGVtcHJlZ2lzdGVy":5,
    "dXNlcg==":"pchav",
    "cGFzc3dvcmQ=":"1234"
    }"""
    print(enc64(original_texto))
    print(json.loads(original_texto))