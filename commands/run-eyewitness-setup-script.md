---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
name: run-eyewitness-setup-script
type: command
executor: bash
data: ./setup/setup.sh
output: null
created_at: '2023-04-06T03:56:25Z'
updated_at: '2023-04-10T20:25:35Z'
platforms:
  - Linux
  - macOS
tags:
  - setup
  - dependencies
verified: true
validated: true
---

# run-eyewitness-setup-script

## Command

```bash
./setup/setup.sh
```

## Description

Runs the EyeWitness setup script to install dependencies like Python packages and browser drivers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | No parameters; run from EyeWitness directory | No |

## Examples

### Basic Usage

```bash
cd EyeWitness && ./setup/setup.sh
```

## Expected Output

Installing dependencies...
Requirement already satisfied: requests in /usr/lib/python3/dist-packages
Collecting PyVirtualDisplay
Successfully installed PyVirtualDisplay-1.3.4
Setup complete.

## Related

- [[procedures/Subdomain-Enumeration-with-Knockpy-and-EyeWitness]]
