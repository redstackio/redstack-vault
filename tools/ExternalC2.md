---
id: e578b8b0-fea2-4af9-91f2-a4a642a886f1
type: tool
verified: true
created_at: '2019-08-28T21:17:34.240651+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
tags:
  - c2
  - cobalt-strike
  - external-c2
  - library
url: 'https://github.com/threatexpress/external-c2-profiles'
commands:
  - '[[commands/externalc2-register-http-profile]]'
  - '[[commands/externalc2-start-http-listener]]'
validated: true
---

# ExternalC2

**Status**: Unverified

## Overview

ExternalC2 is a Python library designed to facilitate the integration of custom communication channels with Cobalt Strike's External C2 server feature. It enables red teams to implement malleable C2 profiles for HTTP/HTTPS, DNS, and other protocols, allowing for stealthier command and control operations during security assessments.

## Description

The library provides APIs for registering custom C2 profiles, starting listeners, and handling beacon communications. It is particularly useful for extending Cobalt Strike's capabilities beyond standard listeners, supporting advanced evasion techniques like domain fronting or custom stagers. Commonly used in post-exploitation phases to maintain persistence and exfiltrate data through non-standard channels.

## Features

- Feature 1: Profile registration for HTTP, HTTPS, DNS protocols with configurable jitter and user-agent rotation.
- Feature 2: Listener management with support for multiple concurrent channels.
- Feature 3: Integration hooks for Cobalt Strike's External C2 server, including sleep mask obfuscation.
- Feature 4: Logging and error handling for debugging C2 traffic.

## Installation

### Requirements

- Python 3.6+
- Cobalt Strike 4.0+ with External C2 enabled
- pip and git

### Install Commands

```bash
# Clone the repository
git clone https://github.com/threatexpress/external-c2-profiles.git externalc2
cd externalc2

# Install dependencies
pip install -r requirements.txt

# For Kali/Ubuntu
sudo apt update
sudo apt install python3-pip git
```

## Basic Usage

```python
import externalc2

# See help or examples in the library
dir(externalc2)
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help for library functions |
| `--verbose` | Enable detailed logging |
| `--profile` | Specify C2 profile file |

## Examples

### Example 1: Basic Usage

Register and start an HTTP listener:

```python
from externalc2 import register_profile, start_listener
register_profile('http', 'basic_profile.conf')
start_listener('http', port=8080, profile='basic_profile.conf')
```

### Example 2: Advanced Usage

Set up an HTTPS listener with SSL:

```python
from externalc2 import register_profile, start_listener
register_profile('https', 'secure_profile.conf')
start_listener('https', port=443, profile='secure_profile.conf', ssl_cert='server.crt', ssl_key='server.key')
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Standard Application Layer Protocol]] Application Layer Protocol
- [[Protocol Tunneling]] Protocol Tunneling

### Tactics

- [[Command and Control]] Command And Control

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual outbound HTTP/HTTPS traffic patterns matching malleable C2 profiles (e.g., via Suricata rules for Cobalt Strike signatures).
- Detection method 2: Python processes importing externalc2 module, visible in process lists or EDR logs.
- Detection method 3: Custom listener ports with encrypted traffic not associated with standard services.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Cobalt Strike]]
- [[Sliver C2]]

## References

- Official Cobalt Strike External C2 documentation: https://hstechdocs.helpsystems.com/manuals/cobaltstrike/current/userguide/content/topics/external_c2.htm
- GitHub Repository: https://github.com/threatexpress/external-c2-profiles
