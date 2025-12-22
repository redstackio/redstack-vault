---
url: null
tags:
  - testing
  - ruby
type: tool
platforms:
  - Web
description: Ruby gem for verifying JSON structures in automated tests
id: 06bcf22a-1cb9-4f23-a6f5-5eef09f23912
created_at: '2025-12-11T06:10:28.417Z'
updated_at: '2025-12-11T06:10:28.417Z'
verified: false
validated: true
submitted: true
---
# approvals-gem

**Status**: Unverified

## Overview

The approvals gem is a Ruby tool used for approval testing, particularly for verifying and normalizing JSON structures in automated tests to ensure consistency.

## Description

This gem facilitates testing by comparing expected and actual outputs, normalizing them for differences like ordering. It's used in Rails environments to check API responses but may overlook issues like duplicate keys in JSON due to parsing behavior.

## Features

- Feature 1: JSON normalization for tests
- Feature 2: Approval-based verification
- Feature 3: Integration with Ruby testing frameworks

## Installation

### Requirements

- Ruby installed
- Gem bundler

### Install Commands

```bash
gem install approvals
```

## Basic Usage

```bash
# In Ruby test file
verify(format: :json) { subject.body }
```

### Common Options

| Option | Description |
|--------|-------------|
| `format: :json` | Specify JSON format |

## Examples

### Example 1: Basic Usage

```ruby
verify(format: :json) { subject.body }
```

### Example 2: Advanced Usage

```ruby
verify(format: :json, scrubber: custom_scrubber) { subject.body }
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Data from Information Repositories]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor Ruby gem installations in development environments
- Detection method 2: Check test logs for approvals usage

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[rspec]]
- [[minitest]]

## References

- Official gem documentation
- Ruby testing resources
