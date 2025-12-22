---
id: f6cfa7aa-885a-4df2-a35e-901da826ea1e
type: command
executor: bash
data: './prowler -E check42,check43'
output: null
created_at: '2023-04-06T03:56:08.938362+00:00'
updated_at: '2023-04-10T20:20:58.747935+00:00'
platforms:
  - Linux
tags:
  - prowler
  - audit
verified: true
validated: true
---

# Run Prowler Exclude Checks

## Command

```bash
./prowler -E check42,check43
```

## Description

Runs Prowler audit excluding specified checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -E check42,check43 | Checks to exclude | Yes |

## Examples

### Basic Usage

```bash
./prowler -E check42,check43
```

## Expected Output

[PASS] check1 | [FAIL] check2
...
