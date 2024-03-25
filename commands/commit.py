from argparse import ArgumentParser, Namespace
import hashlib

def initialize(subparsers):
  subparser: ArgumentParser = subparsers.add_parser("commit", help="commit changes with the given commit message")
  subparser.add_argument("message", help="message describing the commit")
  subparser.set_defaults(func=command_handler)

def command_handler(args: Namespace):

  pathOfFolder = ""
  if not os.path.exists(pathOfFolder+"/.sfit/"):
    raise Exception("Repository has not been initialized. Use sfit init to initialize the repository")
  #to be verified if head exists
  if not os.path.exists(pathOfFolder+"/.sfit/HEAD"):
    ...

  fileName = ""
  if os.path.exists(pathOfFolder+"/.sfit/config"):
    f = open(pathOfFolder+"/.sfit/config", 'r')
    fileName = f.read() # making the assumption that fileName also includes the file extension
  f = open(pathOfFolder+fileName)
  contentsInFile = f.read()
  
  #generating hash using sha-1 algorithm
  commitHash = (hashlib.sha1(contentsInFile.encode())).hexdigest()

  #creating commit file in .sfit/objects with hash as file name and contents as the original file contents
  f = open(pathOfFolder+"/.sfit/objects/"+ hash, 'w')
  f.write(contentsInFile)

  #to be added...





if __name__ == "__main__":
  print("invalid usage")