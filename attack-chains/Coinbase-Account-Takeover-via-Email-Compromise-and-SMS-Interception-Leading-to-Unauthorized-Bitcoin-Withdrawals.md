---
id: ac-coinbase-2fa-takeover-16696
tags:
  - account-takeover
  - 2fa-bypass
  - sms-interception
  - email-compromise
  - coinbase
  - cryptocurrency-theft
type: attack_chain
tools:
  - '[[tools/Authy]]'
  - '[[tools/ATT-Text-to-Web]]'
tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
  - '[[Defense Evasion]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Compromise-Email-Account-for-Initial-Access]]'
  - '[[procedures/Manipulate-Telecom-Account-to-Intercept-SMS]]'
  - '[[procedures/Switch-Coinbase-2FA-to-SMS-via-Intercepted-Codes]]'
  - '[[procedures/Execute-Fraudulent-Bitcoin-Withdrawals-on-Coinbase]]'
step_count: 4
techniques:
  - '[[Valid Accounts]]'
  - '[[Adversary-in-the-Middle]]'
  - '[[Reversible Encryption]]'
  - '[[Data from Cloud Storage]]'
updated_at: '2025-12-14T17:24:45.425Z'
description: >-
  Multi-stage attack exploiting email compromise, SMS interception via telecom
  manipulation, and lack of 2FA change safeguards on Coinbase to enable
  immediate unauthorized cryptocurrency withdrawals.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
  - '[[Defense Evasion]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Adversary-in-the-Middle]]'
  - '[[Reversible Encryption]]'
  - '[[Data from Cloud Storage]]'
---
# Coinbase Account Takeover via Email Compromise and SMS Interception Leading to Unauthorized Bitcoin Withdrawals

Multi-stage attack chain demonstrating a complete account takeover workflow on Coinbase, exploiting interconnected services like email, telecom (ATT), and 2FA systems to steal cryptocurrency without delays or freezes on withdrawals.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~Several days (due to research and staging) |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Email Compromise] --> B[SMS Interception via ATT]
    B --> C[2FA Switch on Coinbase]
    C --> D[Fraudulent Withdrawals]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Authy]]
- [[tools/ATT-Text-to-Web]]

### Target Environment

- Web-based services: Email providers, ATT telecom account, Coinbase exchange
- Required services/ports: Standard HTTPS (443) for web access
- Network access requirements: Internet connectivity to compromised email and telecom portals

### Initial Access Requirements

- Credential requirements: Valid login to target's email (phished or breached)
- Network position: External attacker with no prior internal access
- Prior access needed: None, but knowledge of target's linked accounts

## Detailed Attack Procedures

### Step 1: Initial Access
procedure: [[procedures/Compromise-Email-Account-for-Initial-Access]]

**Objective**: Gain access to the target's email to enable resets and reconnaissance on linked accounts.

**Instructions**: Use compromised credentials to log into the email account and monitor inboxes for several days to identify linked services like ATT and Coinbase. Read emails to gather passwords, recovery options, and account details.

**Expected Output**: Full access to email inbox, including historical data for staging further attacks.

**Success Indicators**:
- Ability to read and send emails from the account
- Identification of linked financial services like Coinbase

### Step 2: Execution
procedure: [[procedures/Manipulate-Telecom-Account-to-Intercept-SMS]]

**Objective**: Compromise the telecom account to enable real-time interception of SMS-based authentication codes.

**Instructions**: Using email access, reset the ATT account password. Once logged in, enable 'Text to Web' feature and call forwarding to redirect SMS to an attacker-controlled viewable web page.

**Expected Output**: All incoming SMS visible online, including 2FA codes sent to the target's phone.

**Success Indicators**:
- Successful login to ATT account
- Confirmation of SMS redirection and visibility

### Step 3: Privilege Escalation
procedure: [[procedures/Switch-Coinbase-2FA-to-SMS-via-Intercepted-Codes]]

**Objective**: Take over the Coinbase account by switching 2FA methods, leveraging intercepted codes.

**Instructions**: Reset Coinbase password using compromised email. Re-sync Authy on the attacker's device to invalidate the target's tokens, then use intercepted SMS codes to change 2FA from Authy to SMS without any platform-enforced delays.

**Expected Output**: Control over Coinbase 2FA, allowing authenticated sessions.

**Success Indicators**:
- 2FA method successfully changed to SMS
- No freezes or alerts triggered on the account

### Step 4: Objective
procedure: [[procedures/Execute-Fraudulent-Bitcoin-Withdrawals-on-Coinbase]]

**Objective**: Drain funds by performing unauthorized withdrawals immediately after takeover.

**Instructions**: Authenticate withdrawals using intercepted SMS codes for two transactions totaling $999.45 (e.g., $666.28 and $333.17), exploiting the $1,000 daily limit and lack of post-2FA-change safeguards.

**Expected Output**: Bitcoin transferred out of the account to attacker-controlled wallets.

**Success Indicators**:
- Successful completion of withdrawal transactions
- Funds moved without interruption or reversal

## Attack Chain Summary

### Key Achievements

1. Full account takeover via chained compromises of email and telecom services
2. Bypass of app-based 2FA by switching to interceptable SMS without delays
3. Immediate exfiltration of $1,000 in Bitcoin, demonstrating high financial impact

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Adversary-in-the-Middle]] Adversary-in-the-Middle
- [[Reversible Encryption]] Multi-Factor Authentication Instrument
- [[Data from Cloud Storage]] Data from Cloud Storage Accounts

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Credential Access]] Credential Access
- [[Defense Evasion]] Defense Evasion
- [[Collection]] Collection

---
*Last updated: 2023-10-01T00:00:00Z*
