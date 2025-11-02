---
id: fc2e0c0c-7263-4709-90ce-ee6fc08cbede
name: Nmap Port Scan with Banner Enumeration
type: command
executor: bash
data: nmap -sV $_TARGET_IP
output: 'root@kali:~# nmap -sV 10.10.10.10

  Starting Nmap 7.80 ( https://nmap.org ) at 2019-09-12 14:23 EDT

  Nmap scan report for 10.10.10.10

  Host is up (0.0000050s latency).

  Not shown: 999 closed ports

  PORT    STATE SERVICE VERSION

  111/tcp open  rpcbind 2-4 (RPC #100000)


  Service detection performed. Please report any incorrect results at https://nmap.org/submit/
  .

  Nmap done: 1 IP address (1 host up) scanned in 6.41 seconds

  '
created_at: '2019-09-12T18:24:17.551382+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Nmap]]'
- '[[host]]'
---

# Nmap Port Scan with Banner Enumeration

```bash
nmap -sV $_TARGET_IP
```

## Expected Output

```
root@kali:~# nmap -sV 10.10.10.10
Starting Nmap 7.80 ( https://nmap.org ) at 2019-09-12 14:23 EDT
Nmap scan report for 10.10.10.10
Host is up (0.0000050s latency).
Not shown: 999 closed ports
PORT    STATE SERVICE VERSION
111/tcp open  rpcbind 2-4 (RPC #100000)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 6.41 seconds

```


