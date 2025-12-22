---
id: 800635a7-b9b2-45a4-8d40-738b1d114735
type: tool
verified: true
created_at: '2023-05-29T16:48:53.029709+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - brute-force
  - enumeration
url: 'https://github.com/fortra/impacket'
commands:
  - '[[commands/impacket-lookupsid-lookup-rid]]'
validated: true
---

# impacket-lookupsid

**Status**: Unverified

## Overview

impacket-lookupsid is a script from the Impacket library designed for resolving Windows Security Identifiers (SIDs) via the Local Security Authority (LSA) Remote Procedure Call (LSARPC) interface. It enables enumeration of users and groups by looking up specific Relative Identifiers (RIDs) or brute-forcing ranges to discover accounts on remote Windows systems. This tool is commonly used in penetration testing for account discovery when valid credentials are available.

## Description

The tool establishes an authenticated MSRPC connection to the target's LSARPC endpoint (typically over SMB port 445) and queries for SID-to-name mappings. It supports various authentication methods, including NTLM passwords, NTLM hashes, and Kerberos tickets. While primarily for single SID lookups, it is frequently scripted for RID brute-forcing (e.g., checking RIDs 500-1100 for common user accounts like Administrator). This helps identify active domain or local accounts without relying on null sessions, making it effective against systems with restricted anonymous access.

## Features

- SID resolution for users, groups, and aliases via LSARPC
- Support for NTLM, NTLM hashes, and Kerberos authentication
- Customizable RID lookups for targeted enumeration
- Integration with other Impacket tools for chained attacks
- Debug mode for troubleshooting RPC communications

## Installation

### Requirements

- Python 3.6+
- Impacket library (v0.9.24 or later)
- Network access to target SMB port (445/TCP)

### Install Commands

```bash
pip3 install impacket
```

On Kali Linux or Ubuntu:

```bash
sudo apt update && sudo apt install impacket-scripts
```

For Windows (using Python):

```bash
pip install impacket
```

Verify installation:

```bash
python3 -c "import impacket; print(impacket.__version__)"
```

## Basic Usage

```bash
python3 lookupsid.py <domain>/<username>:<password>@<target_ip> <rid>
```

This performs a basic lookup of a specific RID (e.g., 500 for Administrator).

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Display help and usage information |
| -debug | Enable verbose DEBUG output for RPC interactions |
| -hashes LMHASH:NTHASH | Authenticate using NTLM hashes instead of password |
| -k | Use Kerberos authentication (requires valid tickets) |
| -no-pass | Prompt for password interactively |
| -dc-ip <ip> | Specify domain controller IP for Kerberos |

## Examples

### Example 1: Basic Usage

Look up RID 500 (Administrator) using plaintext password:

```bash
python3 lookupsid.py WORKSTATION/user:password@10.10.10.10 500
```

### Example 2: Advanced Usage

Use NTLM hashes for stealthier authentication and lookup RID 1001:

```bash
python3 lookupsid.py -hashes aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0 WORKSTATION/user@10.10.10.10 1001
```

For RID brute-forcing (scripted example to enumerate users 500-550):

```bash
for rid in {500..550}; do python3 lookupsid.py DOMAIN/user:pass@10.10.10.10 $rid 2>/dev/null | grep -v "not found"; done
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Account Discovery]] Account Discovery
- [[T1087.002]] Domain Account

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual LSARPC (UUID: 12345778-1234-abcd-ef00-0123456789ab) requests over SMB
- Authentication logs showing repeated SID lookups from a single source
- Network traffic patterns: Multiple RPC calls to port 445 with incremental RIDs
- Enable LSASS auditing and monitor for Event ID 4624 (logon) followed by LSARPC queries
- Use tools like Sysmon or Windows Defender ATP to log RPC endpoint access

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/CrackMapExec]]
- [[tools/impacket-samrdump]]
- [[tools/rpcclient]]

## References

- Official Impacket Repository: https://github.com/fortra/impacket/tree/master/examples/lookupsid.py
- MSRPC Documentation: https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-lsat
- Usage Guide: https://www.secureauth.com/labs/impacket
