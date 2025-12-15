---
url: 'https://jmeter.apache.org/'
tags:
  - load-testing
  - dos
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:55.844Z'
id: 85d42915-69f0-4cfa-b795-a8e38bec614e
validated: true
submitted: true
---
# Apache-JMeter

**Status**: Unverified

## Overview

Apache JMeter is an open-source load testing tool primarily used for performance testing web applications, but also effective for simulating denial-of-service attacks by generating high volumes of concurrent HTTP requests to vulnerable endpoints like WordPress load-scripts.php in CVE-2018-6389 scenarios.

## Description

JMeter supports creating test plans with thread groups, HTTP samplers, and listeners to mimic user traffic. In offensive security, it's used to demonstrate DoS impact by flooding resource-intensive endpoints, measuring response times, throughput, and errors. It runs in GUI or non-GUI mode, making it suitable for both manual testing and automated scripts.

## Features

- Feature 1: Thread Groups for simulating multiple concurrent users
- Feature 2: HTTP Request Samplers for crafting custom requests with parameters like 'load'
- Feature 3: Listeners (e.g., View Results Tree) for analyzing response data and errors

## Installation

### Requirements

- Java 8 or higher
- At least 2GB RAM for large tests

### Install Commands

```bash
# Download and extract
wget https://archive.apache.org/dist/jmeter/binaries/apache-jmeter-5.6.3.tgz
tar -xzf apache-jmeter-5.6.3.tgz
cd apache-jmeter-5.6.3/bin
./jmeter -v
```

## Basic Usage

```bash
jmeter -n -t test-plan.jmx -l results.jtl
```

### Common Options

| Option | Description |
|--------|-------------|
| `-n` | Non-GUI mode |
| `-t` | Test plan file |
| `-l` | Log results file |
| `-v` | Version info |

## Examples

### Example 1: Basic Usage

```bash
jmeter -n -t dos-test.jmx -l dos-results.jtl
```

### Example 2: Advanced Usage

```bash
jmeter -n -t dos-test.jmx -l results.jtl -e -o dashboard
```

(Generates a dashboard report for analysis.)

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Endpoint Denial of Service]]

### Tactics

- [[Privilege Escalation]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic showing bursts of identical HTTP requests from a single source
- JMeter user-agent strings in logs (e.g., Apache-HC/1.1)
- High-volume GET requests to specific endpoints like load-scripts.php

## Related Procedures

- [[procedures/Simulate-DoS-Attack-with-Apache-JMeter]]

## Related Tools

- [[Locust]]
- [[wrk]]

## References

- Official documentation: https://jmeter.apache.org/usermanual/index.html
- Related resources: Apache JMeter DoS tutorials on security blogs
