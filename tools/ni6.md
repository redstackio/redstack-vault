---
id: 66452019-5862-4623-af22-6da737319744
type: tool
verified: true
created_at: '2019-08-28T21:17:39.959000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - ipv6
  - icmpv6
  - security-assessment
  - troubleshooting
url: 'https://www.si6networks.com/tools/ipv6toolkit/ni6'
commands:
  - '[[commands/ni6-send-node-information-query]]'
  - '[[commands/ni6-send-node-information-response]]'
  - '[[commands/ni6-assess-flaws-in-processing]]'
validated: true
---

# ni6

**Status**: Unverified

## Overview

ni6 is a specialized tool from the SI6 Networks’ IPv6 Toolkit designed to send arbitrary ICMPv6 Node Information (NI) messages and assess potential flaws in the processing of such packets. It is commonly used in IPv6 security assessments to test network devices for vulnerabilities related to NI message handling, such as information disclosure or denial of service conditions.

## Description

The tool allows security professionals to craft and send custom ICMPv6 Node Information Queries and Responses, enabling tests for how IPv6-enabled devices handle these messages. This can reveal implementation flaws, aid in reconnaissance by querying node details (e.g., hostnames, IPv4 addresses), or simulate attacks to evaluate resiliency. ni6 is part of a broader suite for IPv6 troubleshooting and penetration testing, focusing on the ICMPv6 protocol's NI extension (RFC 4620).

## Features

- Feature 1: Send arbitrary Node Information Query messages to elicit responses from targets.
- Feature 2: Forge Node Information Response messages for spoofing or testing response validation.
- Feature 3: Assess flaws by sending malformed or oversized NI packets to detect crashes or unexpected behaviors.
- Feature 4: Support for specifying network interfaces and verbose logging for detailed analysis.

## Installation

### Requirements

- Linux system with IPv6 support enabled.
- Root privileges for raw socket access.
- libpcap and other standard build dependencies.

### Install Commands

The ni6 tool is part of the IPv6 Toolkit. Install via source:

```bash
# Clone the repository
sudo apt update
sudo apt install git build-essential libpcap-dev

git clone https://github.com/fgont/ipv6-toolkit.git
cd ipv6-toolkit
./configure
make
sudo make install
```

On Kali Linux, it may be available via package manager:

```bash
sudo apt install ipv6toolkit
```

## Basic Usage

```bash
ni6 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -v, --verbose | Enable verbose output for debugging |
| -i, --interface | Specify the network interface |
| -q | Send Node Information Query |
| -r | Send Node Information Response |
| -f | Assess flaws in NI processing |

## Examples

### Example 1: Basic Usage

Send a Node Information Query for the target's name:

```bash
ni6 -q name 2001:db8::1
```

### Example 2: Advanced Usage

Assess for flaws with verbose output:

```bash
ni6 -f malformed 2001:db8::1 -v -i eth0
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning (for querying node info)
- [[Network Denial of Service]] Network Denial of Service (via malformed packets)

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for unusual ICMPv6 Type 139/140 (NI Query/Response) packets using tools like tcpdump or Wireshark.
- Detection method 2: Log raw IPv6 traffic for forged source IPs or malformed NI payloads.
- Detection method 3: System logs showing crashes or errors in IPv6 stack processing NI messages.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/scan6]] (IPv6 scanning tool from the same toolkit)
- [[tools/ra6]] (Router Advertisement tool)
- [[tools/tcpdump]] (For capturing and analyzing IPv6 traffic)

## References

- Official documentation: https://www.si6networks.com/tools/ipv6toolkit/ni6
- RFC 4620: Node Information Protocol
- GitHub Repository: https://github.com/fgont/ipv6-toolkit
