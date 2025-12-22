---
id: e617c4a3-6968-4cf5-bc09-f36ed629d663
name: SSJI-Detection-Payloads
type: code
language: json
verified: true
created_at: '2023-04-06T03:56:31.495652+00:00'
updated_at: '2023-04-10T20:23:03.486802+00:00'
platforms:
  - Web
tags:
  - injection
  - ssji
  - nosql
validated: true
---

# SSJI-Detection-Payloads

## Code

```json
';return 'a'=='a' && ''=='
";return 'a'=='a' && ''=='
0;return true
```

## Description

This JSON snippet contains test payloads for detecting Server-Side JavaScript Injection (SSJI) vulnerabilities in NoSQL applications. Each line represents a potential injection string designed to close an existing query and inject a simple boolean expression or unconditional return. These are used to probe if user input is evaluated as JavaScript on the server, typically in MongoDB queries.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| N/A | These are static payloads; substitute into JSON 'data' field as needed | ';return 'a'=='a' && ''==' |

## Usage

Embed these payloads into the 'data' field of a JSON request body sent to a vulnerable endpoint, e.g., via curl: {"data": "[payload here]"}. Use in procedures like [[procedures/NoSQL-Injection-via-SSJI-Exploit]] to test for injection. Start with the first payload to check string closure, progressing to others for confirmation.

## Detection

- Application logs showing JavaScript evaluation errors or boolean query results.
- WAF alerts on payloads containing 'return' or comparison operators in JSON.
- Anomalous database query patterns with user-supplied JavaScript.

## Related

- [[procedures/NoSQL-Injection-via-SSJI-Exploit]]
- [[curl-test-ssji-injection]]
