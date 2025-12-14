---
tags:
  - broken-access-control
  - idor
  - api
  - mobile
  - pii-disclosure
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
  - '[[Collection]]'
verified: false
platforms:
  - Mobile (iOS)
  - Web API
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Log-into-MyMTN-NG-App]]'
  - '[[procedures/Intercept-Mobile-API-Traffic-with-Proxy]]'
  - '[[procedures/Capture-Recharge-Transaction-History-Request]]'
  - '[[procedures/Modify-customer_id-to-Access-Other-Users-Data]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:30:35.198Z'
description: >-
  Multi-stage attack exploiting broken access control in the MyMTN NG mobile app
  API to disclose other users' recharge transaction history via unauthorized
  customer_id manipulation.
skill_level: intermediate
impact_level: high
id: 570dd2f0-f56e-4513-9507-5a876ac8fd2f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# Broken Access Control in MyMTN NG API Leading to Transaction History Disclosure

Multi-stage attack chain demonstrating a complete attack workflow exploiting insufficient authorization in the MyMTN NG mobile app's /api/v2/rechargeTransactionHistory endpoint. By intercepting and modifying API requests, an attacker can view sensitive transaction details of any MTN customer, including recharge dates, amounts, transaction IDs, and subscriber IDs, resulting in PII disclosure.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Log into App] --> B[Setup Proxy and Intercept Traffic]
    B --> C[Capture Transaction Request]
    C --> D[Modify customer_id and Retrieve Data]
    D --> E[Data Exfiltration]

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

- Mobile (iOS) app: MyMTN NG
- Web API: MyMTN NG API over HTTP/2 with JSON payloads
- Required services/ports: API endpoint accessible via mobile network (typically port 443 for HTTPS)
- Network access requirements: Valid MTN SIM card for initial login; proxy setup on device or emulator

### Initial Access Requirements

- Credential requirements: Valid MTN phone number (MSISDN) for app login
- Network position: Attacker must have physical access to iOS device or use emulator
- Prior access needed: None, but app installation required

## Detailed Attack Procedures

### Step 1: Log into MyMTN NG App
procedure: [[procedures/Log-into-MyMTN-NG-App]]

**Objective**: Authenticate to the app to access user-specific features and trigger API calls.

**Instructions**: Install the MyMTN NG app on an iOS device, enter your MTN phone number, and complete the authentication process via OTP or similar.

**Expected Output**: Successful login, granting access to sections like transaction history.

**Success Indicators**:
- App dashboard loads with user data
- API calls begin authenticating with your MSISDN

### Step 2: Setup Proxy and Intercept Traffic
procedure: [[procedures/Intercept-Mobile-API-Traffic-with-Proxy]]

**Objective**: Configure a proxy to capture HTTPS traffic from the app, bypassing SSL pinning.

**Instructions**: Launch Burp Suite, configure the iOS device proxy settings to point to Burp's listener (e.g., IP:8080), and install Burp's CA certificate on the device. Use a tool like Objection or Frida to bypass SSL pinning if needed.

**Expected Output**: Proxy intercepts app traffic without errors.

**Success Indicators**:
- HTTPS requests visible in Burp
- No certificate validation errors in app

### Step 3: Capture Recharge Transaction History Request
procedure: [[procedures/Capture-Recharge-Transaction-History-Request]]

**Objective**: Navigate to transaction history to trigger and intercept the API request.

**Instructions**: In the app, go to the transaction history section, selecting a date range. Intercept the POST request to /api/v2/rechargeTransactionHistory in Burp, noting the JSON payload with customer_id (your MSISDN), start_date, and end_date.

**Expected Output**: Intercepted request showing payload like {"customer_id": "2347032233323", "start_date": "2023-01-01", "end_date": "2023-10-01"}.

**Success Indicators**:
- Request captured with valid JSON
- Response returns your own transaction history

### Step 4: Modify customer_id and Retrieve Data
procedure: [[procedures/Modify-customer_id-to-Access-Other-Users-Data]]

**Objective**: Alter the customer_id to a target MTN number and forward the request to disclose unauthorized data.

**Instructions**: In Burp, edit the customer_id in the JSON payload to a different valid MTN number (e.g., change from "2347032233323" to "2348063223665"), then forward the request. Review the response for transaction details.

**Expected Output**: JSON response with target user's data, including rechargeDate, amountBefore, amountAfter, transactionId, subscriberId.

**Success Indicators**:
- Response contains data for the modified customer_id
- No authorization errors; full transaction history disclosed

## Attack Chain Summary

### Key Achievements

1. Successful authentication and proxy setup for mobile API interception
2. Capture and modification of sensitive API request without validation
3. Disclosure of PII for arbitrary MTN customers, enabling privacy violations and potential fraud

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
