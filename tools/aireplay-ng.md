---
id: 9f608193-8e1f-4910-840f-7c7ad1a1136f
type: tool
verified: true
created_at: '2019-08-28T21:17:27.512722+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - wireless
  - injection
  - deauthentication
  - wpa
  - wep
url: 'https://www.aircrack-ng.org/doku.php?id=aireplay-ng'
commands:
  - '[[commands/aireplay-ng-deauthentication-attack]]'
  - '[[commands/aireplay-ng-fake-authentication]]'
  - '[[commands/aireplay-ng-arpreplay-attack]]'
  - '[[commands/aireplay-ng-test-injection]]'
validated: true
---

# aireplay-ng

**Status**: Unverified

## Overview

Aireplay-ng is a tool from the aircrack-ng suite designed for injecting and replaying wireless frames. It is primarily used to generate traffic for cracking WEP and WPA-PSK keys by performing attacks like deauthentication, fake authentication, and packet replay.

## Description

Aireplay-ng enables various wireless attacks, including deauthenticating clients to capture WPA handshakes, faking authentications to associate with access points, interactive packet replay, hand-crafted ARP request injection, and ARP-request reinjection. It requires a wireless interface in monitor mode and is commonly used in wireless penetration testing to assess and exploit Wi-Fi security.

## Features

- Feature 1: Deauthentication attacks to force client reconnections and capture handshakes
- Feature 2: Fake authentication to enable packet injection without legitimate association
- Feature 3: ARP replay for accelerating WEP IV collection
- Feature 4: Injection rate testing to verify hardware capabilities

## Installation

### Requirements

- Linux kernel with wireless extensions
- Compatible wireless card supporting monitor mode and packet injection

### Install Commands

```bash
# On Kali Linux (pre-installed)
# No action needed

# On Ubuntu/Debian
sudo apt update
sudo apt install aircrack-ng

# On macOS (via Homebrew)
brew install aircrack-ng
```

## Basic Usage

```bash
 aireplay-ng --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -v, --verbose | Increase verbosity |
| -D | Disable ACKs for faster injection |
| -x <rate> | Set injection rate in packets per second |

## Examples

### Example 1: Basic Usage

Test injection on an interface:

```bash
[[commands/aireplay-ng-test-injection]]
```

### Example 2: Advanced Usage

Perform deauthentication:

```bash
[[commands/aireplay-ng-deauthentication-attack]]
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Denial of Service]] Network Denial of Service (for deauth attacks)
- [[Domain Controller Authentication]] Domain Policy Modification (in context of credential access via handshakes)
- [[Active Scanning]] Active Scanning (for wireless reconnaissance)

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual deauthentication frames in wireless traffic (using Wireshark or wireless IDS like Kismet)
- Detection method 2: High injection rates or fake auth frames visible in packet captures
- Detection method 3: Monitor mode interfaces on endpoints (e.g., via netstat or wireless tools)

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/aircrack-ng]]
- [[tools/airodump-ng]]

## References

- Official documentation: https://www.aircrack-ng.org/doku.php?id=aireplay-ng
- Aircrack-ng GitHub: https://github.com/aircrack-ng/aircrack-ng
