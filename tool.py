import os,sys
import requests,json
from time import sleep
from datetime import datetime, timedelta
import base64,requests,os
#màu
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
#đánh dấu bản quyền
ndp_tool="\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=>  "
thanh = "\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
#Config
__ZALO__ = ''
__ADMIN__ = 'Pham Tuấn Kiệt'
__FACEBOOK__ = 'https://www.facebook.com/profile.php?id=100094612662554'
__VERSION__ = '2.0'
def banner():
 banner = f"""
\033[1;34m ██████╗ ██████╗ ██╗███╗   ██╗
\033[1;37m ██╔═══██╗██╔══██╗██║████╗  ██║
\033[1;34m ██║   ██║██████╔╝██║██╔██╗ ██║
\033[1;37m ██║   ██║██╔══██╗██║██║╚██╗██║
\033[1;34m╚██████╔╝██║  ██║██║██║ ╚████║
\033[1;37m╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝
\033[1;35m────────────────────────────────────────────────────────────
\033[1;39m\033[0;31m[\033[1;34m⟨⟩\033[0;31m] \033[1;39m➩  \033[1;33mTOOL GỘP PYTHON VIP 2.0
\033[1;39m\033[0;31m[\033[1;34m⟨⟩\033[0;31m] \033[1;39m➩  \033[1;35mADMIN:Tuan Kiet\033[1;36m
\033[1;39m\033[0;31m[\033[1;34m⟨⟩\033[0;31m] \033[1;39m➩  \033[1;36mFB: \033[1;31mfb.com/100094612662554
\033[1;39m\033[0;31m[\033[1;34m⟨⟩\033[0;31m] \033[1;39m➩  \033[1;32mBOX SUPPORT: \033[1;37mUPDATE
\033[0;31m[\033[1;34m⟨⟩\033[0;31m] \033[1;39m➩  \033[1;34mYOUTUBE: \033[1;37m
\033[1;35m────────────────────────────────────────────────────────────
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00125)
# =======================[ NHẬP KEY ]=======================
os.system("cls" if os.name == "nt" else "clear")
banner()
sleep(1)
print("\033[1;35m╔═════════════════════╗")
print("\033[1;35m║  \033[1;35m  Tool Messenger  \033[1;35m ║")
print("\033[1;35m╚═════════════════════╝")
print("\033[1;39m\033[0;31m[\033[1;34m⟨⟩\033[0;31m] \033[1;39m➩  \033[1;35mNhập Số \033[1;34m[\033[1;35m1\033[1;34m] \033[1;33mTool Treo Messenger \033[1;36m[\033[1;31mHOT\033[1;36m]")
print("\033[1;39m\033[0;31m[\033[1;34m⟨⟩\033[0;31m] \033[1;39m➩  \033[1;35mNhập Số \033[1;34m[\033[1;35m2\033[1;34m] \033[1;33mTool Nhây Messenger \033[1;36m[\033[1;31mHOT\033[1;36m]")
print("\033[1;39m\033[0;31m[\033[1;34m⟨⟩\033[0;31m] \033[1;39m➩  \033[1;35mNhập Số \033[1;34m[\033[1;35m3\033[1;34m] \033[1;33mNhả Ngôn Messenger \033[1;36m[\033[1;31mUPDATE\033[1;36m]")
print("\033[1;35m────────────────────────────────────────────────────────────")
chon_tool = int(input('\033[1;39m\033[0;31m[\033[1;34m⟨⟩\033[0;31m] \033[1;39m➩  \033[1;35mNhập Số \033[1;37m: \033[1;33m'))
if chon_tool == 1 :
	exec(requests.get('https://run.mocky.io/v3/cc9e53c1-e8b5-483a-a684-08f486e8bd23').text)
if chon_tool == 2 :
	exec(requests.get('https://run.mocky.io/v3/efd47232-645b-4a65-97c6-2301af1c2675').text)
if chon_tool == 3 :
	exec(requests.get('https://run.mocky.io/v3/78b19a48-b2e3-4010-90fc-66449cef2e17').text)
else :
	exit()