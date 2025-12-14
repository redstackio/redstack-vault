---
data: >-
  CLOUDRON_LDAP_BIND_DN="cn=admin,ou=users,dc=example"
  CLOUDRON_LDAP_BIND_PASSWORD="password"
  CLOUDRON_LDAP_USERS_BASE_DN="ou=users,dc=example"
  CLOUDRON_LDAP_URL="ldap://localhost:3002" node app.js
tags:
  - node
  - app
  - ldap
  - setup
type: command
output: null
executor: bash
platforms:
  - Linux
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.229Z'
id: 733c980a-da79-471b-9784-8aeedc5e1415
verified: false
validated: true
submitted: true
---
# start-meemo-app-with-ldap

## Command

```bash
CLOUDRON_LDAP_BIND_DN="cn=admin,ou=users,dc=example" CLOUDRON_LDAP_BIND_PASSWORD="password" CLOUDRON_LDAP_USERS_BASE_DN="ou=users,dc=example" CLOUDRON_LDAP_URL="ldap://localhost:3002" node app.js
```

## Description

Launches the meemo app with LDAP environment variables set for bind credentials and server URL, enabling vulnerable authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| CLOUDRON_LDAP_BIND_DN | LDAP admin DN | Yes |
| CLOUDRON_LDAP_BIND_PASSWORD | Bind password | Yes |
| CLOUDRON_LDAP_USERS_BASE_DN | Users OU | Yes |
| CLOUDRON_LDAP_URL | LDAP server URL | Yes |
| node | Runtime | Yes |
| app.js | Main app file | Yes |

## Examples

### Basic Usage

```bash
CLOUDRON_LDAP_BIND_DN="cn=admin,ou=users,dc=example" CLOUDRON_LDAP_BIND_PASSWORD="password" CLOUDRON_LDAP_USERS_BASE_DN="ou=users,dc=example" CLOUDRON_LDAP_URL="ldap://localhost:3002" node app.js
```

## Expected Output

App startup logs: Server running on http://localhost:3000, LDAP connected.

## Related

- [[commands/start-ldap-test-server]]
- [[procedures/Setup-Meemo-Environment-with-LDAP]]
