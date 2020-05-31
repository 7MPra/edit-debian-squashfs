import sys
import os
import pathlib
def index_Multi(List,liter):
	index_L = []
	for val in range(0,len(List)):
		if liter == List[val]:
			index_L.append(val)
	return index_L

if "-f" in sys.argv:
	filesystem = sys.argv[sys.argv.index("-f")+1]
elif "--filesystem":
	filesystem = sys.argv[sys.argv.index("--filesystem")+1]
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

incmd = index_Multi(sys.argv,"-c")
incmd += index_Multi(sys.argv,"--command")

addfile = [ { sys.argv[i+1] : sys.argv[i+2] } for i in inaddfile]

removefile = [sys.argv[i+1] for i in inremovefile]

purgepack = [sys.argv[i+1] for i in inpurgepack]

installpack = [sys.argv[i+1] for i in ininstallpack]

debfile = [sys.argv[i+1] for i in indebfile]

cmd = [sys.argv[i+1] for i in incmd]

for r in addfile:
	fromlist = list(r.keys())
	fromfile = fromlist[0]
	tofile = r[fromfile]
	if os.path.isfile(fromfile):
		pass
	elif os.path.isdir(fromfile):
		pass
	else:
		print("{} : error : {} is not file or dirctory.".format(sys.argv[0],fromfile))
		sys.exit(1)
	if tofile[0] != "/":
		print("{} : error : {} is not full path.".format(sys.argv[0],tofile))
		sys.exit(1)
	print("copy from {} to ./squashfs-root{}".format(fromfile,tofile))

for r in removefile:
	if r[0] != "/":
		print("{} : error : {} is not full path.".format(sys.argv[0],r))
		sys.exit(1)
	print("remove {}".format(r))

for r in debfile:
	if not os.path.isfile(r):
		print("{} : error : {} is not found.".format(sys.argv[0],r))
	print("install {}".format(r))

with open("runsquashfs.sh","w") as f:
	f.write("#!/bin/bash\n")
	if purgepack != []:
		for r in purgepack:
			f.write("sudo apt-get remove -y --purge --autoremove {}\n".format(r))
			print("purge {}".format(r))
	if installpack != []:
		f.write("sudo apt-get update\n")
		for r in installpack:
			f.write("sudo apt-get install  -y {}\n".format(r))
			print("install {}".format(r))
	if debfile != []:
		f.write("sudo apt-get install -y gdebi\n")
		for r in debfile:
			f.write("sudo apt-get install  -y /root/{}\n".format(os.path.basename(r)))
		f.write("rm /root/*.deb\n")
	if cmd != []:
		for r in cmd:
			f.write("{}\n".format(r))

print("now unpacking {}".format(filesystem))
os.system("unsquashfs {}".format(filesystem))

with open("./squashfs-root/etc/resolv.conf","w") as f:
	f.write("nameserver 1.1.1.1\n")
	f.write("nameserver 8.8.8.8\n")

for r in debfile:
	os.system("cp {} squashfs-root/root/".format(r))
	print("copy {} to /root/".format(r))

os.system("cp ./runsquashfs.sh ./squashfs-root/root/")

os.system("sudo chroot squashfs-root/ bash /root/runsquashfs.sh")

for r in addfile:
	fromlist = list(r.keys())
	fromfile = fromlist[0]
	tofile = r[fromfile]
	if tofile[-1] != "/":
		tofile += "/"
	print("copy from {} to {}".format(fromfile,tofile))
	if os.path.exists("./squashfs-root{}".format(tofile)):
		if os.path.isdir(fromfile):
			if os.path.exists("./squashfs-root{}{}".format(tofile,pathlib.Path(fromfile).name)):
				os.system("rm -r ./squashfs-root/{}{}".format(tofile,pathlib.Path(fromfile).name))
			os.system("cp -r {} ./squashfs-root{}".format(fromfile,tofile))
		else:
			os.system("cp {} ./squashfs-root{}".format(fromfile,tofile))

for r in removefile:
	if os.path.exists("./squashfs-root{}".format(r)):
		os.system("rm -r ./squashfs-root{}".format(r))

