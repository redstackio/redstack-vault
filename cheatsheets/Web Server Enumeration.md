---
id: 59bdd39f-be63-4653-9dae-6a1bbe4e1032
name: Web Server Enumeration
type: cheatsheet
verified: true
created_at: '2019-09-13T23:40:37.794172+00:00'
updated_at: '2023-05-30T20:08:12.525945+00:00'
---

# Web Server Enumeration

**Status**: ✓ Verified

# Description

Common web server enumeration techniques.

## Fuzing Files and Folders

**Command** ([[Wfuzz Directory Brute Force]]):

```bash
wfuzz --hc 404 -c -w common.txt -u http://$_TARGET_IP/FUZZ
```

**Command** ([[Wfuzz Directory Brute Force with Burp Proxy]]):

```bash
wfuzz --hc 404 -c -w common.txt -u http://$_TARGET_IP/FUZZ -p 127.0.0.1:8080:HTML
```

**Command** ([[Gobuster Directory Brute Force]]):

```bash
gobuster dir -w $_WORDLIST -u http://$_TARGET_IP
```

**Command** ([[Gobuster Directory Brute Force with Burp proxy]]):

```bash
gobuster dir -w $_WORDLIST -u http://$_TARGET_IP -p http://127.0.0.1:8080
```

**Command** ([[Gobuster Directory Brute Force with Extensions]]):

```bash
gobuster dir -w $_WORDLIST -u http://$_TARGET_IP -f -e -x '$_EXT1,$_EXT2,$_EXT3'
```

## Common Vulnerability Enumeration

**Command** ([[Nikto Enumerate Web Server]]):

```bash
nikto -host http://$_TARGET_IP
```

**Command** ([[Nikto Enumerate Web Server with Burp Proxy]]):

```bash
nikto -host http://$_TARGET_IP -useproxy 127.0.0.1:8080
```

## Signature Scanning

**Command** ([[Httprint Scan a Web Server for Known Signatures]]):

```bash
httprint -h http://$_TARGET_IP -s /usr/share/httprint/signatures.txt
```

**Command** ([[Skipfish Scan a Web Server for Known Signatures]]):

```bash
skipfish -m 5 -o results -LY -S /usr/share/skipfish/dictionaries/complete.wl http://$_TARGET_IP
```

## WordPress Enumeration

**Command** ([[WPScan Enumerate WordPress Plugins, Users, Themes and TimThumb]]):

```bash
wpscan --url http://$_TARGET_IP --enumerate p,t,u,tt
```

## XSS and SQL Vulnerability Enumeration

**Command** ([[Grabber Scan a Website for XSS and SQL Vulnerabilities]]):

```bash
grabber --spider 2 --sql --xss --url http://$_TARGET_IP
```

## SSL/TLS Certificate Enumeration

**Command** ([[SSLyze Enumerate a Web Server's SSL/TLS Certificate]]):

```bash
sslyze --regular $_TARGET_HOST
```
