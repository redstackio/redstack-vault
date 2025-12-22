---
tags:
  - xss
  - stored-xss
  - angularjs
  - web-exploitation
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/authenticate-session-post]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Obtain-Initial-Session-Cookie]]'
  - '[[procedures/Authenticate-Session-via-POST-Request]]'
  - '[[procedures/Access-Suggested-Edits-Page]]'
  - '[[procedures/Inject-Malicious-AngularJS-Payload]]'
  - '[[procedures/Trigger-XSS-via-Admin-View]]'
step_count: 5
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
description: >-
  Exploitation of a stored XSS vulnerability in the suggested edits feature of
  uber.readme.io to inject malicious AngularJS payloads, leading to potential
  defacement and account hijacking.
skill_level: intermediate
impact_level: high
id: 06fcd4d6-4b2f-47f0-bbd8-25c5c6de2ac1
created_at: '2025-12-13T23:56:20.328Z'
updated_at: '2025-12-13T23:56:20.328Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
# Stored XSS in Uber Documentation via Suggested Edits

Multi-stage attack chain demonstrating exploitation of a stored XSS vulnerability in uber.readme.io's suggested edits feature, allowing injection of malicious AngularJS payloads that execute when viewed by administrators, potentially leading to page defacement and developer account hijacking.

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
    A[Obtain Session Cookie] --> B[Authenticate Session]
    B --> C[Access Edit Page]
    C --> D[Inject Payload]
    D --> E[Trigger via Admin View]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None specifically required beyond a web browser and HTTP client like curl.

### Target Environment

- Web platform
- Services: uber.readme.io, developer.uber.com
- Tech stack: AngularJS

### Initial Access Requirements

- Valid email and password for authentication on uber.readme.io
- Network access to the target URLs

## Detailed Attack Procedures

### Step 1: Obtain Initial Session Cookie
procedure: [[procedures/Obtain-Initial-Session-Cookie]]

**Objective**: Access the documentation page to receive an initial connect.sid cookie for session management.

**Instructions**: Navigate to the deep-linking documentation page at https://uber.readme.io/docs/deep-linking using a web browser or HTTP client to obtain the initial session cookie.

**Expected Output**: Receipt of a connect.sid cookie in the HTTP response headers.

**Success Indicators**:
- Cookie is set in the browser or captured in the response.
- No authentication errors occur.

### Step 2: Authenticate Session
procedure: [[procedures/Authenticate-Session-via-POST-Request]]

**Objective**: Authenticate the session using provided credentials to gain access to editing features.

**Instructions**: Send a POST request to /users/session using [[commands/authenticate-session-post]]:

```bash
POST /users/session HTTP/1.1
Host: uber.readme.io
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:42.0) Gecko/20100101 Firefox/42.0
Accept: application/json, text/plain, */*
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json;charset=utf-8
Content-Length: 84
Cookie: YOUR CONNECT.SID COOKIE HERE
Connection: close
Pragma: no-cache
Cache-Control: no-cache

{"email":"readme2@thursday.eml.cc","password":"pjJnBODjkLFv!!11","action":"session"}
```

**Expected Output**: JSON response with user details and a new connect.sid cookie.

**Success Indicators**:
- Successful authentication response (200 OK).
- New session cookie issued.

### Step 3: Access Suggested Edits Page
procedure: [[procedures/Access-Suggested-Edits-Page]]

**Objective**: Load the edit page for the target documentation using the authenticated session.

**Instructions**: Access https://uber.readme.io/docs/deep-linking/edit with the authenticated connect.sid cookie to reach the 'Suggest edits' interface.

**Expected Output**: Successful loading of the edit page.

**Success Indicators**:
- Page loads without access denied errors.
- Edit interface is available.

### Step 4: Inject Malicious AngularJS Payload
procedure: [[procedures/Inject-Malicious-AngularJS-Payload]]

**Objective**: Insert the malicious payload into the document and submit the suggestion.

**Instructions**: In the edit interface, insert the payload '{{(_="".sub).call.call({}[$="constructor"].getOwnPropertyDescriptor(_.__proto__,$).value,0,"alert(1)")()}}' into the document content, add a description, and submit the edit suggestion.

**Expected Output**: Successful submission of the suggested edit.

**Success Indicators**:
- Edit suggestion is queued for admin review.
- No validation errors on submission.

### Step 5: Trigger XSS via Admin View
procedure: [[procedures/Trigger-XSS-via-Admin-View]]

**Objective**: Have an administrator view the suggested edit, triggering the payload execution.

**Instructions**: The administrator accesses the dashboard to view the suggestion, which renders the malicious AngularJS expression, executing JavaScript in their context and potentially auto-approving the edit.

**Expected Output**: Execution of the alert(1) or other injected JavaScript.

**Success Indicators**:
- Payload executes in admin context.
- Edit is approved and injected permanently into the documentation.

## Attack Chain Summary

### Key Achievements
1. Successful authentication and access to editing features.
2. Injection of stored XSS payload via suggested edits.
3. Execution of arbitrary JavaScript leading to potential defacement and account hijacking.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

*Last updated: 2023-10-01*
