import os
print ("""



ini hanya persiapan supaya enak jalanin script



""")

print ("""pakai mana masbro?\n \033[39m[1] Termux\033[39m\n \033[38m[2] nethunter\033[38m\n""")

c = input(">>>: ")
if c == "1":
    os.system ("pkg install x11-repo -y")
    os.system ("pkg install python3 -y")
    os.system ("pkg upgrade python3 -y")
    os.system ("pkg install pip -y")
    os.system ("pkg install wget -y")
    os.system ("pkg install openjdk-17 -y")
    os.system ("pkg install golang -y")
    os.system ("pkg install gem -y")
    os.system ("pkg install nmap -y")
    os.system ("pkg install mailutils")
    os.system ("pkg install nodejs")
    os.system ("pkg install openssl")
    os.system ("pkg install perl")
    os.system ("pip install requests")
    os.system ("pip install thread")
    os.system ("pip install colorama")
    os.system ("pip install socks")
    os.system ("pip install pysocks")
    os.system ("pip install pyqt5")
    os.system ("pip install httpx")
    os.system ("pip install cloudscraper")
    os.system ("pip install times")
    os.system ("pip install bs4")
    os.system ("pip install mechanize")
    os.system ("pip install undetected_chromedriver")
    os.system ("pip install ipaddress")
    os.system ("pip install webhooks")
    os.system ("pip install netlib")
    os.system ("pip install pyproject.toml")
    os.system ("pip install dnspython")
    os.system ("pip install scapy")
    os.system ("pip install mechanize")
    os.system ("pip install ipaddress")
    os.system ("pip install --upgrade pip")
    os.system ("apt-get update && apt-get full-upgrade -y")
    os.system ("apt-get dist-upgrade -y")
    os.system ("apt-get autoremove")
    os.system ("chmod +777 run")
    
elif c == "2":
    
    os.system ("sudo apt install wget -y")
    os.system ("sudo apt install build-essential zlib1g-dev libncurses-devlib libgdbm-dev libnss3 libssl-dev libsqlite3-dev libreadline-dev libffi-dev curl libbz2-dev -y")
    os.system ("wget https://www.python.org/ftp/python/3.12.5/Python-3.12.5.tgz")
    os.system ("tar -xvf Python-3.12.5.tgz")
    os.system ("rm Python-3.12.5.tgz")
    os.system ("cd Python-3.12.5 && sudo ./configure --enable-optimizations && sudo make install")
    os.system ("sudo apt upgrade python3 -y")
    os.system ("sudo dpkg --configure -a")
    os.system ("sudo apt install python-is-python3 -y")
    os.system ("sudo apt install pip -y")
    os.system ("sudo apt install default-jdk -y")
    os.system ("sudo apt install golang -y")
    os.system ("sudo apt install gem -y")
    os.system ("sudo apt install nmap -y")
    os.system ("sudo apt install mailcap -y")
    os.system ("sudo apt install sparrow-wifi -y")
    os.system ("sudo apt install openssl")
    os.system ("sudo apt install nodejs")
    os.system ("sudo apt install perl")
    os.system ("pip install requests")
    os.system ("pip install colorama")
    os.system ("pip install thread")
    os.system ("pip install netlib")
    os.system ("pip install pyproject.toml")
    os.system ("pip install dnspython")
    os.system ("pip install socks")
    os.system ("pip install pyroxy")
    os.system ("pip install pysocks")
    os.system ("pip install pyqt5")
    os.system ("pip install httpx")
    os.system ("pip install cloudscraper")
    os.system ("pip install times")
    os.system ("pip install bs4")
    os.system ("pip install mechanize")
    os.system ("pip install undetected_chromedriver")
    os.system ("pip install ipaddress")
    os.system ("pip install scapy")
    os.system ("pip install --upgrade pip")
    os.system ("sudo apt install webhooks")
    os.system ("sudo rm -fr /var/lib/dpkg/info/postgresql* && sudo dpkg --configure -a")
    os.system ("sudo apt update && sudo apt full-upgrade -y")
    os.system ("sudo apt dist-upgrade -y")
    os.system ("sudo apt autoremove")
    os.system ("sudo chmod +777 run")
    
if os.name == "nt":
    pass
    
else:
    os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
    os.system("apt-get install ./google-chrome-stable_current_amd64.deb")
    
print ("""
    SUDAH SELESAI KAKA
    """)