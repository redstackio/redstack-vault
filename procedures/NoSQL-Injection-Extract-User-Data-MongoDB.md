---
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
tactics:
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/Exploit-Public-Facing-Application|T1190 - Exploit Public-Facing
    Application]]
  - >-
    [[techniques/Data-from-Information-Repositories|T1213 - Data from
    Information Repositories]]
sub_techniques: []
tags:
  - '[[tags/Exploit]]'
  - '[[tags/Extract data information]]'
  - '[[tags/NoSQL Injection]]'
  - mongodb
  - authentication-bypass
commands:
  - '[[commands/curl-nosql-injection-url-payload]]'
  - '[[commands/curl-nosql-injection-json-payload]]'
platforms:
  - Web
tools: []
validated: true
---

# NoSQL-Injection-Extract-User-Data-MongoDB

## Summary

This procedure demonstrates how to perform a NoSQL injection attack on a MongoDB-backed web application to extract sensitive user data, such as usernames and passwords, by injecting malicious queries into authentication endpoints. By exploiting improper input validation in login forms or API requests, attackers can use MongoDB operators like $ne and $regex to bypass authentication and dump database contents, enabling unauthorized access to user credentials.

## Description

NoSQL databases like MongoDB offer scalability but are susceptible to injection attacks similar to SQL injection. In vulnerable web applications, user inputs for username and password fields are directly concatenated into MongoDB queries without sanitization, allowing attackers to inject operators that alter the query logic. This procedure focuses on crafting payloads in URL-encoded or JSON formats to match partial passwords via regex patterns, effectively dumping all user records where passwords match certain criteria (e.g., starting with 'm', 'md'). This technique is commonly used against login APIs or forms that use MongoDB for authentication, leading to data exfiltration. The attack assumes the application uses queries like db.users.find({username: req.body.username, password: req.body.password}), which can be manipulated to return all matching documents.

## Requirements

1. Network access to the target web application with a MongoDB backend (e.g., login endpoint at http://target.com/api/login).
2. Knowledge of the authentication endpoint structure (POST method accepting username/password).
3. Tools for sending HTTP requests, such as curl or a proxy like Burp Suite.
4. Basic understanding of MongoDB query operators ($ne, $regex, $eq).

## Defense

- Implement strict input validation and sanitization, using parameterized queries or libraries like mongo-sanitize to strip MongoDB operators from inputs.
- Enforce least privilege access on the database, limiting application accounts to read-only where possible.
- Monitor database logs for anomalous queries involving operators like $regex or $ne, and implement web application firewalls (WAFs) to detect injection patterns.
- Use HTTPS and rate limiting on authentication endpoints to hinder brute-force and injection attempts.

## Objectives

1. Bypass authentication by injecting NoSQL operators to extract all user documents matching regex patterns on passwords.
2. Dump sensitive data including usernames and hashed or plaintext passwords from the MongoDB collection.
3. Identify weak or common password patterns for further exploitation, such as cracking or lateral movement.

## Instructions

### Step 1: Identify the Authentication Endpoint

**Context**: Locate the login form or API endpoint that accepts username and password inputs. This is typically a POST request to /login or /api/auth. Use browser developer tools or reconnaissance to confirm the endpoint URL and request format (form-data or JSON body).

Inspect the request payload to ensure inputs are passed as username and password fields.

### Step 2: Test URL-Encoded Injection Payload

**Context**: Craft a URL-encoded payload using MongoDB operators to exclude a non-existent username ($ne) and match passwords with regex patterns (e.g., starting with 'm'). This alters the query to return all users with matching passwords, bypassing the need for valid credentials.

**Command** ([[commands/curl-nosql-injection-url-payload]]):
```bash
curl -X POST http://target.com/login -d "username[\$ne]=toto&password[\$regex]=m.{2}" -v
```

> This command sends an injected payload to the login endpoint. The $ne operator ensures the query doesn't filter by a specific username, while $regex matches passwords of length 3+ starting with 'm'. Repeat with variations like md.{1}, mdp, m.*, md.* to broaden the search. Expected output includes a successful response (e.g., 200 OK) with user data in JSON, such as {"users": [{"username": "admin", "password": "mypassword"}]}.

### Step 3: Test JSON Injection Payload

**Context**: For APIs expecting JSON bodies, inject operators directly into the JSON structure. Use $eq for exact username matching (to simulate targeted extraction) combined with $regex on passwords to dump records starting with patterns like '^m' or '^md'.

**Command** ([[commands/curl-nosql-injection-json-payload]]):
```bash
curl -X POST http://target.com/api/login -H "Content-Type: application/json" -d '{"username": {"$eq": "admin"}, "password": {"$regex": "^m" }}' -v
```

> This payload targets the 'admin' user but uses regex to match any password starting with 'm'. Variations include '^md' and '^mdp'. If successful, the response will return matching user documents, confirming data extraction. If the endpoint returns all matches without authentication, the injection succeeded.

### Step 4: Analyze and Extract Data

**Context**: Review the response for extracted data. If the application echoes query results or returns user lists on failed logins, compile the output. Use tools like jq to parse JSON responses for usernames and passwords. If no data is returned, refine regex patterns or test for other operators like $exists or $gt (e.g., password: {$exists: true, $ne: null}).

Verify success by checking for multiple user records in the response, indicating bypass and extraction.
