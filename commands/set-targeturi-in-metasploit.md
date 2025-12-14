---
data: set targeturi /auth/facebook
tags:
  - metasploit
  - target
type: command
output: TARGETURI set to /auth/facebook
executor: msfconsole
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.918Z'
id: bd4c5400-04ed-4539-9156-d920ef3e574a
verified: false
validated: true
submitted: true
---
# set-targeturi-in-metasploit

## Command

```msfconsole
set targeturi /auth/facebook
```

## Description

Sets the vulnerable endpoint URI for sending the malicious request.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| targeturi | Path to the auth endpoint | Yes |

## Examples

### Basic Usage

```msfconsole
set targeturi /auth/facebook
```

## Expected Output

TARGETURI set to /auth/facebook.

## Related

- [[Related Procedure: Configure-and-Execute-Rails-Deserialization-Exploit]]
