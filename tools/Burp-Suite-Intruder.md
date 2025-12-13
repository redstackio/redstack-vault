---
url: 'https://portswigger.net/burp'
tags:
  - web-testing
  - exploit-automation
type: tool
platforms:
  - Windows
  - Linux
  - macOS
description: Burp Suite component for automating customized attacks on web applications.
id: 4a230334-3c9c-4589-b613-20b34453797c
created_at: '2025-12-13T09:01:17.699Z'
updated_at: '2025-12-13T09:01:17.699Z'
verified: false
validated: true
submitted: true
---
# Burp Suite Intruder

**Status**: Unverified

## Overview

Burp Suite Intruder is a powerful tool for performing automated, customized attacks on web applications, ideal for testing vulnerabilities like HTTP Request Smuggling by sending varied payloads and analyzing responses.

## Description

It allows configuration of attack payloads, positions for fuzzing, and automation of request sending, making it essential for offensive security tasks involving web exploits.

## Features

- Payload configuration: Support for lists, brute force, and custom generators
- Attack types: Sniper, Battering Ram, Pitchfork, Cluster Bomb
- Response analysis: Grep matching and extraction

## Installation

### Requirements

- Java Runtime Environment
- Burp Suite Professional license

### Install Commands

```bash
# Download from official site and run JAR file
java -jar burpsuite_pro.jar
```

## Basic Usage

```bash
tools/burp-intruder --help  # Not command-line, use GUI
```

### Common Options

| Option | Description |
|--------|-------------|
| Attack Type | Defines payload application |
| Payloads | Sets values to insert |

## Examples

### Example 1: Basic Usage

Configure request in GUI and start attack.

### Example 2: Advanced Usage

Set positions for Host header and run with chunked payloads.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]
- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual request patterns in web logs
- Burp-specific User-Agent strings

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Burp-Collaborator]]

## References

- https://portswigger.net/burp/documentation/intruder
