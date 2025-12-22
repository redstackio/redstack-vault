---
url: 'https://guides.rubyonrails.org/rails_console.html'
tags:
  - rails
  - console
  - irb
type: tool
verified: false
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.161Z'
configuration: Development environment
id: 114e5c60-90f1-4b39-a78c-924ecf16e390
validated: true
submitted: true
---
# rails-console

**Status**: Unverified

## Overview

Interactive Ruby console in the context of the Rails application for executing code and testing payloads.

## Description

Provides Rails-loaded IRB for crafting and testing malicious objects like ERB payloads.

## Features

- Feature 1: App context execution
- Feature 2: ActiveSupport access
- Feature 3: Real-time testing

## Installation

### Requirements

- Rails app

### Install Commands

```bash
# Included in Rails
bundle exec rails console
```

## Basic Usage

```bash
rails console --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -e | Environment |
| --sandbox | Sandbox mode |

## Examples

### Example 1: Basic Usage

```bash
bundle exec rails console
```

### Example 2: Advanced Usage

```bash
rails console -e production
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- IRB processes in app dir
- Console logs

## Related Procedures


## Related Tools

- [[tools/rails-cli]]

## References

- Official documentation: https://guides.rubyonrails.org/rails_console.html
