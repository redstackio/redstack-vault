---
id: 33f2fea4-4ffa-483a-a863-24006a38b7a9
type: tool
verified: true
created_at: '2019-08-28T21:17:27.543929+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - sip
  - voip
  - testing
  - traffic-generation
  - fuzzing
url: 'https://sipp.sourceforge.net/'
validated: true
---

# SIPp

**Status**: Unverified

## Overview

SIPp is a free, open-source performance testing tool and traffic generator specifically designed for the Session Initiation Protocol (SIP). It is commonly used in security testing to simulate SIP user agents, generate call traffic, and test the resilience of VoIP systems such as SIP proxies, gateways, PBXs, and media servers against high loads, fuzzing, or specific attack scenarios.

## Description

SIPp enables the creation of realistic SIP call flows by including built-in scenarios for User Agent Client (UAC) and User Agent Server (UAS) behaviors, supporting methods like INVITE and BYE for establishing and releasing calls. It supports custom XML scenario files for complex interactions, from simple registrations to multi-branch call flows with authentication, media streams, and conditional logic. Key capabilities include dynamic statistics display (call rates, round-trip delays, message counts), CSV dumps for analysis, support for TCP/UDP over multiple sockets with retransmission handling, and adjustable call rates. Advanced features encompass IPv6, TLS, SCTP, SIP authentication, UDP retransmissions, error handling (timeouts, protocol defenses), variable injection from CSV files to mimic live users, and custom actions like logging or executing system commands. SIPp can generate RTP media traffic via echo or PCAP replay for audio/video testing. While optimized for stress, performance, and traffic testing, it can run single calls with pass/fail verdicts. It is invaluable for testing SIP equipment in security contexts, such as identifying denial-of-service vulnerabilities or protocol weaknesses in VoIP infrastructure.

## Features

- **Scenario Support**: Built-in UAC/UAS scenarios and custom XML files for flexible call flows.
- **Traffic Generation**: Adjustable rates, multiple sockets, and retransmission management for high-volume testing.
- **Statistics and Monitoring**: Real-time display of metrics like call rate, RTT, and message stats; periodic CSV exports.
- **Protocol Extensions**: IPv6, TLS, SCTP, authentication, and RTP media handling (echo/PCAP replay).
- **Customization**: Conditional scenarios, regex extraction/re-injection, CSV-driven variables, and custom actions (log, exec, stop).
- **Error Robustness**: Handles timeouts, retransmissions, and protocol errors for reliable testing.
- **Single-Call Mode**: Run one call and exit with verdict for simple validation.

## Installation

### Requirements

- C++ compiler (g++) for building from source.
- Optional: NCurses for statistics display, GSL for random distributions.

### Install Commands

```bash
# On Kali Linux (pre-installed in many distributions)
sudo apt update && sudo apt install sipp

# On Ubuntu
sudo apt update && sudo apt install sipp

# From source (for latest version)
# Download from https://sourceforge.net/projects/sipp/files/sipp/
wget https://sourceforge.net/projects/sipp/files/sipp/sipp-3.7.1.tar.gz/download -O sipp.tar.gz
tar -xzf sipp.tar.gz
cd sipp-3.7.1/
./build.sh
sudo make install

# On macOS (using Homebrew)
brew install sipp

# On Windows (via Cygwin or WSL)
# Install via package manager or build from source in a Unix-like environment
```

## Basic Usage

```bash
sipp --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-sn <scenario>` | Use built-in scenario (e.g., `uac` for client, `uas` for server). |
| `-sf <file>` | Load custom XML scenario file. |
| `-r <rate>` | Set call rate (calls per second). |
| `-m <max_calls>` | Maximum number of calls to place. |
| `-t <transport>` | Transport protocol (u1 for UDP, t1 for TCP, etc.). |
| `-p <port>` | Local port to bind to. |
| `-trace_stat` | Enable statistics tracing to CSV. |
| `-key <csv_name> <file>` | Inject variables from CSV file. |

## Examples

### Example 1: Basic Usage (UAC Scenario)

Simulate a SIP client making calls to a target server:

```bash
sipp -sn uac 192.168.1.100 -s 1234 -m 10
```

This places 10 calls to extension 1234 on the target IP using the built-in UAC scenario.

### Example 2: Advanced Usage (Custom Scenario with Rate)

Run a custom XML scenario with a rate of 5 calls/sec and TLS:

```bash
sipp -sf custom_scenario.xml -t t1 -r 5 -m 50 remote_host:5061
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning (for SIP endpoint discovery and probing).
- [[Network Denial of Service]] Network Denial of Service (for load testing that simulates DoS attacks).

### Tactics

- [[Reconnaissance]] Reconnaissance.
- [[Impact]] Impact.

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic showing high-volume SIP INVITE/BYE messages from a single source.
- Unusual RTP streams or PCAP replays in VoIP logs.
- Process monitoring for `sipp` executable on compromised hosts.
- SIP server logs indicating rapid call initiations or authentication attempts.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Wireshark]] (for capturing and analyzing SIP/RTP traffic).
- [[tools/metasploit]] (for SIP-specific exploits and modules).

## References

- Official documentation: https://sipp.sourceforge.net/doc/reference.html
- SIPp GitHub mirror: https://github.com/SIPp/sipp
- Related resources: RFC 3261 (SIP Protocol).
