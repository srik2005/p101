import dropbox
from dropbox.files import WriteMode
import os
class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            for file_name in files:
                local_path = os.path.join(root,file_name)
                relative_path = os.path.relpath(local_path,file_from)
                dropbox_path = os.path.join(file_to,relative_path)
                 
                with open(file_from,'rb') as f :
                    dbx.files_upload(f.read(),dropbox_path, mode=WriteMode('overwrite'))
            
        

             
def main():
    access_token = 'nlAj5eb9gcIAAAAAAAAAAb47mL7SCGb-t_znevTzhNNLzXndG6j3I_gHLFFxc-g3'
    tranferData = TransferData(access_token)

    file_from = input("Enter the file path to tranfer: ")
    file_to = input("Enter the file path to enter the dropbox: ")
    
    tranferData.upload_file(file_from,file_to)
    print("File has been moved")

main()                