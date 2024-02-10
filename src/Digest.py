import hashlib

class Digest:

    def __init__(self):

        self.digests = {}

        
    def getMD5ofObject(self, obj):
        return hashlib.md5(obj).hexdigest()

    
    def getMD5ofFile(self, f):
        """
        Concatenates the contents of the given file and hashes them to MD5
        """
        
        hashable = b""  #  b means that this is a binaries object, not a string

        with open(f,'rb') as binfile: #  Make sure file is opened as binary
            for line in binfile:
                hashable += line

        return self.getMD5ofObject(hashable)

            



