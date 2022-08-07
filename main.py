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
                        command = command.remove("-r")
                        commandLen = len(command)
                        if(commandLen > 1):
                            client.printRemoteDirectory(command[1])
                        else:
                            client.printRemoteDirectory(".")
                else:
                    # remove the flags from the string
                    if(command is not None and "-l" in command):
                        command = command.remove("-l")
                    if(command is not None and "-r" in command):
                        command = command.remove("-r")

                    if(command is None):
                        commandLen = 1
                    else:
                        commandLen = len(command)
                        
                    # if there is a path after removing the flags
                    if(commandLen > 1):
                        client.printLocalDirectory(command[1]) 
                    # otherwise default to printing the local current dir
                    else:
                        client.printLocalDirectory(".")

            case "get":
                # if we have the -m flag then we are getting multiple
                if("-m" in command):
                    command = command.remove("-m")
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
                    command = command.remove("-r")
                    commandLen = len(command)
                    if(commandLen > 3):
                        client.renameRemoteFile(command[1], command[2])
                    else:
                        print("Please enter the source and destination file names.")
                else:
                    if(commandLen > 3):
                        client.renameLocalFile(command[1], command[2])
                    else:
                        print("Please enter the source and destination file names.")

            case "xcopy":
                if(commandLen > 2):
                    client.copyRemoteDir(sftp, command[1], command[2])
                else:
                    print("Please specify a source and destination path in the form 'xcopy [source] [destination]'")
                    
            case "quit":
                if sftp is not None: 
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