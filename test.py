import os
try:
	import requests
except:
	os.system("pip install requests")
	import requests
version="2.2.9"
blue= '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan  = "\033[96m"
end = '\033[0m'
line=yellow+"======================================================================================================================"
logo=red+str("""
     .oOOOo.     Oo    `o    O  ooOoOOo  o
     o     o    o  O    o   O      O    O 
     O.        O    o   O  O       o    o   
     `OOoo.  oOooOoOo  oOo        O    o   
     `O o      O  o  o       o    O   
     o O      o  O   O      O    O   
     O.    .O o      O  o    o     O    o     .  
      `oooO'  O.     O  O     O ooOOoOo OOoOooO""")
     
slogan2="                   ★★★ 𝔹𝔼 𝔸ℕ 𝔼𝕋ℍ𝕀ℂ𝔸𝕃 ★★★                      "
header=logo+cyan+"\n\n\n\t\tDeveloped By : Sanaur Asif\n\n"+green+"\t\t     Version : "+str(version)+" \n\n"+end+line+"\n"+end

print_check=requests.get("https://pastebin.com/raw/8iYF39Zc").text

if print_check=="header":
	print(header)
elif print_check=="logo":
	print(logo)
elif print_check=="slogan2":
	print(slogan2)