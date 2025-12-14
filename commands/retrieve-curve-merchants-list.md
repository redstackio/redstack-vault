---
data: >-
  curl -X GET
  "https://api.imaginecurve.com/v1/rewards/users/programs/e329e463-7f5d-4358-9109-4f97c9f86abd/merchants"
  -H "Accept: application/json" -H "Curve-UserAgent: Android;Genymotion;Custom
  Phone" -H "Curve-AppAndVersion: Curve Android 2.9.0" -H "crv-user-agent:
  Android 2.9.0/20900" -H "Authorization:
  APE7kg446BXw2iFEI6Ca079RaGrJ3bcelA9DKDoUFUA" -H "crv-idempotency-key:
  a161ccfc-077c-4099-a180-ebbbacb50da6" -H "crv-request-id:
  88fb2296-46f4-49e4-858f-8aff312a9587" -H "crv-correlation-id:
  android-98600fe2-6b09-48d8-94b1-cecf73094c43" -H "Host: api.imaginecurve.com"
  --connect-timeout 10
tags:
  - api
  - recon
  - android
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.374Z'
id: db22abb5-172c-4a0d-941c-9083f364cc8c
verified: false
validated: true
submitted: true
---
# retrieve-curve-merchants-list

## Command

```bash
curl -X GET "https://api.imaginecurve.com/v1/rewards/users/programs/e329e463-7f5d-4358-9109-4f97c9f86abd/merchants" \
  -H "Accept: application/json" \
  -H "Curve-UserAgent: Android;Genymotion;Custom Phone" \
  -H "Curve-AppAndVersion: Curve Android 2.9.0" \
  -H "crv-user-agent: Android 2.9.0/20900" \
  -H "Authorization: APE7kg446BXw2iFEI6Ca079RaGrJ3bcelA9DKDoUFUA" \
  -H "crv-idempotency-key: a161ccfc-077c-4099-a180-ebbbacb50da6" \
  -H "crv-request-id: 88fb2296-46f4-49e4-858f-8aff312a9587" \
  -H "crv-correlation-id: android-98600fe2-6b09-48d8-94b1-cecf73094c43" \
  -H "Host: api.imaginecurve.com" \
  --connect-timeout 10
```

## Description

This command sends a GET request to the Curve API endpoint to retrieve the list of selected merchants for a user's rewards program. It mimics the Android app's request headers for authentication and tracking. Use this to inspect or manipulate the response in a proxy tool like Burp Suite during vulnerability testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method | Yes |
| URL path `/v1/rewards/users/programs/[id]/merchants` | Endpoint for merchants list; replace [id] with program UUID | Yes |
| `-H "Authorization: ..."` | Bearer token for authenticated access | Yes |
| `-H "crv-idempotency-key: ..."` | Unique key to prevent duplicates | Yes |
| `-H "crv-request-id: ..."` | Unique request identifier | Yes |
| `-H "crv-correlation-id: ..."` | Session correlation ID | Yes |
| `--connect-timeout 10` | Timeout for connection in seconds | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://api.imaginecurve.com/v1/rewards/users/programs/e329e463-7f5d-4358-9109-4f97c9f86abd/merchants" -H "Authorization: APE7kg446BXw2iFEI6Ca079RaGrJ3bcelA9DKDoUFUA"
```

### Advanced Usage

Include all headers as shown in the main command for full app emulation, especially in scripted testing.

## Expected Output

HTTP/1.1 200 OK with JSON: `{"success":true,"data":{"merchants":[{"id":"retailer1","name":"Waitrose"},{"id":"retailer2","name":"Whole Foods"},{"id":"retailer3","name":"Tesco"}]}}`. On failure, 401 Unauthorized if auth invalid.

## Related

- [[procedures/Bypass-Curve-Retailer-Limit-via-API-Manipulation]]
