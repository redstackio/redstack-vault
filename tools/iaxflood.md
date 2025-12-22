---
id: 1cca54e2-2114-4165-9505-3d156fc815e6
type: tool
verified: true
created_at: '2019-08-28T21:17:38.360373+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - dos
  - voip
  - iax
  - asterisk
  - flood
url: 'https://www.kali.org/tools/iaxflood/'
commands:
  - '[[commands/iaxflood-flood-iax-target]]'
validated: true
---

# iaxflood

**Status**: Unverified

## Overview

iaxflood is a specialized denial-of-service (DoS) tool designed to target Asterisk-based IP PBX systems using the Inter-Asterisk eXchange (IAX) protocol. It sends floods of crafted UDP packets mimicking legitimate IAX channel traffic, which can overwhelm the target's processing resources more effectively than generic UDP floods. This tool is useful in penetration testing VoIP infrastructures to evaluate resilience against protocol-specific attacks.

Common use cases include red team exercises simulating VoIP service disruptions and security assessments of Asterisk deployments.

## Description

The tool originates from a captured IAX packet exchanged between two Asterisk PBX systems. This packet's payload is reused to construct attack packets, ensuring they resemble valid IAX traffic. Although the IAX protocol headers may not perfectly match all target configurations, the realistic payload forces the PBX to perform additional parsing and processing, amplifying the DoS impact compared to random UDP floods.

iaxflood operates over UDP (default port 4569) and is implemented as a Perl script. It supports customizing source/destination ports and the volume of packets sent, making it adaptable for different testing scenarios. Note that this tool can cause real service interruptions, so it should only be used in controlled environments with explicit permission.

## Features

- **Crafted IAX Payloads**: Uses real captured IAX channel data to create more effective flood packets.
- **Customizable Parameters**: Adjustable source/destination ports and packet counts for tailored attacks.
- **UDP-Based Flooding**: Simple, lightweight implementation focused on VoIP protocol exploitation.
- **Asterisk-Specific**: Optimized for targeting Asterisk PBX systems running IAX2.

## Installation

### Requirements

- Perl (version 5.x or higher)
- Root privileges for raw socket access (optional, but recommended for high-volume floods)
- Kali Linux or similar distribution for pre-built package

### Install Commands

iaxflood is pre-installed on Kali Linux. For other Debian-based systems like Ubuntu:

```bash
sudo apt update
sudo apt install iaxflood
```

If building from source (available from Kali repositories or GitHub mirrors):

```bash
# Clone or download the script
wget https://gitlab.com/kalilinux/packages/iaxflood/raw/master/iaxflood.pl
chmod +x iaxflood.pl
sudo mv iaxflood.pl /usr/local/bin/
```

For non-Linux platforms, ensure Perl is installed and adjust paths accordingly, though it's primarily designed for Unix-like systems.

## Basic Usage

```bash
perl iaxflood.pl --help
```

This displays available options, including target IP, ports, and call count.

### Common Options

| Option | Description |
|--------|-------------|
| No explicit flags; parameters passed positionally | Target IP, source port, dest port, num calls |
| Run as root | Enables higher packet rates via raw sockets |

## Examples

### Example 1: Basic Usage

Perform a basic IAX flood on a target PBX:

```perl
perl /usr/share/iaxflood/iaxflood.pl 192.168.1.100 4569 4569 1000
```

This sends 1000 IAX packets to the target at port 4569.

### Example 2: Advanced Usage

Flood with a custom source port for evasion:

```perl
perl /usr/share/iaxflood/iaxflood.pl 10.0.0.50 5000 4569 2000
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Denial of Service]] Network Denial of Service
- [[Direct Network Flood]] Direct Network Flood

### Tactics

- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- **Network Traffic**: Sudden spikes in UDP traffic to port 4569 (IAX default) with repeated IAX protocol signatures.
- **PBX Logs**: Asterisk logs showing excessive IAX registration or call attempts from a single source IP.
- **Process Monitoring**: Presence of iaxflood.pl or Perl processes with high network I/O on the attacker's machine.
- **IDS/IPS Rules**: Signatures for IAX flood patterns, such as anomalous packet rates from non-VoIP sources.
- **Firewall Logs**: Blocked or rate-limited UDP/4569 traffic.

Mitigation includes rate limiting on IAX ports, IP whitelisting for PBX access, and deploying VoIP-specific firewalls like Kamailio or intrusion prevention systems.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/hping3]] (General packet crafting and flooding)
- [[tools/scapy]] (Custom protocol flood scripting)

## References

- Kali Linux Tools: https://www.kali.org/tools/iaxflood/
- IAX Protocol Documentation: https://wiki.asterisk.org/wiki/display/AST/IAX
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1498/
