---
tags:
  - broken-access-control
  - information-disclosure
  - api
  - wakatime
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
procedures:
  - '[[procedures/Exploit-WakaTime-API-Broken-Access-Control]]'
step_count: 3
techniques:
  - '[[Valid Accounts]]'
  - '[[Account Discovery]]'
description: >-
  Multi-stage attack exploiting broken access control in WakaTime's API to
  disclose emails and membership details of team members using only member
  privileges.
skill_level: beginner
impact_level: medium
id: 3d93bbf4-c25a-41c5-a359-7972a515f800
created_at: '2025-12-14T17:29:09.771Z'
updated_at: '2025-12-14T17:29:09.771Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Account Discovery]]'
---
# WakaTime API Broken Access Control for Team Member Information Disclosure

Multi-stage attack chain demonstrating a complete attack workflow exploiting broken access control in WakaTime's leaderboard API, allowing authenticated members to access sensitive team member data including emails and membership details, which should be restricted to owners and admins.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Join Team as Member] --> B[Extract Team ID]
    B --> C[Access Members API Endpoint]
    C --> D[Disclose Sensitive Information]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (manual browser or API client access)

### Target Environment

- WakaTime web platform
- Authenticated user account with member privileges in a target team
- No specific ports or services beyond standard HTTPS (443)

### Initial Access Requirements

- Valid WakaTime user credentials
- Ability to join a public or accessible leaderboard team
- Network access to wakatime.com

## Detailed Attack Procedures

### Step 1: Join Team as Member
procedure: [[procedures/Exploit-WakaTime-API-Broken-Access-Control]]

**Objective**: Gain member-level access to a target leaderboard team to enable subsequent unauthorized data retrieval.

**Instructions**: Authenticate into WakaTime using your credentials, navigate to the leaderboards section, and join a team where you have or can obtain member privileges. This establishes an authenticated session.

**Expected Output**: Successful team membership confirmation in the user dashboard.

**Success Indicators**:
- Team listed under user's memberships with 'member' role
- No admin or owner privileges required

### Step 2: Extract Team ID
procedure: [[procedures/Exploit-WakaTime-API-Broken-Access-Control]]

**Objective**: Identify the unique team identifier needed to construct the vulnerable API endpoint.

**Instructions**: From the team settings or leaderboard interface in the WakaTime dashboard, locate and copy the team_id parameter, typically visible in the URL or team details page.

**Expected Output**: A numeric or string team_id value, e.g., '12345'.

**Success Indicators**:
- Team ID successfully copied without elevated privileges
- ID verifiable by inspecting page source or network requests

### Step 3: Access Members API Endpoint
procedure: [[procedures/Exploit-WakaTime-API-Broken-Access-Control]]

**Objective**: Retrieve unauthorized sensitive data by directly querying the vulnerable API endpoint using the member session.

**Instructions**: With the authenticated session (e.g., via browser cookies or API token), construct and visit the endpoint https://wakatime.com/api/v1/users/current/leaderboards/<team_id>/members. Use a tool like curl with session cookies or a browser's developer tools to make the request.

Execute [[commands/curl-wakatime-members-api]] to query the endpoint:

```bash
curl -H "Cookie: session=your_session_cookie" "https://wakatime.com/api/v1/users/current/leaderboards/12345/members"
```

**Expected Output**: JSON response containing an array of team members with fields like email addresses, usernames, and membership details.

**Success Indicators**:
- JSON data includes emails and details of users beyond the attacker's own account
- No access denied errors; full team roster disclosed

## Attack Chain Summary

### Key Achievements

1. Authenticated as member without needing admin access
2. Extracted team ID from standard interface
3. Disclosed sensitive personal information of all team members via API

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Account Discovery]] Account Discovery

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Discovery]] Discovery

---
*Last updated: 2023-10-01*
