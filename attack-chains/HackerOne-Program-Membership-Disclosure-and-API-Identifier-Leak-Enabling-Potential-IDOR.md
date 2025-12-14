---
tags:
  - information-disclosure
  - privacy-bypass
  - idor
  - hackerone
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Disclose-Private-Program-Memberships-via-Profile-Analysis]]'
  - '[[procedures/Expose-API-Identifiers-for-IDOR-Exploitation]]'
step_count: 2
techniques:
  - '[[Gather Victim Identity Information]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:32:39.590Z'
description: >-
  Attack chain exploiting ineffective visibility controls in HackerOne's program
  preferences to disclose private program memberships and API identifiers,
  potentially leading to IDOR attacks.
skill_level: intermediate
impact_level: high
id: 8012dc94-b5da-4e75-a197-3ca3c3fae7df
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Identity Information]]'
  - '[[Account Discovery]]'
---
# HackerOne Program Membership Disclosure and API Identifier Leak Enabling Potential IDOR

Multi-stage attack chain demonstrating how to bypass privacy settings on HackerOne to reveal private program participants and leak API identifiers that could facilitate IDOR attacks.

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
    A[Profile Analysis for Membership Disclosure] --> B[API Inspection for Identifier Leak]
    B --> C[Potential IDOR Exploitation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Browser Developer Tools
- [[tools/curl]]

### Target Environment

- HackerOne platform (Web)
- Access to public user profiles
- No special privileges required

### Initial Access Requirements

- Valid HackerOne account (anonymous browsing may suffice for public profiles)
- Network access to hackerone.com
- No prior access needed beyond internet connectivity

## Detailed Attack Procedures

### Step 1: Profile Analysis for Membership Disclosure
procedure: [[procedures/Disclose-Private-Program-Memberships-via-Profile-Analysis]]

**Objective**: Bypass visibility preferences to identify participants in private or restricted HackerOne programs.

**Instructions**: Navigate to a target user's HackerOne profile using a browser. Inspect the profile page source or use developer tools to examine the program preferences section. Despite privacy settings set to hide memberships, the list of programs will be visible in the HTML structure under the visibility feature.

For automated verification, use [[commands/curl-fetch-profile]] to retrieve the profile page:

```bash
curl -s "https://hackerone.com/user-handle" > profile.html
```

Then grep for program indicators:

```bash
grep -i "program" profile.html
```

**Expected Output**: HTML containing program names and memberships, even for blocked or private programs.

**Success Indicators**:
- Program memberships listed despite privacy settings
- Ability to correlate users with private programs

### Step 2: API Inspection for Identifier Leak
procedure: [[procedures/Expose-API-Identifiers-for-IDOR-Exploitation]]

**Objective**: Extract API identifiers from progress and data sections to enable potential unauthorized access via IDOR.

**Instructions**: While viewing the profile or related pages, open browser developer tools and inspect network requests to HackerOne's API endpoints (e.g., /api/v1/progress or /api/v1/data). The responses will include exposed identifiers without proper access controls.

To replicate via command line, use [[commands/curl-api-request]] to query relevant API endpoints (replace {token} with any session token if authenticated):

```bash
curl -H "Authorization: Token {token}" "https://api.hackerone.com/v1/progress" | jq '.data[] | .id'
```

**Expected Output**: JSON response with API identifiers visible in progress and data arrays.

**Success Indicators**:
- Identifiers extracted from API responses
- Potential to use identifiers in direct object references for unauthorized access testing

## Attack Chain Summary

### Key Achievements

1. Successful bypass of program visibility privacy settings to disclose memberships
2. Exposure of API identifiers in unprotected sections
3. Foundation for follow-on IDOR attacks targeting program data

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Gather Victim Identity Information]] Gather Victim Identity Information
- [[Account Discovery]] Account Discovery

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance
- [[Discovery]] Discovery

---
*Last updated: 2023-10-01T00:00:00Z*
