---
data: bundle init
tags:
  - setup
type: command
output: 'Creates Gemfile with default content including source ''https://rubygems.org'''
executor: bash
platforms:
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:41.203Z'
id: fc9037a9-8fba-41f1-8c1b-829516839d53
verified: false
validated: true
submitted: true
---
# bundle-init

## Command

```bash
bundle init
```

## Description

Initializes a new Bundler project by creating a Gemfile in the current directory.

## Parameters

None.

## Examples

### Basic Usage

```bash
bundle init
```

## Expected Output

Gemfile created with default source.

## Related

- [[commands/bundle-install-exploit]]
- [[procedures/Trigger-RCE-by-Configuring-Bundler-to-Use-Malicious-Source]]
