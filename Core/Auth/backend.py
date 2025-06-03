# myproject/auth/backends.py
from rest_framework_simplejwt.backends import TokenBackend

class UnsafeTokenBackend(TokenBackend):
    def __init__(self, algorithm='HS256'):
        # On garde la clé de signature pour émettre
        super().__init__(
            algorithm=algorithm,
            #signing_key='super-secret-key-used-for-signing'
        )
        

    def decode(self, token, verify=True):
        # ⚠️ On désactive la vérification malgré la présence de la signature
        return super().decode(token, verify=False)
