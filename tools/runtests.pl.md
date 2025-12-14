---
url: 'https://curl.se/docs/testcurl.html'
tags:
  - testing
  - curl
type: tool
verified: false
platforms:
  - Linux
  - Unix
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:48.568Z'
id: e7d496c8-1c5c-4037-a7b7-dd4012bc14c5
validated: true
submitted: true
---
# runtests.pl

**Status**: Unverified

## Overview

runtests.pl is a Perl script used in the curl project to automate and execute the comprehensive test suite, including vulnerability reproductions like CVE-2023-23916 DoS tests.

## Description

This tool runs individual or batches of tests from the curl source, simulating various network scenarios, including HTTP responses. It's essential for developers and security researchers to verify fixes and reproduce issues in a controlled environment. In offensive security, it's used to demonstrate client-side vulnerabilities without external servers.

## Features

- Feature 1: Selective test execution by number (e.g., runtests.pl 418)
- Feature 2: Verbose logging for debugging allocation issues
- Feature 3: Integration with curl builds for cross-platform testing

## Installation

### Requirements

- Perl 5.x
- Curl source code cloned from repository

### Install Commands

```bash
# Clone curl source
git clone https://github.com/curl/curl.git
cd curl
# runtests.pl is in the root or tests/ directory; no separate install needed
```

## Basic Usage

```bash
runtests.pl --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v` | Verbose output for detailed test logs |
| `N` | Run specific test number N |

## Examples

### Example 1: Basic Usage

```bash
runtests.pl 418
```

Reproduces the DoS by running the multi-header test.

### Example 2: Advanced Usage

```bash
runtests.pl 418 -v
```

Provides verbose details on memory allocations during execution.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Tactics

- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of curl source directory with runtests.pl execution
- Perl process running with curl test arguments
- Logs showing test failures related to memory in /tmp/curl-tests

## Related Procedures

- [[procedures/Run-curl-DoS-Reproduction-Test]]

## Related Tools

- [[curl]]

## References

- Official curl testing docs: https://curl.se/docs/testcurl.html
- CVE-2023-23916 report: https://hackerone.com/reports/1826048
