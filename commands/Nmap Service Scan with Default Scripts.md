---
id: f8a860fd-f488-4bba-bd23-84e2dd9c2c7c
name: Nmap Service Scan with Default Scripts
type: command
executor: bash
data: nmap -sV -sC $_TARGET_IP
output: "root@kali:~# nmap -sV -sC 10.10.10.10\nStarting Nmap 7.80 ( https://nmap.org\
  \ ) at 2019-09-12 14:32 EDT\nNmap scan report for 10.10.10.10\nHost is up (0.00057s\
  \ latency).\nNot shown: 999 closed ports\nPORT     STATE SERVICE     VERSION\n21/tcp\
  \   open  ftp         vsftpd 2.3.4\n|_ftp-anon: Anonymous FTP login allowed (FTP\
  \ code 230)\n| ftp-syst: \n|   STAT: \n| FTP server status:\n|      Connected to\
  \ 10.10.10.13\n|      Logged in as ftp\n|      TYPE: ASCII\n|      No session bandwidth\
  \ limit\n|      Session timeout in seconds is 300\n|      Control connection is\
  \ plain text\n|      Data connections will be plain text\n|      vsFTPd 2.3.4 -\
  \ secure, fast, stable\n|_End of status\n\nService detection performed. Please report\
  \ any incorrect results at https://nmap.org/submit/ .\nNmap done: 1 IP address (1\
  \ host up) scanned in 34.97 seconds"
created_at: '2019-09-12T18:35:43.264851+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Nmap Service Scan with Default Scripts

```bash
nmap -sV -sC $_TARGET_IP
```

## Expected Output

```
root@kali:~# nmap -sV -sC 10.10.10.10
Starting Nmap 7.80 ( https://nmap.org ) at 2019-09-12 14:32 EDT
Nmap scan report for 10.10.10.10
Host is up (0.00057s latency).
Not shown: 999 closed ports
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         vsftpd 2.3.4
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to 10.10.10.13
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      vsFTPd 2.3.4 - secure, fast, stable
|_End of status

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 34.97 seconds
```
