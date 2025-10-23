---
id: 8930e4b1-5b14-47a4-83c0-a251cbf8740a
name: Anonymous FTP
type: command
executor: bash
data: 'nmap -sC -sV -p21

  nmap -sV -n -sS -Pn-vv --open -p21 --script=ftp-anon,ftp-bounce,ftp-libopie,ftp-proftpd-backdoor,ftp-vsftpd-backdoor,ftp-vuln-cve2010-4221

  '
output: null
created_at: '2020-07-14T18:21:14.335653+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Anonymous FTP

```bash
nmap -sC -sV -p21
nmap -sV -n -sS -Pn-vv --open -p21 --script=ftp-anon,ftp-bounce,ftp-libopie,ftp-proftpd-backdoor,ftp-vsftpd-backdoor,ftp-vuln-cve2010-4221

```


