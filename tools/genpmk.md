---
id: b9748435-c0c9-4ca8-bad1-d91d7a07b23a
type: tool
verified: true
created_at: '2019-08-28T21:17:31.986073+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - wireless
  - credential-access
  - pmk-generation
  - wpa-cracking
url: 'https://github.com/joswr1ght/cowpatty'
validated: true
---

# genpmk

**Status**: Unverified

## Overview

genpmk is a utility for generating precomputed Pairwise Master Keys (PMKs) used in offline dictionary attacks against WPA/WPA2-Personal (PSK-based) Wi-Fi networks. It computes PMKs from an SSID and a wordlist of potential passwords, creating files that accelerate cracking with tools like cowpatty. This is particularly useful for auditing enterprise networks that use simple PSK authentication instead of more secure WPA-Enterprise setups with RADIUS and certificates.

## Description

genpmk implements the PBKDF2-HMAC-SHA1 key derivation function to precompute PMKs offline. By generating these keys in advance for a target SSID, attackers can perform faster dictionary attacks on captured handshakes without recomputing keys during the cracking phase. This tool is part of the cowpatty suite and is commonly used in wireless penetration testing to assess the strength of PSK passwords in WPA/WPA2 networks.

## Features

- Precomputes PMKs for specific SSIDs using password dictionaries
- Supports large wordlists for comprehensive coverage
- Outputs in a format compatible with cowpatty for accelerated cracking
- Leverages OpenSSL for cryptographic operations

## Installation

### Requirements

- OpenSSL development libraries
- GCC compiler
- Standard build tools (make)

### Install Commands

On Kali Linux (pre-installed as part of cowpatty):

```bash
sudo apt update && sudo apt install cowpatty
```

On Ubuntu:

```bash
sudo apt update && sudo apt install cowpatty
```

From source (if needed):

```bash
wget https://www.coresecurity.com/files/uploads/cowpatty-4.6.tar.gz
tar -xzf cowpatty-4.6.tar.gz
cd cowpatty-4.6
./configure
make
sudo make install
```

## Basic Usage

```bash
genpmk --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Display help message and exit |
| --ssid SSID | Specify the target Wi-Fi network name (SSID) |
| --wordlist FILE | Path to the password wordlist |
| --output FILE | Path for the output PMK file |
| -v, --verbose | Enable verbose output during computation |

## Examples

### Example 1: Basic Usage

Generate a PMK file for a target SSID using a standard wordlist:

```bash
genpmk --ssid "TargetWiFi" --wordlist /usr/share/wordlists/rockyou.txt --output target.pmk
```

### Example 2: Advanced Usage

Use verbose mode for a custom dictionary:

```bash
genpmk --verbose --ssid "EnterpriseNet" --wordlist custom_passwords.txt --output enterprise.pmk
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Credentials in Files]] Password Policy Discovery (for wireless PSK assessment)
- [[Software]] Software (for precomputing keys in credential access)

### Tactics

- [[Credential Access]] Credential Access

## Detection

- genpmk is an offline tool, so detection focuses on its output usage: monitor for cowpatty or aircrack-ng processes handling PMK files
- File system monitoring for large .pmk files with SSID:password:PMK format
- Network traffic analysis for WPA handshake captures (e.g., via airodump-ng)

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/cowpatty]] (for using generated PMK files in cracking)
- [[tools/aircrack-ng]] (for capturing handshakes)
- [[tools/Hashcat]] (alternative cracking tool supporting WPA)

## References

- Official repository: https://github.com/joswr1ght/cowpatty
- Core Security article: https://www.coresecurity.com/core-labs/articles/wireless-auditing-cracking-wpa-psk-networks
- Kali Tools documentation: https://www.kali.org/tools/cowpatty/
