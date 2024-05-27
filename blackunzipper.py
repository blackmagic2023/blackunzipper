import zipfile
import sys
import os

try:
    target_file = sys.argv[1]
    password_dict = sys.argv[2]
    try:
        if os.path.isfile(password_dict) == True:
            pass
        else:
            print('[-] Wrong dictionary path.')
            sys.exit(0)

        def pass_checker(bpassword, password):
            try:
                zfile = zipfile.ZipFile(target_file)
                zfile.extractall(pwd=bpassword)
                print(f'[+] Password Cracked = {password}')
                exit()
            except Exception as e:
                pass
        def checker(fref_var):
            if fref_var == False:
                print("[-] Could not find password in wordlist.")
        ref_var = True
        def main():
            global ref_var
            with open(password_dict, 'r') as pass_dict:
                for line in pass_dict.readlines():
                    password = line.strip('\n')
                    bpassword = bytes(password, 'latin-1')
                    pass_checker(bpassword, password)
                ref_var = False
                checker(ref_var)



        if __name__ == "__main__":
            main()
    except:
        pass
except:
    print("Usage:python3 blackunzipper.py <target_file> <wordlist>")
