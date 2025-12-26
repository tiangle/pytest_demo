import hashlib


class md5_util:
    def __init__(self):
        pass

    @staticmethod
    def md5_encode(text) -> str:
        md5 = hashlib.md5()
        md5.update(text.encode("utf-8"))
        return md5.hexdigest()
