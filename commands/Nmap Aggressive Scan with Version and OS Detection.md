---
id: 97f02023-0cc3-48f3-9931-fe989c40ca6e
name: Nmap Aggressive Scan with Version and OS Detection
type: command
executor: bash
data: nmap -A $_TARGET_IP
output: "root@kali:~# nmap -A 10.10.10.10\nStarting Nmap 7.80 ( https://nmap.org )\
  \ at 2019-09-12 14:43 EDT\nNmap scan report for 10.10.10.10\nHost is up (0.00073s\
  \ latency).\nNot shown: 977 closed ports\nPORT     STATE SERVICE     VERSION\n21/tcp\
  \   open  ftp         vsftpd 2.3.4\n|_ftp-anon: Anonymous FTP login allowed (FTP\
  \ code 230)\n| ftp-syst: \n|   STAT: \n| FTP server status:\n|      Connected to\
  \ 10.10.10.13\n|      Logged in as ftp\n|      TYPE: ASCII\n|      No session bandwidth\
  \ limit\n|      Session timeout in seconds is 300\n|      Control connection is\
  \ plain text\n|      Data connections will be plain text\n|      vsFTPd 2.3.4 -\
  \ secure, fast, stable\n|_End of status\nMAC Address: 00:0C:29:66:97:CB (VMware)\n\
  Device type: general purpose\nRunning: Linux 2.6.X\nOS CPE: cpe:/o:linux:linux_kernel:2.6\n\
  OS details: Linux 2.6.9 - 2.6.33\nNetwork Distance: 1 hop\nService Info: Hosts:\
  \  metasploitable.localdomain, irc.Metasploitable.LAN; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel\n\
  \nHost script results:\n|_clock-skew: mean: -6s, deviation: 0s, median: -6s\n|_ms-sql-info:\
  \ ERROR: Script execution failed (use -d to debug)\n|_nbstat: NetBIOS name: METASPLOITABLE,\
  \ NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)\n|_smb-os-discovery:\
  \ ERROR: Script execution failed (use -d to debug)\n|_smb-security-mode: ERROR:\
  \ Script execution failed (use -d to debug)\n|_smb2-time: Protocol negotiation failed\
  \ (SMB2)\n\nTRACEROUTE\nHOP RTT     ADDRESS\n1   0.73 ms 10.10.10.10\n\nOS and Service\
  \ detection performed. Please report any incorrect results at https://nmap.org/submit/\
  \ .\nNmap done: 1 IP address (1 host up) scanned in 35.76 seconds\n"
created_at: '2019-09-12T18:44:52.374985+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Nmap]]'
- '[[host]]'
- '[[type]]'
---

# Nmap Aggressive Scan with Version and OS Detection

```bash
nmap -A $_TARGET_IP
```

## Expected Output

```
root@kali:~# nmap -A 10.10.10.10
Starting Nmap 7.80 ( https://nmap.org ) at 2019-09-12 14:43 EDT
Nmap scan report for 10.10.10.10
Host is up (0.00073s latency).
Not shown: 977 closed ports
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
MAC Address: 00:0C:29:66:97:CB (VMware)
Device type: general purpose
Running: Linux 2.6.X
OS CPE: cpe:/o:linux:linux_kernel:2.6
OS details: Linux 2.6.9 - 2.6.33
Network Distance: 1 hop
Service Info: Hosts:  metasploitable.localdomain, irc.Metasploitable.LAN; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: -6s, deviation: 0s, median: -6s
|_ms-sql-info: ERROR: Script execution failed (use -d to debug)
|_nbstat: NetBIOS name: METASPLOITABLE, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
|_smb-os-discovery: ERROR: Script execution failed (use -d to debug)
|_smb-security-mode: ERROR: Script execution failed (use -d to debug)
|_smb2-time: Protocol negotiation failed (SMB2)

TRACEROUTE
HOP RTT     ADDRESS
1   0.73 ms 10.10.10.10

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 35.76 seconds

```


