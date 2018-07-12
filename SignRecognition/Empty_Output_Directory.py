import glob, os, os.path

filelist = glob.glob(os.path.join("/home/jsingh/Codeblocks Projects/PROJECT/SignRecognition/DATA/EXPORT", "*.jpg"))
for f in filelist:
    os.remove(f)
