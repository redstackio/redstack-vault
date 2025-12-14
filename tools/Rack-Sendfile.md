---
id: tool-uuid-6
url: 'https://github.com/rack/rack/blob/master/lib/rack/sendfile.rb'
tags:
  - middleware
  - rack
type: tool
verified: false
platforms:
  - Ruby on Rails
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:36.446Z'
validated: true
submitted: true
---
# Rack::Sendfile

**Status**: Unverified

## Overview

Rack middleware for efficient file sending, which triggers SystemStackError when processing the mutated recursive response body.

## Description

In the exploit, the recursive proxy causes infinite recursion in Sendfile's each method, leading to stack overflow.

## Features

- Feature 1: OS-level file sending (sendfile syscall)
- Feature 2: Fallback to body streaming
- Feature 3: Integration with Rack env

## Installation

### Requirements

- Rack (part of Rails)

### Install Commands

```bash
# Bundled with Rack
gem 'rack'
```

## Basic Usage

```ruby
use Rack::Sendfile
```

### Common Options

| Option | Description |
|--------|-------------|
| root | Set sendfile root |
| fallback | Disable if unsupported |

## Examples

### Example 1: Basic Usage

```ruby
use Rack::Sendfile
```

### Example 2: Advanced Usage

```ruby
use Rack::Sendfile, root: '/path'
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Endpoint Denial of Service]]

### Tactics

- [[Impact]]

## Detection

Indicators and methods for detecting this tool's usage:

- Middleware in stack trace
- Sendfile errors in logs

## Related Procedures


## Related Tools

- [[tools/Puma]]

## References

- GitHub: https://github.com/rack/rack/blob/master/lib/rack/sendfile.rb
