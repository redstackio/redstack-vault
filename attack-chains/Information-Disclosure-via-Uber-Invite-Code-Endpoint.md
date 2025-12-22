---
id: ac-uber-invite-disclosure-178503
tags:
  - information-disclosure
  - privacy-leak
  - web-vulnerability
  - uber
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
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Retrieve-User-Contact-via-Invite-Code]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:52.059Z'
description: >-
  Exploit a public endpoint in Uber's invite system to disclose users' email and
  phone numbers associated with invite codes, leading to privacy violations.
skill_level: beginner
impact_level: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Information Disclosure via Uber Invite Code Endpoint

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via Public Endpoint] --> B[Data Disclosure]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP client like curl or browser)

### Target Environment

- Web platform
- Access to Uber's public join endpoint
- Valid invite code (obtainable from public sources or social engineering)

### Initial Access Requirements

- No credentials required
- Internet access
- Knowledge of a valid invite code

## Detailed Attack Procedures

### Step 1: Access Invite Join Endpoint
procedure: [[procedures/Retrieve-User-Contact-via-Invite-Code]]

**Objective**: Retrieve the email and/or phone number associated with a given Uber invite code by exploiting the lack of authentication on the join endpoint.

**Instructions**: Obtain a valid invite code (e.g., from shared links or user invitations). Then, use [[commands/curl-access-uber-join]] to query the endpoint:

```bash
curl "https://www.uber.com/a/join?invite_code=EXAMPLE_INVITE_CODE"
```

Parse the response HTML or JSON for the disclosed contact information.

**Expected Output**: The page response includes the inviter's email address and/or phone number in plain text, visible without authentication.

**Success Indicators**:
- Response contains user email or phone number
- No authentication prompt or error for invalid access

## Attack Chain Summary

### Key Achievements

1. Unauthorized access to personal contact information tied to invite codes
2. Demonstration of privacy risk in public-facing endpoints
3. Successful report leading to vulnerability fix and bounty

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
