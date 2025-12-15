---
tags:
  - idor
  - glassdoor
  - profile-picture
  - data-disclosure
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-IDOR-in-Profile-Picture-Upload]]'
step_count: 1
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:34.695Z'
description: >-
  Attack chain exploiting an Insecure Direct Object Reference (IDOR)
  vulnerability in Glassdoor's profile picture changing mechanism to disclose
  unauthorized access to other users' profile pictures via manipulated image
  IDs.
skill_level: intermediate
impact_level: medium
id: 1a9050d4-25e0-4ad2-9996-208aa3a931aa
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# IDOR in Glassdoor Profile Picture Upload Exposing User Images

Multi-stage attack chain demonstrating a complete attack workflow exploiting IDOR in Glassdoor's profile picture mechanism.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via Profile Update] --> B[IDOR Exploitation]
    B --> C[Data Disclosure]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser Developer Tools or [[tools/Burp-Suite]]

### Target Environment

- Web application (Glassdoor platform)
- Required services/ports: HTTPS on port 443
- Network access requirements: Internet access to Glassdoor

### Initial Access Requirements

- Valid user account on Glassdoor
- Network position: External
- Prior access needed: Authenticated session

## Detailed Attack Procedures

### Step 1: Exploit IDOR in Profile Picture Upload
procedure: [[procedures/Exploit-IDOR-in-Profile-Picture-Upload]]

**Objective**: Identify and manipulate exposed image IDs in HTTP responses to access unauthorized user profile pictures.

**Instructions**: Log in to your Glassdoor account and navigate to the profile picture upload section. Upload a test image and inspect the HTTP response using browser developer tools or a proxy like Burp Suite. Look for exposed image IDs in the JSON response. Once identified, modify the ID in subsequent requests to target other users' images (e.g., increment or guess sequential IDs). Use a tool like curl to simulate the request:

```bash
curl -X GET 'https://www.glassdoor.com/profile/picture?image_id=TARGET_IMAGE_ID' -H 'Cookie: session=your_session_cookie' -H 'Authorization: Bearer your_token'
```

Replace `TARGET_IMAGE_ID` with a manipulated ID (e.g., from 12345 to 12346 for adjacent user). Repeat for multiple IDs to enumerate images.

**Expected Output**: HTTP response containing binary image data or metadata for the targeted user's profile picture.

**Success Indicators**:
- Unauthorized image data retrieved without errors
- Confirmation of access to non-owned profile pictures via visual inspection or response size

## Attack Chain Summary

### Key Achievements

1. Successful identification of exposed image IDs in profile update responses
2. Unauthorized disclosure of other users' profile pictures
3. Demonstration of IDOR leading to privacy violation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
