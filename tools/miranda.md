---
id: 7980406f-e5f2-45ba-afe9-81963c061482
type: tool
verified: true
created_at: '2019-08-28T21:17:38.829935+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
tags:
  - upnp
  - reconnaissance
  - network
  - igmp
  - router
url: ''
validated: true
---

# miranda

**Status**: Unverified

## Overview

Miranda is a Python-based Universal Plug-N-Play (UPnP) client application designed to discover, query, and interact with UPnP devices, particularly Internet Gateway Devices (IGDs) such as routers. It is used in security testing to audit UPnP-enabled devices on a network for vulnerabilities, including unauthorized port forwarding, information disclosure, and configuration manipulation.

## Description

Miranda provides a comprehensive interface for interacting with UPnP services. It supports both passive and active discovery methods, customizable queries, and full control over network settings like IP addresses, ports, and headers. The tool enables enumeration of devices, services, actions, and state variables, as well as sending actions to services for testing purposes. Data can be saved to files for analysis, and all interactions are logged. Built for Linux with Python 2.5, it has been tested against IGDs from vendors like Linksys, D-Link, Belkin, and ActionTec. While primarily for Linux, its Python nature allows portability to other platforms with Python support.

## Features

- Interactive shell with tab completion and command history for real-time interaction
- Passive and active discovery of UPnP devices using SSDP/M-SEARCH
- Customizable M-SEARCH queries to target specific devices or services
- Full control over application settings including IP addresses, ports, and HTTP headers
- Enumeration of UPnP devices, services, actions, and state variables
- Correlation of input/output state variables with service actions
- Sending custom actions to UPnP services and devices
- Data export to files for offline analysis and collaboration
- Built-in command logging for auditing sessions

## Installation

### Requirements

- Python 2.5 or later (tested on Python 2.5 with Linux 2.6 kernel)
- Standard Python libraries (no additional dependencies on default Linux Mint 5/Ubuntu 8.04 installs)
- Network access to multicast (UDP 1900) for discovery

### Install Commands

Miranda is typically run from source as it is not available via standard package managers. Download the source code (legacy tool, source may need to be obtained from archives or repositories like GitHub mirrors).

```bash
# Clone or download source (example assuming a repo URL; adjust as needed)
git clone https://github.com/example/miranda-upnp.git
cd miranda-upnp

# No formal install; run directly
python miranda.py --help

# For Ubuntu/Kali (Python 2.x may need installation if not present)
sudo apt update
sudo apt install python2.7  # If Python 2 is not installed
```

Note: This is a legacy tool (circa 2009); consider modern alternatives like upnp-client or gupnp for newer Python versions.

## Basic Usage

```bash
python miranda.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and available commands |
| -i, --interface | Specify network interface for operations |
| -v, --verbose | Enable verbose output for debugging |
| --config | Load custom configuration file |

## Examples

### Example 1: Basic Usage

Start the interactive shell for manual exploration:

```bash
python miranda.py shell -i eth0
```

Within the shell:
- `discover` to find devices
- `query <url>` to enumerate a device
- `action <url> <service> <action>` to invoke an action

### Example 2: Advanced Usage

Perform discovery and save results:

```bash
python miranda.py discover -i eth0 -t 60 --output devices.xml
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning (for UPnP discovery and enumeration)
- [[System Information Discovery]] System Information Discovery (querying device details)

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual SSDP/M-SEARCH multicast traffic on UDP/1900
- HTTP requests to UPnP control URLs (e.g., /rootDesc.xml, /wanipc1) from non-browser user agents
- Python processes with network activity to router IPs on high ports (e.g., 49152)
- Log entries for UPnP actions like AddPortMapping without legitimate user initiation
- Network logs showing repeated device queries from a single host

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Nmap]] (for initial port scanning before UPnP interaction)
- [[tools/scapy]] (for custom SSDP packet crafting)

## References

- Original tool documentation (legacy, circa 2009)
- UPnP specifications: http://upnp.org/specs/arch/UPnP-arch-DeviceArchitecture.pdf
- Related resources: UPnP security auditing guides
