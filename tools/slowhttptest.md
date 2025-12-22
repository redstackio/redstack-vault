---
id: 1116bb84-1862-44f3-882c-aaebb0a2672f
type: tool
description: >-
  A highly configurable tool for simulating low-bandwidth Application Layer
  Denial of Service (DoS) attacks such as Slowloris, Slow HTTP POST, Slow Read,
  and Apache Range Header attacks.
verified: true
created_at: '2019-08-28T21:17:38.325581+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - dos
  - slowloris
  - application-layer-attack
url: 'https://github.com/shekyan/slowhttptest'
commands:
  - '[[commands/slowhttptest-slowloris-attack]]'
  - '[[commands/slowhttptest-slow-http-post]]'
  - '[[commands/slowhttptest-slow-read-attack]]'
  - '[[commands/slowhttptest-range-header-attack]]'
validated: true
---

# slowhttptest

**Status**: Unverified

## Overview

SlowHTTPTest is a highly configurable tool designed to simulate low-bandwidth Application Layer Denial of Service (DoS) attacks. It is particularly useful for testing the resilience of web servers against attacks that exhaust server resources through partial or slow HTTP requests. Common use cases include penetration testing web applications, assessing server configurations for DoS vulnerabilities, and training security teams on application-layer threats. The tool supports multiple attack vectors and works on Linux, macOS, and Windows (via Cygwin).

## Description

SlowHTTPTest implements several common low-bandwidth Application Layer DoS attacks, including Slowloris (which holds connections open with partial headers), Slow HTTP POST (sending data slowly in POST bodies), Slow Read (exploiting TCP persist timers to drain connection pools), and Apache Range Header attacks (causing excessive memory and CPU usage via malformed range requests). These attacks leverage the HTTP protocol's design, where servers must wait for complete requests before processing, allowing attackers to tie up resources with minimal bandwidth. The tool sends partial HTTP requests to overwhelm the target's connection pool, leading to denial of service for legitimate users.

## Features

- **Slowloris Attack**: Keeps connections alive by sending incomplete HTTP headers at intervals.
- **Slow HTTP POST**: Simulates slow uploads in POST requests to exhaust server timeouts.
- **Slow Read Attack**: Reads responses slowly to exploit TCP persistence and drain pools.
- **Range Header Attack**: Targets Apache servers with excessive byte-range requests.
- **Configurable Parameters**: Adjust connection count, intervals, rates, and timeouts for realistic simulations.
- **Statistics Logging**: Provides real-time stats on connections, errors, and attack progress.
- **Multi-Platform Support**: Runs on Linux, macOS, and Windows environments.

## Installation

### Requirements

- GCC compiler and make (for building from source)
- Autoconf and Automake (for generating build files)
- Git (to clone the repository)

### Install Commands

On Kali Linux (pre-built package available):
```bash
sudo apt update
sudo apt install slowhttptest
```

On Ubuntu:
```bash
sudo apt update
sudo apt install git build-essential autoconf automake libtool
```

Building from source (all platforms):
```bash
git clone https://github.com/shekyan/slowhttptest.git
cd slowhttptest
./autogen.sh
./configure
make
sudo make install
```

On macOS (using Homebrew for dependencies):
```bash
brew install autoconf automake libtool
# Then follow source build steps
```

On Windows (via Cygwin):
Install Cygwin with GCC, make, git, autoconf, automake, then follow source build.

## Basic Usage

```bash
slowhttptest --help
```

This displays all available options, attack types, and parameters.

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and exit |
| `-c NUM` | Number of connections to initiate |
| `-i SEC` | Interval between partial requests (seconds) |
| `-r NUM` | Rate of follow-up requests per second |
| `-u URL` | Target URL for the attack |
| `-v` | Verbose output for debugging |

## Examples

### Example 1: Basic Usage

For a simple Slowloris attack, see [[commands/slowhttptest-slowloris-attack]].

### Example 2: Advanced Usage

For a Slow HTTP POST attack with custom parameters, refer to [[commands/slowhttptest-slow-http-post]].

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Denial of Service]] Network Denial of Service
- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Tactics

- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual patterns of partial HTTP requests or slow connections in server logs (e.g., Apache access logs showing incomplete headers).
- High number of open but idle TCP connections from a single source IP.
- Anomalous byte-range requests in HTTP headers.
- Network monitoring tools like Wireshark showing low-bandwidth, persistent traffic to port 80/443.
- IDS/IPS signatures for Slowloris or Range Header exploits (e.g., Snort rules for T1498).

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/hping3]] (for TCP-based DoS testing)
- [[tools/slowloris]] (Python implementation of Slowloris)

## References

- Official GitHub Repository: https://github.com/shekyan/slowhttptest
- Original Slowloris Paper: https://ha.ckers.org/slowloris/
