from types import NoneType
from features import SFTP

client = SFTP()

def menu(sftp):
    quitLoop = False
    while not quitLoop:
        commandString = input(">> ")
        command = commandString.split()
        commandLen = len(command)

        match command[0]:
            case "login":
                if(commandLen > 1):
                    sftp = client.login(command[1])
                    client.printRemoteWorkingDirectory(sftp)
                    serverHostName = command[1]
                else:
                    print("Please input a server address.")

            case "logoff":
                sftp.close()
                print("Connection closed.")

            case "mkdir":
                if(commandLen > 1):
                    client.makeDir(sftp, command[1])
                else:
                    print("Please input a directory name.")

            case "chmod":
                if(commandLen> 2):
                    client.chmod(sftp, command[1], command[2])
                elif(commandLen > 1):
                    print("Please enter the octal permission.")
                else:
                    print("Please input the file path.")

            case "ls":
                # check if command had the -l flag for local
                if(commandLen > 2):
                    if("-l" in command):
                        command.remove("-l")
                        commandLen = len(command)
                        if(commandLen > 1):
                            client.printLocalDirectory(command[1])
                        else:
                            client.printLocalDirectory(".")
                    elif("-r" in command):
                        if sftp == NoneType:
                            print("Not logged into a remote server")
                            continue
                        command.remove("-r")
                        commandLen = len(command)
                        if(commandLen > 1):
                            client.printRemoteDirectory(sftp, command[1])
                        else:
                            client.printRemoteDirectory(sftp, sftp.getcwd())
                else:
                    # ls + a flag
                    if(command is not None and "-l" in command):
                        client.printLocalDirectory(".")
                        continue
                    if(command is not None and "-r" in command):
                        if sftp == NoneType:
                            print("Not logged into a remote server")
                            continue
                        client.printRemoteDirectory(sftp, sftp.getcwd())
                        continue

                    # ls + a path
                    if(commandLen > 1):
                        client.printLocalDirectory(command[1]) 
                    # otherwise default to printing the local current dir
                    else:
                        client.printLocalDirectory(".")

            case "get":
                if sftp == NoneType:
                    print("Not logged into a remote server")
                    continue

                # if we have the -m flag then we are getting multiple
                if("-m" in command):
                    command.remove("-m")
                    commandLen = len(command)
                    if(commandLen > 1):
                        path = client.getMultipleList()
                        client.getMultiple(sftp, path, command[1])
                    else:
                        print("Please specify a destination path.")
                else:
                    if(command > 3): 
                        client.getFile(sftp, command[1], command[2])
                    else:
                        print("Please specify a source and destination path.")

            case "mv":
                if("-r" in command):
                    if sftp == NoneType:
                            print("Not logged into a remote server")
                            continue

                    command.remove("-r")
                    commandLen = len(command)
                    if(commandLen > 3):
                        client.renameRemoteFile(sftp, command[1], command[2])
                    else:
                        print("Please enter the source and destination file names.")
                else:
                    if(commandLen > 3):
                        client.renameLocalFile(command[1], command[2])
                    else:
                        print("Please enter the source and destination file names.")

            case "xcopy":
                if(commandLen > 2):
                    if sftp == NoneType:
                            print("Not logged into a remote server")
                            continue

                    client.copyRemoteDir(sftp, command[1], command[2])
                else:
                    print("Please specify a source and destination path in the form 'xcopy [source] [destination]'")
                    
            case "quit":
                if sftp is not NoneType:
                    print(f"Closed connection to {serverHostName}")
                    sftp.close()
                    
                quitLoop = True

            case "help":
                print("COMING SOON!")
            case _:
                print("Command not recognized, try \'help\' to see what commands are available.")

def main():
    sftp = NoneType
    menu(sftp)


if __name__ == "__main__":
    main()