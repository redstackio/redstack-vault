---
data: >-
  curl -G "https://liberapay.com/about/me/edit" --data-urlencode
  "sign-in.currency=USD<WDILR9>G8OAI[ !+! ]</WDILR9>"
tags:
  - web
  - xss
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:30.902Z'
id: caa9be68-8fb1-4a92-8c1b-b55b773c022d
verified: false
validated: true
submitted: true
---
# curl-get-payload

## Command

```bash
curl -G "https://liberapay.com/about/me/edit" --data-urlencode "sign-in.currency=USD<WDILR9>G8OAI[ !+! ]</WDILR9>"
```

## Description

This command sends a GET request to the Liberapay edit endpoint with a URL-encoded XSS payload in the sign-in.currency parameter to test for reflection and content-sniffing vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-G` | Treats the request as GET with data-urlencode | Yes |
| `--data-urlencode` | Encodes the payload for safe transmission | Yes |
| URL | Target endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -G "https://liberapay.com/about/me/edit" --data-urlencode "sign-in.currency=USD<WDILR9>G8OAI[ !+! ]</WDILR9>"
```

### Advanced Usage

```bash
curl -v -G "https://liberapay.com/about/me/edit" --data-urlencode "sign-in.currency=USD<WDILR9>G8OAI[ !+! ]</WDILR9>" -o response.html
```

## Expected Output

HTTP response with status 200, containing HTML where the payload is reflected in a text element, e.g., a currency field showing the decoded string without execution.

## Related

- [[Related Procedure|procedures/Inject-Payload-via-GET-Parameter]]
