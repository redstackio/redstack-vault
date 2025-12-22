---
id: ef776319-717e-4446-8b68-b14aafadb14e
name: PHP-Serialized-Array-Payload-For-Admin-Hash-Bypass
type: code
language: PHP
verified: true
created_at: '2023-04-06T03:55:59.357531+00:00'
updated_at: '2023-04-06T03:55:59.362718+00:00'
platforms:
  - Web
  - PHP
tags:
  - payload
  - serialized
  - bypass
  - auth
validated: true
---

# PHP-Serialized-Array-Payload-For-Admin-Hash-Bypass

## Code

```php
a:2:{s:10:"admin_hash";N;s:4:"hmac";R:2;}
```

## Description

This serialized array payload sets admin_hash to null (N) and hmac to a self-reference (R:2). When deserialized in an authentication routine, it can nullify hash checks, allowing bypass of admin validation by referencing invalid or manipulated values.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| (none) | Static payload; adjust keys (e.g., admin_hash) to match target auth logic. | N/A |

## Usage

Inject into endpoints handling session or auth deserialization, e.g., via POST data or query param. Combine with curl to forge admin access, potentially leading to privileged actions or RCE.

## Detection

- Intrusion detection for array serializations in auth flows.
- Failed auth logs with null hash values.
- Anomalous session creations post-deserialization.

## Related

- [[procedures/Exploit-PHP-Object-Injection-for-Arbitrary-Code-Execution]]
