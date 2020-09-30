from mega import Mega
import os

def upload_files(listOfFiles):
    
    print ("Beginning upload to mega")
    email = 'vraj690@gmail.com'
    password = '+.@`Ps6^R5{4xJ*[[]'
    mega = Mega()
    m = mega.login(email, password)
    folder = m.find('books')
    links =[]
    for file in listOfFiles:
        f = m.upload(file,folder[0])
        links.append(m.get_upload_link(f))
    print("finished")
    return links


if __name__ == "__main__":
    files = ['/Users/vrajpatel/PycharmProjects/libgen.py/libgen/test/abc1.txt','/Users/vrajpatel/PycharmProjects/libgen.py/libgen/test/abc2.txt']

    link = upload_files(files)
    print("LINK: ",link)