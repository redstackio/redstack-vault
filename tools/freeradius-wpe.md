---
id: 58ddf169-873c-4fda-8b32-4b6a5e93d243
type: tool
verified: true
created_at: '2019-08-28T21:17:30.208054+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - radius
  - wireless
  - credential-harvest
  - eap
  - impersonation
url: 'https://github.com/brad-antoniewicz/freeradius-wpe'
description: >-
  A patched version of FreeRADIUS for demonstrating RADIUS impersonation
  vulnerabilities and capturing wireless credentials.
validated: true
---

# freeradius-wpe

**Status**: Unverified

## Overview

freeradius-wpe is a modified version of the open-source FreeRADIUS server, developed by Joshua Wright and Brad Antoniewicz, designed to highlight RADIUS protocol impersonation vulnerabilities in wireless networks. It facilitates evil twin attacks or rogue AP scenarios by impersonating legitimate RADIUS servers, capturing EAP authentication credentials such as usernames and passwords. Commonly used in penetration testing for WiFi security assessments, it supports multiple EAP types including PEAP, TTLS, LEAP, EAP-MD5, EAP-MSCHAPv2, PAP, and CHAP.

## Description

This tool patches the standard FreeRADIUS implementation to simplify deployment in testing environments. It automatically configures acceptance of all RFC1918 private IP addresses as NAS (Network Access Server) devices, enabling broad compatibility without manual client configuration. It includes built-in support for all EAP authentication methods, a default users file that accepts any username for easy setup, and specialized WPE (Wireless Password Exposure) logging to capture credentials in a dedicated log file. The log can be customized via the 'wpelogfile' directive in radiusd.conf. This makes it ideal for red team operations simulating man-in-the-middle attacks on enterprise WiFi networks to harvest credentials.

## Features

- **Simplified NAS Configuration**: Automatically accepts all RFC1918 addresses (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) as valid clients, reducing setup time.
- **EAP Support**: Full compatibility with PEAP, TTLS, LEAP, EAP-MD5, EAP-MSCHAPv2, PAP, CHAP, and other methods for credential capture.
- **WPE Logging**: Captures authentication details (usernames, passwords, NAS IPs) in /var/log/radius/freeradius-server-wpe.log.
- **Default User Acceptance**: Includes a pre-configured users file that authenticates any provided username, simulating vulnerable authentication.
- **Debug and Monitoring**: Supports verbose logging for real-time observation of RADIUS exchanges.

## Installation

### Requirements

- Linux system (tested on Ubuntu/Debian derivatives like Kali)
- Build essentials: gcc, make, libssl-dev, libtalloc-dev
- Git

### Install Commands

```bash
# Clone the repository
git clone https://github.com/brad-antoniewicz/freeradius-wpe.git
cd freeradius-wpe

# Bootstrap and configure
./bootstrap
./configure --prefix=/usr/local/freeradius-wpe

# Build and install
make
sudo make install

# Set up directories and configs
sudo mkdir -p /var/log/radius
sudo cp freeradius-server-wpe.log /var/log/radius/
```

For Kali Linux, it may be available via apt, but building from source is recommended for the latest patches:

```bash
sudo apt update
sudo apt install freeradius-wpe
```

## Basic Usage

```bash
radiusd --help
```

Configure the server by editing /usr/local/freeradius-wpe/etc/raddb/clients.conf if needed (though defaults cover RFC1918). Start the server and monitor logs during a wireless association test.

### Common Options

| Option | Description |
|--------|-------------|
| -X | Debug mode with verbose output |
| -f | Run in foreground |
| -c <config> | Specify configuration file |
| -l <logdir> | Set log directory |

## Examples

### Example 1: Basic Usage

Start in debug mode to monitor authentications:

```bash
radiusd -X
```

See [[commands/freeradius-wpe-start-debug]] for details.

### Example 2: Advanced Usage

Tail the WPE log while the server runs:

In one terminal:

```bash
radiusd -f
```

In another:

```bash
tail -f /var/log/radius/freeradius-server-wpe.log
```

See [[commands/freeradius-wpe-tail-logs]] for details.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[LLMNR-NBT-NS Poisoning and SMB Relay]] Adversary-in-the-Middle: LLMNR/NBT-NS Poisoning and Relay (adapted for RADIUS/WiFi)
- [[Password Filter DLL]] Modify Authentication Process: Password Policy Discovery (credential capture via impersonation)

### Tactics

- [[Credential Access]] Credential Access
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual RADIUS server processes (radiusd with non-standard paths or configs)
- Log entries for rogue authentications or high failure rates in legitimate RADIUS logs
- Network traffic: Unexpected RADIUS packets (UDP 1812/1813) from unauthorized sources
- File system artifacts: Presence of freeradius-wpe.log or patched binaries
- Process monitoring: radiusd running in debug mode (-X flag)

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
- [[hostapd]]

## References

- Official GitHub: https://github.com/brad-antoniewicz/freeradius-wpe
- Original Paper: "Wireless Password Exposure" by Joshua Wright and Brad Antoniewicz
- FreeRADIUS Documentation: https://freeradius.org/documentation/
