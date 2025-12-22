---
id: new-uuid-2
name: curl-download-linpeas-script
type: command
executor: bash
data: >-
  curl
  "https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh"
  -o linpeas.sh
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - download
  - enumeration
verified: true
validated: true
---

# curl-download-linpeas-script

## Command

```bash
curl "https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh" -o linpeas.sh
```

## Description

Alternative download method for LinPEAS using curl, useful if wget is unavailable.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -o linpeas.sh | Output file name | Yes |
| URL | GitHub release URL | Built-in |

## Examples

### Basic Usage

```bash
curl "https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh" -o linpeas.sh
```

## Expected Output

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 1234k  100 1234k    0     0  2468k      0 --:--:-- --:--:-- --:--:-- 2468k

## Related

- [[procedures/Linux-Privilege-Escalation-Enumeration]]
- [[tools/linPEAS]]
