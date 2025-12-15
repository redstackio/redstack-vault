---
data: set target 0
tags:
  - metasploit
  - config
type: command
output: Target set
executor: msfconsole
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:37.168Z'
id: 2104f8ee-5836-45b4-b5ab-d487fa602bbb
verified: false
validated: true
submitted: true
---
# msf-set-target-0

## Command

```msf
set target 0
```

## Description

Sets the target index in Metasploit to 0 (default, e.g., Linux x86_64 for Kibana container).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| target | 0 for automatic/generic | Yes |

## Examples

### Basic Usage

```msf
set target 0
```

## Expected Output

'Target => 0' confirmation.

## Related

- [[commands/msf-use-chrome-exploit]]
- [[procedures/Set-Up-Metasploit-Exploit-Server-for-Browser-RCE]]
