from Digest import Digest
from ResponseCodes import R
import os

class Compute:

    digest : Digest

    def __init__(self):
        self.digest = Digest()


    def monoFile(self, filename):

        if not self.isValidFile(filename):
            return R.RESPONSE_CHECK_FILE_1_NOTFOUND

        return self.digest.getMD5ofFile(filename)

    def fileToFile(self, filename1, filename2):

        if not self.isValidFile(filename1):
            return R.RESPONSE_CHECK_FILE_1_NOTFOUND

        if not self.isValidFile(filename2):
            return R.RESPONSE_CHECK_FILE_2_NOTFOUND

        hashOf1 = self.digest.getMD5ofFile(filename1)
        hashOf2 = self.digest.getMD5ofFile(filename2)

        return R.RESPONSE_CHECK_VALID if hashOf1 == hashOf2 else R.RESPONSE_CHECK_INVALID



    def fileToHash(self, filename1, givenHash):

        if not self.isValidFile(filename1):
            return R.RESPONSE_CHECK_FILE_1_NOTFOUND

        hashOf1 = self.digest.getMD5ofFile(filename1)

        return R.RESPONSE_CHECK_VALID if hashOf1 == givenHash else R.RESPONSE_CHECK_INVALID

    

    def isValidFile(self, path): 
        
        return os.path.isfile(path) if isinstance(path, str) else False