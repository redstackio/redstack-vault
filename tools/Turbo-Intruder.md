---
url: ''
tags:
  - http
  - exploitation
  - burp-extension
type: tool
platforms:
  - Web
description: >-
  Burp Suite extension for sending large numbers of HTTP requests and analyzing
  results, used here for HTTP desync attacks.
id: 4e8d813f-6cd0-4613-a28f-df77dc095db3
created_at: '2025-12-13T09:01:22.442Z'
updated_at: '2025-12-13T09:01:22.442Z'
verified: false
validated: true
submitted: true
---
# Turbo Intruder

**Status**: Unverified

## Overview

Turbo Intruder is a Burp Suite extension designed for high-performance HTTP request sending and response analysis, particularly useful for exploits like HTTP Request Smuggling.

## Description

It allows scripting of complex request sequences, concurrent connections, and custom handling, making it ideal for desync exploits without reliably poisoning innocent users.

## Features

- Feature 1: Concurrent request handling
- Feature 2: Custom Python scripting
- Feature 3: Integration with Burp Suite

## Installation

### Requirements

- Burp Suite Professional
- Java Runtime

### Install Commands

```bash
# Install via Burp Extensions tab
```

## Basic Usage

```python
turbo-intruder --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `concurrentConnections` | Set number of connections |
| `engine` | Set engine type (e.g., THREADED) |

## Examples

### Example 1: Basic Usage

Load script in Turbo Intruder UI.

### Example 2: Advanced Usage

Configure with concurrentConnections=5 and Engine.THREADED.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Adversary-in-the-Middle]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual burst of HTTP requests
- Detection method 2: Anomalous chunked encoding in logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Burp-Suite]]

## References

- Official Burp Suite documentation
