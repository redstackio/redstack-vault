---
tags:
  - idor
  - pii-leak
  - brute-force
  - web-vulnerability
  - unauthorized-access
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Foxy-Proxy]]'
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
  - ASP.NET Core
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-IDOR-for-Victim-PII-Access]]'
  - '[[procedures/Exploit-IDOR-for-Contact-Deletion]]'
  - '[[procedures/Brute-Force-Authentication-Endpoints]]'
step_count: 10
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Brute Force]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:25:29.310Z'
description: >-
  A multi-stage attack exploiting Insecure Direct Object Reference (IDOR) in a
  web application's VendorId parameter to access and potentially delete other
  users' company contact PII, combined with missing rate limiting for
  brute-force risks.
skill_level: intermediate
impact_level: high
id: 34a78111-1778-491d-b46b-9f5217857720
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Brute Force]]'
  - '[[Steal Web Session Cookie]]'
---
# IDOR in VendorId Parameter Leading to PII Leakage and Unauthorized Contact Deletion

Multi-stage attack chain demonstrating exploitation of IDOR in a U.S. Department of Defense vendor management web application to leak sensitive PII and potentially delete contacts, with additional risks from missing rate limiting on authentication.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 10 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Account Creation and Login] --> B[Intercept and Modify Requests]
    B --> C[PII Access via IDOR]
    C --> D[Contact Deletion via IDOR]
    D --> E[Brute-Force Exploitation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#e67e22
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]
- [[tools/Foxy-Proxy]]
- [[tools/curl]]

### Target Environment

- Web application built on ASP.NET Core
- Access to signup, login, and company management endpoints
- No specific ports required beyond standard HTTPS (443)

### Initial Access Requirements

