---
type: command
executor: powershell
data: >-
  winrm identify -r:http://$_TARGET_IP:5985/wsman -auth:basic -u:$_USERNAME
  -p:$_PASSWORD -encoding:utf-8
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - winrm
  - test
verified: true
validated: true
---

# winrm-identify-basic

## Command

```powershell
winrm identify -r:http://$_TARGET_IP:5985/wsman -auth:basic -u:$_USERNAME -p:$_PASSWORD -encoding:utf-8
```

## Description

Tests WinRM connectivity and authentication to a remote host, returning service identification info.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -r:http://$_TARGET_IP:5985/wsman | Remote endpoint URL | Yes |
| -auth:basic | Use Basic authentication | Yes |
| -u:$_USERNAME | Username | Yes |
| -p:$_PASSWORD | Password | Yes |
| -encoding:utf-8 | Character encoding | No |

## Examples

### Basic Usage

```powershell
winrm identify -r:http://192.168.1.100:5985/wsman -auth:basic -u:admin -p:Pass123 -encoding:utf-8
```

## Expected Output

ProtocolVersion = http://schemas.dmtf.org/wbem/wsman/1/wsman.xsd
ProductVendor = Microsoft Corporation
ProductVersion = OS: 10.0.19041 SP: 0.0 Stack: 3.0

## Related

- [[procedures/windows-remoting-via-winrm]]
- [[commands/enter-pssession-basic-auth]]
