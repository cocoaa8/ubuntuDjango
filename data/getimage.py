class image:
    base64 = ""
    imagecode = 0
    def __init__(self, base64, imagecode):
        self.base64 = base64
        self.imagecode = imagecode
        
    def getbase64(self):
        return self.base64
        
    def getimagecode(self):
        return self.imagecode
        