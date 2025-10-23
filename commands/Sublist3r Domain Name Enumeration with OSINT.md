---
id: c4391d16-b30e-4054-b465-70efbad8c528
name: Sublist3r Domain Name Enumeration with OSINT
type: command
executor: bash
data: sublist3r -d $_DOMAIN
output: "root@kali:/opt/Sublist3r# ./sublist3r.py -d cisco.com           \n      \
  \                                                          \n                 ____\
  \        _     _ _     _   _____            \n                / ___| _   _| |__\
  \ | (_)___| |_|___ / _ __       \n                \\___ \\| | | | '_ \\| | / __|\
  \ __| |_ \\| '__|      \n                 ___) | |_| | |_) | | \\__ \\ |_ ___) |\
  \ |         \n                |____/ \\__,_|_.__/|_|_|___/\\__|____/|_|        \
  \ \n\n                # Coded By Ahmed Aboul-Ela - @aboul3la\n    \n[-] Enumerating\
  \ subdomains now for cisco.com\n[-] Searching now in Baidu..\n[-] Searching now\
  \ in Yahoo..\n[-] Searching now in Google..\n[-] Searching now in Bing..\n[-] Searching\
  \ now in Ask..\n[-] Searching now in Netcraft..\n[-] Searching now in DNSdumpster..\n\
  [-] Searching now in Virustotal..\n[-] Searching now in ThreatCrowd..\n[-] Searching\
  \ now in SSL Certificates..\n[-] Searching now in PassiveDNS..\n[-] Total Unique\
  \ Subdomains Found: 1255\nwww.cisco.com\n173-39-226-40.cisco.com\n173-39-227-1.cisco.com\n\
  173-39-234-141.cisco.com\n6lab.cisco.com"
created_at: '2019-09-12T17:55:35.975030+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Sublist3r Domain Name Enumeration with OSINT

```bash
sublist3r -d $_DOMAIN
```

## Expected Output

```
root@kali:/opt/Sublist3r# ./sublist3r.py -d cisco.com           
                                                                
                 ____        _     _ _     _   _____            
                / ___| _   _| |__ | (_)___| |_|___ / _ __       
                \___ \| | | | '_ \| | / __| __| |_ \| '__|      
                 ___) | |_| | |_) | | \__ \ |_ ___) | |         
                |____/ \__,_|_.__/|_|_|___/\__|____/|_|         

                # Coded By Ahmed Aboul-Ela - @aboul3la
    
[-] Enumerating subdomains now for cisco.com
[-] Searching now in Baidu..
[-] Searching now in Yahoo..
[-] Searching now in Google..
[-] Searching now in Bing..
[-] Searching now in Ask..
[-] Searching now in Netcraft..
[-] Searching now in DNSdumpster..
[-] Searching now in Virustotal..
[-] Searching now in ThreatCrowd..
[-] Searching now in SSL Certificates..
[-] Searching now in PassiveDNS..
[-] Total Unique Subdomains Found: 1255
www.cisco.com
173-39-226-40.cisco.com
173-39-227-1.cisco.com
173-39-234-141.cisco.com
6lab.cisco.com
```


