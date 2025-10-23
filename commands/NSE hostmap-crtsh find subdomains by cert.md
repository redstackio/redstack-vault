---
id: ba1e442a-e4f8-46b8-b9b6-d1db825cab5d
name: NSE hostmap-crtsh find subdomains by cert
type: command
executor: ''
data: nmap -sn --script hostmap-crtsh $_TARGET_DOMAIN
output: "root@kali ~/owasp.org=# nmap -sn --script hostmap-crtsh redstack.io\nStarting\
  \ Nmap 7.70 ( https://nmap.org ) at 2020-06-29 21:32 EDT\nNmap scan report for redstack.io\
  \ (99.84.71.85)\nHost is up (0.00019s latency).\nOther addresses for redstack.io\
  \ (not scanned): 99.84.71.69 99.84.71.60 99.84.71.49\nrDNS record for 99.84.71.85:\
  \ server-99-84-71-85.hio50.r.cloudfront.net\n\nHost script results:\n| hostmap-crtsh:\
  \ \n|   subdomains: \n|_    *.redstack.io\\nredstack.io\n\nNmap done: 1 IP address\
  \ (1 host up) scanned in 1.21 seconds\n"
created_at: '2020-06-30T01:33:49.185132+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# NSE hostmap-crtsh find subdomains by cert

```bash
nmap -sn --script hostmap-crtsh $_TARGET_DOMAIN
```

## Expected Output

```
root@kali ~/owasp.org=# nmap -sn --script hostmap-crtsh redstack.io
Starting Nmap 7.70 ( https://nmap.org ) at 2020-06-29 21:32 EDT
Nmap scan report for redstack.io (99.84.71.85)
Host is up (0.00019s latency).
Other addresses for redstack.io (not scanned): 99.84.71.69 99.84.71.60 99.84.71.49
rDNS record for 99.84.71.85: server-99-84-71-85.hio50.r.cloudfront.net

Host script results:
| hostmap-crtsh: 
|   subdomains: 
|_    *.redstack.io\nredstack.io

Nmap done: 1 IP address (1 host up) scanned in 1.21 seconds

```


