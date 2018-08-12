import os,sys,glob2
from datetime import datetime
outfile = datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt"
files   = glob2.glob(os.path.dirname(sys.argv[0])+"\*.txt")

def merge(files,writeFile):
    with open(writeFile,"a") as writer:
        for f in files:
            with open(f,"r") as readFile:
                writer.write(readFile.read()+"\n")
merge(files,outfile)
