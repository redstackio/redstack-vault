---
id: 33949ca9-b182-4969-a58a-1eebc2dda7b9
name: Nmap Enumerate SMB with Unsafe Vuln Scripts
type: command
executor: bash
data: nmap --script=vuln -p139,445 --script-args=unsafe=1 $_TARGET_IP
output: "root@kali:~# nmap --script=vuln -p135,445 --script-args=unsafe=1 10.10.10.10\n\
  Starting Nmap 7.70 ( https://nmap.org ) at 2019-09-13 18:24 EDT\nNmap scan report\
  \ for 10.10.10.10\nHost is up (0.00039s latency).\n\nPORT    STATE SERVICE\n135/tcp\
  \ open  msrpc\n445/tcp open  microsoft-ds\nMAC Address: 08:00:27:02:B4:38 (Oracle\
  \ VirtualBox virtual NIC)\n\nHost script results:\n|_samba-vuln-cve-2012-1182: NT_STATUS_ACCESS_DENIED\n\
  |_smb-vuln-ms10-054: ERROR: Script execution failed (use -d to debug)\n|_smb-vuln-ms10-061:\
  \ NT_STATUS_ACCESS_DENIED\n| smb-vuln-ms17-010: \n|   VULNERABLE:\n|   Remote Code\
  \ Execution vulnerability in Microsoft SMBv1 servers (ms17-010)\n|     State: VULNERABLE\n\
  |     IDs:  CVE:CVE-2017-0143\n|     Risk factor: HIGH\n|       A critical remote\
  \ code execution vulnerability exists in Microsoft SMBv1\n|        servers (ms17-010).\n\
  |           \n|     Disclosure date: 2017-03-14\n|     References:\n|       https://technet.microsoft.com/en-us/library/security/ms17-010.aspx\n\
  |       https://blogs.technet.microsoft.com/msrc/2017/05/12/customer-guidance-for-wannacrypt-attacks/\n\
  |_      https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-0143\n\nNmap done:\
  \ 1 IP address (1 host up) scanned in 15.44 seconds\n"
created_at: '2019-09-13T22:29:10.943183+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Nmap Enumerate SMB with Unsafe Vuln Scripts

```bash
nmap --script=vuln -p139,445 --script-args=unsafe=1 $_TARGET_IP
```

## Expected Output

```
root@kali:~# nmap --script=vuln -p135,445 --script-args=unsafe=1 10.10.10.10
Starting Nmap 7.70 ( https://nmap.org ) at 2019-09-13 18:24 EDT
Nmap scan report for 10.10.10.10
Host is up (0.00039s latency).

PORT    STATE SERVICE
135/tcp open  msrpc
445/tcp open  microsoft-ds
MAC Address: 08:00:27:02:B4:38 (Oracle VirtualBox virtual NIC)

Host script results:
|_samba-vuln-cve-2012-1182: NT_STATUS_ACCESS_DENIED
|_smb-vuln-ms10-054: ERROR: Script execution failed (use -d to debug)
|_smb-vuln-ms10-061: NT_STATUS_ACCESS_DENIED
| smb-vuln-ms17-010: 
|   VULNERABLE:
|   Remote Code Execution vulnerability in Microsoft SMBv1 servers (ms17-010)
|     State: VULNERABLE
|     IDs:  CVE:CVE-2017-0143
|     Risk factor: HIGH
|       A critical remote code execution vulnerability exists in Microsoft SMBv1
|        servers (ms17-010).
|           
|     Disclosure date: 2017-03-14
|     References:
|       https://technet.microsoft.com/en-us/library/security/ms17-010.aspx
|       https://blogs.technet.microsoft.com/msrc/2017/05/12/customer-guidance-for-wannacrypt-attacks/
|_      https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-0143

Nmap done: 1 IP address (1 host up) scanned in 15.44 seconds

```


