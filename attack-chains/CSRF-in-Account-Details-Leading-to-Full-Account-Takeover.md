---
tags:
  - csrf
  - account-takeover
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Lateral Movement]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Craft-and-Deliver-CSRF-Payload-for-Account-Modification]]'
  - '[[procedures/Verify-Account-Modification-via-CSRF]]'
  - '[[procedures/Exploit-Password-Reset-for-Account-Takeover]]'
step_count: 6
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:58.275Z'
description: >-
  A multi-stage attack exploiting a CSRF vulnerability in the account details
  section to modify user email and username, followed by password reset to
  achieve full account takeover.
skill_level: intermediate
impact_level: high
id: e1181c33-fcc1-416b-b443-ea282ec9216e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Valid Accounts]]'
---
# CSRF in Account Details Leading to Full Account Takeover

Multi-stage attack chain demonstrating a complete workflow for account takeover via CSRF exploitation in a web application's account details feature.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Victim Authentication] --> B[CSRF Payload Delivery]
    B --> C[Account Details Modification]
    C --> D[Anonymous Password Reset Request]
    D --> E[Reset Link Exploitation]
    E --> F[Full Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (relies on HTML crafting and browser simulation)

### Target Environment

- Web application with account management features
- No CSRF protection on POST endpoints for account updates
- Password reset functionality tied to email

### Initial Access Requirements

- Victim must be authenticated in the target application
- Ability to trick victim into opening a malicious HTML file (e.g., via phishing or shared link)
- Attacker's email address for reset linkage

## Detailed Attack Procedures

### Step 1: Victim Authentication and Initial Account Check
procedure: [[procedures/Craft-and-Deliver-CSRF-Payload-for-Account-Modification]]

**Objective**: Ensure the victim is logged in and verify current account details to establish baseline.

**Instructions**: Have the victim log in to the target web application. Navigate to the 'Account details' section to view and note the current email and username.

**Expected Output**: Display of victim's original email and username.

**Success Indicators**:
- Victim is authenticated
- Baseline account details are visible and recorded

### Step 2: Deliver and Execute CSRF Payload
procedure: [[procedures/Craft-and-Deliver-CSRF-Payload-for-Account-Modification]]

**Objective**: Trick the victim into loading a malicious HTML page that submits a forged POST request to modify account details.

**Instructions**: Craft an HTML file with an auto-submitting form targeting the account details POST endpoint (e.g., /account/details). URL-encode special characters like '@' in the email as '%40'. Host or deliver the file to the victim (e.g., via email attachment or link). Instruct the victim to open it while authenticated.

Example HTML payload:

```html
<!DOCTYPE html>
<html>
<body>
<form action="https://█████████/account/details" method="POST" id="csrf-form">
    <input type="hidden" name="email" value="attacker@example.com">
    <input type="hidden" name="username" value="attacker_user">
</form>
<script>document.getElementById('csrf-form').submit();</script>
</body>
</html>
```

**Expected Output**: Silent form submission updating the account.

**Success Indicators**:
- No visible errors on the malicious page
- Victim remains unaware of the change

### Step 3: Verify Account Modification
procedure: [[procedures/Verify-Account-Modification-via-CSRF]]

**Objective**: Confirm that the CSRF attack successfully altered the victim's email and username to the attacker's values.

**Instructions**: After the victim interacts with the malicious file, have them revisit the 'Account details' section in the application.

**Expected Output**: Updated email and username matching attacker's details.

**Success Indicators**:
- Email changed to attacker's email
- Username overwritten with attacker's username

### Step 4: Simulate Anonymous Access
procedure: [[procedures/Exploit-Password-Reset-for-Account-Takeover]]

**Objective**: Ensure the attacker operates without prior session to mimic external takeover.

**Instructions**: Log out of any existing sessions or use an incognito/private browser window to access the login page anonymously.

**Expected Output**: Clean login interface without authentication.

**Success Indicators**:
- No active session interference
- Access to public features like password reset

### Step 5: Request Password Reset
procedure: [[procedures/Exploit-Password-Reset-for-Account-Takeover]]

**Objective**: Use the modified email to initiate a password reset, directing the link to the attacker.

**Instructions**: On the login page, select the 'Forgot password' option and enter the attacker's email (now associated with the victim's account).

**Expected Output**: Password reset request processed, email sent to attacker's inbox.

**Success Indicators**:
- Confirmation message for reset initiation
- Email received in attacker's mailbox

### Step 6: Complete Takeover with Reset Link
procedure: [[procedures/Exploit-Password-Reset-for-Account-Takeover]]

**Objective**: Use the reset link to set a new password and gain full control of the account.

**Instructions**: Open the reset link from the email, follow the prompts to set a new password, then log in with the new credentials.

**Expected Output**: Successful login and access to the victim's account.

**Success Indicators**:
- New password accepted
- Full access to account features and data

## Attack Chain Summary

### Key Achievements

1. Unauthorized modification of account details via CSRF without user awareness
2. Redirection of password reset to attacker's control
3. Complete takeover of the victim's account for potential data exfiltration or further abuse

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Drive-by Compromise]] Drive-by Compromise
- [[Valid Accounts]] Valid Accounts

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Lateral Movement]] Lateral Movement

---
*Last updated: 2023-10-01T00:00:00Z*
