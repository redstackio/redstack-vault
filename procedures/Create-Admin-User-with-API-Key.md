---
id: proc-uuid-2
tags:
  - admin-creation
  - database-manipulation
  - authentication
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Create Account]]'
updated_at: '2025-12-14T03:46:37.394Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Create Account]]'
---
# Create-Admin-User-with-API-Key

## Summary

This procedure manually inserts an admin user into the database of the RATELIMITED API test instance, complete with a valid API key, to enable authenticated access to protected endpoints like /users/[id]/set_tier.

## Description

The API requires authentication via API keys stored in the database. By directly inserting a record into the users table, an admin role can be assigned without using the application's registration flow. This setup is crucial for testing the XSS vulnerability, which affects authenticated users.

## Requirements

1. Database access (e.g., MySQL credentials for the test instance)
2. Knowledge of the users table schema (fields like id, role, api_key)
3. Deployed API instance from prior procedure

## Defense

Defensive measures and detection strategies:

- Enforce database access controls and audit logs for INSERT operations
- Use parameterized queries in application code to prevent unauthorized inserts
- Monitor for anomalous user creation events in logs

## Objectives

1. Gain admin-level access to the API
2. Obtain a valid API key for requests
3. Validate authentication works

## Instructions

### Step 1: Access Database

**Context**: Connect to the database hosting the API's user data.

```bash
mysql -u root -p ratelimited_db
```

> Log in to the MySQL database named 'ratelimited_db' or equivalent.

### Step 2: Insert Admin User

**Context**: Create the admin record with role 'admin' and generate an API key.

Execute SQL:

```sql
INSERT INTO users (id, username, role, api_key) VALUES (1, 'admin_test', 'admin', 'test-api-key-123');
```

> Insert the record. Use a secure key in production, but 'test-api-key-123' for testing. Verify with `SELECT * FROM users;`.

### Step 3: Test Authentication

**Context**: Confirm the user can authenticate.

Send a test request:

```bash
curl -X GET http://localhost:8000/users -H "Authorization: Bearer test-api-key-123"
```

> Expect a successful response with user data, confirming admin access.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Create Account]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[admin-creation]]
- [[database-manipulation]]
