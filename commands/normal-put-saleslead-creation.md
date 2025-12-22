---
id: cmd-uuid-001
data: >-
  curl -X PUT
  "https://api.hyperpure.com/consumer/onboarding/saleslead/6b6a8a5a-4a74-46db-b2fe-32a46f927ecc"
  -H "Content-Type: application/json;charset=utf-8" -H "X-Client: consumer" -H
  "X-TrackingId: 8242c5a2-6325-4101-96b8-c7ed6008e92a" -H "HeaderRoute: v2" -H
  "APIVersion: 4.2" -H "AppType: web" -H "Origin: https://www.hyperpure.com/" -H
  "Referer: https://www.hyperpure.com/register" -d
  '{"address":{"addressLine":"test","cityId":34,"state":{"name":"Gujarat"},"zipCode":"388001"},"deliveryTime":0,"email":"hoteyes@wearehackerone.com","outletName":"test","phoneNumber":"█████","salesLeadId":"31cf8eb0-f81e-4c99-acad-35eae89ed659"}'
tags:
  - api
  - put
  - baseline
type: command
output: >-
  HTTP/1.1 200 OK with
  {"response":{"salesLeadId":"6b6a8a5a-4a74-46db-b2fe-32a46f927ecc"}}
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:10.118Z'
verified: false
validated: true
submitted: true
---
# normal-put-saleslead-creation

## Command

```bash
curl -X PUT "https://api.hyperpure.com/consumer/onboarding/saleslead/6b6a8a5a-4a74-46db-b2fe-32a46f927ecc" -H "Content-Type: application/json;charset=utf-8" -H "X-Client: consumer" -H "X-TrackingId: 8242c5a2-6325-4101-96b8-c7ed6008e92a" -H "HeaderRoute: v2" -H "APIVersion: 4.2" -H "AppType: web" -H "Origin: https://www.hyperpure.com/" -H "Referer: https://www.hyperpure.com/register" -d '{"address":{"addressLine":"test","cityId":34,"state":{"name":"Gujarat"},"zipCode":"388001"},"deliveryTime":0,"email":"hoteyes@wearehackerone.com","outletName":"test","phoneNumber":"█████","salesLeadId":"31cf8eb0-f81e-4c99-acad-35eae89ed659"}'
```

## Description

Sends a baseline PUT request to create a sales lead in the Hyperpure API, using test data to verify normal endpoint behavior before injection testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL salesLeadId | UUID for the sales lead (e.g., 6b6a8a5a-4a74-46db-b2fe-32a46f927ecc) | Yes |
| email | Test email address | Yes |
| phoneNumber | Redacted phone number | Yes |
| address | JSON object with address details | Yes |

## Examples

### Basic Usage

```bash
curl -X PUT "https://api.hyperpure.com/consumer/onboarding/saleslead/{uuid}" [headers] -d '{json body}'
```

### Advanced Usage

Modify UUID or body for variations, but keep headers consistent for API compatibility.

## Expected Output

HTTP/1.1 200 OK response body: {"response":{"salesLeadId":"6b6a8a5a-4a74-46db-b2fe-32a46f927ecc"}}, indicating successful creation.

## Related

- [[commands/sqli-payload-put-saleslead]]
- [[procedures/Exploit-Blind-SQL-Injection-in-Sales-Lead-Endpoint]]
