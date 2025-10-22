---
id: b7174369-6c55-4f43-9436-26902a81f7e2
name: Nmap
type: cheatsheet
verified: false
created_at: '2020-07-14T18:21:14.549941+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# Nmap

**Command** ([[Host discovery]]):

```bash
nmap -sn -n

```

**Command** ([[Scan for everything]]):

```bash
nmap -A (run this second)

```

**Command** ([[sV Scan]]):

```bash
nmap -sV -F

```

**Command** ([[??]]):

```bash
nmap -p- -sV -O -T4 -v7 -sC

```

**Command** ([[Open SMB shares]]):

```bash
nmap --script=smb-enum-shares -p445

```

**Command** ([[Open NFS Shares]]):

```bash
nmap -p 111,2049 --script nfs-ls,nfs-showmount

```

**Command** ([[UDP scan:]]):

```bash
nmap -sU -F -Pn -v -d -sC -sV --open --reason -T5

```

**Command** ([[Anonymous FTP]]):

```bash
nmap -sC -sV -p21
nmap -sV -n -sS -Pn-vv --open -p21 --script=ftp-anon,ftp-bounce,ftp-libopie,ftp-proftpd-backdoor,ftp-vsftpd-backdoor,ftp-vuln-cve2010-4221

```

**Command** ([[VNC Brute]]):

```bash
nmap --script=vnc-brute -p5800,5900

```

**Command** ([[Rawr Scan]]):

```bash
nmap -sV --open -T4 -v7 -p80,280,443,591,593,981,1311,2031,2480,3181,4444,4445,4567,4711,4712,5104,5280,5800,5988,5989,7000,7001,7002,8008,8011,8012,8013,8014,8042,8069,8080,8081,8243,8280,8281,8531,8887,8888,9080,9443,11371,12443,16080,18091,18092 -iL live-hosts.txt -oA web

```

**Command** ([[MSSQL Scan]]):

```bash
nmap -vv-sV -Pn-n -p1433 --script=ms-sql-info,ms-sql-config,ms-sql-dump-hashes --script-args=mssql.instance-port=1433,smsql.username-sa,mssql.password-sa -oA

```

**Command** ([[HTTP Scan]]):

```bash
nmap -vv -sS -Pn-n -p80,443,8080 --script=http-vhosts,http-userdir-enum,http-apache-negotiation,http-backup-finder,http-config-backup,http-default-accounts,http-email-harvest,http-methods,http-method-tamper,http-passwd,http-robots.txt -oA

```
