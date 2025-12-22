---
id: 64bc01f0-c50a-404c-b306-18236e582ee5
type: tool
verified: true
created_at: '2020-02-18T21:38:17.472868+00:00'
updated_at: '2023-05-30T19:59:39.202777+00:00'
platforms:
  - Linux
  - Windows
tags:
  - '[[Brute Force]]'
  - '[[Cryptography]]'
  - '[[Web Applications]]'
url: 'https://github.com/AonCyberLabs/PadBuster'
commands:
  - '[[commands/padbuster-decrypt-cookie]]'
validated: true
---

# PadBuster

**Status**: ✓ Verified

## Overview

PadBuster is a Perl-based tool designed for automating Padding Oracle Attacks on encrypted data in web applications. It excels at decrypting arbitrary ciphertext, encrypting plaintext, and performing automated response analysis to identify padding oracle vulnerabilities, making it essential for testing cryptographic implementations in HTTP cookies, parameters, or other encoded data.

## Description

PadBuster automates the exploitation of padding oracle vulnerabilities, where a server inadvertently leaks information about padding validity in block ciphers like AES or 3DES. By iteratively modifying ciphertext blocks and observing server responses (e.g., error messages or status codes), it reveals plaintext byte-by-byte. Common use cases include decrypting session cookies to extract user data or tokens, encrypting malicious payloads for privilege escalation, and brute-forcing encryption oracles in web apps. It supports various encodings (raw, Base64, hex) and integrates with Burp Suite or proxies for request interception.

## Features

- **Decrypt Mode**: Automatically decrypts ciphertext by exploiting padding validation responses.
- **Encrypt Mode**: Encrypts arbitrary plaintext using the oracle to generate valid ciphertexts.
- **Response Analysis**: Automatically detects vulnerability by analyzing HTTP response variations (status, length, content).
- **Encoding Support**: Handles raw bytes, Base64URL, and hex encodings for flexible input/output.
- **Proxy Integration**: Supports HTTP proxies for traffic interception and modification.
- **Interactive Mode**: Prompts for error signature selection during analysis for accurate oracle identification.

## Installation

### Requirements

- Perl 5 (with LWP::UserAgent module for HTTP requests)
- Access to a vulnerable target (web app with padding oracle)

### Install Commands

On Kali Linux (pre-installed in some repos, or manual):

```bash
# Download from GitHub
wget https://github.com/AonCyberLabs/PadBuster/raw/master/PadBuster.pl -O /usr/local/bin/PadBuster.pl
chmod +x /usr/local/bin/PadBuster.pl

# Or via apt if available
apt update && apt install padbuster
```

On Ubuntu:

```bash
sudo apt update
sudo apt install libwww-perl  # For LWP dependencies
# Then download as above
wget https://github.com/AonCyberLabs/PadBuster/raw/master/PadBuster.pl -O /usr/local/bin/PadBuster.pl
chmod +x /usr/local/bin/PadBuster.pl
```

On Windows:

- Install Strawberry Perl from https://strawberryperl.com/
- Download PadBuster.pl and run via `perl PadBuster.pl`

## Basic Usage

```bash
perl PadBuster.pl http://target.com $_CIPHERTEXT $_BLOCK_SIZE -encoding 0
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Display help and usage information |
| `-verbose` | Enable verbose output for debugging |
| `-proxy http://localhost:8080` | Route requests through a proxy like Burp |
| `-file input.txt` | Read ciphertext from a file instead of command line |
| `-output output.txt` | Write decrypted plaintext to a file |

## Examples

### Example 1: Basic Decryption

```bash
perl PadBuster.pl http://example.com/login "encrypted_cookie_value" 16 -cookies "session=encrypted_cookie_value" -encoding 1
```

This decrypts a Base64URL-encoded AES cookie by sending modified requests to the login endpoint.

### Example 2: Encrypt Plaintext

```bash
perl PadBuster.pl http://example.com/login "known_plaintext" 16 -encrypt -plaintext "admin=true" -encoding 0
```

Encrypts "admin=true" using the oracle to generate a valid ciphertext for injection.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Asymmetric Cryptography]] Encrypted Channel: Asymmetric Cryptography (for exploiting weak implementations)
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application (padding oracles in web crypto)

### Tactics

- [[Initial Access]] Initial Access
- [[Collection]] Collection (decrypting sensitive data like sessions)

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual HTTP request patterns: High volume of similar requests with incrementally modified ciphertext blocks to the same endpoint.
- Response analysis artifacts: Server logs showing varying response lengths or error rates indicative of padding validation.
- Network traffic: Requests with Base64/hex-encoded payloads routed through proxies; monitor for Perl user-agent strings.
- File system: Presence of PadBuster.pl script or temporary files with ciphertexts.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Burp-Suite]] (for proxying and manual request modification)
- [[tools/sqlmap]] (for related web vuln testing)

## References

- Official GitHub: https://github.com/AonCyberLabs/PadBuster
- Padding Oracle Attacks: https://www.dwheeler.com/secure-programs/PADDING-ORACLE-attack.html
