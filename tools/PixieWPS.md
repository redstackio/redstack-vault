---
id: 51343a1a-9137-4951-b75b-05b1e3144307
type: tool
verified: true
created_at: '2019-08-28T21:17:19.954739+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - wifi
  - wps
  - bruteforce
  - pixie-dust
  - credential-access
url: 'https://github.com/wiire-a/PixieWPS'
commands:
  - '[[commands/pixiewps-basic-pin-bruteforce]]'
  - '[[commands/pixiewps-advanced-pin-bruteforce]]'
validated: true
---

# PixieWPS

**Status**: Unverified

## Overview

PixieWPS is a specialized tool for performing offline WPS PIN recovery attacks, known as the Pixie Dust attack. It exploits access points with low or non-existent entropy in their Wi-Fi Protected Setup (WPS) implementation, allowing rapid PIN bruteforcing without online attempts. Primarily used in wireless penetration testing to demonstrate vulnerabilities in legacy WPS-enabled routers.

## Description

PixieWPS, written in C, implements the Pixie Dust attack discovered by Dominique Bongard. It works by analyzing captured WPS registration messages (M1/M2) to recover the PIN offline using optimizations on the access point's weak pseudorandom number generator (PRNG). This tool is intended for educational and authorized security testing purposes only, as unauthorized use may violate laws regarding network access.

## Features

- **Checksum Optimization**: Prioritizes trying the 11,000 valid PIN checksums first for faster recovery.
- **Reduced Entropy Handling**: Optimizes the C LCG PRNG seed entropy from 32 bits down to 25 bits, making bruteforcing feasible.
- **Small Diffie-Hellman Support**: Compatible with Reaver's small DH key mode; no need to specify the Public Registrar Key.
- **E-Nonce Mode**: Attempts E-S0 = E-S1 = 0 initially, then bruteforces the PRNG seed if the --e-nonce option is used.
- **Offline Operation**: All computation is local, avoiding repeated association attempts that could alert the target.

## Installation

### Requirements

- Linux environment (Kali Linux recommended)
- Git and build essentials (gcc, make)
- libpcap-dev for packet capture dependencies (if integrating with Reaver)

### Install Commands

On Kali Linux (pre-compiled package available):
```bash
sudo apt update
sudo apt install pixiewps
```

Manual compilation from source:
```bash
git clone https://github.com/wiire-a/PixieWPS.git
cd PixieWPS/src
make
sudo make install
```

## Basic Usage

```bash
pixiewps --help
```

This displays all available options, including modes for nonce handling and MAC specifications.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and exit |
| -v, --version | Display PixieWPS version |
| -e, --e-nonce | Specify E-Nonce for attack (32 bytes hex) |
| -s, --e-s1 | Specify E-S1 value (32 bytes hex) |
| -z, --e-z1 | Specify E-Z1 value (32 bytes hex) |
| -a, --ap-mac | Target access point MAC address |
| -S, --seed | Enable PRNG seed bruteforcing |
| -f, --force | Force bruteforce on failure |

## Examples

### Example 1: Basic Usage

Use with values captured from Reaver:
```bash
pixiewps -e 1234567890abcdef1234567890abcdef1234567890abcdef -s 00000000000000000000000000000000 -z 00000000000000000000000000000000 -a aa:bb:cc:dd:ee:ff -m 11:22:33:44:55:66 -m 77:88:99:aa:bb:cc
```

### Example 2: Advanced Usage

With seed bruteforcing:
```bash
pixiewps -e $_E_NONCE -s $_E_S1 -z $_E_Z1 -a $_AP_MAC -m $_M1 -m $_M2 -S -f
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Brute Force]] Brute Force (exploiting weak WPS PIN generation for credential recovery)
- [[Unsecured Credentials]] Unsecured Credentials (recovering WPS PINs from vulnerable implementations)

### Tactics

- [[Credential Access]] Credential Access
- [[Initial Access]] Initial Access (gaining wireless network access via recovered credentials)

## Detection

Indicators and methods for detecting this tool's usage:

- **Network Traffic**: Monitor for WPS M1/M2 message captures using tools like Wireshark; look for repeated WPS associations from tools like Reaver preceding PixieWPS use.
- **Process Monitoring**: Detection of 'pixiewps' binary execution on attacker machines; check for compilation artifacts in /tmp or source directories.
- **AP Logs**: Vulnerable access points may log failed WPS attempts; correlate with offline computation times.
- **Entropy Analysis**: Advanced IDS can flag low-entropy PRNG patterns in captured WPS exchanges.
- **Disable WPS**: Best defense is to disable WPS on all access points, as Pixie Dust targets this feature specifically.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/reaver]] (for capturing WPS messages to feed into PixieWPS)
- [[tools/bully]] (alternative WPS attack tool compatible with PixieWPS)
- [[tools/aircrack-ng]] (suite for WiFi auditing, including WPS components)

## References

- Official GitHub Repository: https://github.com/wiire-a/PixieWPS
- Original Research: Dominique Bongard's Pixie Dust paper
- WiFi Alliance WPS Documentation

*Last updated: 2023-10-01T00:00:00Z*
