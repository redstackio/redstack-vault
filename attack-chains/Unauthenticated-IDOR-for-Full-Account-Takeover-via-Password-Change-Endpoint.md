---
tags:
  - idor
  - account-takeover
  - web-vulnerability
  - dod
  - unauthenticated
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Setup-Burp-Suite-and-Load-Request]]'
  - '[[procedures/Modify-Request-for-IDOR-Exploitation]]'
  - '[[procedures/Execute-Account-Takeover-Request]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:33:11.905Z'
description: >-
  An unauthenticated Insecure Direct Object Reference (IDOR) vulnerability
  allowing attackers to change any user's password, leading to complete account
  takeover in a DoD web application.
skill_level: intermediate
impact_level: high
id: 411df3fb-649f-4122-87db-34fc29a3fa5a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Manipulation]]'
---
---

# Unauthenticated IDOR for Full Account Takeover via Password Change Endpoint

Multi-stage attack chain demonstrating a complete attack workflow for exploiting an unauthenticated IDOR in a DoD web application's password change functionality, enabling arbitrary account takeover.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Burp Suite] --> B[Modify Request for IDOR] --> C[Execute Takeover]
    A -->|Capture and Load| B
    B -->|Target User ID| C
    C --> D[Account Compromised]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web application (DoD system)
- Access to unauthenticated password change endpoint
- Victim's user ID and email (email from prior enumeration, e.g., report #1004745)

### Initial Access Requirements

- No credentials required (unauthenticated)
- Network access to the target web application
- No prior access needed

## Detailed Attack Procedures

### Step 1: Setup Burp Suite and Load Request
procedure: [[procedures/Setup-Burp-Suite-and-Load-Request]]

**Objective**: Launch Burp Suite, configure for request interception, and load a captured unauthenticated password change request into the Repeater for modification.

**Instructions**: Install and open Burp Suite if not already running. Switch to the Repeater tab to prepare for request manipulation. Paste the content of a previously captured HTTP request (a POST to the password change endpoint) into the Repeater. This request is typically obtained by intercepting an unauthenticated attempt to change one's own password or from an attachment in the vulnerability report.

**Expected Output**: The raw HTTP request loaded in Burp Repeater, ready for editing, showing headers like Cookie: UID2=... and body parameters like userName and password.

**Success Indicators**:
- Burp Suite Repeater tab active with request loaded
- Request details visible, including UID2 cookie and userName parameter

### Step 2: Modify Request for IDOR Exploitation
procedure: [[procedures/Modify-Request-for-IDOR-Exploitation]]

**Objective**: Alter the request to target a victim's account by replacing the user ID in the cookie and setting the username to the victim's email, exploiting the IDOR to bypass authorization.

**Instructions**: In the Burp Repeater, edit the Cookie header to change the UID2 value from the current user ID (e.g., UID2=4820041) to the target victim's user ID (obtained from prior testing or enumeration). Then, update the userName parameter in the request body to the victim's email address (sourced from related enumeration report #1004745). Ensure the new password field is set to the desired value for the takeover.

**Expected Output**: Modified HTTP request with updated UID2 cookie and userName parameter reflecting the target victim.

**Success Indicators**:
- Cookie UID2 updated to victim's ID
- Request body userName set to victim's email
- No syntax errors in the modified request

### Step 3: Execute Account Takeover Request
procedure: [[procedures/Execute-Account-Takeover-Request]]

**Objective**: Send the modified request to change the victim's password, achieving full account takeover without authentication.

**Instructions**: In Burp Repeater, click 'Send' to transmit the modified POST request to the password change endpoint. Monitor the response for success indicators, such as a 200 OK status or confirmation message indicating the password update.

**Expected Output**: Server response confirming password change (e.g., JSON success message or redirect), allowing subsequent login with the new password.

**Success Indicators**:
- HTTP 200 response or success status
- Ability to login to victim's account with new password
- Confirmation of access to sensitive DoD data

## Attack Chain Summary

### Key Achievements

1. Bypassed authentication via IDOR in UID2 cookie
2. Changed arbitrary user's password without credentials
3. Achieved full account takeover, compromising DoD accounts

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Account Manipulation]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Persistence]]

---

*Last updated: 2023-10-01T00:00:00Z*
