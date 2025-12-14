---
url: 'https://bundler.io/'
tags:
  - dependency-management
type: tool
verified: false
platforms:
  - Linux
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:26:22.309Z'
id: a239696b-d380-44f9-b817-de56ca75b6a8
validated: true
submitted: true
---
# Bundler

**Status**: Unverified

## Overview

Bundler is a dependency management tool for Ruby projects, used to load gems for Rails commands.

## Description

It ensures proper gem versions are used when executing rails runner or server start.

## Features

- Feature 1: Gemfile-based dependency resolution
- Feature 2: bundle exec for isolated execution
- Feature 3: Version locking

## Installation

### Requirements

- Ruby

### Install Commands

```bash
gem install bundler
```

## Basic Usage

```bash
bundle install
```

### Common Options

| Option | Description |
|--------|-------------|
| exec | Run command with bundle |

## Examples

### Example 1: Basic Usage

```bash
bundle exec rails s
```

### Example 2: Advanced Usage

```bash
bundle update
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[PowerShell]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- bundle processes in task manager

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Rails]]

## References

- Official documentation: https://bundler.io/
