---
id: cmd-uuid-1
data: >-
  curl -X GET "https://target-domain/gwtmain/" -H "User-Agent: Mozilla/5.0
  (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)"
  --connect-timeout 10
tags:
  - recon
  - probe
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:19.930Z'
verified: false
validated: true
submitted: true
---
# curl-basic-endpoint-probe

## Command

```bash
curl -X GET "https://target-domain/gwtmain/" -H "User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)" --connect-timeout 10
```

## Description

Probes the /gwtmain/ servlet endpoint to confirm its availability and responsiveness in a Java GWT environment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP GET method | Yes |
| `URL` | Target endpoint URL | Yes |
| `-H "User-Agent: ..."` | Spoofs browser user agent to mimic legitimate traffic | Yes |
| `--connect-timeout 10` | Sets connection timeout to 10 seconds | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://target-domain/gwtmain/" -H "User-Agent: Mozilla/5.0"
```

### Advanced Usage

```bash
curl -X GET "https://target-domain/gwtmain/" -H "User-Agent: Mozilla/5.0" -v
```

## Expected Output

HTTP 200 OK response with servlet content or static files; body may include CSS or error pages indicating active servlet.

## Related

- [[Related Procedure: Identify-Vulnerable-GWT-Servlet-Endpoint]]
