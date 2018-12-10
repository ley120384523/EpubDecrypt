import hashlib
import os
import re
import sys
import zipfile

from Crypto.Cipher import AES


def decrypt_bytes(content):
    """解密"""
    md5 = hashlib.md5()
    md5.update("xingshulin.com.!#%@)@*^!^*".encode())
    password = md5.hexdigest()
    return AES.new(password.encode(), AES.MODE_ECB).decrypt(content)


if __name__ == "__main__":
    for filepath in sys.argv[1:]:
        name, ext = os.path.splitext(filepath)

        originfile = zipfile.ZipFile(filepath, "r", zipfile.ZIP_DEFLATED)
        copyfile = zipfile.ZipFile("{0}.decrypt.epub".format(name), "w", zipfile.ZIP_DEFLATED)

        for zf in originfile.infolist():
            content = decrypt_bytes(originfile.read(zf.filename)) \
                if re.match(r"^OPS/.*?\.html$", zf.filename) else originfile.read(zf.filename)
            copyfile.writestr(zf, content)
