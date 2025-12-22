---
id: 30678ec0-afd7-42b9-8373-7735e4eeef40
name: CrackMapExec-Retrieve-Password-Policy
type: command
executor: bash
data: crackmapexec $_TARGET_IP -u $_USERNAME -p $_PASSWORD --pass-pol
output: null
created_at: '2023-01-11T20:38:26.005237+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - Enumeration
verified: true
validated: true
---

# CrackMapExec-Retrieve-Password-Policy

## Command

```bash
crackmapexec $_TARGET_IP -u $_USERNAME -p $_USERNAME --pass-pol
```

## Description

This command uses CrackMapExec to query a Windows domain controller for password policy details over SMB, including lockout thresholds and complexity rules. It helps plan brute-force or spraying attacks by revealing policy constraints.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address of the target domain controller | Yes |
| $_USERNAME | Username for authentication (can be empty for null session) | No |
| $_PASSWORD | Password for authentication (can be empty) | No |
| --pass-pol | Flag to retrieve password policy information | Yes |

## Examples

### Basic Usage

```bash
crackmapexec 192.168.1.10 -u '' -p '' --pass-pol
```

### With Credentials

```bash
crackmapexec 192.168.1.10 -u guest -p guest --pass-pol
```

## Expected Output

Password Policy for DC01:
Lockout Threshold: 5
Lockout Duration: 15
Password History: 24
Minimum Password Length: 8
Complexity Requirements: Enabled

## Related

- [[procedures/Domain-Password-Spraying-with-Known-Usernames]]
- [[tools/CrackMapExec]]
