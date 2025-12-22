---
type: tool
verified: true
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - '[[dns]]'
  - '[[Enumeration]]'
url: 'https://github.com/vortexau/dnsvalidator'
description: >-
  A tool for fetching and validating lists of IPv4 DNS resolvers to ensure
  reliability and accuracy in DNS-based operations.
validated: true
---

# dnsvalidator

**Status**: ✓ Verified

## Overview

Dnsvalidator is a utility designed to fetch a list of public IPv4 DNS servers and validate them against known baseline servers (such as 1.1.1.1, 8.8.8.8, and 9.9.9.9) to ensure they provide accurate and timely responses. It is particularly useful in reconnaissance phases for maintaining a high-quality list of DNS resolvers, which can be used with tools like Amass for subdomain enumeration, zone transfers, or other DNS querying tasks. By filtering out unreliable or slow resolvers, it improves the efficiency of DNS enumeration workflows.

Category: Reconnaissance

## Description

The tool performs multithreaded validation by sending test queries to candidate DNS servers and comparing responses to baselines. It supports input from text files or URLs containing IP lists and outputs a cleaned list of validated resolvers. This helps avoid issues like rate limiting or inconsistent results during large-scale DNS operations. Dnsvalidator is written in Go, making it cross-platform, and can be run natively or via Docker for isolated execution.

## Features

- Multithreaded validation for fast processing of large resolver lists
- Baseline comparison using trusted DNS servers
- Support for custom timeouts and thread counts
- Output to file for easy integration with other tools
- Docker support for containerized environments

## Installation

### Requirements

- Go 1.13 or later (for native installation)
- Docker (for containerized usage)

### Install Commands

#### Native Installation (Kali/Ubuntu/macOS/Windows with Go)

```bash
# Install via Go
GO111MODULE=on go install github.com/vortexau/dnsvalidator@latest

# Or clone and build
mkdir -p $GOPATH/src/github.com/vortexau
cd $GOPATH/src/github.com/vortexau
git clone https://github.com/vortexau/dnsvalidator.git
dnsvalidator/go build -o dnsvalidator
sudo mv dnsvalidator /usr/local/bin/
```

#### Docker

Dnsvalidator has an official Docker image available on Docker Hub. Pull and use directly:

```bash
docker pull codingo/dnsvalidator
```

## Basic Usage

```bash
dnsvalidator --help
```

This displays all available options, including input sources (-tL for URL/text list), threading (-threads), output (-o), and timeout (--timeout).

### Common Options

| Option | Description |
|--------|-------------|
| -tL | Specify URL or file path to a list of DNS server IPs (one per line) |
| -threads | Set number of concurrent validation threads (default: 50, range: 1-200) |
| -o | Output file for validated resolvers |
| --timeout | DNS query timeout in seconds (default: 2) |
| -v | Verbose logging for detailed output |

## Examples

### Example 1: Native Fetch and Validate

Use [[commands/dnsvalidator-fetch-and-validate-resolvers]] to fetch from a public list and validate with 50 threads.

### Example 2: Docker-Based Validation

Use [[commands/dnsvalidator-docker-fetch-and-validate-resolvers]] to run in a container with mounted output.

## Related Commands

- [[commands/dnsvalidator-fetch-and-validate-resolvers]]
- [[commands/dnsvalidator-docker-fetch-and-validate-resolvers]]

## References

- Official GitHub: https://github.com/vortexau/dnsvalidator
- Public DNS List Source: https://public-dns.info/
