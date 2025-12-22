---
id: 7d605408-814b-4daf-89d5-3ecd843f4a12
name: genkeys
type: tool
verified: true
created_at: '2019-08-28T21:17:24.951616+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - credential-access
  - wireless-security
  - ms-chapv2
  - leap
url: 'https://www.kali.org/tools/asleap/'
validated: true
---

# genkeys

**Status**: Unverified

## Overview

genkeys is a utility tool included in the asleap package, used to generate MS-CHAPv2 challenge-response pairs from known usernames and passwords. It is primarily employed in offensive security testing to simulate or prepare data for offline dictionary attacks against protocols vulnerable to MS-CHAPv2, such as Cisco LEAP wireless networks and PPTP VPNs. This tool helps demonstrate weaknesses in authentication exchanges by creating test vectors for cracking tools.

## Description

genkeys exploits the known vulnerabilities in MS-CHAPv2 authentication, which is a reversible challenge-response protocol susceptible to offline attacks. By providing a username, password, and challenge value, genkeys computes the corresponding NTLM hash and response, which can then be fed into cracking tools like hashcat or John the Ripper. It is particularly useful in wireless security assessments targeting legacy Cisco LEAP implementations, where captured authentication packets can be replayed or analyzed. genkeys does not perform network captures itself but serves as a key generation component in broader attack workflows involving tools like airodump-ng for packet collection and asleap for processing.

## Features

- Generates MS-CHAPv2 NTLM hashes and responses from plaintext credentials
- Supports custom challenge values for targeted simulations
- Outputs in formats compatible with popular cracking tools
- Lightweight and scriptable for automation in testing pipelines

## Installation

### Requirements

- Linux environment (Kali Linux recommended)
- asleap package (genkeys is bundled within it)
- Basic dependencies: libc, standard build tools

### Install Commands

```bash
# On Kali Linux (pre-installed in many distributions)
sudo apt update
sudo apt install asleap

# On Ubuntu/Debian
sudo apt update
sudo apt install asleap

# Manual build from source (if needed)
git clone https://github.com/joswright/asleap.git
cd asleap/src
gcc -o genkeys genkeys.c -lcrypto
sudo make install
```

## Basic Usage

```bash
genkeys --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Display help message and usage |
| No additional flags | genkeys operates with positional arguments: username, password, challenge |

## Examples

### Example 1: Basic Usage

Generate a response for a test user:

```bash
genkeys testuser "password123" 0102030405060708090a0b0c0d0e0f10
```

### Example 2: Advanced Usage

Script it for batch generation (example in a loop for dictionary attacks):

```bash
while read username password; do
  genkeys "$username" "$password" "$(xxd -p -l 16 /dev/urandom | tr -d '\n')"
  echo "---"
done < credentials.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Password Guessing]] Password Guessing
- [[Password Managers]] RAMP (Reversible Add-on Management Protocol, related to MS-CHAPv2 weaknesses)

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of asleap/genkeys binaries in /usr/bin or custom paths
- Process monitoring for genkeys executions, often paired with hash cracking tools
- Log analysis for unusual crypto library calls (libcrypto) in security testing contexts
- Network traffic analysis for LEAP/PPTP probes preceding offline cracking attempts

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/asleap]]
- [[tools/Hashcat]]
- [[tools/airodump-ng]]

## References

- Official Kali Tools page: https://www.kali.org/tools/asleap/
- Asleap GitHub repository: https://github.com/joswright/asleap
- MS-CHAPv2 vulnerability details: https://tools.ietf.org/html/rfc2759
