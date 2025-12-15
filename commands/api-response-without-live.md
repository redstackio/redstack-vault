---
data: '{"code":0,"data":{"amount":null,"invited_amount":0},"message":"success"}'
tags:
  - api-validation
type: command
executor: json
platforms:
  - Web
id: dd16dfaf-7d83-4253-ad98-0d1be5746e18
created_at: '2025-12-14T17:28:36.435Z'
updated_at: '2025-12-14T17:28:36.435Z'
verified: false
validated: true
submitted: true
---
# api-response-without-live

## Command

```json
{"code":0,"data":{"amount":null,"invited_amount":0},"message":"success"}
```

## Description

Example JSON response from TikTok API when 'live' parameter is omitted, showing no data leakage.

## Parameters

None; this is a response format.

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

Received after POST without 'live'.

### Advanced Usage

Compare to exploited response.

## Expected Output

Empty data fields: amount null, no products listed.

## Related

- [[procedures/Test-API-Response-Without-Live-Parameter]]
