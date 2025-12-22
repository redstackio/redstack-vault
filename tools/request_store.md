---
id: tool-uuid-5
url: 'https://github.com/steveklabnik/request_store'
tags:
  - storage
  - middleware
type: tool
verified: false
platforms:
  - Ruby on Rails
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:36.452Z'
validated: true
submitted: true
---
# request_store

**Status**: Unverified

## Overview

Gem for storing per-request data in Rails, which mutates the response body, contributing to recursive object creation in the vulnerability.

## Description

RequestStore accesses and modifies request-scoped data, inadvertently mutating the FAILSAFE_RESPONSE when exceptions occur.

## Features

- Feature 1: Thread-local storage
- Feature 2: Rails middleware integration
- Feature 3: Data persistence across middleware

## Installation

### Requirements

- Rails

### Install Commands

```bash
# In Gemfile
gem 'request_store'
bundle install
```

## Basic Usage

```ruby
RequestStore.store[:key] = value
```

### Common Options

| Option | Description |
|--------|-------------|
| store | Access storage |
| middleware | Enable in stack |

## Examples

### Example 1: Basic Usage

```ruby
RequestStore[:user] = current_user
```

### Example 2: Advanced Usage

```ruby
use RequestStore::Middleware
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Impact]]

## Detection

Indicators and methods for detecting this tool's usage:

- Gem in dependencies
- Storage access in code

## Related Procedures


## Related Tools

- [[tools/lograge]]

## References

- GitHub: https://github.com/steveklabnik/request_store
