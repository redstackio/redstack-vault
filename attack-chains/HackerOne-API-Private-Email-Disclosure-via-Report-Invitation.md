---
tags:
  - information-disclosure
  - api-abuse
  - email-leak
  - hackerone
type: attack_chain
tools:
  - '[[tools/Curl]]'
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Disclose-User-Email-via-HackerOne-Report-API]]'
step_count: 4
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:32:48.504Z'
description: >-
  An authenticated information disclosure attack exploiting the HackerOne API to
  reveal any user's private email address by inviting them as a report
  participant and fetching report details.
skill_level: intermediate
impact_level: high
id: cbab5af7-fbf3-4d9d-a935-96078781cf09
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# HackerOne API Private Email Disclosure via Report Invitation

Multi-stage attack chain demonstrating a complete attack workflow for disclosing private user emails through the HackerOne API.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Report] --> B[Invite Victim]
    B --> C[Generate API Token]
    C --> D[Fetch Report via API]
    D --> E[Extract Email]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Curl]]

### Target Environment

- HackerOne platform (web-based bug bounty service)
- Authenticated access to a HackerOne program (e.g., sandbox program)
- No specific ports or services beyond standard HTTPS (443)

### Initial Access Requirements

- Valid HackerOne account with ability to create/submit reports in a program
- Knowledge of target victim's public username (obtainable from HackerOne sitemap or profiles)
- API access enabled on the account

## Detailed Attack Procedures

### Step 1: Access Any Report
procedure: [[procedures/Disclose-User-Email-via-HackerOne-Report-API]]

**Objective**: Gain access to a report in the attacker's HackerOne program to serve as the invitation target.

**Instructions**: Log in to your HackerOne account and navigate to the program dashboard (e.g., a sandbox program). Select or create a report to use for the invitation.

**Expected Output**: Report dashboard open, with report ID visible (e.g., in URL as /reports/[report_id]).

**Success Indicators**:
- Report accessible in dashboard
- Report ID noted for API use

### Step 2: Invite Victim as Participant
procedure: [[procedures/Disclose-User-Email-via-HackerOne-Report-API]]

**Objective**: Add the target user to the report without their acceptance, triggering the email inclusion in API responses.

**Instructions**: In the report interface, use the 'Add Participant' or invitation feature to invite the victim by their public username. No email or acceptance from the victim is needed.

**Expected Output**: Invitation sent; victim added to participants list in the report view.

**Success Indicators**:
- Victim username appears in report participants
- No errors in invitation process

### Step 3: Generate API Token
procedure: [[procedures/Disclose-User-Email-via-HackerOne-Report-API]]

**Objective**: Obtain an API token for authenticated access to report details.

**Instructions**: Go to your HackerOne account settings, navigate to API tokens section, and create a new token with read access to reports.

**Expected Output**: API identifier and token generated (e.g., api_identifier:your_token).

**Success Indicators**:
- Token created and copied securely
- Token valid for API authentication

### Step 4: Fetch Report via API
procedure: [[procedures/Disclose-User-Email-via-HackerOne-Report-API]]

**Objective**: Retrieve the report details via API to expose the victim's private email in the activities data.

**Instructions**: Use [[commands/curl-hackerone-report-fetch]] to query the API endpoint with the report ID and token:

```bash
curl "https://api.hackerone.com/v1/reports/[report_id]" -u "api_identifier:token"
```

Parse the JSON response for the activities array, looking for 'activity-external-user-invited' type containing attributes.email.

**Expected Output**: JSON with report data, including activities object showing victim's email.

**Success Indicators**:
- API response received without auth errors
- Victim's private email visible in activities.data.attributes.email

## Attack Chain Summary

### Key Achievements

1. Authenticated access to any HackerOne report for manipulation
2. Invitation of target user exposing their email in API without consent
3. Retrieval of sensitive user data via standard API call
4. Potential for mass email collection using public usernames

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
