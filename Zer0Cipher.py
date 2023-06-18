import os
import pyAesCrypt

class Cg:
    def __init__(self):
        self.dir = os.getcwd()
        self.password = ''
        self.action = ''
        self.exception_file = "Zer0Cipher.exe"
        print(self.exception_file)
        self.chooseAnAction()
        self.checkPassword()

    def crypt(self, file):
        buffer_size = 512*1024
        pyAesCrypt.encryptFile(str(file), str(file) + ".crp", self.password, buffer_size)
        print("[Encrypted] '" + os.path.basename(file) +".crp'")
        os.remove(file)

    def decrypt(self, file):
        buffer_size = 512 * 1024
        pyAesCrypt.decryptFile(str(file), str(os.path.splitext(file)[0]), self.password, buffer_size)
        print("[Decrypted] '" + os.path.basename(file) + "'")
        os.remove(file)    

    def run(self):
        for name in os.listdir(self.dir):
            if name == self.exception_file:
                continue
            path = os.path.join(self.dir, name)
            if os.path.isfile(path):
                if self.action == 1:
                    self.crypt(path)
                elif self.action == 2:
                    try:
                        self.decrypt(path)
                    except:
                        print("Wrong Password")
            else:
                main_dir = self.dir
                self.dir = path
                self.run()
                self.dir = main_dir

    def chooseAnAction(self):
        print("[1] Encrypt \n[2] Decrypt")
        inputAction = int(input("Choose action: "))
        if inputAction == 1:
            self.action = 1
        elif inputAction == 2:
            self.action = 2                      
        else:
            print("No avaliable action")
            return self.chooseAnAction()


    def checkPassword(self):
        checkpswd1 = str(input("Password: "))
        checkpswd2 = str(input("Repeat Password: "))
        if checkpswd1 == checkpswd2:
            self.password = checkpswd2
        else:
            print("Not correct password check")
            return self.checkPassword()

if __name__ == "__main__":
    #print(__file__)
    #print(os.path.basename(__file__))
    
    cg = Cg()
    
    cg.run()