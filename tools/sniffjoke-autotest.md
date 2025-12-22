---
id: 4e8664ab-78c7-4018-8c13-ca14006f4701
type: tool
verified: true
description: >-
  Automated testing suite for SniffJoke, a Linux tool that transparently handles
  TCP connections by delaying, modifying, and injecting fake packets to evade
  passive wiretapping technologies like IDS and sniffers.
url: 'https://github.com/friedrichsf/SniffJoke'
created_at: '2019-08-28T21:17:42.832810+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - defense-evasion
  - network
  - testing
  - sniffer-evasion
  - ids
validated: true
---

# sniffjoke-autotest

**Status**: Unverified

## Overview

SniffJoke-Autotest is the automated testing component of the SniffJoke framework, designed for Linux systems. It verifies the effectiveness of SniffJoke's TCP connection manipulation features, which delay, modify, and inject fake packets to make traffic nearly impossible for passive sniffers or IDS to interpret correctly. Use it during setup or validation to ensure evasion capabilities work as expected in simulated environments.

## Description

SniffJoke-Autotest runs scripted tests that simulate real-world network sniffing scenarios, measuring evasion success rates for packet injections and modifications. It's particularly useful for red teamers testing network evasion tools or defenders evaluating IDS resilience. The tool integrates with SniffJoke's core library and supports both basic and advanced test modes, providing detailed reports on undetectability.

## Features

- **Basic Testing**: Quick validation of core TCP handling and simple packet injection.
- **Advanced Simulation**: Emulates IDS/sniffer detection with configurable durations and scenarios.
- **Reporting**: Generates logs and metrics on evasion rates, undetected packets, and test outcomes.
- **Integration**: Works seamlessly with SniffJoke's transparent proxy mode for live traffic testing.
- **Customizable**: Supports verbose output, custom durations, and output file generation.

## Installation

### Requirements

- Linux kernel with iptables support
- libevent-dev and libpcap-dev
- Python 2.7 or 3.x for autotest scripts
- build-essential (gcc, make)

### Install Commands

```bash
# Clone the repository
sudo apt update && sudo apt install git build-essential libevent-dev libpcap-dev python3

git clone https://github.com/friedrichsf/SniffJoke.git
cd SniffJoke

# Configure with autotest support
./configure --enable-autotest

# Build and install
make
sudo make install

# Verify installation
sniffjoke -h
```

For Kali Linux, most dependencies are pre-installed; simply clone and build.

## Basic Usage

```bash
cd SniffJoke/autotest
python autotest.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Display help and usage information |
| `-v, --verbose` | Enable detailed logging during tests |
| `-o, --output FILE` | Save test results to a file |

## Examples

### Example 1: Basic Usage

Run a quick basic test:

```bash
python autotest.py --basic
```

### Example 2: Advanced Usage

Simulate IDS evasion for 5 minutes:

```bash
python autotest.py --advanced --duration 300 -v
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Disable or Modify Tools]] Disable or Modify Tools (impairing IDS/sniffer detection)
- [[Obfuscated Files or Information]] Obfuscated Files or Information (packet modification for evasion)

### Tactics

- [[Defense Evasion]] Defense Evasion
- [[Reconnaissance]] Reconnaissance (testing network visibility)

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of SniffJoke binaries or autotest.py in /usr/local/bin or custom paths.
- Unusual iptables rules or libevent processes handling TCP traffic.
- Network anomalies like delayed packets or unexpected fake connections during tests.
- Log entries for 'sniffjoke' or 'autotest' in system journals.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/sniffjoke]] (core framework)
- [[tools/Wireshark]] (for validating test results)
- [[Scapy]] (alternative packet manipulation)

## References

- Official GitHub: https://github.com/friedrichsf/SniffJoke
- Documentation: README in the repository
- Related: SniffJoke whitepaper on packet injection techniques
