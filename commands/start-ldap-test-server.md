---
data: node ldapjstestserver.js
tags:
  - ldap
  - server
  - setup
type: command
output: null
executor: bash
platforms:
  - Linux
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.234Z'
id: 865d07b9-15f6-4233-baef-0adf46fe2b43
verified: false
validated: true
submitted: true
---
# start-ldap-test-server

## Command

```bash
node ldapjstestserver.js
```

## Description

Starts a JavaScript-based LDAP test server on localhost:3002 to simulate authentication backend for meemo.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| node | Node.js runtime | Yes |
| ldapjstestserver.js | Test server script | Yes |

## Examples

### Basic Usage

```bash
node ldapjstestserver.js
```

## Expected Output

Server startup message: Listening on port 3002.

## Related

- [[commands/start-meemo-app-with-ldap]]
- [[procedures/Setup-Meemo-Environment-with-LDAP]]
