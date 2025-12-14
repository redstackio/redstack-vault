---
id: tool-uuid-3
url: 'https://puma.io/'
tags:
  - server
  - web
type: tool
verified: false
platforms:
  - Ruby on Rails
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:36.472Z'
validated: true
submitted: true
---
# Puma

**Status**: Unverified

## Overview

Ruby web server that handles requests in Rails apps, crashing due to stack overflow from the recursive response in this vulnerability.

## Description

Puma processes the mutated Rack response, leading to SystemStackError in critical regions when handling Sendfile.

## Features

- Feature 1: Multi-threaded request handling
- Feature 2: Production-ready clustering
- Feature 3: Integration with Rack middleware

## Installation

### Requirements

- Ruby

### Install Commands

```bash
# Via Bundler in Gemfile
gem 'puma'
bundle install
```

## Basic Usage

```bash
puma --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -p | Port |
| -t | Threads |
| -C | Config file |

## Examples

### Example 1: Basic Usage

```bash
puma
```

### Example 2: Advanced Usage

```bash
puma -p 3000 -t 2
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Endpoint Denial of Service]]

### Tactics

- [[Impact]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process: puma executable
- Logs: Stack overflow errors

## Related Procedures


## Related Tools

- [[tools/rails]]

## References

- Official documentation: https://puma.io/docs/
