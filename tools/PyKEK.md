---
id: 45a3a340-ab76-4f7b-b649-29369cdb13d3
type: tool
verified: true
created_at: '2019-08-28T21:17:30.416548+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - kerberos
  - credential-access
  - exploitation
  - python-library
url: 'https://github.com/skelsec/pykek'
commands:
  - '[[commands/pykek-parse-kerberos-ticket]]'
  - '[[commands/pykek-forge-silver-ticket]]'
  - '[[commands/pykek-extract-session-key]]'
category: Credential Access
validated: true
---

# PyKEK

**Status**: Unverified

## Overview

PyKEK (Python Kerberos Exploitation Kit) is a Python library designed for manipulating Kerberos (KRB5) data structures. It enables security researchers and red teams to parse, decrypt, encrypt, and forge Kerberos tickets and related artifacts in Active Directory environments. Commonly used for credential dumping analysis, ticket forgery (e.g., golden/silver tickets), and Kerberos-based attacks like pass-the-ticket.

## Description

PyKEK provides low-level access to Kerberos protocol elements, including AS-REQ/REP, TGS-REQ/REP, and ticket formats. It's particularly valuable in post-exploitation scenarios for Active Directory domains, allowing attackers to impersonate users or services without valid credentials. The library supports common encryption types like AES and RC4, and integrates with tools like Impacket for broader Kerberos exploitation workflows.

## Features

- Feature 1: Parsing of Kerberos tickets from ccache, keytab, or raw ASN.1 formats
- Feature 2: Forging custom tickets (golden, silver, etc.) with specified principals and keys
- Feature 3: Decryption and extraction of session keys, PAC data, and authorization info
- Feature 4: Support for multiple Kerberos encryption algorithms and versions (v5)

## Installation

### Requirements

- Python 3.6+
- pip and git

### Install Commands

```bash
# Install from GitHub
pip install git+https://github.com/skelsec/pykek.git

# Or clone and install
git clone https://github.com/skelsec/pykek.git
cd pykek
pip install .
```

For Kali Linux (pre-built packages may vary; use pip for latest):

```bash
sudo apt update
pip install pykek
```

## Basic Usage

```python
import pykek
help(pykek.kerberos)
```

### Common Options

PyKEK is a library, so usage is via Python scripts. Common imports:

| Option | Description |
|--------|-------------|
| `from pykek.kerberos import Ticket` | Core class for ticket manipulation |
| `Ticket.from_ccache(file)` | Load ticket from ccache file |
| `ticket.to_ccache(output)` | Export ticket to ccache |

## Examples

### Example 1: Basic Usage (Parsing a Ticket)

See [[commands/pykek-parse-kerberos-ticket]] for a full example.

### Example 2: Advanced Usage (Forging a Ticket)

Refer to [[commands/pykek-forge-silver-ticket]] for forging a silver ticket.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Steal or Forge Kerberos Tickets]] Steal or Forge Kerberos Tickets
- [[Pass the Ticket]] Use Alternate Authentication Material: Pass the Ticket

### Tactics

- [[Credential Access]] Credential Access
- [[Lateral Movement]] Lateral Movement

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for unusual Python imports or scripts accessing Kerberos files (e.g., via Sysmon process creation with pykek module)
- Detection method 2: Audit Kerberos ticket requests for anomalies (e.g., forged timestamps or principals) using Windows Event Logs (Event ID 4769)
- Detection method 3: Network traffic analysis for Kerberos over non-standard ports or unusual TGS requests

## Related Procedures

- [[procedures/Forge-Kerberos-Tickets-for-Lateral-Movement]]
- [[procedures/Analyze-and-Decrypt-Kerberos-Tickets]]

## Related Tools

- [[tools/Impacket]]
- [[tools/Mimikatz]]

## References

- Official GitHub: https://github.com/skelsec/pykek
- Kerberos documentation: https://tools.ietf.org/html/rfc4120
