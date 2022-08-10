import os

def isdir(path):
	try:
		return S_ISDIR(sftp.stat(path).st_mode)
	except IOError:
		return False

def deletedir(path):
	files = sftp.listdir(path=path)
	
	for f in files:
		filepath = os.path.join(path,f)
		if isdir(filepath):
			rm(filepath)
		else
			sftp.remove(filepath)
	sftp.rmdir(path)

