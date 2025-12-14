---
id: cmd-433792-curl-inspect
data: 'curl -v ''https://rocket.chat/'''
tags:
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:07.764Z'
verified: false
validated: true
submitted: true
---
# curl-inspect-endpoint

## Command

```bash
curl -v 'https://rocket.chat/'
```

## Description

This command performs a verbose GET request to the target site, displaying headers and connections to help identify embedded third-party requests during manual inspection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose mode showing details | Yes |
| URL | Target website | Yes |

## Examples

### Basic Usage

```bash
curl -v 'https://rocket.chat/'
```

### Advanced Usage

```bash
curl -v -H "User-Agent: Mozilla/5.0" 'https://rocket.chat/'
```

## Expected Output

Verbose logs including HTTP headers, response code 200, and hints of script-loaded requests; no direct third-party output but aids in browser correlation.

## Related

- [[Related Procedure]]
