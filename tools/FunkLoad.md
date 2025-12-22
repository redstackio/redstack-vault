---
id: 331285a1-c442-42d9-9586-fb3e3f25b593
name: FunkLoad
type: tool
verified: true
created_at: '2019-08-28T21:17:30.607119+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - load-testing
  - web-testing
  - performance-testing
  - stress-testing
  - python
url: 'https://funkload.nuxeo.com/'
commands:
  - '[[commands/funkload-install]]'
  - '[[commands/funkload-build-test]]'
  - '[[commands/funkload-run-test]]'
validated: true
---

# FunkLoad

**Status**: Unverified

## Overview

FunkLoad is a Python-based tool for functional, load, and stress testing of web applications. It is commonly used in security testing to simulate high traffic volumes, identify performance bottlenecks, and uncover issues like resource exhaustion that could lead to denial-of-service conditions.

## Description

FunkLoad allows testers to script web interactions using Python, mimicking real user behavior for regression testing, volume testing, and longevity testing. In offensive security contexts, it helps expose vulnerabilities in web apps under load, such as slow responses or crashes, and can be adapted for controlled DoS simulations to assess recoverability.

## Features

- Feature 1: Scriptable web agents for automating repetitive tasks and custom test scenarios.
- Feature 2: Detailed performance reporting, including hit rates, response times, and error logs.
- Feature 3: Support for multiple HTTP methods, authentication, and session handling.
- Feature 4: Integration with monitoring tools to track server metrics during tests.
- Feature 5: Functional testing for validating application behavior under normal loads.

## Installation

### Requirements

- Python 2.7 or 3.x
- pip package manager
- Access to target web application for testing

### Install Commands

```bash
# Install via pip
[[commands/funkload-install]]
```

For development setups:

```bash
pip install funkload --user
```

## Basic Usage

```bash
fl-run-test --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and usage |
| `-v, --verbose` | Enable verbose output for debugging |
| `-u, --users` | Specify number of virtual users |
| `-c, --cycles` | Set number of test cycles per user |

## Examples

### Example 1: Basic Usage

Build and run a simple test:

```bash
# Build test skeleton
[[commands/funkload-build-test]] simpletest

# Run the test
[[commands/funkload-run-test]] tests.simpletest.SimpleTestCase http://example.com
```

### Example 2: Advanced Usage

Load test with 50 users over 10 cycles:

```bash
fl-run-test tests.loadtest.LoadTestCase http://target.com -u 50 -c 10
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Denial of Service]] Network Denial of Service (for stress testing that simulates resource exhaustion)
- [[Endpoint Denial of Service]] Endpoint Denial of Service (when targeting specific application endpoints)

### Tactics

- [[Impact]] Impact (disruption through overload testing)

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual Python processes (fl-run-test) with high network outbound traffic to web servers.
- Detection method 2: Logs showing repeated HTTP requests from a single source with scripted patterns.
- Detection method 3: Server metrics indicating simulated load spikes without organic user increase.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Locust]] (Python-based load testing)
- [[tools/JMeter]] (Java-based performance testing)
- [[tools/Siege]] (HTTP load testing and benchmarking)

## References

- Official documentation: https://funkload.nuxeo.com/
- GitHub repository: https://github.com/nuxeo/funkload
- Python Package Index: https://pypi.org/project/FunkLoad/
