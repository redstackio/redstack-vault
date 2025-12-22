---
id: cmd-curl-v-001
data: curl -v
tags:
  - version-check
  - curl
type: command
output: Version string of the installed curl
executor: bash
platforms:
  - Linux
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:25.535Z'
verified: false
validated: true
submitted: true
---
# curl-version-verbose

## Command

```bash
curl -v
```

## Description

Displays verbose output including the curl version to verify the tool under test during vulnerability assessment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose mode to show version details | Yes |

## Examples

### Basic Usage

```bash
curl -v
```

### Advanced Usage

```bash
curl -v https://example.com
```

## Expected Output

'* curl 8.4.0 ...' at the beginning, followed by connection details if a URL is provided.

## Related

- [[commands/curl-xss-payload-test]]
- [[procedures/Test-XSS-Payloads-in-curl-URL-Processing]]
