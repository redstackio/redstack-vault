---
id: 3637dbfc-ff2c-4e68-ad66-47bb117cad01
name: Nmap Enumerate SMTP Server with Scripts
type: command
executor: null
data: nmap --script smtp* -p25 $_TARGET_IP
output: "root@kali:~# nmap --script smtp* -p25 10.10.10.10\nStarting Nmap 7.70 ( https://nmap.org\
  \ ) at 2019-09-24 15:31 EDT\nNmap scan report for 10.10.10.10\nHost is up (0.00032s\
  \ latency).\n\nPORT   STATE SERVICE\n25/tcp open  smtp\n|_smtp-commands: host.localdomain,\
  \ PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME,\
  \ DSN, \n| smtp-enum-users: \n|_  Method RCPT returned a unhandled status code.\n\
  |_smtp-open-relay: Server doesn't seem to be an open relay, all tests failed\n|\
  \ smtp-vuln-cve2010-4344: \n|_  The SMTP server is not Exim: NOT VULNERABLE\nMAC\
  \ Address: 08:00:27:31:27:7A (Oracle VirtualBox virtual NIC)\n\nNmap done: 1 IP\
  \ address (1 host up) scanned in 21.53 seconds"
created_at: '2019-09-24T19:45:11.088786+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Nmap]]'
- '[[host]]'
---

# Nmap Enumerate SMTP Server with Scripts

```bash
nmap --script smtp* -p25 $_TARGET_IP
```

## Expected Output

```
root@kali:~# nmap --script smtp* -p25 10.10.10.10
Starting Nmap 7.70 ( https://nmap.org ) at 2019-09-24 15:31 EDT
Nmap scan report for 10.10.10.10
Host is up (0.00032s latency).

PORT   STATE SERVICE
25/tcp open  smtp
|_smtp-commands: host.localdomain, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN, 
| smtp-enum-users: 
|_  Method RCPT returned a unhandled status code.
|_smtp-open-relay: Server doesn't seem to be an open relay, all tests failed
| smtp-vuln-cve2010-4344: 
|_  The SMTP server is not Exim: NOT VULNERABLE
MAC Address: 08:00:27:31:27:7A (Oracle VirtualBox virtual NIC)

Nmap done: 1 IP address (1 host up) scanned in 21.53 seconds
```


