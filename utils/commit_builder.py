import datetime
import pathlib as Path
import Hash
import sys

class Commit:
    def __init__(self,blob_hash, parent_hash, author_name, committer_name, commit_message):
        
        self.blob_hash = blob_hash
        self.parent_hash = parent_hash
        self.author_name = author_name
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.timezone = datetime.datetime.now().astimezone().tzname()
        self.committer_name = committer_name
        self.commit_message = commit_message
        self.name = Hash.hash_string(str(self))

    def __str__(self):
        return f"blob {self.blob_hash}\nparent {self.parent_hash}\nauthor {self.author_name} {self.timestamp} {self.timezone}\ncommitter {self.committer_name}\n{self.commit_message}"
    
    def save(self):
        temp = Path.Path("../.sfit/objects") / self.name 
        with temp.open("w") as f:
            f.write(str(self))
        print(f"Commit saved to {temp}")



if __name__ == "__main__":
    print("Invalid use")
    sys.exit(-1)
