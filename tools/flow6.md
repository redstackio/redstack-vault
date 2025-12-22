---
id: b05cd5c2-91d6-4f57-9033-d0ed05997770
type: tool
verified: true
created_at: '2019-08-28T21:17:23.012685+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
tags:
  - ipv6
  - flow-label
  - security-assessment
  - network-testing
url: 'https://www.si6networks.com/tools/ipv6toolkit/'
commands:
  - '[[commands/flow6-send-specific-flow-label]]'
  - '[[commands/flow6-random-flow-label-test]]'
  - '[[commands/flow6-flow-label-flood]]'
validated: true
---

# flow6

**Status**: Unverified

## Overview

flow6 is a specialized tool from the SI6 Networks’ IPv6 Toolkit designed for security assessment of the IPv6 Flow Label. It enables testers to craft and send IPv6 packets with controlled flow labels to evaluate how devices process, preserve, or mishandle flow-labeled traffic, identifying potential vulnerabilities in IPv6 implementations related to traffic classification, privacy, and denial-of-service resilience.

## Description

The IPv6 Flow Label is an 20-bit field intended for labeling packets belonging to specific flows for efficient processing by intermediate devices. flow6 allows security professionals to perform targeted tests, such as sending packets with specific or random flow labels, to check for flaws like improper stripping, leaking of flow information, or overload from flow-based processing. It's particularly useful in IPv6 network penetration testing, compliance audits, and troubleshooting flow label-related issues. As part of the broader IPv6 Toolkit, it complements other tools like scan6 for comprehensive IPv6 assessments but focuses exclusively on flow label behavior.

## Features

- Feature 1: Send IPv6 packets with arbitrary flow labels to test preservation and processing.
- Feature 2: Support for random flow label generation to simulate varied traffic patterns.
- Feature 3: Flooding capabilities to evaluate DoS resilience against flow-labeled packets.
- Feature 4: Integration with network interfaces for real-world IPv6 traffic injection.
- Feature 5: Verbose logging for detailed analysis of sent packets and potential errors.

## Installation

### Requirements

- Linux system with IPv6 support enabled.
- Root privileges for raw socket access.
- Compiler (gcc) and make for building from source.

### Install Commands

The flow6 tool is part of the SI6 IPv6 Toolkit. Install as follows:

```bash
# Clone the repository (open-source version available via forks or official download)
git clone https://github.com/fgontipv6/ipv6-toolkit.git  # Note: Official may require download from SI6 site
cd ipv6-toolkit
./configure
make
sudo make install
```

For Kali Linux (pre-built package may be available):

```bash
sudo apt update
sudo apt install ipv6toolkit
```

Verify installation:

```bash
flow6 --help
```

## Basic Usage

```sh
flow6 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -i, --interface | Specify network interface |
| -f, --flowlabel | Set specific flow label value |
| -r, --random | Use random flow labels |
| -c, --count | Number of packets to send |
| -F, --flood | Set flooding rate (pps) |
| -v, --verbose | Enable verbose output |

## Examples

### Example 1: Basic Usage

Send a single packet with flow label 12345:

```sh
flow6 -i eth0 -f 12345 2001:db8::1
```

### Example 2: Advanced Usage

Flood with random flow labels:

```sh
flow6 -i eth0 -r -c 100 -F 200 2001:db8::1
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning (for IPv6 flow assessment)
- [[Network Denial of Service]] Network Denial of Service (via flow label flooding)

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual IPv6 packet bursts with varying or specific flow labels (monitor with tcpdump or Wireshark filters like 'ipv6.flowlabel == 12345').
- Detection method 2: High packet rates from a single source targeting IPv6 interfaces, logged in firewall or IDS rules for IPv6 anomalies.
- Detection method 3: Presence of SI6 Toolkit binaries or processes named 'flow6' in system logs.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/scan6]] (IPv6 scanning companion)
- [[tools/ra6]] (Router Advertisement testing)
- [[tools/Nmap]] (General network scanning)

## References

- Official documentation: https://www.si6networks.com/tools/ipv6toolkit/flow6.phtml
- IPv6 Flow Label RFC: https://datatracker.ietf.org/doc/html/rfc6437
- GitHub mirror: https://github.com/fgontipv6/ipv6-toolkit
