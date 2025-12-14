---
id: ac-okru-private-video-bypass-001
tags:
  - broken-authentication
  - access-bypass
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - >-
    [[procedures/Bypass-Access-Controls-to-View-Private-Group-Videos-on-ok.ru-Mobile]]
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:11.360Z'
description: >-
  A single-step attack exploiting broken authentication and missing access
  controls on the mobile version of ok.ru to view restricted private group
  videos without membership or login.
skill_level: beginner
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Unauthorized Access to Private Group Videos via Broken Authentication on ok.ru Mobile

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via Direct URL] --> D[Objective: View Private Videos]

    style A fill:#e74c3c
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- Platform: Web (mobile version of ok.ru)
- Required services/ports: HTTP/80
- Network access requirements: Internet connection to access ok.ru

### Initial Access Requirements

- No credentials required
- No prior access or membership to the private group needed
- Public internet access

## Detailed Attack Procedures

### Step 1: Bypass Authentication to Access Private Video
procedure: [[procedures/Bypass-Access-Controls-to-View-Private-Group-Videos-on-ok.ru-Mobile]]

**Objective**: Gain unauthorized access to videos restricted to private group members by exploiting the lack of access controls on the mobile site.

**Instructions**: Construct and navigate to a direct URL that bypasses authentication checks. No login or group membership is required; simply open the URL in a web browser.

The vulnerable URL format targets the mobile endpoint with parameters for group ID and video subject ID:

```url
http://m.ok.ru/dk?st.cmd=altGroupMovieComments&st.ord=off&st.groupId=53605096554748&st.sbj=31115578108
```

Replace `st.groupId` with the target private group's ID and `st.sbj` with the video's subject ID if known. Access the URL directly.

**Expected Output**: The browser loads the private group video comments and playback interface, displaying content normally restricted to authenticated group members.

**Success Indicators**:
- Video content loads without prompting for login or group membership
- Unauthorized user can view and interact with restricted videos
- No access denied errors appear

## Attack Chain Summary

### Key Achievements

1. Bypassed authentication entirely using a crafted mobile URL
2. Accessed private group videos without any permissions
3. Demonstrated critical impact on user privacy and content security

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
