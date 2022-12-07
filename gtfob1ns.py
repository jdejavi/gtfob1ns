#!/usr/bin/env python3

'''
	Herramienta que tira de gtfobins pero a nivel de consola
		- Creada por: Javier Matilla Martín (aka m4t1)
'''


import requests, sys, pdb, signal, os, time, re, subprocess

#Ctrl + C

def ctrl_c(sig, frame):
	print("\n\n[*] Saliendo... \n")
	sys.exit(1)

signal.signal(signal.SIGINT, ctrl_c)

def banner():
	print("#"*100)
	print("#" + (" "*10) + "             /$$      /$$$$$$          /$$        /$$                      " + (" "*13)+"#")
	print("#" + (" "*10) + "            | $$     /$$__  $$        | $$      /$$$$                      " + (" "*13)+"#")
	print("#" + (" "*10) + "  /$$$$$$  /$$$$$$  | $$  \__//$$$$$$ | $$$$$$$|_  $$   /$$$$$$$   /$$$$$$$" + (" "*13)+"#")
	print("#" + (" "*10) + " /$$__  $$|_  $$_/  | $$$$   /$$__  $$| $$__  $$ | $$  | $$__  $$ /$$_____/" + (" "*13)+"#")
	print("#" + (" "*10) + "| $$  \ $$  | $$    | $$_/  | $$  \ $$| $$  \ $$ | $$  | $$  \ $$|  $$$$$$ " + (" "*13)+"#")
	print("#" + (" "*10) + "| $$  | $$  | $$ /$$| $$    | $$  | $$| $$  | $$ | $$  | $$  | $$ \____  $$" + (" "*13)+"#")
	print("#" + (" "*10) + "|  $$$$$$$  |  $$$$/| $$    |  $$$$$$/| $$$$$$$//$$$$$$| $$  | $$ /$$$$$$$/" + (" "*13)+"#")
	print("#" + (" "*10) + " \____  $$   \___/  |__/     \______/ |_______/|______/|__/  |__/|_______/ " + (" "*13)+"#")
	print("#" + (" "*10) + " /$$  \ $$                                                                 " + (" "*13)+"#")
	print("#" + (" "*10) + "|  $$$$$$/                                                                 " + (" "*13)+"#")
	print("#" + (" "*10) + " \______/                                                                  " + (" "*13)+"#")
	print("#" + (" "*60) + "By Javier Matilla (m4t1) <3" + (" "*11) + "#")
	print("#"*100)

def prettifier(url):

	listPermissionsTemp = re.findall("<h2(.*?)</h2>",str(url))
	listCommandsTemp = re.findall("<ul(.*?)</ul>",str(url))

	listPermFin = []
	listComFin = []
	for perm in listPermissionsTemp:
		formatted = re.findall("(?<=>)(.*)",perm)
		listPermFin.append(formatted)
	for com in listCommandsTemp:
		if(re.search("code",com)):
			fullform = re.findall("<code>(.*?)</code>",com)
			listComFin.append(fullform)

	for tupla in zip(listPermFin, listComFin):
		if(sys.argv[2] in tupla[0]):
			print("#"*30)
			print("#" + (" "*12) + tupla[0][0] + (" "*(30-(14+len(tupla[0][0])))) + "#")
			print("#"*30)
			print("\n")
			for com in tupla[1]:
				comm = re.sub("\$", "\\\$", com)
				print(os.popen('''echo "%s" 2>/dev/null | sed 's/\&quot;/\"/g' | sed 's/\&gt;/\>/g' | sed 's/\&lt;/\</g' | sed 's/\&amp/\&/g' | sed 's/\&nbsp;/\s/g' | sed "s/\&#39;/\'/g" | sed "s/\&;/\&/g" ''' % comm).read())
			print("\n")

#Main flow
if __name__ == '__main__':
	os.system("clear")
	banner()
	print("\n\n")
	if (len(sys.argv) != 3):
		print("\n\n[*] Mala especificación de comandos: python3 %s <function> <perm>\n" % sys.argv[0])
		print("[*] Ejemplo: python3 %s awk sudo" % sys.argv[0])
		print('[*] Ejemplo: python3 %s awk "File write"\n' % sys.argv[0])
		print("[*] Saliendo...")
		sys.exit(1)
	else:
		url= "https://gtfobins.github.io/gtfobins/%s/" % sys.argv[1]
		resp = requests.get(url)
		prettifier(resp.content)
