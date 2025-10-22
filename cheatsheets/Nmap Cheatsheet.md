---
id: 3f81a7c5-75c8-4c05-b8b7-1d4535980fa5
name: Nmap Cheatsheet
type: cheatsheet
verified: false
created_at: '2020-07-14T18:15:19.825737+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# Nmap Cheatsheet

# Description

This nmap cheatsheet covers basic and advanced cheatsheet commands.

**Command** ([[Banners and OS]]):

```bash
nmap -sV -sT -O $ip

```

# Description

**Command** ([[All scans (Exhaustive)]]):

```bash
nmap -A $ip

```

**Command** ([[NSE Port 80, all HTTP scripts]]):

```bash
nmap --script=http-* -p 80 $ip

```

**Command** ([[NSE Port 80 CVEs]]):

```bash
nmap --script=http-vuln-cve* -p80 $ip

```

**Command** ([[NSE SMB]]):

```bash
nmap --script=smb-* -p139,445 $ip

```

**Command** ([[NSE SMB unsafe]]):

```bash
nmap --script=smb-* -p139,445 --script-args=unsafe=1 $ip

```

**Command** ([[SNMP]]):

```bash
nmap -sU -p161 --open $ip

```

**Command** ([[Decoy Masqurade Scan]]):

```bash
nmap -sS -sV -D $ip2,$ip3,$ip4,$ip5 -f --mtu=24 --data-length=1337 -T2 $ip
nmap -Pn -T2 -sV --randomize-hosts $ip,$ip2

```

**Command** ([[Aggressive UDP Scan]]):

```bash
nmap -sU -v $ip
nmap -sU -P0 $ip
nmap -sU -P0 -T Aggressive $ip

```

**Command** ([[More aggressive Full TCP Scan]]):

```bash
nmap -sA -PN -sN $ip
nmap -sS -sV -T4 -F -A -O $ip

```

**Command** ([[Default Full Scan]]):

```bash
nmap -sC $ip

```
