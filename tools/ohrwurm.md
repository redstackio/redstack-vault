---
type: tool
description: >-
  A lightweight RTP fuzzer for testing SIP-based VoIP systems, focusing on
  injecting malformed packets to identify vulnerabilities in RTP handling.
url: 'https://github.com/example/ohrwurm'
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - fuzzing
  - rtp
  - sip
  - voip
  - exploitation
validated: true
---

# ohrwurm

**Status**: Unverified

## Overview

ohrwurm is a compact RTP (Real-time Transport Protocol) fuzzer designed for security testing of SIP (Session Initiation Protocol) phones and VoIP systems. It generates malformed RTP packets to probe for crashes, denial-of-service conditions, or other vulnerabilities in RTP processing. Commonly used in penetration testing to simulate noisy line attacks or disrupt audio streams in switched LAN environments.

## Description

ohrwurm operates by either parsing SIP messages to identify RTP ports or accepting manual RTP port input, allowing it to fuzz any RTP traffic. It supports suppressing RTCP (RTP Control Protocol) traffic to prevent codecs from adapting to fuzz-induced noise, and applies a configurable constant Bit Error Rate (BER) to RTP payloads. Special fuzzing targets RTP header and payload structures to break handling logic. It requires a Man-in-the-Middle (MITM) setup using tools like arpspoof for traffic interception and injection, and is optimized for switched LANs where both endpoints are accessible (gateway mode has limited functionality).

## Features

- **SIP Message Parsing**: Automatically extracts RTP port numbers from captured SIP traffic.
- **Manual RTP Targeting**: Bypass SIP reading by specifying ports directly for broader RTP fuzzing.
- **RTCP Suppression**: Prevents RTCP from alerting codecs to noisy conditions, maintaining stealth.
- **Configurable BER Fuzzing**: Applies bit errors to RTP payloads at user-defined rates (e.g., 0.01 for 1% error).
- **MITM Integration**: Works with arpspoof for ARP poisoning in LAN environments.
- **Targeted RTP Breaking**: Focuses on corrupting RTP headers and payloads to exploit parsing flaws.

## Installation

### Requirements

- Linux environment (tested on Kali/Ubuntu)
- dsniff package for arpspoof (MITM dependency)
- libpcap for packet capture
- GCC for compilation

### Install Commands

```bash
# Clone the repository (assuming source availability)
git clone https://github.com/example/ohrwurm.git
cd ohrwurm

# Install dependencies
sudo apt update
sudo apt install dsniff libpcap-dev build-essential

# Compile the tool
make
sudo make install
```

## Basic Usage

```bash
ohrwurm --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -i, --interface | Specify network interface for traffic handling |
| -r, --rtp-port | Manually set RTP port(s) to fuzz |
| -s, --sip-file | Path to SIP capture file for port extraction |
| -b, --ber | Set Bit Error Rate (float, e.g., 0.01) |
| --no-rtcp | Suppress RTCP traffic during fuzzing |
| -h, --help | Display usage information |

## Examples

### Example 1: Basic Usage

Perform RTP fuzzing on a known port after setting up MITM with arpspoof.

```bash
# Setup MITM (in separate terminal)
arpspoof -i eth0 -t 192.168.1.10 192.168.1.1

# Run ohrwurm
ohrwurm -i eth0 -r 10000 -b 0.01
```

### Example 2: Advanced Usage

Use SIP file to auto-extract ports and suppress RTCP.

```bash
ohrwurm -i eth0 -s sip_capture.pcap -b 0.005 --no-rtcp
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service (fuzzing to disrupt VoIP services)
- [[Data Manipulation]] Data Manipulation (altering RTP payloads)

### Tactics

- [[Impact]] Impact
- [[Defense Evasion]] Defense Evasion (suppressing RTCP to avoid detection)

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual ARP traffic indicative of poisoning (monitor with arpwatch)
- Anomalous RTP packets with high BER or malformed headers (VoIP IDS like Snort rules for RTP)
- Network interface promiscuous mode on testing machines
- Process monitoring for ohrwurm or libpcap usage in unexpected contexts

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[arpspoof]] (for MITM setup)
- [[tools/Wireshark]] (for SIP/RTP capture)

## References

- Original tool source and documentation (if available via repository)
- VoIP security testing guides (e.g., OWASP VoIP resources)
