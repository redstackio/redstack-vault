---
id: tool-002
url: 'https://rubygems.org/'
tags:
  - package-manager
  - ruby
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:23:36.625Z'
validated: true
submitted: true
---
# gem

**Status**: Unverified

## Overview

Gem is Ruby's package manager, used to install libraries like nokogiri for exploit scripts in security operations.

## Description

It fetches and installs Ruby gems, enabling dependencies for tools like Drupalgeddon2. Common in pentesting for Ruby-based exploits.

## Features

- Feature 1: Install from remote repositories
- Feature 2: Dependency resolution
- Feature 3: Version management

## Installation

### Requirements

- Ruby installed

### Install Commands

```bash
# Included with Ruby
```

## Basic Usage

```bash
gem --help
```

### Common Options

| Option | Description |
|--------|-------------|
| install | Install a gem |
| list | List installed gems |

## Examples

### Example 1: Basic Usage

```bash
gem install nokogiri
```

### Example 2: Advanced Usage

```bash
gem install nokogiri --no-ri --no-rdoc
```

## MITRE ATT&CK Mapping

### Techniques

- [[Video Capture]]

### Tactics

- [[Execution]]

## Detection

- Monitor gem install traffic to rubygems.org

## Related Procedures

- [[procedures/Download-and-Setup-Drupalgeddon2-Exploit]]

## Related Tools

- [[Related Tool: pip]]

## References

- https://guides.rubygems.org/
