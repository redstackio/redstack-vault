---
data: 'rpm -i [input]'
tags:
  - rpm
  - install
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:30.948Z'
id: d994ba7e-9a7d-4aeb-a729-b613174a9e4f
verified: false
validated: true
submitted: true
---
# RPM Install Fuzzed

## Command

```bash
rpm -i [input]
```

## Description

Installs fuzzed RPM to trigger bugs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -i | Install | Yes |
| [input] | Fuzzed RPM | Yes |

## Examples

### Basic Usage

```bash
rpm -i malformed.rpm
```

## Expected Output

Crash (overflow, OOB, null).

## Related

- [[commands/rpm-query-fuzzed]]
