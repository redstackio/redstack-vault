---
id: f6g7h8i9-j0k1-2345-fghi-678901234567
url: 'https://github.com/paper-trail-gem/paper_trail'
tags:
  - versioning
  - deserialization
type: tool
verified: false
platforms:
  - Linux
  - Ruby on Rails
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:29:56.581Z'
validated: true
submitted: true
---
---

# paper_trail

**Status**: Unverified

## Overview

Paper Trail is a Ruby gem for versioning Rails models by storing snapshots of changes in a database table (e.g., user_versions). It is commonly used for audit trails but vulnerable to YAML deserialization attacks in its reify method when handling untrusted data.

## Description

The gem serializes model states as YAML in the object column. The reify method deserializes this YAML to reconstruct objects, allowing gadget chains for code execution if malicious YAML is inserted. This tool is integral to the attack as the target for payload persistence and trigger.

## Features

- Feature 1: Automatic versioning of model changes with whodunit tracking
- Feature 2: Reify method to restore historical states from YAML snapshots
- Feature 3: Integration with ActiveRecord for easy setup in Rails apps

## Installation

### Requirements

- Ruby 2.7+ and Rails 5+
- PostgreSQL or compatible database

### Install Commands

```bash
# Add to Gemfile
gem 'paper_trail'

# Install
bundle install
```

## Basic Usage

```bash
gem 'paper_trail'
rails generate paper_trail:migration
rails db:migrate
```

### Common Options

| Option | Description |
|--------|-------------|
| `--help` | Show gem documentation |
| `-v` | Verbose installation output |

## Examples

### Example 1: Basic Usage

In a Rails model:
```ruby
class User < ApplicationRecord
  has_paper_trail
end
```

### Example 2: Advanced Usage

Trigger reify:
```ruby
version = UserVersion.find_by(email: 'test')
version.reify
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Client Execution]]
- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor database for anomalous INSERTs into *_versions tables
- Log deserialization calls and scan for unsafe YAML gadgets
- Use gem auditing tools like bundler-audit for known vulnerabilities

## Related Procedures


## Related Tools

- [[ActiveRecord]]
- [[Psych YAML Parser]]

## References

- Official documentation: https://github.com/paper-trail-gem/paper_trail
- Related resources: Ruby YAML deserialization exploits

---
