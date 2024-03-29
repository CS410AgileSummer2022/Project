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
                if sftp == NoneType:
                            print("Not logged into a remote server")
                            continue

                if(commandLen > 1):
                    client.makeDir(sftp, command[1])
                else:
                    print("Please input a directory name.")

            case "chmod":
                if sftp == NoneType:
                            print("Not logged into a remote server")
                            continue

                if(commandLen > 2):
                    client.chmod(sftp, command[1], command[2])
                elif(commandLen > 1):
                    print("Please enter the octal permission.")
                else:
                    print("Please input the file path.")

            case "ls":
                flag = None
                if ("-l" in command): 
                    command.remove("-l")
                    flag = "-l"
                elif ("-r" in command):
                    command.remove("-r")
                    flag = "-r"
                commandLen = len(command)

                if flag == "-l":
                    match commandLen:
                        case 2:
                            client.printLocalDirectory(command[1])
                        case 1:
                            client.printLocalDirectory(".")
                        case _:
                            print("ls takes two arguments.")
                elif flag == "-r":
                    if sftp == NoneType:
                            print("Not logged into a remote server")
                            continue

                    match commandLen:
                        case 2:
                            client.printRemoteDirectory(sftp, command[1])
                        case 1:
                            client.printRemoteDirectory(sftp, ".")
                        case _:
                            print("ls takes two arguments.")
                else:
                    print("Please specify a local or remote repository with -l or -r.")

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
                    if(commandLen == 3): 
                        client.getFile(sftp, command[1], command[2])
                    else:
                        print("Please specify a source and destination path.")

            case "put":
                flag = None
                if ("-m" in command):
                    flag = "-m"
                    command.remove("-m")
                commandLen = len(command)
                
                if (flag == "-m"):
                    if (commandLen == 1):
                        files = client.getMultipleList()
                        dest = input("Enter the destination path: ")
                        client.putMultiple(sftp, files, dest)
                    else:
                        files = command[1:-1]
                        client.putMultiple(sftp, files, command[-1])
                else:
                    if (commandLen == 3):
                        client.putFile(sftp, command[1], command[2])
                    else:
                        print("Please specify a source and destination path.")

            case "mv":
                if("-r" in command):
                    if sftp == NoneType:
                            print("Not logged into a remote server")
                            continue

                    command.remove("-r")
                    commandLen = len(command)
                    if(commandLen > 2):
                        client.renameRemoteFile(sftp, command[1], command[2])
                    else:
                        print("Please enter the full path to the file you'd like to rename and the name of the new file.")
                elif("-l" in command):
                    command.remove("-l")
                    commandLen = len(command)
                    if(commandLen > 2):
                        client.renameLocalFile(sftp, command[1], command[2])
                    else:
                        print("Please enter the full path to the file you'd like to rename and the name of the new file.")
                else:
                    if(commandLen > 2):
                        client.renameLocalFile(command[1], command[2])
                    else:
                        print("Please enter the full path to the file you'd like to rename and the name of the new file.")

            case "search":
                flag = None
                if ("-l" in command): 
                    command.remove("-l")
                    flag = "-l"
                elif ("-r" in command):
                    command.remove("-r")
                    flag = "-r"
                commandLen = len(command)

                locations = None
                if flag == "-l":
                    # Due to the way commands are handled,
                    # filenames CANNOT contain spaces if they're entered at the command level.
                    # That's basically unacceptable (in my opinion),
                    # so as a workaround, filenames are entered inside the command logic instead.
                    filename = input("Enter the name of the file you wish to search for: ")
                    path = input("Enter the path you wish to search in: ") 
                    locations = client.localSearch(filename, path)
                elif flag == "-r":
                    print("not yet implemented - sit tight!")
                else:
                    print("Please specify a local or remote search with -l or -r.")

                if locations:
                    for location in locations:
                        print("Found at", location)
                        
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
                print(
                "login: Log in to a remote server.\n"
                "logoff: Log off of the remote server.\n"
                "mkdir: Make a directory on the remote server.\n"
                "chmod: Change permissions of a file on the remote server.\n"
                "ls <-l / -r>: List the contents of a directory on the <local / remote> machine.\n"
                "get <-m>: Get <multiple> files from the remote server and move them to the local machine.\n"
                "put <-m>: Put <multiple> files on the remote server from the local machine.\n"
                "mv <-l / -r>: Move files <locally / remotely>.\n"
                "search <-l / -r>: Search for a file on the <local / remote> machine.\n"
                "xcopy: Copy a file or folder on the remote server."
                )

            case _:
                print("Command not recognized, try \'help\' to see what commands are available.")

def main():
    sftp = NoneType
    menu(sftp)


if __name__ == "__main__":
    main()
