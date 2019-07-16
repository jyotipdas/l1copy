import os,hashlib

def md5Check(filePath):
    with open(filePath,'rb') as f:
        contents = f.read()
        md5 = hashlib.md5()
        for i in range(0,len(contents),8192):
            md5.update(contents[i:i+8192])
        
        return md5.hexdigest()
md5sumDict={}

for cPath,dirList,fileList in os.walk(os.getcwd()):
    for file1 in fileList:
        absFile=os.path.join(cPath,file1)
        print absFile
        md5 = md5Check(absFile)
        if md5 in md5sumDict:
            os.remove(absFile)
        else:
            md5sumDict[md5]=absFile
