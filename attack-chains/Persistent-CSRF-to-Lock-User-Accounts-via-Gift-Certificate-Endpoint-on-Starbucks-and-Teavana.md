---
id: ac-csrf-giftcert-lockout
tags:
  - csrf
  - web
  - ecommerce
  - account-lockout
  - demandware
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-GiftCert-Purchase-Endpoint]]'
  - '[[procedures/Identify-Lack-of-CSRF-Protection]]'
  - '[[procedures/Test-Impact-of-Adding-Gift-Certificate]]'
  - '[[procedures/Create-and-Test-CSRF-POC]]'
  - '[[procedures/Verify-CSRF-on-Other-Sites]]'
step_count: 5
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:42.825Z'
description: >-
  A multi-stage CSRF attack exploiting the lack of protection on the
  GiftCert-AddToBasket endpoint to add unwanted gift certificates to a user's
  cart, preventing purchases and causing account lockout.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
---
# Persistent CSRF to Lock User Accounts via Gift Certificate Endpoint on Starbucks and Teavana

Multi-stage attack chain demonstrating a complete CSRF workflow to exploit unprotected endpoints on Teavana and Starbucks eCommerce sites, leading to persistent cart modifications and user account disruption.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Endpoint Discovery] --> B[CSRF Validation Check]
    B --> C[Impact Testing]
    C --> D[POC Development]
    D --> E[Cross-Site Verification]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
    style E fill:#9b59b6
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools for inspection
- Text editor for HTML POC creation

### Target Environment

- Web platform
- Demandware (Salesforce Commerce Cloud) eCommerce sites
- No specific ports; HTTP/HTTPS access required

### Initial Access Requirements

- Ability to create a malicious webpage (e.g., hosted on attacker-controlled domain)
- Target user must be authenticated on the victim site
- No prior credentials needed for discovery

## Detailed Attack Procedures

### Step 1: Endpoint Discovery
procedure: [[procedures/Discover-GiftCert-Purchase-Endpoint]]

**Objective**: Identify the vulnerable GiftCert-Purchase endpoint by searching for hidden links in Demandware domains.

**Instructions**: Use browser inspection or manual searching to locate the endpoint http://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/GiftCert-Purchase, which allows adding custom gift cards valued between 5 and 5000 to the cart without authentication.

**Expected Output**: Confirmation of the endpoint URL and its functionality to add items to cart.

**Success Indicators**:
- Endpoint URL retrieved
- Ability to add gift card via direct access confirmed

### Step 2: CSRF Protection Check
procedure: [[procedures/Identify-Lack-of-CSRF-Protection]]

**Objective**: Verify the absence of CSRF tokens or validation on the endpoint.

**Instructions**: Inspect the POST request to /GiftCert-AddToBasket and observe no requirement for CSRF tokens, allowing unauthorized submissions.

**Expected Output**: Successful POST without tokens, adding item to cart.

**Success Indicators**:
- Request succeeds without CSRF token
- Cart modified via external request

### Step 3: Impact Assessment
procedure: [[procedures/Test-Impact-of-Adding-Gift-Certificate]]

**Objective**: Evaluate the persistent effects of adding a gift certificate to the cart.

**Instructions**: Manually submit a POST to add a gift card, then attempt to empty the cart, use credit card payments, and log out/in to check persistence.

**Expected Output**: Cart cannot be emptied; credit card option disappears; issue persists across sessions for weeks.

**Success Indicators**:
- Payment options locked
- Cart item remains after logout/login

### Step 4: POC Development and Testing
procedure: [[procedures/Create-and-Test-CSRF-POC]]

**Objective**: Build and validate a malicious HTML form to exploit the CSRF.

**Instructions**: Create an HTML page with a form posting to the endpoint with parameters like dwfrm_giftcert_purchase_amount=100 and dwfrm_giftcert_purchase_recipientEmail=valid@iamvalid.com. Host it and trick a logged-in user into visiting/submitting.

**Expected Output**: Gift certificate added to victim's cart, locking purchases.

**Success Indicators**:
- Victim's cart modified remotely
- Attacker receives gift card email if specified

### Step 5: Cross-Site Verification
procedure: [[procedures/Verify-CSRF-on-Other-Sites]]

**Objective**: Confirm the vulnerability on related sites like Starbucks.

**Instructions**: Test the same POST on https://store.starbucks.com/on/demandware.store/Sites-Starbucks-Site/default/Sites-Teavana-Site/default/GiftCert-Purchase.

**Expected Output**: Similar cart lockout behavior observed.

**Success Indicators**:
- Vulnerability replicated on Starbucks site
- Consistent impact across platforms

## Attack Chain Summary

### Key Achievements

1. Discovered unprotected GiftCert endpoint allowing cart manipulation.
2. Confirmed persistent account lockout via CSRF.
3. Developed exploitable POC for remote execution.
4. Verified impact on multiple eCommerce sites.
5. Demonstrated financial and usability disruption.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Drive-by Compromise]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
