import os
import requests

# Fungsi untuk menghapus file proxy.txt
def remove_proxy_file():
    proxy_file = "proxy.txt"
    if os.path.exists(proxy_file):
        os.remove(proxy_file)
        print("File proxy.txt berhasil dihapus")
    else:
        print("File proxy.txt tidak ditemukan")

# Fungsi untuk mendapatkan daftar proxy dari API URL
def get_proxy_list(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        proxy_list = response.text.split("\n")
        return proxy_list
    else:
        print("Gagal mendapatkan daftar proxy dari", api_url)
        return []

# API URL yang akan digunakan
api_urls = [
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
    "https://api.proxyscrape.com/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
    "https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&protocol=http&proxy_format=ipport&format=text&timeout=15005",
    "https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&protocol=http&proxy_format=ipport&format=text&anonymity=Elite&timeout=15005",
    "https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&protocol=http&proxy_format=ipport&format=text&anonymity=Anonymous&timeout=15005",
    "https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&protocol=http&proxy_format=ipport&format=text&anonymity=Transparent&timeout=15005",
    "https://yakumo.rei.my.id/HTTP",
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=anonymous",
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
    "https://yakumo.rei.my.id/SOCKS4",
    "https://yakumo.rei.my.id/SOCKS5",
    "https://raw.githubusercontent.com/Hhhusvdjwhsh/Fuckproxy/main/list.txt",
    "https://api.openproxylist.xyz/http.txt",
    "https://api.openproxylist.xyz/socks4.txt",
    "https://rootjazz.com/proxies/proxies.txt",
    "https://api.proxyscrape.com/v2/?request=displayproxies",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks5/socks5.txt",
    "https://github.com/officialputuid/KangProxy/blob/KangProxy/socks4/socks4.txt",
    "https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&format=text",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
    "https://raw.githubusercontent.com/yuceltoluyag/GoodProxy/main/raw.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
    "https://proxyspace.pro/http.txt",
    "https://api.proxyscrape.com/?request=displayproxies&proxytype=http",
    "http://worm.rip/http.txt",
    "http://alexa.lr2b.com/proxylist.txt",
    "https://api.openproxylist.xyz/http.txt",
    "http://rootjazz.com/proxies/proxies.txt",
    "https://multiproxy.org/txt_all/proxy.txt",
    "https://proxy-spider.com/api/proxies.example.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
    "https://proxyspace.pro/socks5.txt",
    "http://worm.rip/socks5.txt",
    "https://api.openproxylist.xyz/socks5.txt",
    "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
    "https://github.com/mmpx12/proxy-list/blob/master/socks4.txt",
    "https://proxyspace.pro/socks4.txt",
    "http://worm.rip/socks4.txt",
    "https://api.openproxylist.xyz/socks4.txt"
]

# Menghapus file proxy.txt jika sudah ada
remove_proxy_file()

# Mengambil daftar proxy dari setiap API URL dan menyimpannya ke file proxy.txt
for api_url in api_urls:
    proxy_list = get_proxy_list(api_url)
    with open("proxy.txt", "a") as file:
        for proxy in proxy_list:
            file.write(proxy + "\n")

print("Daftar proxy telah berhasil disimpan di file proxy.txt")