---
id: 13e2a085-4f9d-42fd-bdc5-3b1abeb38bdf
name: Port Scanning
type: cheatsheet
verified: true
created_at: '2019-09-12T20:52:23.863158+00:00'
updated_at: '2023-05-30T20:07:03.746781+00:00'
---

# Port Scanning

**Status**: ✓ Verified

# Description

Common port scanning techniques and approaches.

**Command** ([[Nmap Service Scan with Default Scripts]]):

```bash
nmap -sV -sC $_TARGET_IP
```

**Command** ([[Nmap Service Scan of All TCP Ports]]):

```bash
nmap -p- -sV $_TARGET_IP
```

**Command** ([[Nmap Service Scan of UDP ports]]):

```bash
nmap -sU -sV $_TARGET_IP
```

**Command** ([[Nmap Service Scan with No Host Discovery]]):

```bash
nmap -sV -Pn $_TARGET_IP
```

**Command** ([[Nmap Service Scan with OS Detection]]):

```bash
nmap -O -sV $_TARGET_IP
```

**Command** ([[Nmap Service Scan with Log File Output]]):

```bash
nmap -sV -oA $_OUTPUT.log $_TARGET_IP
```

**Command** ([[Nmap Aggressive Scan with Version and OS Detection]]):

```bash
nmap -A $_TARGET_IP
```

**Command** ([[Nmap Connect Scan]]):

```bash
nmap -sT $_TARGET_IP
```

**Command** ([[Nmap Service Scan of a Single Port]]):

```bash
nmap -p $_TARGET_PORT -sV $_TARGET_IP
```

**Command** ([[Nmap Ping Sweep]]):

```bash
nmap -sn $_TARGET_IP/$_CIDR
```

**Command** ([[Nmap LDAP Enumeration with Scripts]]):

```bash
nmap -p $_TARGET_PORT -script ldap-search $_TARGET_IP
```

**Command** ([[Nmap Enumerate SMTP with Unsafe Vuln Scripts]]):

```bash
nmap --script vuln --script-args=unsafe -p $_TARGET_PORT $_TARGET_IP
```

**Command** ([[Nmap Enumerate HTTP with Vuln Scripts]]):

```bash
nmap --script vuln -p $_TARGET_PORT $_TARGET_IP
```

**Command** ([[Nmap Enumerate SMB with Unsafe Vuln Scripts]]):

```bash
nmap --script=vuln -p139,445 --script-args=unsafe=1 $_TARGET_IP
```

**Command** ([[xprobe2 Fingerprint a Target's OS]]):

```bash
xprobe2 $_TARGET_IP
```

**Command** ([[Whatweb Identify a Web Server's Technology]]):

```bash
whatweb http://$_TARGET_IP
```
