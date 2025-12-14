---
url: 'https://bundler.io/'
tags:
  - dependency
  - gem
  - manager
type: tool
verified: false
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:43.888Z'
id: 8305fb80-867a-4f9e-8391-7d6e552c4036
validated: true
submitted: true
---
# bundle

**Status**: Unverified

## Overview

Bundler is a gem dependency manager for Ruby projects, used to install Rails dependencies and execute commands securely in the PoC environment.

## Description

It resolves and installs gems from Gemfile, preventing version conflicts. In security contexts, it's used to set up vulnerable app dependencies for exploitation demos.

## Features

- Feature 1: Lockfile for reproducible environments
- Feature 2: Exec for safe command running
- Feature 3: Group-based dependency management

## Installation

### Requirements

- RubyGems

### Install Commands

```bash
gem install bundler
```

## Basic Usage

```bash
bundle --help
bundle install
```

### Common Options

| Option | Description |
|--------|-------------|
| exec | Run command in bundle context |
| install | Install gems |

## Examples

### Example 1: Basic Usage

```bash
bundle install
```

### Example 2: Advanced Usage

```bash
bundle exec rails s
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Gemfile and Gemfile.lock files
- bundle process execution

## Related Procedures


## Related Tools

- [[tools/rails]]
- [[tools/ruby]]

## References

- Official documentation: https://bundler.io/guides/index.html
