import os,platform,time,requests

bitt=platform.architecture()[0]

if bitt=="64bit":
    ip = requests.get("https://api.ipify.org").text
    os.system('clear');print('[!] Your Device is 64 bit');time.sleep(1);print('\n\n[!] Your Ip : '+ip);time.sleep(1);print('\n\n[!] Your Python Version :');time.sleep(1);os.system('python --version')
    time.sleep(5)
    import cooking

else:

    print('\nYOUR DEVICE 32 BIT NOT SUPPORT')
