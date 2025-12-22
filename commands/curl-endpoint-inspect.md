---
id: cmd-curl-endpoint-inspect
data: 'curl "https://help.glassdoor.com/gd_requestsubmitpage?lang=test"'
tags:
  - web
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T00:11:15.999Z'
verified: false
validated: true
submitted: true
---
# curl-endpoint-inspect

## Command

```bash
curl "https://help.glassdoor.com/gd_requestsubmitpage?lang=test"
```

## Description

This command sends an HTTP GET request to the Glassdoor endpoint with a test parameter to inspect for input reflection, useful in initial XSS reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target endpoint with parameter | Yes |

## Examples

### Basic Usage

```bash
curl "https://help.glassdoor.com/gd_requestsubmitpage"
```

### Advanced Usage

```bash
curl -v "https://help.glassdoor.com/gd_requestsubmitpage?lang=test" | grep -i lang
```

## Expected Output

HTML response containing the page, with 'test' echoed if vulnerable.

## Related

- [[Related Procedure]]
