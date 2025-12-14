---
url: 'https://github.com/paper-trail-gem/paper_trail'
tags:
  - ruby
  - rails
  - versioning
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:25.909Z'
id: c6911aa1-c9e0-4493-85de-772063fe6d28
validated: true
submitted: true
---
# paper_trail

**Status**: Unverified

## Overview

Paper Trail is a Ruby gem for versioning changes to Rails model records, storing snapshots in an audit table like user_versions. In this context, it's a vulnerable component where the reify method deserializes YAML from the object attribute, enabling RCE if untrusted data is persisted.

## Description

Paper Trail tracks create/update/destroy events by serializing model state to YAML in a versions table. The reify method reconstructs objects from these snapshots via YAML.load, which is unsafe for attacker-controlled input. Commonly used in Rails apps for audit trails; vulnerable versions allow deserialization gadgets leading to code execution.

## Features

- Feature 1: Automatic versioning of model changes
- Feature 2: YAML serialization of object state
- Feature 3: Reify method for snapshot reconstruction

## Installation

### Requirements

- Ruby 2.0+
- Rails 4.0+
- PostgreSQL or compatible DB

### Install Commands

```bash
gem install paper_trail
```

Add to Gemfile: gem 'paper_trail'

## Basic Usage

```ruby
class User < ActiveRecord::Base
  has_paper_trail
end
```

### Common Options

| Option | Description |
|--------|-------------|
| `-v, --version` | Show version |
| `--help` | Show help |

## Examples

### Example 1: Basic Usage

```ruby
user = User.create(name: 'Test')
version = user.versions.last
reconstructed = version.reify  # Vulnerable if YAML tainted
```

### Example 2: Advanced Usage

Configure safe YAML: PaperTrail.config.serializer = YAML
But default is unsafe.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for YAML deserialization errors in logs
- Scan for paper_trail versions < 12.0 without safe YAML
- Alert on anomalous reify calls with user-supplied data

## Related Procedures


## Related Tools

- [[ActiveRecord]]
- [[YAML Ruby]]

## References

- Official documentation: https://github.com/paper-trail-gem/paper_trail
- Related resources: Ruby YAML deserialization advisories
