---
id: cmd-curl-test-parameter
data: >-
  curl
  "https://www.veris.in/wp-includes/js/mediaelement/flashmediaelement.swf?test=1"
  -I
tags:
  - recon
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:26.623Z'
verified: false
validated: true
submitted: true
---
# curl-test-parameter

## Command

```bash
curl "https://www.veris.in/wp-includes/js/mediaelement/flashmediaelement.swf?test=1" -I
```

## Description

This command performs a HEAD request to test if the SWF endpoint accepts URL parameters without rejection, aiding in vulnerability confirmation for XSS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | HEAD request only | Yes |
| URL with ?test=1 | Target with benign parameter | Yes |

## Examples

### Basic Usage

```bash
curl "https://target.com/swf?test=1" -I
```

### Advanced Usage

```bash
curl "https://target.com/swf?jsinitfunctio=test" -I -v
```

## Expected Output

HTTP headers with 200 OK status, indicating parameter acceptance; no body returned.

## Related

- [[commands/curl-fetch-swf]]
- [[procedures/Identify-Vulnerable-Flash-Media-Element-Endpoint-in-WordPress]]
