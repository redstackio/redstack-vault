---
id: 54edbce5-cad1-48cb-8d71-acf146c3074b
name: DNSRecon Brute Force DNS Subdomains
type: command
executor: ''
data: dnsrecon -d $_TARGET_DOMAIN -t brt -D $_FULL_PATH_TO_DICTIONARY
output: 'root@kali:~# dnsrecon -d testsite.com -D `pwd`/words.txt -t brt

  [*] Performing host and subdomain brute force against testsite.com

  [*]      A home.testsite.com 127.0.0.1

  [*]      AAAA deadbeef.testsite.com dead:beaf::

  [*]      A asfdbbox.testsite.com 127.0.0.1

  [*]      A canberra-office.testsite.com 203.22.87.231

  [*]      A dc-office.testsite.com 126.138.222.133

  [*]      A email.testsite.com 69.76.28.144

  [*]      A intns2.testsite.com 69.76.27.21

  [*]      A office.testsite.com 14.25.64.223

  [*]      A owa.testsite.com 109.64.224.85

  [*]      A intns1.testsite.com 82.64.74.22

  [*]      A vpn.testsite.com 188.24.86.169

  [*]      A www.testsite.com 3.23.54.21

  [+] 12 Records Found'
created_at: '2019-09-20T18:53:20.015420+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# DNSRecon Brute Force DNS Subdomains

```bash
dnsrecon -d $_TARGET_DOMAIN -t brt -D $_FULL_PATH_TO_DICTIONARY
```

## Expected Output

```
root@kali:~# dnsrecon -d testsite.com -D `pwd`/words.txt -t brt
[*] Performing host and subdomain brute force against testsite.com
[*]      A home.testsite.com 127.0.0.1
[*]      AAAA deadbeef.testsite.com dead:beaf::
[*]      A asfdbbox.testsite.com 127.0.0.1
[*]      A canberra-office.testsite.com 203.22.87.231
[*]      A dc-office.testsite.com 126.138.222.133
[*]      A email.testsite.com 69.76.28.144
[*]      A intns2.testsite.com 69.76.27.21
[*]      A office.testsite.com 14.25.64.223
[*]      A owa.testsite.com 109.64.224.85
[*]      A intns1.testsite.com 82.64.74.22
[*]      A vpn.testsite.com 188.24.86.169
[*]      A www.testsite.com 3.23.54.21
[+] 12 Records Found
```
