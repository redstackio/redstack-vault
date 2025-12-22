---
data: set railsversion 4
tags:
  - metasploit
  - config
type: command
output: RailsVersion set to 4
executor: msfconsole
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.938Z'
id: 70218f88-8846-4fc2-ba77-c2c37157601b
verified: false
validated: true
submitted: true
---
# set-railsversion-in-metasploit

## Command

```msfconsole
set railsversion 4
```

## Description

Specifies the Rails version for compatibility in the deserialization payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| railsversion | Version number (e.g., 4) | Yes |

## Examples

### Basic Usage

```msfconsole
set railsversion 4
```

## Expected Output

RailsVersion set to 4.

## Related

- [[Related Procedure: Configure-and-Execute-Rails-Deserialization-Exploit]]
