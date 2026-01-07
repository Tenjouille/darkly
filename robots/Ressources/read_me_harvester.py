#!/usr/bin/python3
import subprocess
url = "http://127.0.0.1:8080/.hidden/"


blacklist = [
	"Demande Ã  ton voisin du dessous",
	"Demande Ã  ton voisin du dessus",
	"Demande Ã  ton voisin de gauche",
	"Demande Ã  ton voisin de droite"
	"Non ce n'est toujours pas bon ...",
	"Tu veux de l'aide ? Moi aussi !",
	"Toujours pas tu vas craquer non ?",
]

def	getNextEndpoint(new_url):
	response = subprocess.run(["curl", "-ls", new_url], capture_output=True, text=True, encoding='latin1')
	res = response.stdout.split("href=")
	for chunk in res:
		if len(chunk) == 0 or chunk[0] != '"' or chunk[1:4] == "../":
			continue
		if chunk[:8] == '"README"':
			rd = subprocess.run(["curl", "-ls", new_url + "README"], capture_output=True, text=True, encoding='latin1')
			print("["+ rd.stdout.strip() + "]")
		else:
			endpoint = chunk[1:28]
			getNextEndpoint(new_url + endpoint)

if __name__ == "__main__":
	getNextEndpoint(url)
	print("DONE")

