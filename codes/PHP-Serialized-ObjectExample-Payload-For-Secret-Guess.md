---
id: ed12f6ab-bc7a-4275-a8a9-e81b7fc147cb
name: PHP-Serialized-ObjectExample-Payload-For-Secret-Guess
type: code
language: PHP
verified: true
created_at: '2023-04-06T03:55:59.357418+00:00'
updated_at: '2023-04-06T03:55:59.362624+00:00'
platforms:
  - Web
  - PHP
tags:
  - payload
  - serialized
  - object-injection
validated: true
---

# PHP-Serialized-ObjectExample-Payload-For-Secret-Guess

## Code

```php
O:13:"ObjectExample":2:{s:10:"secretCode";N;s:5:"guess";R:2;}
```

## Description

This serialized payload injects an ObjectExample instance, setting secretCode to null (N) and guess to a reference (R:2) to the second property (itself). When deserialized and properties are accessed, it can force logic bypass by making guess match secretCode unexpectedly.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| (none) | Static payload; customize class name (O:13) and properties for target. | N/A |

## Usage

URL-encode and append to vulnerable endpoint, e.g., vuln.php?input=<encoded_payload>. Use in curl or browser to test property manipulation leading to 'Win' condition or similar bypass.

## Detection

- WAF alerts on serialized strings in requests.
- PHP errors for reference resolution failures.
- Application logs showing unexpected property values post-deserialization.

## Related

- [[procedures/Exploit-PHP-Object-Injection-for-Arbitrary-Code-Execution]]
