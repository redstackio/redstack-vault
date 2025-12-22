---
type: code
language: powershell
verified: true
platforms:
  - Windows
tags:
  - enumeration
  - services
validated: true
---

# enumerate-running-services-multiple-methods

## Code

```powershell
net start
wmic service list brief
tasklist /SVC
```

## Description

Multi-method enumeration of running services using net, WMIC, and tasklist to map services to processes, revealing potential T1035 Service Execution opportunities through weak configurations.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| N/A | Built-in commands only | N/A |

## Usage

Execute sequentially in cmd/PowerShell; redirect to file for parsing. Identify services with unquoted paths or modifiable binaries for privilege escalation.

## Detection

- Command line auditing (Event ID 4688) for net start, wmic, tasklist executions.
- Service-related events (Event ID 7036 for service control).

## Related

- [[procedures/windows-processes-and-tasks-enumeration-for-privilege-escalation]]
