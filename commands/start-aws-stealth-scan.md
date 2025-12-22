---
id: 3bff4d53-5cbf-41b0-be24-e740a55760d6
type: command
executor: powershell
data: Start-AWStealth
output: null
created_at: '2023-04-06T03:56:08.936720+00:00'
updated_at: '2023-04-10T20:20:58.747935+00:00'
platforms:
  - Windows
tags:
  - aws
  - scan
verified: true
validated: true
---

# Start AWS Stealth Scan

## Command

```powershell
Start-AWStealth
```

## Description

Initiates a stealthy scan of AWS permissions to identify privileged entities without triggering alerts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Uses configured AWS credentials | No |

## Examples

### Basic Usage

```powershell
Start-AWStealth
```

## Expected Output

Scanning AWS... Completed stealth scan.
