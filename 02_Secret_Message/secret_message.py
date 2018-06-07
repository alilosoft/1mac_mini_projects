import os


def rename_files():
    working_dir = os.getcwd()
    print "Current Working Directory: " + working_dir
    secret_msg_dir = working_dir + "/message"
    # list file_list in dir
    file_list = os.listdir(secret_msg_dir)
    # rename each file
    os.chdir(secret_msg_dir)
    print "Current Working Directory Changed to: " + os.getcwd()
    for file_name in file_list:
        new_file_name = file_name.translate(None, "0123456789")
        os.rename(file_name, new_file_name)
        # printing a nice report
        file_name = " " * (25 - len(file_name)) + file_name
        print file_name, "------ renamed to --------> ", new_file_name


rename_files()
