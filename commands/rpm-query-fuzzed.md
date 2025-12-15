---
data: 'rpm -qi -p -- [input]'
tags:
  - rpm
  - query
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:30.941Z'
id: 4923c44d-f209-438e-90bd-2d9c7ce8196d
verified: false
validated: true
submitted: true
---
# RPM Query Fuzzed

## Command

```bash
rpm -qi -p -- [input]
```

## Description

Queries fuzzed RPM info.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -qi | Info | Yes |
| -p | Package file | Yes |
| -- [input] | Fuzzed RPM | Yes |

## Examples

### Basic Usage

```bash
rpm -qi -p -- malformed.rpm
```

## Expected Output

OOB read crash.

## Related

- [[commands/rpm-install-fuzzed]]
