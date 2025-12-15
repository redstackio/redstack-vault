---
id: ac-openmage-idor-dos-001
tags:
  - idor
  - dos
  - web
  - php
  - openmage
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-User-Accounts-and-Addresses-in-OpenMage]]'
  - '[[procedures/Capture-and-Modify-Address-Edit-Request-with-Burp-Suite]]'
  - '[[procedures/Automate-IDOR-Exploitation-for-DoS-with-Burp-Intruder]]'
step_count: 8
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:25:33.620Z'
description: >-
  A multi-stage attack exploiting an Insecure Direct Object Reference (IDOR) in
  the OpenMage demo application's address editing feature to create unauthorized
  addresses on the attacker's account and escalate to resource exhaustion
  causing Denial of Service (DoS).
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
---
# IDOR in OpenMage Address Editing Leading to Unauthorized Address Creation and DoS

Multi-stage attack chain demonstrating exploitation of an IDOR vulnerability in the OpenMage demo site to bypass authorization checks during address editing, resulting in unauthorized address creation on the attacker's account, and further automation to cause server resource exhaustion and DoS.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 8 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Account Setup] --> B[IDOR Exploitation]
    B --> C[Automation and DoS]
    C --> D[Resource Exhaustion]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform
- OpenMage e-commerce application (PHP-based)
- Access to demo.openmage.org or similar instance
- No specific ports required beyond standard HTTP/HTTPS (80/443)

### Initial Access Requirements

- Ability to register user accounts
- Network access to the target site
- Burp Suite configured as proxy for traffic interception

## Detailed Attack Procedures

### Step 1: Create User Accounts
procedure: [[procedures/Create-User-Accounts-and-Addresses-in-OpenMage]]

**Objective**: Establish two separate user accounts to simulate attacker and victim scenarios for IDOR testing.

**Instructions**: Navigate to the registration page on demo.openmage.org and create two accounts using distinct email addresses, such as attacker@example.com and victim@example.com. Complete the registration process for each.

**Expected Output**: Successful account creation with login credentials for both users.

**Success Indicators**:
- Confirmation emails or success messages for registrations
- Ability to log in to both accounts

### Step 2: Add Addresses to Accounts
procedure: [[procedures/Create-User-Accounts-and-Addresses-in-OpenMage]]

**Objective**: Populate each account with at least one address to obtain valid address IDs for exploitation.

**Instructions**: Log in to each account separately, navigate to the address management section, and add sample addresses (e.g., street, city, zip code) for both the attacker and victim accounts. Save the addresses to generate unique IDs.

**Expected Output**: Addresses listed in the account dashboard with assigned IDs (e.g., address_id=123).

**Success Indicators**:
- Addresses visible and editable in each account
- Note the address IDs from the victim account for later use

### Step 3: Capture Address Edit Request
procedure: [[procedures/Capture-and-Modify-Address-Edit-Request-with-Burp-Suite]]

**Objective**: Intercept a legitimate address edit request from the attacker's account to understand the request structure.

**Instructions**: Configure Burp Suite proxy to intercept traffic from your browser. Log in as the attacker, attempt to edit an address on account 1, and capture the HTTP GET request in Burp. Forward the request to the Repeater tab for analysis.

**Expected Output**: Captured HTTP request showing parameters like address_id in the URL and Referer header.

**Success Indicators**:
- Request visible in Burp Repeater
- Parameters including address_id identified

### Step 4: Modify Request with Victim's Address ID
procedure: [[procedures/Capture-and-Modify-Address-Edit-Request-with-Burp-Suite]]

**Objective**: Alter the request to reference a victim's address ID, testing for IDOR bypass.

**Instructions**: In Burp Repeater, replace the address_id parameter in the GET URL (e.g., /edit/address_id=123 to /edit/address_id=456 where 456 is victim's ID). Also update the Referer header to match the new ID. Ensure the request is sent from the attacker's session.

**Expected Output**: Server response indicating a new address created on attacker's account instead of an access denied error.

**Success Indicators**:
- New address appears in attacker's account with a different ID
- No authorization error thrown

### Step 5: Submit Modified Request
procedure: [[procedures/Capture-and-Modify-Address-Edit-Request-with-Burp-Suite]]

**Objective**: Confirm the IDOR allows unauthorized address duplication.

**Instructions**: Send the modified request via Burp Repeater and verify the outcome by checking the attacker's address list.

**Expected Output**: Successful creation of a duplicate address on the attacker's account.

**Success Indicators**:
- Attacker's account now has the victim's address data as a new entry
- HTTP 200 response with success message

### Step 6: Configure Burp Intruder for Automation
procedure: [[procedures/Automate-IDOR-Exploitation-for-DoS-with-Burp-Intruder]]

**Objective**: Set up automated fuzzing using the victim's address ID and a null byte payload to exploit the IDOR repeatedly.

**Instructions**: From the captured request in Repeater, send to Intruder. Mark the address_id position as a payload position. Set the payload type to a single null byte (%00) or simple string, and configure to use the victim's ID as base.

**Expected Output**: Intruder configuration ready with payload positions set.

**Success Indicators**:
- Payload positions highlighted in the request
- Test run completes without errors

### Step 7: Launch Automated Attack
procedure: [[procedures/Automate-IDOR-Exploitation-for-DoS-with-Burp-Intruder]]

**Objective**: Flood the server with rapid requests to create excessive addresses and exhaust resources.

**Instructions**: Start the Intruder attack with at least 60 concurrent threads. Monitor the attack progress, targeting the address editing endpoint repeatedly.

**Expected Output**: Multiple rapid requests sent, leading to numerous new addresses on the attacker's account.

**Success Indicators**:
- High request rate observed in Burp
- Server responses initially successful, then degrading

### Step 8: Observe DoS Impact
procedure: [[procedures/Automate-IDOR-Exploitation-for-DoS-with-Burp-Intruder]]

**Objective**: Verify resource exhaustion resulting in service unavailability.

**Instructions**: Continue the attack and monitor the target site for errors. Check the attacker's account for flooded addresses and the site for overall responsiveness.

**Expected Output**: HTTP 503 Service Unavailable errors; site becomes unresponsive.

**Success Indicators**:
- 503 errors in responses
- Excessive addresses (hundreds) in attacker's account
- Site downtime observed

## Attack Chain Summary

### Key Achievements

1. Bypassed authorization via IDOR to create unauthorized addresses
2. Automated exploitation to generate resource-intensive operations
3. Achieved DoS through server overload on the demo site

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Network Denial of Service]] Network Denial of Service

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Impact]] Impact

---

*Last updated: 2023-10-01T00:00:00Z*
