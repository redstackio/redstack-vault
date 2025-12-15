---
data: 'curl -s http://target-ip/phppgadmin/ | grep -i "phpPgAdmin"'
tags:
  - web-probing
  - information-disclosure
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
id: 267015ba-8555-4a61-9edc-480d1548a9a3
created_at: '2025-12-14T17:24:55.749Z'
updated_at: '2025-12-14T17:24:55.749Z'
verified: false
validated: true
submitted: true
---
# curl-access-phppgadmin

## Command

```bash
curl -s http://target-ip/phppgadmin/ | grep -i "phpPgAdmin"
```

## Description

This command uses curl to silently fetch the PHPpgAdmin interface page and grep for identifiers, confirming exposure without access controls. Use it during reconnaissance to detect vulnerable database management tools.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode, suppresses progress meter | Yes |
| `http://target-ip/phppgadmin/` | Target URL path for PHPpgAdmin | Yes |
| `| grep -i "phpPgAdmin"` | Pipe to search for case-insensitive matches | Yes |

## Examples

### Basic Usage

```bash
curl -s http://192.168.1.100/phppgadmin/ | grep -i "phpPgAdmin"
```

### Advanced Usage

```bash
curl -s -H "User-Agent: Mozilla/5.0" http://target.com/phppgadmin/servers.php | head -20
```

## Expected Output

Lines containing "phpPgAdmin" or similar strings if the interface is exposed, e.g., "Welcome to phpPgAdmin". No output indicates it's not accessible or protected.

## Related

- [[Related Procedure|procedures/Discover-Exposed-PHPpgAdmin-Interface]]
