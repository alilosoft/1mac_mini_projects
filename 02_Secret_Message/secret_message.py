import os

def rename_files():
    print "Current Working Directory: " + os.getcwd()
    # list file_list in dir
    secret_msg_dir = r"D:\My\Learning\1MAC\Code\Mini_Projects\02_Secret_Message\message"
    file_list = os.listdir(secret_msg_dir)
    # rename each file
    os.chdir(secret_msg_dir)
    print "Current Working Directory Changed to: " + os.getcwd()
    for file_name in file_list:
        new_file_name = file_name.translate(None, "0123456789")
        os.rename(file_name, new_file_name)
        print file_name, " renamed to > ", new_file_name

rename_files()

# os.rename("alilo", "ali")
