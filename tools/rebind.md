---
id: 5188e0d0-3400-44f1-84d6-d37655037e65
type: tool
verified: true
created_at: '2019-08-28T21:17:30.797003+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
tags:
  - dns-rebinding
  - exploitation
  - network-attack
  - router-exploitation
url: 'https://github.com/mogwai-poietic/rebind'
commands:
  - '[[commands/rebind-basic-dns-rebinding-attack]]'
  - '[[commands/rebind-advanced-multi-target-rebinding]]'
validated: true
---

# rebind

**Status**: Unverified

## Overview

Rebind is a specialized tool for executing DNS rebinding attacks, primarily targeting home routers and other devices with internal web interfaces. It exploits DNS resolution to bypass network restrictions, allowing an external attacker to access internal services by tricking the victim's browser into resolving the same domain to different IP addresses sequentially.

## Description

Rebind implements the multiple A record DNS rebinding technique, where the attacker's DNS server responds with the attacker's IP first (to serve a malicious webpage) and then switches to the target's internal IP (to access restricted services). Originally designed for home routers, it works against any public (non-RFC1918) IP address if the target implements a weak end-system model in its IP stack, has permissive firewall rules, and binds web services to the WAN interface. Remote administration does not need to be enabled; the attack relies on a user within the target network visiting a compromised or attacker-controlled website. This enables unauthorized access to internal admin panels, potentially leading to configuration changes, credential theft, or further network compromise.

## Features

- **Multiple A Record Support**: Rapidly cycles DNS responses between attacker and target IPs to evade same-origin policy.
- **HTTP Proxying**: Acts as a man-in-the-middle to relay requests to internal services and capture responses.
- **Customizable Cycling**: Adjustable timing for DNS record changes to match target browser behaviors.
- **Target Flexibility**: Works on routers, IoT devices, or any internal web service exposed indirectly.
- **Logging and Monitoring**: Real-time logs of rebinding attempts and successful internal accesses.

## Installation

### Requirements

- Python 3.x
- Access to a domain with controllable DNS (e.g., via a VPS or dynamic DNS service)
- Network privileges to bind to port 53 (DNS) and HTTP ports (may require sudo)

### Install Commands

```bash
# Clone the repository (assuming GitHub source)
git clone https://github.com/mogwai-poietic/rebind.git
cd rebind

# Install dependencies (if Python-based)
pip install -r requirements.txt

# For Kali/Ubuntu, ensure dnsmasq or similar is not conflicting on port 53
sudo apt update && sudo apt install python3-pip git
```

On macOS:
```bash
brew install python git
# Then follow clone steps
```

## Basic Usage

```bash
rebind --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -d, --domain | Specify the attacker-controlled domain |
| -i, --ip | Target internal IP address |
| -p, --port | Target service port |
| -l, --listen | Attacker's HTTP listen port |
| --cycle-time | DNS cycle interval in seconds |
| -v, --verbose | Enable detailed logging |

## Examples

### Example 1: Basic Usage

Set up a simple rebinding attack against a router's web interface:

```bash
rebind -d attacker.com -i 192.168.1.1 -p 80 -l 8080
```

Direct the victim to http://attacker.com, where the tool serves a page that triggers internal requests.

### Example 2: Advanced Usage

Target multiple internal services with custom cycling:

```bash
rebind -d attacker.com -i 192.168.1.1,10.0.0.50 -p 80,443 --cycle-time 0.5 -l 8080
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[LLMNR-NBT-NS Poisoning and SMB Relay]] [[Adversary-in-the-Middle: LLMNR/NBT-NS Poisoning and Relay]] (adapted for DNS manipulation)
- [[Drive-by Compromise]] [[Drive-by Compromise]]
- [[Exploit Public-Facing Application]] [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]] [[Initial Access]]
- [[Execution]] [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Anomalous DNS responses from legitimate domains resolving to multiple IPs rapidly.
- Unexpected outbound HTTP connections from browsers to attacker domains followed by internal service accesses.
- Network logs showing port 53 traffic from unauthorized sources or high-frequency A record queries.
- Browser developer tools revealing cross-origin requests to internal IPs.
- Firewall logs of internal-to-external IP cycling patterns.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[dnsmasq]]
- [[tools/bettercap]]

## References

- Official GitHub: https://github.com/mogwai-poietic/rebind
- DNS Rebinding Attacks: https://www.blackhat.com/presentations/bh-usa-07/Yoshioka/Presentation/bh-usa-07-yoshioka.pdf
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1557/
