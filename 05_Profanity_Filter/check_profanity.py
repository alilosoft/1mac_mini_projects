import urllib


def read_txt(txt_file_path):
    txt_file = open(txt_file_path)
    file_content = txt_file.read()
    txt_file.close()
    return file_content


def check_profanity(text):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text)
    response = connection.read()
    connection.close()
    if "true" in response:
        print "Watch your language"
    elif "false" in response:
        print "Clean speech"
    else:
        print "Unknown response from the server"
    return response


print check_profanity(read_txt("story.txt"))
