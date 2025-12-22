---
id: 76f03c6d-d39b-4b74-9a48-7268e94d518a
name: use-rpo-tool
type: command
executor: bash
data: 'java -jar rpo.jar -url http://www.example.com -depth 3'
output: null
created_at: '2023-04-06T03:56:43.833298+00:00'
updated_at: '2023-04-06T03:56:43.857575+00:00'
platforms:
  - Linux
tags:
  - rpo
  - tool
verified: true
validated: true
---

# use-rpo-tool

## Command

```bash
java -jar rpo.jar -url http://www.example.com -depth 3
```

## Description

Runs the RPO tool to scan a URL for relative path overwrite vulnerabilities up to specified depth.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -url | Target website URL | Yes |
| -depth 3 | Scan depth for paths | Yes |

## Examples

### Basic Usage

```bash
java -jar rpo.jar -url http://www.example.com -depth 3
```

## Expected Output

Report listing vulnerable relative paths and potential exploits.

## Related

- [[tools/RPO-Tool]]
- [[procedures/Exploit-RPO-for-Stored-XSS-via-CSS-Injection-in-IE]]
