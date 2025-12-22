---
id: b3690bcd-dfa6-4de1-a716-85ad6c5a7ae6
type: tool
verified: true
created_at: '2019-08-28T21:17:39.981662+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - network
  - mobile
  - 3g
  - modem
url: 'https://github.com/alfonskerke/sakis3g'
validated: true
---

# sakis3g

**Status**: Unverified

## Overview

Sakis3G is a shell script designed to establish 3G, UMTS, and GPRS connections using USB or Bluetooth modems on Linux systems. It automates modem detection, configuration, and connection setup, making it valuable for security testers needing mobile network access for pivoting, anonymous browsing, or evading network restrictions in pentesting scenarios.

## Description

Sakis3G works out-of-the-box with various modem-operator combinations by detecting hardware, setting up interfaces, and configuring APNs. It supports interactive mode for troubleshooting and command-line options for scripted deployments. Commonly used in Kali Linux for mobile forensics, network evasion, or establishing connections in remote testing environments where wired access is unavailable.

## Features

- Feature 1: Automatic USB/Bluetooth modem detection and chipset identification
- Feature 2: Interactive setup wizard for APN, PIN, and authentication configuration
- Feature 3: Support for multiple carriers and modem models with fallback options
- Feature 4: PPP interface management and connection monitoring
- Feature 5: Logging and error handling for debugging connection issues

## Installation

### Requirements

- Linux kernel with USB modem support (e.g., usb_modeswitch, pppd)
- Root privileges for interface configuration
- Compatible USB modem (e.g., Huawei, ZTE models)

### Install Commands

```bash
# Download the latest version from GitHub
wget https://raw.githubusercontent.com/alfonskerke/sakis3g/master/sakis3g.gz

# Extract the script
gzip -d sakis3g.gz
chmod +x sakis3g

# For Kali Linux (often pre-configured, but verify)
# The script is available in repositories or can be manually placed in /usr/local/bin
sudo cp sakis3g /usr/local/bin/
```

## Basic Usage

```bash
tool-name --help
```

Sakis3G is executed as a script; use `./sakis3g --help` for options.

### Common Options

| Option | Description |
|--------|-------------|
| `-d` | Detect USB modem |
| `--interactive` | Launch interactive setup |
| `--apn` | Specify APN for connection |
| `--console` | Run in console mode without GUI |
| `-l` | List available connections |

## Examples

### Example 1: Basic Usage

Detect and connect to a USB modem interactively.

```bash
./sakis3g --interactive
```

### Example 2: Advanced Usage

Automate connection with specific APN.

```bash
./sakis3g --apn "internet" --mpin "1234" --console
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Encrypted Channel]] Encrypted Channel: Used for establishing secure mobile connections to evade monitoring
- [[Connection Proxy]] Proxy: Facilitates network pivoting via mobile data

### Tactics

- [[Command and Control]] Command and Control: Enables alternative C2 channels over cellular networks

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Presence of sakis3g script in /tmp or /usr/local/bin directories
- Detection method 2: USB modem enumeration logs showing frequent attachments/detachments
- Detection method 3: Network traffic over PPP interfaces with mobile carrier IP ranges
- Detection method 4: Process monitoring for pppd spawned by sakis3g

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/usb_modeswitch]]
- [[tools/modemmanager]]

## References

- Official GitHub Repository: https://github.com/alfonskerke/sakis3g
- Kali Tools Documentation: https://www.kali.org/tools/sakis3g
- Original Project Page: http://www.sakis3g.info
