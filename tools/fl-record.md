---
type: tool
description: >-
  A session recording utility from the FunkLoad suite for capturing web
  interactions to generate automated test scripts.
url: 'https://funkload.nexedi.com/'
verified: true
commands:
  - '[[commands/fl-record-start-recording]]'
  - '[[commands/fl-record-dump-browser-cookies]]'
platforms:
  - Linux
  - macOS
tags:
  - web-testing
  - load-testing
  - functional-testing
  - session-recording
validated: true
---

# fl-record

**Status**: Unverified

## Overview

fl-record is a command-line tool from the FunkLoad Python framework designed for recording web browser sessions to automatically generate Python test scripts. It is primarily used for functional testing, regression testing, and preparing scripts for load and stress testing of web applications. In security contexts, it can simulate user behaviors for testing application robustness under load or for scripting repetitive web tasks during reconnaissance or exploitation preparation.

Category: Web Application Testing

## Description

FunkLoad, including its fl-record component, enables testers to record real user interactions with a web application via a launched browser (using Python's webbrowser module). The tool captures HTTP requests, form submissions, and navigation to create reusable Python scripts that mimic the session. These scripts can then be executed with fl-run for functional validation or scaled for performance/load testing to identify bottlenecks, simulate high traffic, or test recoverability. It supports writing web agents for automating repetitive tasks, making it valuable for red teaming scenarios involving web application assessment.

## Features

- Feature 1: Automatic script generation from browser interactions, including GET/POST requests and parameters.
- Feature 2: Cookie dumping for session persistence in tests.
- Feature 3: Integration with FunkLoad's broader suite for load simulation and monitoring.
- Feature 4: Support for HTTPS and basic authentication flows during recording.

## Installation

### Requirements

- Python 2.7 or 3.x (FunkLoad is Python-based).
- Access to pip for installation.

### Install Commands

```bash
# Install via pip (recommended)
pip install funkload

# Verify installation
fl-record --help
```

On Kali Linux or Ubuntu, it may not be in default repositories, so use pip. For development environments, clone from the repository if needed.

## Basic Usage

```bash
fl-record --help
```

This displays available options and usage for recording sessions.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and exit |
| --dump-browser | Dump browser cookies to cookies.txt after recording |
| --dump-referer | Dump referer headers for each request |
| -u USER, --user=USER | Specify username for basic auth |
| -p PASS, --password=PASS | Specify password for basic auth |

## Examples

### Example 1: Basic Usage

```bash
fl-record http://example.com
```

Launches a browser to example.com, records interactions, and generates test_Example.py.

### Example 2: Advanced Usage

```bash
fl-record --dump-browser -u admin -p secret https://secure-site.com/login
```

Records an authenticated session, dumps cookies, and creates a script for replay.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Denial of Service]] Network Denial of Service (when used for load testing to simulate DoS conditions)

### Tactics

- [[Impact]] Impact (via stress testing to assess application resilience)

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of FunkLoad-generated Python scripts (e.g., files named test_*.py with specific imports like from funkload.FunkLoadTestCase).
- Network traffic patterns showing scripted browser-like requests during testing.
- Process monitoring for fl-record or Python processes launching webbrowser module.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/FunkLoad]] (parent framework for running recorded tests)
- [[tools/Selenium]] (alternative for more advanced browser automation)

## References

- Official documentation: https://funkload.nexedi.com/
- GitHub repository: https://github.com/Nexedi/funkload (if available)
- Python Package Index: https://pypi.org/project/FunkLoad/
