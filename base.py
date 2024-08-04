import comp64
import json

class TheWorldHardestApiForever:
    def __init__(self):
        self._actived = 0
        self._key = ""
        pass

    @property
    def actived(self):
        return self._actived

    def key(self,apiKey: str):
        try:
            self._key = apiKey
            decoded = json.loads(comp64.dec64(apiKey))
            self._codelines = decoded["Y29kZWxpbmVz"]
            self._parsecount = decoded["cGFyc2Vjb3VudA=="]
            self._ramsize = decoded["cmFtc2l6ZQ=="]
            self._tempregister = decoded["dGVtcHJlZ2lzdGVy"]
            self._user = decoded["dXNlcg=="]
            self._password = decoded["cGFzc3dvcmQ="]
        except:
            raise SyntaxError("Invalid Api Key")
        self._actived = 1

    def get_key(self):
        return self._key

if __name__ == "__main__":
    api = TheWorldHardestApiForever()
    key = "ewogICAgIlkyOWtaV3hwYm1WeiI6IDUsCiAgICAiY0dGeWMyVmpiM1Z1ZEE9PSI6IDE2LAogICAgImNtRnRjMmw2WlE9PSI6IDUwLAogICAgImRHVnRjSEpsWjJsemRHVnkiOjUsCiAgICAiZFhObGNnPT0iOiJwY2hhdiIsCiAgICAiY0dGemMzZHZjbVE9IjoiMTIzNCIKICAgIH0="
    api.key(key)
