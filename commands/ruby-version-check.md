---
data: ruby -v
tags:
  - setup
  - version
type: command
output: 'ruby 3.2.2 (2023-03-30 revision e51014f9c0) [arm64-darwin22]'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:43.918Z'
id: f6ceb3b1-826e-4c06-af20-b70386bd8863
verified: false
validated: true
submitted: true
---
# ruby-version-check

## Command

```bash
ruby -v
```

## Description

Displays the installed Ruby interpreter version to verify compatibility before setting up a Rails PoC.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -v | Version flag | Yes |

## Examples

### Basic Usage

```bash
ruby -v
```

### Advanced Usage

N/A

## Expected Output

ruby 3.2.2 (2023-03-30 revision e51014f9c0) [arm64-darwin22]

## Related

- [[commands/rails-new-poc]]
