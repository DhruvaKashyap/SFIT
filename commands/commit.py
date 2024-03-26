from argparse import ArgumentParser, Namespace
import hashlib
from datetime import datetime
import os

def initialize(subparsers):

    subparser: ArgumentParser = subparsers.add_parser("commit", help="commit changes with the given commit message")
    subparser.add_argument("message", help="message describing the commit")
    subparser.set_defaults(func=command_handler)

def command_handler(args: Namespace):

  #check if .sfit folder exists
    if not os.path.exists(".sfit/"):
        raise Exception("Repository has not been initialized. Use sfit init to initialize the repository")

    fileName = ""
    if os.path.exists(".sfit/config"):
        f = open(".sfit/config", 'r')
        fileName = f.read() # making the assumption that fileName also includes the file extension
    f = open(fileName, 'r')
    contentsInFile = f.read()  

    #generating hash using sha-1 algorithm  
    blobHash = (hashlib.sha1(contentsInFile.encode())).hexdigest()

    #creating commit hash
    commitHash = (hashlib.sha1(("commit" + str(len(contentsInFile))+"\0"  + contentsInFile).encode())).hexdigest()
    

    #creating blob object in .sfit/objects with hash as file name and contents as the original file contents
    f = open(".sfit/objects/"+ blobHash, 'w')
    f.write(contentsInFile)

    #check if HEAD exists
    if not os.path.exists(".sfit/HEAD"):
        #init commit has to be made
        f = open(".sfit/refs/heads/main", 'w')
        f.write(blobHash)
        f = open(".sfit/HEAD")
        f.write("/heads/main")

        #creating commit object
        f = open('.sfit/objects/'+commitHash, 'w')

        author = "" #need to collect it from config file but not yet decided on the format of config file        
        commitMessage = args # needs verification
        commitObjectContent = "blob " + blobHash +"\n"+"parent " + "NULL" + "\n"+ "author"+ author + datetime.utcnow() + commitMessage
    else:
        #not init commit
        f = open('.sfit/HEAD', 'r')
        branchReference = f.read()
        f = open(branchReference, 'w')
        parentCommitHash = f.read()
        f.write(blobHash)

        #creating commit object
        f = open('.sfit/objects/'+commitHash, 'w')
        author = "" #need to collect it from config file but not yet decided on the format of config file
        commitMessage = args
        commitObjectContent = "blob " + blobHash +"\n"+"parent " + parentCommitHash + "\n"+ "author"+ author + datetime.utcnow() + commitMessage
    


if __name__ == "__main__":
    raise Exception("invalid usage")
