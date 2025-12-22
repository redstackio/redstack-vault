---
url: 'https://guides.rubyonrails.org/command_line.html'
tags:
  - rails
  - cli
type: tool
verified: false
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.168Z'
id: ec6497ac-b805-42cf-ac34-93f8ea0382b7
validated: true
submitted: true
---
# rails-cli

**Status**: Unverified

## Overview

Command-line tool for generating, running, and managing Rails applications, used here for setup and server start.

## Description

Rails CLI handles app creation, route listing, and server execution in offensive security for PoC environments.

## Features

- Feature 1: App generation with `rails new`
- Feature 2: Route inspection with `rails routes`
- Feature 3: Server boot with `rails s`

## Installation

### Requirements

- Ruby installed
- Gem bundler

### Install Commands

```bash
# Rails is a gem, installed via bundler in app
```

## Basic Usage

```bash
rails --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -v, --version | Show version |
| -h, --help | Help message |

## Examples

### Example 1: Basic Usage

```bash
rails new app
```

### Example 2: Advanced Usage

```bash
rails routes
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process: rails process
- Logs: Rails startup logs

## Related Procedures


## Related Tools

- [[tools/bundler]]

## References

- Official documentation: https://guides.rubyonrails.org/command_line.html
