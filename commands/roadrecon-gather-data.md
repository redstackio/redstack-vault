---
id: 55f83d6d-f230-469e-b1b2-696066362468
type: command
executor: bash
data: roadrecon gather
output: null
created_at: '2023-04-06T03:56:14.584802+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - gather
  - azure
verified: true
validated: true
---

# roadrecon-gather-data

## Command

```bash
roadrecon gather
```

## Description

Gathers AAD data into local database after authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -d, $_DATABASE | Database file | No |
| -f, $_TOKENFILE | Token file path | No |
| --mfa | Enable MFA handling | No |

## Examples

### Basic Usage

```bash
roadrecon gather
```

## Expected Output

Data collected; progress logs to console.

## Related

- [[procedures/Azure-Reconnaissance]]
- [[tools/ROADRecon]]
