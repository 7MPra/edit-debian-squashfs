import sys
import os
def index_Multi(List,liter):
	index_L = []
	for val in range(0,len(List)):
		if liter == List[val]:
		index_L.append(val)
	return index_L

if "-f" in sys.argv:
	filesystem = sys.argv[sys.argv.index("-f")]
elif "--filesystem":
	filesystem = sys.argv[sys.argv.index("--filesystem")]
else:
	print("{} : File system file not specified")
	sys.exit(1)

inaddfile = index_Multi(sys.argv,"-a")
inaddfile += index_Multi(sys.argv,"--add")

inremovefile = index_Multi(sys.argv,"-r")
inremovefile += index_Multi(sys.argv,"--remove")

inpurgepack = index_Multi(sys.argv,"-p")
inpurgepack += index_Multi(sys.argv,"--purge")

ininstallpack = index_Multi(sys.argv,"-i")
ininstallpack += index_Multi(sys.argv,"--install")

indebfile = index_Multi(sys.argv,"-d")
indebfile += index_Multi(sys.argv,"--debfile")

addfile = [ { sys.argv[i+1] : sys.argv[i+2] } for i in inaddfile]

removefile = [sys.argv[i+1] for i in inremovefile]

purgepack = [sys.argv[i+1] for i in inpurgepack]

installpack = [sys.argv[i+1] for i in ininstallpack]

debfile = [sys.argv[i+1] for i in indebfile]

for r in addfiles:
	if not os.path.isfile(list(r.keys())[0]) or os.path.isdir(list(r.keys())[0]):
		print("{} : error : {} is not file.".format(sys.argv[0],list(r.keys())[0]))
		sys.exit(1)
	if r[list(r.keys())[0]][0] != "/":
		print("{} : error : {} is not full path.".format(sys.argv[0],r[list(r.keys())[0]]))
		sys.exit(1)

for r in removefile:
	if r[0] != "/"
		print("{} : error : {} is not full path.".format(sys.argv[0],r[0]))
		sys.exit(1)

for r in debfile:
	if not os.path.isfile(r):
		print("{} : error : {} is not found.".format(sys.argv[0],r))

with open("runsquashfs.sh","w") as f:
	f.write("#!/bin/bash\n")
	if purgepack != []:
		for r in purgepack:
			f.write("sudo apt-get remove -y --purge --autoremove {}/n".format(r))
	if installpack != []:
		for r in installpack:
			f.write("sudo apt-get install  -y {}/n".format(r))
	if debpack != []:
		f.write("cd root/\n")
		for r in debpack:
			f.write("sudo apt-get install  -y ./{}/n".format(r))
		f.write("rm *.deb\n")
		f.write("cd ../\n")

os.system("unsquashfs {}".format(filesystem))

for r in addfiles:
	if os.path.exists("./squashfs-root{}".format(r[list(r.keys())[0]]))
		if os.path.isdir(list(r.keys())[0]):
			if os.path.exists("./squashfs-root{}/{}".format(r[list(r.keys())[0]],os.path.basename(list(r.keys())[0]))
				os.system("rm -r ./squashfs-root/{}/{}".format(r[list(r.keys())[0]],os.path.basename(list(r.keys())[0])))
		os.system("cp -r {} squashfs-root/{}".format(list(r.keys())[0],r[list(r.keys())[0]]))

for r in removefile:
	if os.path.exists("./squashfs-root{}".format(r)):
		os.system("rm -r ./squashfs-root{}".format(r))

for r in debpack:
	os.system("cp -r {} squashfs-root/root/".format(r)

os.system("chroot squashfs-root/ /bin/bash runsquashfs.sh")
os.system("rm {}".format(filesystem))
os.system("mksquashfs squashfs-root/ {}".format(filesystem)
