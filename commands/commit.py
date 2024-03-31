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
        configFile = open(".sfit/config", 'r')
        fileNameme = configFile.read() # making the assumption that fileName also includes the file extension
        configFile.close()

    blobFile = open(fileName, 'r')
    contentsInFile = blobFile.read()
    blobFile.close()

    #generating hash using sha-1 algorithm  
    blobHash = (hashlib.sha1(contentsInFile.encode())).hexdigest()

    #creating commit hash
    

    #creating blob object in .sfit/objects with hash as file name and contents as the original file contents
    snapshotFile = open(".sfit/objects/"+ blobHash, 'w')
    snapshotFile.write(contentsInFile)
    snapshotFile.close()

    #check if HEAD exists
    if not os.path.exists(".sfit/HEAD"):
        #init commit has to be made
        branchReferenceFile = open(".sfit/refs/heads/main", 'w')
        branchReferenceFile.write(blobHash)
        branchReferenceFile.close()

        headFile = open(".sfit/HEAD")
        headFile.write("/heads/main")
        headFile.close()

        #creating commit object

        author = "" #need to collect it from config file but not yet decided on the format of config file        
        commitMessage = args.message # needs verification
        commitObjectContent = "blob " + blobHash +"\n"+"parent " + "NULL" + "\n"+ "author "+ author + " " + str(datetime.utcnow()) +'\n' + commitMessage
        commitHash = (hashlib.sha1(commitObjectContent.encode())).hexdigest()

        commitObjectFile = open('.sfit/objects/'+commitHash, 'w')

        commitObjectFile.write(commitObjectContent)
        commitObjectFile.close()
    else:
        #not init commit
        headFile = open('.sfit/HEAD', 'r')
        branchReference = headFile.read()
        branchReferenceFile = open(branchReference, 'r+')
        parentCommitHash = branchReferenceFile.read()
        branchReferenceFile.write(blobHash)
        branchReferenceFile.close()


        #creating commit object

        author = "" #need to collect it from config file but not yet decided on the format of config file        
        commitMessage = args.message # needs verification

        commitObjectContent = "blob " + blobHash +"\n"+"parent " + parentCommitHash + "\n"+ "author "+ author + " " + str(datetime.utcnow()) +'\n' + commitMessage
        commitHash = (hashlib.sha1(commitObjectContent.encode())).hexdigest()

        commitObjectFile = open('.sfit/objects/'+commitHash, 'w')
        commitObjectFile.write(commitObjectContent)
        commitObjectFile.close()

if __name__ == "__main__":
    raise Exception("invalid usage")