- Ability to create multiple accounts (attacker and victim)
- Valid network access to the target URL (e.g., https://████)
- Burp Suite configured as proxy for request interception

## Detailed Attack Procedures

### Step 1: Access the Application and Create Accounts
procedure: [[procedures/Exploit-IDOR-for-Victim-PII-Access]]

**Objective**: Establish attacker and victim accounts to set up the exploitation scenario.

**Instructions**: Navigate to the redacted target URL (https://████) and create two separate accounts: one for the attacker and one simulating the victim. No special tools are needed for this step.

**Expected Output**: Successful account creation with login credentials for both.

**Success Indicators**:
- Attacker account dashboard accessible
- Victim account created and verifiable

### Step 2: Login as the Attacker Account
procedure: [[procedures/Exploit-IDOR-for-Victim-PII-Access]]

**Objective**: Authenticate as the attacker to access the application interface.

**Instructions**: Use the attacker's credentials to log in via the application's login page.

**Expected Output**: Redirect to the authenticated dashboard.

**Success Indicators**:
- Session cookies established
- Access to 'my companies' section granted

### Step 3: Navigate to My Companies Section
procedure: [[procedures/Exploit-IDOR-for-Victim-PII-Access]]

**Objective**: Reach the company management area where contacts are editable.

**Instructions**: From the dashboard, click on the 'my companies' link to load the relevant page.

**Expected Output**: Company profile page with contacts section visible.

**Success Indicators**:
- Company contacts list displayed
- Edit functionality available

### Step 4: Access Company Contacts and Initiate Edit
procedure: [[procedures/Exploit-IDOR-for-Victim-PII-Access]]

**Objective**: Trigger the request that can be intercepted for parameter manipulation.

**Instructions**: Scroll to the company contacts section and click the edit button to initiate a save action, which generates a POST request.

**Expected Output**: Edit form opens, ready for proxy interception.

**Success Indicators**:
- POST request to /Vendor/Company/Contacts/SavePOC triggered
- Parameters including VendorId visible in traffic

### Step 5: Intercept the Request Using Proxy Tools
procedure: [[procedures/Exploit-IDOR-for-Victim-PII-Access]]

**Objective**: Capture the editable request for modification.

**Instructions**: Enable [[tools/Foxy-Proxy]] to route traffic through [[tools/Burp-Suite]]. Perform the edit action to intercept the POST request to /Vendor/Company/Contacts/SavePOC.

**Expected Output**: Request captured in Burp Suite with VendorId parameter.

**Success Indicators**:
- Traffic routed successfully
- Request details including headers and body visible

### Step 6: Send the Intercepted Request to Burp Repeater
procedure: [[procedures/Exploit-IDOR-for-Victim-PII-Access]]

**Objective**: Prepare the request for parameter tampering.

**Instructions**: In Burp Suite, forward the captured POST request to the Repeater tab.

**Expected Output**: Request loaded in Repeater for editing.

**Success Indicators**:
- Repeater tab active with full request payload
- Ready for VendorId modification

### Step 7: Modify VendorId to Victim's ID
procedure: [[procedures/Exploit-IDOR-for-Victim-PII-Access]]

**Objective**: Swap the parameter to target victim data.

**Instructions**: In Burp Repeater, edit the VendorId in the request body from the attacker's ID to the victim's VendorId.

**Expected Output**: Modified request with victim's VendorId.

**Success Indicators**:
- Parameter change confirmed
- No syntax errors in payload

### Step 8: Send the Modified Request and Observe Response
procedure: [[procedures/Exploit-IDOR-for-Victim-PII-Access]]

**Objective**: Retrieve unauthorized PII.

**Instructions**: Replay the modified request in Burp Repeater.

**Expected Output**: Response containing victim's PII (names, emails, phones, positions).

**Success Indicators**:
- 200 OK response
- Sensitive data leaked in response body

### Step 9: Obtain Victim's VendorId if Needed
procedure: [[procedures/Exploit-IDOR-for-Victim-PII-Access]]

**Objective**: Acquire the target ID for exploitation.

**Instructions**: Log in as the victim, intercept a request (e.g., via Burp) to capture their VendorId, or attempt brute-forcing numeric IDs.

**Expected Output**: Victim's VendorId extracted.

**Success Indicators**:
- Valid ID obtained
- Confirmed via prior interception

### Step 10: Exploit for Deletion (Potential Extension)
procedure: [[procedures/Exploit-IDOR-for-Contact-Deletion]]

**Objective**: Attempt unauthorized removal of victim contacts.

**Instructions**: Use [[commands/curl-delete-poc-contact]] to send a POST to /Vendor/Company/Contacts/DeletePOC with the victim's pocId.

```bash
curl -i -s -k -X $'POST' -H $'Host: ████' -H $'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0' -H $'Accept: */*' -H $'Accept-Language: hr,hr-HR;q=0.8,en-US;q=0.5,en;q=0.3' -H $'Accept-Encoding: gzip, deflate' -H $'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H $'X-Csrf-Token: █████████' -H $'X-Requested-With: XMLHttpRequest' -H $'Content-Length: 26' -H $'Origin: https://████' -H $'Referer: █████████/Vendor/Company/Profile/129111' -H $'Sec-Fetch-Dest: empty' -H $'Sec-Fetch-Mode: cors' -H $'Sec-Fetch-Site: same-origin' -H $'Te: trailers' -H $'Connection: close' -b $'.AspNetCore.Antiforgery.wZhPOrJ1UhI=CfDJ8LTOEQjKnQRBhUKhTTOOit8CeSwiAzq1rveGhuP0xQJ5zgfDGoJhSN6xIO-5u9EUQW57_fcCBFDd5aabeWVSnSE7i40fuT7qOiTJ0fZ8qw_IoDW-NmNoSenQyHUXbO2KqEuvWN3Hi-7rR_UoLKZqGGM; TS014b77bb=01d263603a810528ade1b657e0385976b5acd6fdc2c03362a92881cea479e86280aaf5a469e93b2f6f255bd8b8a367ed9ad90941256753f414e03329b77cfc14c5f046bbb63a756384e7f686dcfd142272a7a8cf488f236de71dbe9bfe918979628567f86ddbb13b932bb4a1cb8d55f463ef78a133; .AspNetCore.Mvc.CookieTempDataProvider=CfDJ8LTOEQjKnQRBhUKhTTOOit_o0TeUroaEAfgtmMiCa9fB4ObkOQhAfzgbc17DvUpI3wVOOvZaUjZ0GHZjA5nJuRn5ludklhmtQqTGTIdAitoOIOLricizg2OBd4sIb6PTerrkyyQL7lRWF8Q4qMvy50qDCo1yPExe71j6qQ2gnE6ryKPk1vs-FWBOnWnEb9-qBUbzIyQ-K1gB51gQS0TeD__K0b5byVkJbIjca8Sd7Yq5; .AspNetAuth=CfDJ8LTOEQjKnQRBhUKhTTOOit8Vdo3-_HKifEFVq5lbA8g8edNiFpe0cQuw2M-osgD16XeoIdxnkoUIiqHwZjDMYf5rKsQYkLtHxtKtol2HRQ6EzODg4Yffc49tYIb-OfSuLj34UNgPo0Qm2F95pjXcsWjZ_jv_YEC2cZ67FH_mZsw7_QnC345IyWnHp5Le0bppltpp06x4dnoxK1Fo89-60U5G-suswckXhTLfkOw3xw2kc4DQssSKyBcr5aQJEmhRwfDmmQN2mqeXYG-6-w7jtsam5hCx1u1yN4U6Ar9JIbipRrBYk2r7pdWGuHkFNZDIqQ; TS0144f203=01d263603a05a2c5a6860e2c7c0c412143fc7375fa739551ff09b8936241b33c09409383f587d9d22cf5dd3d2595d7b49431eadd7e5c228e7c5bf79ab734ee800d7772dd6792ca46e6d2f8cc20a6a5829e3ba369d60624352c46436b3621ce4cba36f79b1259e316e3742fa232790b49b7b52ab68120104a99c4f3025c9aa65507f72c8212ce22cb19ff62a406ca448b7bde696749; CSRF-TOKEN=<yourtoken>' --data-binary $'pocId=<yourid>&disabled=false' $'██████████████/Vendor/Company/Contacts/DeletePOC'
```

**Expected Output**: 200 OK response indicating deletion success.

**Success Indicators**:
- Contact removed from victim profile
- No authorization error

## Attack Chain Summary

### Key Achievements

1. Unauthorized access to victim PII including names, emails, phones, and positions
2. Potential for phishing, account takeover, or brute-force attacks enabled by leaked data
3. Unauthorized deletion of victim contacts via similar IDOR
4. Exploitation of missing rate limits for credential guessing

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Brute Force]] Brute Force
- [[Steal Web Session Cookie]] Data from Information Repositories

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Discovery]] Discovery
- [[Collection]] Collection

---

*Last updated: 2023-10-01T00:00:00Z*
