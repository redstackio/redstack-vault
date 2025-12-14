---
url: 'https://github.com/geminabox/geminabox'
tags:
  - gem-server
  - proxy
type: tool
verified: false
platforms:
  - Web
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:41.179Z'
id: 6e4d0dbf-ee3c-45eb-b7a6-9a62adafdb0c
validated: true
submitted: true
---
# Geminabox

**Status**: Unverified

## Overview

Geminabox is a Ruby gem server framework used to create a private gem hosting service, modified here to serve malicious responses for the attack.

## Description

It allows uploading and serving gems, but is customized to respond with Marshal payloads on /api/v1/dependencies, simulating a compromised RubyGems.org.

## Features

- Feature 1: Simple gem hosting and proxying
- Feature 2: Rack-compatible for easy deployment
- Feature 3: API endpoints mimicking RubyGems

## Installation

### Requirements

- Ruby and Bundler

### Install Commands

```bash
# Gem install
gem install geminabox
```

## Basic Usage

```bash
rackup
```

### Common Options

| Option | Description |
|--------|-------------|
| RUBYGEMS_PROXY | Enable proxy mode |

## Examples

### Example 1: Basic Usage

```bash
RUBYGEMS_PROXY=true rackup
```

### Example 2: Advanced Usage

Modify config.ru for custom routes.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Compromise Hardware Supply Chain]] Supply Chain Compromise

### Tactics

- [[Privilege Escalation]] Privilege Escalation

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual gem server traffic on non-standard ports
- Modified response payloads in network logs

## Related Procedures

- [[procedures/Set-Up-Malicious-Gem-Server-to-Serve-Deserialization-Payload]]

## Related Tools

- [[tools/Puma]]

## References

- GitHub: https://github.com/geminabox/geminabox
