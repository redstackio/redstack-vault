---
url: null
tags:
  - exfiltration
  - oob
type: tool
platforms:
  - Linux
  - macOS
  - Windows
description: Tool for generating unique URLs to detect out-of-band interactions.
id: bf6fae01-5fa7-4b2d-b468-e3301d42674d
created_at: '2025-12-11T06:10:33.287Z'
updated_at: '2025-12-11T06:10:33.287Z'
verified: false
validated: true
submitted: true
---
# Burp Collaborator Client

**Status**: Unverified

## Overview

Burp Collaborator Client generates unique URLs to receive and log interactions, such as leaked data from exploits like redirects.

## Description

Integrated with Burp Suite, it polls for DNS/HTTP interactions, capturing details like cookies from victim redirects.

## Features

- Feature 1: Unique domain generation.
- Feature 2: Interaction logging.
- Feature 3: Polling for real-time data.

## Installation

### Requirements

- Burp Suite installed

### Install Commands

```bash
# Included in Burp Suite
```

## Basic Usage

Launch within Burp Suite and generate a Collaborator payload.

### Common Options

| Option | Description |
|--------|-------------|
| Poll | Check for interactions |

## Examples

### Example 1: Basic Usage

Generate URL and poll.

### Example 2: Advanced Usage

Use in payloads for OOB exfiltration.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Steal Web Session Cookie]]

### Tactics

- [[Credential Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Outbound requests to collaborator domains.
- Detection method 2: DNS queries to unique subdomains.

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

- Burp documentation
