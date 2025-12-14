---
tags:
  - idor
  - web
  - financial-data
  - access-control
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-IDOR-in-Starbucks-Card-Balance]]'
step_count: 4
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:30.031Z'
description: >-
  Multi-stage attack exploiting an Insecure Direct Object Reference (IDOR)
  vulnerability in the Starbucks Thailand card balance system to access
  sensitive financial data of other users' cards via URL manipulation.
skill_level: low
impact_level: medium
id: df7c4a97-6b07-4419-adcb-a1582c63cf12
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# IDOR in Starbucks Thailand Card System to View Unauthorized Card Balances

Multi-stage attack chain demonstrating a complete workflow to exploit an IDOR vulnerability in the Starbucks Thailand card management system, allowing unauthorized viewing of other users' card balances by manipulating URL parameters.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Low |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Perform Balance Transfer] --> B[Identify URL Parameter]
    B --> C[Modify URL Parameter]
    C --> D[View Unauthorized Balance]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome with developer tools)

### Target Environment

- Web platform
- Starbucks Thailand card system at www.starbuckscardth.in.th
- No specific ports or services beyond standard HTTPS

### Initial Access Requirements

- Valid logged-in account with at least two registered Starbucks Thailand cards
- Knowledge of another valid Starbucks Thailand card number (e.g., from public sources or testing)
- Network access to the internet

## Detailed Attack Procedures

### Step 1: Perform Balance Transfer
procedure: [[procedures/Exploit-IDOR-in-Starbucks-Card-Balance]]

**Objective**: Initiate a legitimate balance transfer between two of your own registered cards to generate a URL containing the target card reference.

**Instructions**: Log in to www.starbuckscardth.in.th and navigate to the balance transfer feature. Select your first card as the source and a second registered card as the destination, then complete the transfer.

**Expected Output**: Successful transfer confirmation page or URL that references the second card's details.

**Success Indicators**:
- Balance transfer completes without errors
- URL or endpoint displays the second card's balance

### Step 2: Identify URL Parameter
procedure: [[procedures/Exploit-IDOR-in-Starbucks-Card-Balance]]

**Objective**: Examine the post-transfer URL or page to locate the parameter holding the card number.

**Instructions**: After the transfer, inspect the browser's address bar or use developer tools (F12) to view the network requests or page source. Look for a query parameter like ?card= or /card/{number} that contains the second card's number.

**Expected Output**: Identification of the vulnerable parameter, e.g., a URL like https://www.starbuckscardth.in.th/balance?card=1234567890123456.

**Success Indicators**:
- Parameter clearly references the card number
- No additional authentication tokens tied to ownership

### Step 3: Modify URL Parameter
procedure: [[procedures/Exploit-IDOR-in-Starbucks-Card-Balance]]

**Objective**: Alter the card number parameter to point to an unauthorized card while staying logged in.

**Instructions**: Copy the identified URL, replace the card number value with a known different valid Thailand Starbucks card number, and ensure you remain authenticated (session cookie intact).

**Expected Output**: Modified URL ready for submission, e.g., https://www.starbuckscardth.in.th/balance?card=9876543210987654.

**Success Indicators**:
- URL updates without session invalidation
- Browser accepts the change

### Step 4: Access and View Balance
procedure: [[procedures/Exploit-IDOR-in-Starbucks-Card-Balance]]

**Objective**: Submit the modified request to retrieve and display the unauthorized card's balance.

**Instructions**: Paste the modified URL into the browser and load the page. The system will fetch and show the balance without verifying ownership.

**Expected Output**: Display of the target card's balance information, confirming unauthorized access.

**Success Indicators**:
- Balance data loads successfully
- No access denied errors or redirects

## Attack Chain Summary

### Key Achievements

1. Successful manipulation of URL parameter to bypass access controls
2. Unauthorized viewing of sensitive financial data (card balances)
3. Demonstration of privacy violation without needing advanced tools

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
