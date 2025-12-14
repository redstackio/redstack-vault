---
tags:
  - xss
  - open-redirect
  - moodle
  - lti
  - php
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/test-moodle-open-redirect-with-curl]]'
  - '[[commands/test-moodle-xss-payload-with-curl]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Discover-Open-Redirect-in-Moodle-LTI-redirect_uri-Parameter]]'
  - '[[procedures/Escalate-Open-Redirect-to-Reflected-XSS-in-Moodle-LTI]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
description: >-
  Escalates an open redirect vulnerability in Moodle's LTI authentication
  endpoint to reflected XSS, enabling JavaScript execution and session cookie
  theft.
skill_level: intermediate
impact_level: high
id: 0693c7ff-0366-41f4-b919-e1dcfef4090f
created_at: '2025-12-13T23:52:39.027Z'
updated_at: '2025-12-13T23:52:39.027Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Reflected XSS via Open Redirect in Moodle LTI Authentication

Multi-stage attack chain demonstrating escalation from open redirect to reflected XSS in the Moodle LTI authentication endpoint on evolve.glovoapp.com.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discover Open Redirect] --> B[Escalate to Reflected XSS]
    B --> C[Execute JavaScript and Steal Cookies]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome with developer tools)
- curl (for initial response checks)

### Target Environment

- Web platform on port 443
- Moodle application with PHP backend
- Publicly accessible /mod/lti/auth.php endpoint

### Initial Access Requirements

- No credentials required (public endpoint)
- Direct network access to the target domain (e.g., evolve.glovoapp.com)
- No prior access needed

## Detailed Attack Procedures

### Step 1: Discover Open Redirect
procedure: [[procedures/Discover-Open-Redirect-in-Moodle-LTI-redirect_uri-Parameter]]

**Objective**: Identify lack of validation in the redirect_uri parameter, allowing arbitrary external redirects.

**Instructions**: Target the /mod/lti/auth.php endpoint and append an external URL to the redirect_uri parameter. Use [[commands/test-moodle-open-redirect-with-curl]] to fetch the response and check for redirect headers:

```bash
curl -i -L "https://evolve.glovoapp.com/mod/lti/auth.php?redirect_uri=https://example.com"
```

Follow up by visiting the URL in a web browser to confirm the redirect occurs without blocking.

**Expected Output**: HTTP 3xx status code with Location header pointing to the external URL (e.g., https://example.com), and browser navigates away from the origin.

**Success Indicators**:
- Redirect to external site confirmed via curl Location header
- Browser successfully redirects without validation errors

### Step 2: Escalate to Reflected XSS
procedure: [[procedures/Escalate-Open-Redirect-to-Reflected-XSS-in-Moodle-LTI]]

**Objective**: Inject a javascript: URI scheme into redirect_uri to execute arbitrary JavaScript in the victim's browser context.

**Instructions**: Modify the redirect_uri to include a javascript: payload. First, use [[commands/test-moodle-xss-payload-with-curl]] to inspect the response and confirm the parameter is reflected unsanitized:

```bash
curl -i "https://evolve.glovoapp.com/mod/lti/auth.php?redirect_uri=javascript:alert(document.domain)"
```

Then, visit the crafted URL in a web browser to trigger execution.

**Expected Output**: The response reflects the javascript: URI without escaping; in the browser, an alert box displays the document domain (e.g., evolve.glovoapp.com).

**Success Indicators**:
- Payload reflected in response body
- JavaScript executes in browser, confirming XSS

## Attack Chain Summary

### Key Achievements

1. Confirmed open redirect vulnerability in Moodle LTI endpoint
2. Escalated to reflected XSS using javascript: URI schemes
3. Enabled potential theft of session cookies for admin or user impersonation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution
- [[Collection]] Collection

---
*Last updated: 2023-10-01*
