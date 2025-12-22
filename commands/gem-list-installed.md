---
type: command
executor: bash
data: gem list
output: null
platforms:
  - Linux
  - macOS
tags:
  - package-management
  - ruby
verified: true
validated: true
---

# gem-list-installed

## Command

```bash
gem list
```

## Description

Lists all installed Ruby gems and their versions. Useful for verifying if a malicious package was installed during dependency confusion testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --local | List only locally installed gems (default) | No |
| $_PATTERN | Filter by pattern (e.g., internal*) | No |

## Examples

### Basic Usage

```bash
gem list
```

### Filtered List

```bash
gem list internal*
```

## Expected Output

*** LOCAL GEMS ***

internal-auth-lib (1.2.4)

## Related

- [[commands/gem-install-gem]]
