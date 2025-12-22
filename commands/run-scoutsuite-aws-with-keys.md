---
id: a45e667e-6fa9-493f-97fd-18b000644a7e
type: command
executor: bash
data: >-
  python scout.py aws --access-keys --access-key-id $_ACCESS_KEY_ID
  --secret-access-key $_SECRET_ACCESS_KEY --session-token $_SESSION_TOKEN
output: null
created_at: '2023-04-06T03:56:08.938855+00:00'
updated_at: '2023-04-10T20:20:58.747935+00:00'
platforms:
  - Linux
tags:
  - aws
  - scoutsuite
verified: true
validated: true
---

# Run ScoutSuite AWS with Keys

## Command

```bash
python scout.py aws --access-keys --access-key-id $_ACCESS_KEY_ID --secret-access-key $_SECRET_ACCESS_KEY --session-token $_SESSION_TOKEN
```

## Description

Runs ScoutSuite audit on AWS using explicit credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --access-keys | Use keys auth | Yes |
| --access-key-id | Access key | Yes |
| --secret-access-key | Secret key | Yes |
| --session-token | Optional token | No |

## Examples

### Basic Usage

```bash
python scout.py aws --access-keys --access-key-id AKIA... --secret-access-key wJalr...
```

## Expected Output

Auditing AWS... Report generated in scoutsuite_report/
