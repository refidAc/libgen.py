from mega import Mega
import os

def main():
    print ("Test")
    print ("Beginning upload to mega")
    email = os.environ['MEGA_USER']
    password = os.environ['MEGA_PASS']
    mega = Mega()
    m = mega.login(email, password)
    folder = m.find('adfkaf')
if __name__ == "__main__":
    main()