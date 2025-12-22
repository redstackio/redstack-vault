---
url: 'https://pastebin.com/BEy5iDLA'
tags:
  - automation
  - exploit
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:19.922Z'
id: d76d7b67-6d6a-4c99-a9a3-b4415d8b469f
validated: true
submitted: true
---
# autoxploiter

**Status**: Unverified

## Overview

autoxploiter is a custom automated script for exploiting the Articulate WordPress plugin vulnerability, handling ZIP creation, upload, and initial RCE commands.

## Description

Hosted on Pastebin, this script streamlines the multi-step process into a one-liner or configurable tool, useful for rapid testing in pentests.

## Features

- Feature 1: Automated ZIP payload generation with webshell
- Feature 2: Curl-based upload to endpoint
- Feature 3: Post-upload verification and command execution

## Installation

### Requirements

- curl and zip utilities
- Bash environment

### Install Commands

```bash
# Download from Pastebin
curl https://pastebin.com/raw/BEy5iDLA -o autoxploiter.sh
chmod +x autoxploiter.sh
```

## Basic Usage

```bash
autoxploiter.sh -t http://target.com
```

### Common Options

| Option | Description |
|--------|-------------|
| `-t` | Target URL |
| `-c` | Custom command for RCE |
| `-h` | Help |

## Examples

### Example 1: Basic Usage

```bash
autoxploiter.sh -t http://example.com
```

### Example 2: Advanced Usage

```bash
autoxploiter.sh -t http://target.com -c "id"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote File Copy]]
- [[Unix Shell]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Script downloads from Pastebin
- Sudden ZIP uploads followed by RCE attempts
- Log patterns matching script behavior

## Related Procedures


## Related Tools

- [[Related Tool: Metasploit]]
- [[Related Tool: curl]]

## References

- Script source: https://pastebin.com/BEy5iDLA
- Related resources: Custom exploit repos
