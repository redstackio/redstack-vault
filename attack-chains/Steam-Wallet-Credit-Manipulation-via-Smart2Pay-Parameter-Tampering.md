---
tags:
  - parameter-tampering
  - hash-weakness
  - payment-fraud
  - steam
  - smart2pay
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Prepare-Email-for-Parameter-Injection]]'
  - '[[procedures/Initiate-Steam-Payment-with-Smart2Pay]]'
  - '[[procedures/Intercept-Smart2Pay-POST-Request]]'
  - '[[procedures/Modify-Request-Parameters-for-Tampering]]'
  - '[[procedures/Complete-Tampered-Payment-Transaction]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1659]]'
description: >-
  Exploitation of weak hash signature in Smart2Pay payment requests allowing
  parameter tampering to credit arbitrary amounts to Steam wallet while paying
  less
skill_level: intermediate
impact_level: high
id: c130bf60-7139-4d14-95fb-7506d9399536
created_at: '2025-12-11T06:10:15.798Z'
updated_at: '2025-12-11T06:10:15.798Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1190]]'
  - '[[T1659]]'
---
# Steam Wallet Credit Manipulation via Smart2Pay Parameter Tampering

Multi-stage attack chain demonstrating exploitation of a weak hash in Smart2Pay payment processing for Steam, allowing attackers to tamper with payment amounts via email injection, resulting in crediting large wallet balances for minimal payments.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Prepare Email] --> B[Initiate Payment]
    B --> C[Intercept Request]
    C --> D[Modify Parameters]
    D --> E[Complete Transaction]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform
- Required services: Steam, Smart2Pay
- Network access requirements: Access to Steam store and ability to intercept HTTPS traffic

### Initial Access Requirements

- Valid Steam account
- Network position: Client-side with proxy capability
- Prior access needed: Ability to change Steam account email

## Detailed Attack Procedures

### Step 1: Prepare Email for Parameter Injection - [[procedures/Prepare-Email-for-Parameter-Injection]]

**Objective**: Set up the Steam account email to enable injection of tampering parameters in the payment request.

**Expected Output**: Email changed to a format that allows splitting to inject fields like 'amount'.

**Success Indicators**:
- Email successfully updated in Steam account settings
- Format verified as injectable (e.g., 'brixamount100abc@domain')

### Step 2: Initiate Steam Payment with Smart2Pay - [[procedures/Initiate-Steam-Payment-with-Smart2Pay]]

**Objective**: Navigate to the Steam add funds page and select a Smart2Pay payment method to trigger the vulnerable request.

**Expected Output**: Payment process initiated, leading to the POST request to Smart2Pay.

**Success Indicators**:
- Reached the payment selection page
- Selected Przelewy24 or similar Smart2Pay method

### Step 3: Intercept Smart2Pay POST Request - [[procedures/Intercept-Smart2Pay-POST-Request]]

**Objective**: Use a proxy tool to capture the HTTP POST request sent to the Smart2Pay API during the payment process.

Use [[tools/Burp-Suite]] to intercept the request:

```http
POST / HTTPS/1.1
Host: globalapi.smart2pay.com
Content-Type: application/x-www-form-urlencoded

MerchantID=...&Amount=...&CustomerEmail=...
```

**Expected Output**: Captured request with fields like MerchantID, Amount, CustomerEmail, and Hash.

**Success Indicators**:
- Request intercepted successfully
- All parameters visible for analysis

### Step 4: Modify Request Parameters for Tampering - [[procedures/Modify-Request-Parameters-for-Tampering]]

**Objective**: Alter the intercepted request to inject a new 'amount' field via the email parameter while preserving the hash validity.

Use [[tools/Burp-Suite]] to modify the parameters:

Change 'Amount=2000' to 'Amount2=000'; modify 'CustomerEmail=brixamount100abc%40domain' to 'CustomerEmail=brix&amount=100&ab=c%40domain'.

**Expected Output**: Tampered request that injects the desired amount while keeping the concatenated string valid for the hash.

**Success Indicators**:
- Hash remains unchanged and valid
- Injected 'amount=100' appears in the parsed parameters

### Step 5: Complete Tampered Payment Transaction - [[procedures/Complete-Tampered-Payment-Transaction]]

**Objective**: Proceed with the modified payment to credit the injected amount to the Steam wallet.

**Expected Output**: Small payment (e.g., $1) processed, but larger amount (e.g., $100) credited.

**Success Indicators**:
- Transaction completes successfully
- Steam wallet balance reflects the injected amount

## Attack Chain Summary

### Key Achievements

1. Successful tampering of payment amount without invalidating the hash
2. Crediting arbitrary funds to Steam wallet with minimal payment
3. Potential for financial loss to Steam and market disruption

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[T1659]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

*Last updated: 2023-10-01*
