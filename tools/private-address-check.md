---
id: tool-uuid-2
url: 'https://github.com/jtdowney/private_address_check'
tags:
  - ruby
  - ssrf-protection
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.117Z'
validated: true
submitted: true
---
# private-address-check

**Status**: Unverified

## Overview

private_address_check is a Ruby gem designed to prevent SSRF attacks by checking if resolved IP addresses from hostnames are private or internal, but it's vulnerable due to reliance on buggy Resolv.getaddresses.

## Description

The gem resolves user-supplied URLs via DNS and validates IPs against private ranges (e.g., 127.0.0.0/8). In security testing, it's analyzed for weaknesses like empty resolution bypasses. Alternatives include custom Socket-based checks.

## Features

- Feature 1: Hostname resolution and private IP detection
- Feature 2: Blacklist-based filtering for SSRF mitigation
- Feature 3: Integration with Rails/Ruby apps for URL validation

## Installation

### Requirements

- Ruby 2.0+
- Bundler for gem management

### Install Commands

```bash
# Add to Gemfile: gem 'private_address_check'
# Then bundle install
bundle install
# Or direct: gem install private_address_check
```

## Basic Usage

```ruby
gem 'private_address_check'
require 'private_address_check'
PrivateAddressCheck.valid?('127.0.0.1')  # false for private
```

### Common Options

| Option | Description |
|--------|-------------|
| valid?(ip) | Checks if IP is non-private
| getaddresses(host) | Resolves and filters (internal method)

## Examples

### Example 1: Basic Usage

```ruby
require 'private_address_check'
PrivateAddressCheck.valid?('8.8.8.8')  # true (public)
```

### Example 2: Advanced Usage

```ruby
# In app: if PrivateAddressCheck.valid?(url_host), allow request
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Gem dependency scans in Ruby apps
- Logs of resolution failures or bypass attempts

## Related Procedures


## Related Tools

- [[tools/irb]]

## References

- GitHub repo: https://github.com/jtdowney/private_address_check
