---
id: c2c8a1bd-09b1-4ea8-9b55-d9c23f609332
name: hash-identifier
type: tool
verified: true
created_at: '2019-08-28T21:17:28.132451+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - hash
  - identification
  - cracking
  - password
  - analysis
url: 'https://github.com/blackploit/Hash-Identifier'
validated: true
---

# hash-identifier

**Status**: Unverified

## Overview

Hash-Identifier is a Python-based tool designed to identify the type of hash used to encrypt data, particularly passwords. It analyzes the format, length, and structure of a hash string to suggest possible algorithms such as MD5, SHA-1, SHA-256, bcrypt, and many others. This tool is essential in offensive security operations for reconnaissance of credential dumps, determining compatible cracking tools like Hashcat or John the Ripper, and understanding password storage mechanisms during vulnerability assessments.

## Description

The tool works by comparing the input hash against a database of known hash patterns, including salted and unsalted variants, domain credentials, and custom formats. It provides a probability-ranked list of matches, helping pentesters quickly triage hashes from sources like web app databases, memory dumps, or leaked files. Hash-Identifier is lightweight, runs interactively via command line, and supports a wide range of hash types (over 200), making it a go-to utility for credential access and cracking workflows in red teaming and CTF challenges.

## Features

- **Hash Pattern Matching**: Identifies algorithms based on length, character set, and delimiters (e.g., MD5's 32 hex chars, SHA-1's 40 hex chars).
- **Support for Variants**: Covers standard hashes, salted hashes, Windows NTLM/LM, Unix crypt, and application-specific formats like Joomla or Drupal.
- **Interactive Mode**: Simple input prompt for hashes, with real-time analysis speed and minimum character requirements.
- **Extensible Database**: Easy to update the internal hash signature list for new algorithms.
- **No Dependencies**: Pure Python script, runs on any platform with Python 2/3.

## Installation

### Requirements

- Python 2.7 or 3.x
- No additional libraries required

### Install Commands

```bash
# On Kali Linux (pre-installed in many distributions)
sudo apt update && sudo apt install hash-identifier

# Manual installation from GitHub
cd /opt && sudo git clone https://github.com/blackploit/Hash-Identifier.git
cd Hash-Identifier && sudo python setup.py install

# Alternative: Run directly without installation
wget https://raw.githubusercontent.com/blackploit/Hash-Identifier/master/hash-identifier.py
python hash-identifier.py

# On Ubuntu
sudo apt update && sudo apt install python3 git
git clone https://github.com/blackploit/Hash-Identifier.git
cd Hash-Identifier
sudo python3 setup.py install

# On Windows (using Python)
pip install git+https://github.com/blackploit/Hash-Identifier.git

# On macOS
brew install python && git clone https://github.com/blackploit/Hash-Identifier.git
cd Hash-Identifier && python3 setup.py install
```

After installation, ensure the script is in your PATH or run it directly with `python hash-identifier.py`.

## Basic Usage

```bash
hash-identifier
```

The tool will prompt: "Enter The Hash Value:". Paste your hash (e.g., `5f4dcc3b5aa765d61d8327deb882cf99`) and press Enter. It analyzes and outputs possible matches.

### Common Options

| Option | Description |
|--------|-------------|
| None (interactive only) | No command-line flags; input hash via stdin prompt |
| -h, --help | Not supported; view source for details |

## Examples

### Example 1: Basic Usage

```bash
hash-identifier
Enter The Hash Value: 5f4dcc3b5aa765d61d8327deb882cf99
```

Output:

```
Possible Hashs:
[+]  MD5
[+]  ... (list of matches)
[I] Hash Type:  MD5
```

### Example 2: Advanced Usage (Scripted Input)

For batch processing multiple hashes, you can pipe input:

```bash
(echo "5f4dcc3b5aa765d61d8327deb882cf99"; echo "e99a18c428cb38d5f260853678922e03") | hash-identifier
```

This processes multiple hashes sequentially in interactive mode.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials (for analyzing dumped hashes)
- [[Brute Force]] Brute Force (to select cracking method based on identified hash type)

### Tactics

- [[Credential Access]] Credential Access
- [[Persistence]] Persistence (via credential analysis)

## Detection

Indicators and methods for detecting this tool's usage:

- **Process Monitoring**: Look for `python hash-identifier.py` or `hash-identifier` executions in logs.
- **Network Indicators**: None, as it's offline/local.
- **File Artifacts**: Presence of the script in `/opt/Hash-Identifier/` or downloaded files like `hash-identifier.py`.
- **Behavioral**: Unusual analysis of hash files in temp directories during cracking attempts; monitor for tools like Hashcat following Hash-Identifier use.
- **EDR Rules**: Alert on Python scripts matching hash pattern databases or credential analysis behaviors.

## Related Procedures

- [[procedures/Extract-and-Identify-Hashes-from-Dump]]
- [[procedures/Crack-Identified-Hash-Types]]

## Related Tools

- [[tools/Hashcat]] (for cracking identified hashes)
- [[tools/john-the-ripper]] (alternative cracker with built-in identification)
- [[tools/hashid]] (similar Python tool for hash identification)

## References

- Official GitHub: https://github.com/blackploit/Hash-Identifier
- Usage Guide: https://www.kali.org/tools/hash-identifier/
- Related: OWASP Password Storage Cheat Sheet for hash best practices
