---
id: 1ede7371-6186-4bb5-b7b9-ee8b071f3e11
name: Nmap Service Scan of a Single Port
type: command
executor: bash
data: nmap -p $_TARGET_PORT -sV $_TARGET_IP
output: 'root@kali:~# nmap -p80 -sV 10.10.10.10

  Starting Nmap 7.70 ( https://nmap.org ) at 2019-09-13 17:52 EDT

  Nmap scan report for 10.10.10.10

  Host is up (0.00030s latency).


  PORT   STATE SERVICE VERSION

  80/tcp open  http    Apache httpd 2.2.8 ((Ubuntu) DAV/2)

  MAC Address: 08:00:27:31:27:7A (Oracle VirtualBox virtual NIC)


  Service detection performed. Please report any incorrect results at https://nmap.org/submit/
  .

  Nmap done: 1 IP address (1 host up) scanned in 6.55 seconds'
created_at: '2019-09-13T22:29:10.934214+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Nmap]]'
- '[[host]]'
---

# Nmap Service Scan of a Single Port

```bash
nmap -p $_TARGET_PORT -sV $_TARGET_IP
```

## Expected Output

```
root@kali:~# nmap -p80 -sV 10.10.10.10
Starting Nmap 7.70 ( https://nmap.org ) at 2019-09-13 17:52 EDT
Nmap scan report for 10.10.10.10
Host is up (0.00030s latency).

PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.2.8 ((Ubuntu) DAV/2)
MAC Address: 08:00:27:31:27:7A (Oracle VirtualBox virtual NIC)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 6.55 seconds
```


