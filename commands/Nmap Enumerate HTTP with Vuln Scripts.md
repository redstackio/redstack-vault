---
id: e459592f-6b52-4444-9592-8897321b36a0
name: Nmap Enumerate HTTP with Vuln Scripts
type: command
executor: bash
data: nmap --script vuln -p $_TARGET_PORT $_TARGET_IP
output: "root@kali:~# nmap --script vuln -p80 10.10.10.10\nStarting Nmap 7.70 ( https://nmap.org\
  \ ) at 2019-09-13 18:11 EDT\nNmap scan report for 10.10.10.10\nHost is up (0.00036s\
  \ latency).\n\nPORT   STATE SERVICE\n80/tcp open  http\n|_http-dombased-xss: Couldn't\
  \ find any DOM based XSS.\n| http-enum: \n|   /tikiwiki/: Tikiwiki\n|   /test/:\
  \ Test page\n|   /phpinfo.php: Possible information file\n|   /phpMyAdmin/: phpMyAdmin\n\
  |   /doc/: Potentially interesting directory w/ listing on 'apache/2.2.8 (ubuntu)\
  \ dav/2'\n|   /icons/: Potentially interesting folder w/ directory listing\n|_ \
  \ /index/: Potentially interesting folder\nMAC Address: 08:00:27:31:27:7A (Oracle\
  \ VirtualBox virtual NIC)\n\nNmap done: 1 IP address (1 host up) scanned in 320.97\
  \ seconds"
created_at: '2019-09-13T22:29:10.939839+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Nmap Enumerate HTTP with Vuln Scripts

```bash
nmap --script vuln -p $_TARGET_PORT $_TARGET_IP
```

## Expected Output

```
root@kali:~# nmap --script vuln -p80 10.10.10.10
Starting Nmap 7.70 ( https://nmap.org ) at 2019-09-13 18:11 EDT
Nmap scan report for 10.10.10.10
Host is up (0.00036s latency).

PORT   STATE SERVICE
80/tcp open  http
|_http-dombased-xss: Couldn't find any DOM based XSS.
| http-enum: 
|   /tikiwiki/: Tikiwiki
|   /test/: Test page
|   /phpinfo.php: Possible information file
|   /phpMyAdmin/: phpMyAdmin
|   /doc/: Potentially interesting directory w/ listing on 'apache/2.2.8 (ubuntu) dav/2'
|   /icons/: Potentially interesting folder w/ directory listing
|_  /index/: Potentially interesting folder
MAC Address: 08:00:27:31:27:7A (Oracle VirtualBox virtual NIC)

Nmap done: 1 IP address (1 host up) scanned in 320.97 seconds
```


