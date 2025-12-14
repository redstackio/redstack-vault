---
id: tool-uuid-4
url: 'https://github.com/roidrage/lograge'
tags:
  - logging
  - middleware
type: tool
verified: false
platforms:
  - Ruby on Rails
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:36.457Z'
validated: true
submitted: true
---
# lograge

**Status**: Unverified

## Overview

Gem for customizing Rails logging, which in this case contributes to the vulnerability by not wrapping responses in Rack::BodyProxy, allowing direct mutation.

## Description

Lograge alters log formatting but bypasses proxy wrapping, enabling middleware to mutate the shared FAILSAFE_RESPONSE constant.

## Features

- Feature 1: Structured JSON logging
- Feature 2: Custom logger integration
- Feature 3: Performance optimization

## Installation

### Requirements

- Rails app

### Install Commands

```bash
# In Gemfile
gem 'lograge'
bundle install
```

## Basic Usage

```ruby
# In application.rb
config.lograge.enabled = true
```

### Common Options

| Option | Description |
|--------|-------------|
| enabled | Toggle lograge |
| formatter | Set log format |

## Examples

### Example 1: Basic Usage

```ruby
config.lograge.enabled = true
```

### Example 2: Advanced Usage

```ruby
config.lograge.formatter = Lograge::Formatters::Json.new
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Impact]]

## Detection

Indicators and methods for detecting this tool's usage:

- Gem presence in Gemfile.lock
- Log format changes

## Related Procedures


## Related Tools

- [[tools/rails]]

## References

- GitHub: https://github.com/roidrage/lograge
