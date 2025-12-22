---
id: cmd-curl-multi-site-test
data: 'curl -v "https://teavana.com/?prefv1=<>//example.com" 2>&1 | grep Location'
tags:
  - web-testing
  - verification
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:23.365Z'
verified: false
validated: true
submitted: true
---
# curl-multi-site-test

## Command

```bash
curl -v "https://teavana.com/?prefv1=<>//example.com" 2>&1 | grep Location
```

## Description

Verifies vulnerability on additional sites.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose | Yes |
| Target URL | Different site/param | Yes |

## Examples

### Basic Usage

```bash
curl -v "https://othersite/?test=<>//external" 2>&1 | grep Location
```

## Expected Output

Redirect confirmation.

## Related

- [[Related Procedure]]
