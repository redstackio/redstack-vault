---
id: 39222e4f-9269-4895-a8c1-22cf4ded889e
name: Identify Operating System and Version
type: procedure
verified: true
submitted: true
created_at: '2019-10-19T01:09:28.077023+00:00'
updated_at: '2023-05-26T00:40:19.084222+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[System Information Discovery|T1082 - System Information Discovery]]'
platforms:
- Linux
- Windows
tags:
- '[[Network]]'
commands:
- '[[Nmap Service Scan with OS Detection]]'
---

# Identify Operating System and Version

**Status**: ✓ Verified

## Summary

It is often possible to fingerprint devices by sending queries via the network and analyzing the results. While broadly identifying the operating system can be trivial, referencing OSINT can help identify exact the exact version. 

## Description

# Description

It is often possible to fingerprint devices by sending queries via the network and analyzing the results. While broadly identifying the operating system can be trivial, referencing OSINT can help identify exact the exact version.

# Instructions

## Identify the Operating System

Windows and *nix based systems respond differently to ping requests. Windows replies by setting the TTL to 128, while *nix systems respond with a TTL of 64.

Pings to a Windows host:

Pings to a *nix host:

The TTL value is decremented every time it passes through a router. This means the ping replies may not be exactly 128/64, but it will be close enough to identify the OS.

Nmap includes an OS scanner, which attempts to fingerprint the target and compare it to known fingerprints of other devices.

**Command** ([[Nmap Service Scan with OS Detection]]):

```bash
nmap -O -sV $_TARGET_IP
```

This method is not always accurate, and should be used in tandem with other fingerprinting techniques.

## Manually Identify the Exact OS and Release

By enumerating banners of network services, the OS and release information can reliably be determined by searching Google and OSINT services.

**Identify the Linux/Unix Release**

Scan the system using Nmap to enumerate banners

In this example, Nmap returned banners for SSH and Apache. Use Google to search using the Apache version information. The top results will often disclose which distribution and release include this package. 

Out of the top results when searching for `Apache httpd 2.4.18`, Launchpad.net suggests this package is installed with Ubuntu 17.04, Xenial Xerus.

**Identify the Windows OS and Release**

Scan the system using Nmap to enumerate banners

In this example, Nmap's results include the web server's banner which lists the version as `Microsoft IIS httpd 10.0`. By referencing Wikipedia's entry for IIS[ (https://en.wikipedia.org/wiki/Internet_Information_Servic](https://en.wikipedia.org/wiki/Internet_Information_Services)es), we can confirm the OS is Windows 10.

## Platforms

- Linux
- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[Nmap Service Scan with OS Detection]]

## Tags

- [[Network]]
