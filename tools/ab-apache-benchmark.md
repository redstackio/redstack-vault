---
url: 'https://httpd.apache.org/docs/2.4/programs/ab.html'
tags:
  - load-testing
  - dos
type: tool
verified: false
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:37.223Z'
id: 5cbc3090-59a5-482c-aea2-e8b8dd04db6f
validated: true
submitted: true
---
# ab-apache-benchmark

**Status**: Unverified

## Overview

Apache Benchmark (ab) is a command-line tool for benchmarking HTTP server performance, commonly used in security testing to simulate concurrent requests and demonstrate denial-of-service impacts like resource exhaustion.

## Description

ab measures server performance by sending multiple requests and reporting metrics such as requests per second, time per request, and transfer rates. In offensive security, it's ideal for validating DoS vulnerabilities by overwhelming endpoints with concurrency, as seen in simulating OOM on memory-intensive handlers.

## Features

- Feature 1: Supports concurrent and total request counts for load simulation
- Feature 2: Reports detailed stats including latency and failure rates
- Feature 3: Simple CLI interface for quick tests without complex setup

## Installation

### Requirements

- Apache HTTP Server utilities (part of httpd package)

### Install Commands

```bash
# On Ubuntu/Debian
sudo apt-get install apache2-utils

# On macOS with Homebrew
brew install httpd
```

## Basic Usage

```bash
ab -n 10 -c 5 http://example.com/
```

### Common Options

| Option | Description |
|--------|-------------|
| `-n` | Number of requests to perform |
| `-c` | Concurrency level |
| `-k` | Enable keep-alive connections |

## Examples

### Example 1: Basic Usage

```bash
ab -n 30 -c 30 http://localhost:8090/download
```

### Example 2: Advanced Usage

```bash
ab -n 100 -c 50 -T "application/json" http://target.com/api
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Endpoint Denial of Service]]

### Tactics

- [[Impact]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing high-volume requests from ab's user-agent (ApacheBench)
- Sudden spikes in concurrent connections to endpoints

## Related Procedures

- [[procedures/Simulate-DoS-with-Local-Go-Server-and-Load-Testing]]

## Related Tools

- [[wrk]]
- [[hey]]

## References

- Official documentation: https://httpd.apache.org/docs/2.4/programs/ab.html
