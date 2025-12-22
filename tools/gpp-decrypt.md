---
id: 07ac6a4f-9131-4513-a485-fe436d976f0e
type: tool
verified: true
created_at: '2019-08-28T21:17:38.502874+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
  - Windows
tags:
  - '[[Cryptography]]'
  - '[[known vulnerability]]'
url: 'https://github.com/HarmJ0y/NetExec/blob/master/external/gpp-decrypt.rb'
commands:
  - '[[commands/gpp-decrypt-decrypt-cpassword]]'
validated: true
---

# gpp-decrypt

**Status**: Unverified

## Overview

gpp-decrypt is a Ruby script designed to decrypt passwords stored in Microsoft Group Policy Preferences (GPP) XML files, commonly found in Active Directory environments within the SYSVOL share. These files often contain weakly encrypted credentials like local admin passwords, which Microsoft disclosed the AES key for in 2012 (MS14-025), making decryption straightforward and useful for post-exploitation in Windows domains.

## Description

GPP files in SYSVOL can expose sensitive information such as administrator passwords in cleartext after decryption. The tool targets the 'cPassword' attribute in these XML files, which uses a static AES-256 key. It's particularly valuable during Active Directory assessments to recover credentials from domain-joined systems without needing additional privileges beyond read access to SYSVOL.

## Features

- Decrypts base64-encoded cPassword fields from GPP XML files
- Uses the publicly known Microsoft AES key for trivial decryption
- Simple command-line interface for quick password extraction
- Supports offline processing of captured GPP files

## Installation

### Requirements

- Ruby 2.0 or later
- OpenSSL library (for AES decryption)

### Install Commands

On Kali Linux (pre-installed in many pentesting distros):

```bash
# If not present, install Ruby and dependencies
sudo apt update
sudo apt install ruby openssl

# Clone or download the script
git clone https://github.com/rapid7/metasploit-framework.git
# Or directly: wget https://raw.githubusercontent.com/rapid7/metasploit-framework/master/external/src/gpp_decrypt.rb
# Rename to gpp-decrypt.rb and make executable: chmod +x gpp-decrypt.rb
```

On Ubuntu/Debian:

```bash
sudo apt update
sudo apt install ruby-full libruby
# Download the script as above
```

On Windows (using RubyInstaller):

- Install Ruby from rubyinstaller.org
- Download the script and run via `ruby gpp-decrypt.rb`

## Basic Usage

```bash
gpp-decrypt 'encrypted_cpassword_here'
```

### Common Options

| Option | Description |
|--------|-------------|
| None (stdin support) | Reads encrypted string from command line or pipe |
| -h | Show basic help (if implemented in script) |

## Examples

### Example 1: Basic Usage

Decrypt a known cPassword:

```bash
gpp-decrypt 'CiDUq6tbrBL1m/js9DmZNIydXpsE69WB9JrhwYRW9xywOz1/0W5VCUz8tBPXUkk9y80n4vw74KeUWc2+BeOVDQ'
```

### Example 2: Advanced Usage

Pipe from a file containing multiple cPasswords:

```bash
cat gpp_passwords.txt | while read line; do echo "Password: $(gpp-decrypt $line)"; done
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Group Policy Preferences]] Group Policy Preferences

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Ruby process executing gpp-decrypt.rb or similar scripts
- Access to SYSVOL shares followed by offline decryption attempts
- Log entries for Ruby/OpenSSL usage in non-standard contexts
- Network transfers of GPP XML files to attacker-controlled systems

## Related Procedures

- [[procedures/decrypt-gpp-password-from-sysvol]]

## Related Tools

- [[tools/Impacket]]
- [[tools/pypykatz]]

## References

- Microsoft Security Bulletin MS14-025
- Original script from Metasploit Framework
- GitHub: https://github.com/rapid7/metasploit-framework/blob/master/external/src/gpp_decrypt.rb
