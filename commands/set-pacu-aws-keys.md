---
id: 81eabab5-f7fb-4124-80ad-da9e5d76360e
type: command
executor: bash
data: set_keys
output: null
created_at: '2023-04-06T03:56:08.937266+00:00'
updated_at: '2023-04-10T20:20:58.747935+00:00'
platforms:
  - Linux
tags:
  - aws
  - credentials
verified: true
validated: true
---

# Set Pacu AWS Keys

## Command

```bash
set_keys
```

## Description

Sets AWS access keys within the Pacu session (use swap_keys to switch).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Prompts for keys | No |

## Examples

### Basic Usage

```bash
set_keys
```

## Expected Output

Enter AWS Access Key ID: AKIA...
Keys set successfully.
