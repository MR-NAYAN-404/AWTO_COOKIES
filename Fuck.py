import os,platform,time,requests
P = "\x1b[1;97m"
M = "\x1b[1;91m"
H = "\x1b[1;92m"
K = "\x1b[1;93m"
B = "\x1b[1;94m"
U = "\x1b[1;95m" 
O = "\x1b[1;96m"
N = "\x1b[0m"
nm = random.choice([m,k,h,u,b])
bitt=platform.architecture()[0]

if bitt=="64bit":
    ip = requests.get("https://api.ipify.org").text
    os.system("clear");nm = random.choice([m,k,h,u,b]);print(f"[!]{nm} Your Device is 64 bit");time.sleep(1);print("\n\n[!] Your Ip : "+ip);time.sleep(1);print("\n\n[!] Your Python Version :");time.sleep(1);os.system("python --version")
    time.sleep(5)
    import cooking

else:

    print("\nYOUR DEVICE 32 BIT NOT SUPPORT")
