---
url: 'https://www.google.com'
tags:
  - recon
  - dorking
type: tool
platforms:
  - Web
description: Web search engine used for dorking to discover leaked sensitive information.
id: fe4e7560-23c0-4e13-af24-43ef9a1bb1e0
created_at: '2025-12-14T17:33:24.365Z'
updated_at: '2025-12-14T17:33:24.365Z'
verified: false
validated: true
submitted: true
---
# Google Search

**Status**: Unverified

## Overview

Google Search is a powerful tool for reconnaissance in security testing, particularly through advanced operators (dorking) to uncover misconfigurations like indexed sensitive URLs.

## Description

It indexes vast web content, allowing queries to find domain-specific leaks. In offensive ops, it's used for passive recon to identify exposed tokens, configs, or endpoints without direct interaction.

## Features

- Advanced search operators (site:, inurl:, filetype:)
- Real-time indexing of public web pages
- Cache and snippet previews for quick validation

## Installation

### Requirements

- Web browser
- Internet connection

### Install Commands

No installation needed; access via browser.

## Basic Usage

```
[query]
```

### Common Options

| Option | Description |
|--------|-------------|
| site:domain.com | Limit to specific site |
| inurl:keyword | Search URLs containing keyword |

## Examples

### Example 1: Basic Usage

```
site:sorare.com
```

### Example 2: Advanced Usage

```
site:sorare.com inurl:token
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Search logs showing dork-like queries
- Anomalous traffic to search engines from security tools

## Related Procedures


## Related Tools

- [[tools/Web-Browser]]

## References

- Google Advanced Search documentation
