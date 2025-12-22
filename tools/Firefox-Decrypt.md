---
id: 1cba2ba1-32a1-4a7d-b14d-55cfe9830b67
name: Firefox-Decrypt
type: tool
verified: true
created_at: '2020-02-19T00:01:25.730729+00:00'
updated_at: '2023-05-30T19:53:04.360154+00:00'
commands:
  - '[[commands/firefox-decrypt-extract-passwords-from-profile]]'
platforms:
  - Linux
  - Windows
tags:
  - '[[Cryptography]]'
  - '[[data encryption]]'
  - '[[data exposure]]'
  - credential-access
url: 'https://github.com/unode/firefox_decrypt'
validated: true
---

# Firefox-Decrypt

**Status**: ✓ Verified

## Overview

Firefox Decrypt is a Python 3 tool used to extract and decrypt saved passwords from profiles in Mozilla Firefox, Thunderbird, SeaMonkey, and their derivatives. It supports recovering passwords protected by a master password (if known) or profiles without one. The tool accesses browser storage files like logins.json and key4.db to retrieve plaintext credentials.

## Description

Firefox Decrypt parses the NSS (Network Security Services) database used by Firefox to store encrypted credentials. It requires the path to the user's profile directory and optionally the master password. This tool is useful in post-exploitation scenarios for credential dumping from compromised user systems where browser-saved passwords provide access to other services.

## Features

- Decrypts passwords from Firefox, Thunderbird, and SeaMonkey profiles
- Handles master password protection (blank if none set)
- Outputs website, username, and password in plaintext
- Cross-platform compatibility (Linux, Windows)
- No additional dependencies beyond Python 3 and NSS libraries

## Installation

### Requirements

- Python 3.x
- NSS (Network Security Services) libraries (pre-installed on most Linux distros; on Windows, may require manual setup via NSS binaries)

### Install Commands

```bash
# Clone the repository
git clone https://github.com/unode/firefox_decrypt.git
cd firefox_decrypt

# No further installation needed; run directly with Python
```

On Windows, ensure Python is in PATH and NSS is available (download from Mozilla if needed).

## Basic Usage

```bash
python firefox_decrypt.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and usage |
| `-d, --dir` | Specify profile directory (alternative to positional argument) |

## Examples

### Example 1: Basic Usage

Extract passwords from the default Firefox profile on Linux:

```bash
python firefox_decrypt.py ~/.mozilla/firefox
```

### Example 2: Advanced Usage

Extract from a specific profile directory on Windows:

```cmd
python firefox_decrypt.py %APPDATA%\Mozilla\Firefox\Profiles
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Password Managers]] Credentials from Password Managers (Browsers)

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of firefox_decrypt.py in temporary directories or downloads
- Python processes accessing Mozilla profile paths (e.g., ~/.mozilla/firefox)
- File access to logins.json or key4.db outside normal browser activity
- Network logging of credential use post-extraction

## Related Procedures

- [[procedures/Extract-Firefox-and-Thunderbird-Passwords-from-Profiles]]

## Related Tools

- [[tools/Mimikatz]] (for broader credential dumping)
- [[tools/LaZagne]] (multi-browser credential extractor)

## References

- Official GitHub Repository: https://github.com/unode/firefox_decrypt
- Mozilla NSS Documentation: https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS
