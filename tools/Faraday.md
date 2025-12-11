---
url: ''
tags:
  - http
  - ruby
type: tool
platforms:
  - Linux
description: HTTP client library used in exploit scripts for API interactions.
id: fa6a88fa-d13a-490f-9f42-918b352703de
created_at: '2025-12-11T03:47:39.715Z'
updated_at: '2025-12-11T03:47:39.715Z'
verified: false
validated: true
submitted: true
---
# Faraday

**Status**: Unverified

## Overview

Faraday is a flexible HTTP client library for Ruby, used in scripts to interact with APIs like GitLab's package upload endpoint.

## Description

It supports multiple adapters and is used here for sending malicious packages in exploit scripts.

## Features

- Modular HTTP requests
- Support for middleware
- Connection pooling

## Installation

### Requirements

- Ruby

### Install Commands

```bash
gem install faraday
```

## Basic Usage

```ruby
require 'faraday'
conn = Faraday.new(url: 'https://example.com')
```

### Common Options

| Option | Description |
|--------|-------------|
| `-v` | Verbose (CLI if applicable) |

## Examples

### Example 1: Basic Usage

```ruby
response = conn.get('/')
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor API traffic for anomalous requests

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- #rubyzip

## References

- https://github.com/lostisland/faraday
