---
tags:
  - xss
  - stored-xss
  - javascript
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-User-Profile-After-Login]]'
  - '[[procedures/Inject-XSS-Payload-in-Recommendation-Description]]'
  - '[[procedures/Save-Malicious-Recommendation]]'
  - '[[procedures/Trigger-Stored-XSS-on-Public-Profile]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:20.840Z'
description: >-
  A multi-stage attack exploiting insufficient HTML sanitization in Judge.me's
  recommendation description field to inject and trigger stored XSS, leading to
  arbitrary JavaScript execution on victims viewing the public profile.
skill_level: intermediate
impact_level: high
id: e9fae939-4ecd-491b-93c8-1be6ac38dced
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Stored XSS in Judge.me Public Profile Reviews via Malicious Product Description

Multi-stage attack chain demonstrating a complete stored XSS workflow in Judge.me's public profile reviews, where an attacker injects malicious HTML into the product description field of a recommendation, bypassing filters with a base64-encoded data URI to execute JavaScript when victims interact with the profile.

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
    A[Initial Access: Login and Profile] --> B[Injection: Add Recommendation with Payload]
    B --> C[Persistence: Save Malicious Content]
    C --> D[Execution: View Profile and Trigger XSS]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome with developer tools for testing)

### Target Environment

- Judge.me platform (web application)
- Required services/ports: HTTPS (443)
- Network access requirements: Internet access to Judge.me site

### Initial Access Requirements

- Registered user account on Judge.me
- Valid credentials for login
- No prior access needed beyond standard user privileges

## Detailed Attack Procedures

### Step 1: Access User Profile After Login
procedure: [[procedures/Access-User-Profile-After-Login]]

**Objective**: Authenticate as a registered user and navigate to the profile section to prepare for injecting the payload.

**Instructions**: Open a web browser and navigate to the Judge.me login page. Enter your registered username and password to authenticate. After login, locate and click on the profile or account settings section to access the recommendations area.

**Expected Output**: Successful login and access to the user profile dashboard, where recommendation forms are available.

**Success Indicators**:
- User is redirected to the authenticated profile page
- No authentication errors or redirects to login

### Step 2: Inject XSS Payload in Recommendation Description
procedure: [[procedures/Inject-XSS-Payload-in-Recommendation-Description]]

**Objective**: Fill the recommendation form with product details and insert the malicious HTML payload into the description field to store XSS content.

**Instructions**: In the profile section, click on "Add Recommendation". Enter valid product details such as name, image, and other required fields. In the description field, insert the payload: `<a href="data:text/html;charset=utf-7;base64,PHNjcmlwdD5hbGVydCgiWFNTIik8L3NjcmlwdD4=">Click Here</a>`. This payload uses a base64-encoded data URI that decodes to `<script>alert('XSS')</script>` upon execution.

**Expected Output**: The form accepts the input without immediate errors, displaying the "Click Here" link in the description preview.

**Success Indicators**:
- Payload is entered without sanitization errors
- HTML tag renders as a clickable link in the form

### Step 3: Save Malicious Recommendation
procedure: [[procedures/Save-Malicious-Recommendation]]

**Objective**: Submit the recommendation form to persist the injected HTML in the database, making it available on the public profile.

**Instructions**: Complete any remaining form fields (e.g., rating, date) and click the "Save" or "Submit" button to store the recommendation.

**Expected Output**: Confirmation message that the recommendation has been saved, and it appears in the user's recommendation list.

**Success Indicators**:
- No validation errors on submission
- Recommendation is listed in the profile without alterations to the payload

### Step 4: Trigger Stored XSS on Public Profile
procedure: [[procedures/Trigger-Stored-XSS-on-Public-Profile]]

**Objective**: View the public profile to load the stored malicious HTML, then interact with the payload to execute JavaScript in the victim's browser.

**Instructions**: Log out or use an incognito window to simulate a victim. Navigate to the attacker's public profile URL. Locate the recommendation section, find the "Click Here" link in the description, and click it to trigger the data URI payload.

**Expected Output**: An alert box pops up displaying "XSS", confirming JavaScript execution. In a real attack, this could be replaced with phishing or data theft code.

**Success Indicators**:
- JavaScript executes without browser errors
- Alert or other payload effect is observed on click

## Attack Chain Summary

### Key Achievements

1. Successful injection of unsanitized HTML into the recommendation description field
2. Persistence of the payload on the public profile without detection
3. Arbitrary JavaScript execution on any viewer who interacts with the link, enabling phishing, session hijacking, or data theft

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
