---
data: set uripath /
tags:
  - metasploit
  - config
type: command
output: URI path set
executor: msfconsole
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:37.150Z'
id: 972f90f9-8fa1-4ff7-afb9-169e7258aecb
verified: false
validated: true
submitted: true
---
# msf-set-uripath-root

## Command

```msf
set uripath /
```

## Description

Sets the URI path for the Metasploit exploit server to root (/), hosting the malicious page there.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| uripath | / for root path | Yes |

## Examples

### Basic Usage

```msf
set uripath /
```

## Expected Output

'URIPATH => /'.

## Related

- [[commands/msf-set-payload-5]]
- [[procedures/Set-Up-Metasploit-Exploit-Server-for-Browser-RCE]]
