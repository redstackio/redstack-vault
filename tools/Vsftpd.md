---
id: tool-vsftpd
url: 'https://security.appspot.com/vsftpd.html'
tags:
  - ftp
  - server
  - logging
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.053Z'
validated: true
submitted: true
---
# Vsftpd

**Status**: Unverified

## Overview

VSFTPD (Very Secure FTP Daemon) is a lightweight, secure FTP server used to log incoming connections from SSRF exploits targeting FTP protocol.

## Description

In this attack, vsftpd runs on the attacker's server to capture and log FTP attempts from the Discourse Ruby client following redirects, providing evidence of protocol abuse.

## Features

- Feature 1: Anonymous FTP support
- Feature 2: Detailed logging of connections/commands
- Feature 3: Chroot isolation for security

## Installation

### Requirements

- Linux system with kernel support

### Install Commands

```bash
# On Ubuntu
apt install vsftpd
# Configure /etc/vsftpd.conf for anonymous access
systemctl start vsftpd
```

## Basic Usage

```bash
vsftpd /etc/vsftpd.conf
```

### Common Options

| Option | Description |
|--------|-------------|
| anonymous_enable=YES | Allow anon logins |
| xferlog_enable=YES | Enable transfer logs |
| log_ftp_protocol=YES | Detailed protocol logging |

## Examples

### Example 1: Basic Usage

Edit conf: anonymous_enable=YES, then systemctl restart vsftpd.

### Example 2: Advanced Usage

Monitor logs: tail -f /var/log/vsftpd.log during SSRF test.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exfiltration Over Alternative Protocol]] Exfiltration Over Alternative Protocol

### Tactics

- [[Exfiltration]] Exfiltration

## Detection

Indicators and methods for detecting this tool's usage:

- FTP service on non-standard hosts
- Logs showing anomalous logins from web app IPs
- vsftpd processes running

## Related Procedures

- [[procedures/Setup-Malicious-Redirect-Server]]

## Related Tools

- [[tools/ProFTPD]]

## References

- Official documentation: https://security.appspot.com/vsftpd.html
- Related resources: FTP security hardening
