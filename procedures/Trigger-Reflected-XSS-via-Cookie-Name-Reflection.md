---
id: proc-uuid-002
name: Trigger-Reflected-XSS-via-Cookie-Name-Reflection
tags:
  - xss
  - reflected-xss
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:25.660Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-Reflected-XSS-via-Cookie-Name-Reflection

## Summary

This procedure triggers a reflected XSS vulnerability in an ASP.NET endpoint by redirecting to it after setting a malicious cookie. The endpoint unsafely reflects the first cookie name on the page, executing the embedded JavaScript payload in the context of an authenticated session.

## Description

The Registration.aspx endpoint in the target application reflects the name of the first cookie without HTML or JavaScript sanitization, allowing arbitrary code execution. This is chained from a prior cookie-setting step, enabling attacks on authenticated areas handling login, registration, and course management. The attack requires the malicious cookie to be present and uses a simple redirect to trigger reflection. Outcomes include potential session hijacking or unauthorized actions on behalf of users in a military (.mil) environment.

## Requirements

1. Malicious cookie already set for the domain (from prior procedure)
2. Browser session with the cookie
3. Access to the vulnerable endpoint: https://www2.petersons.af.mil/nssi/core/dot_stu_reg/Registration.aspx

## Defense

Defensive measures and detection strategies:

- Sanitize all user-controlled inputs, including cookie names, before rendering
- Implement output encoding for HTML contexts (e.g., HtmlEncode in ASP.NET)
- Use strict cookie parsing and validation on the server side
- Deploy WAF rules to detect script tags in cookie values/names

## Objectives

1. Redirect to the vulnerable endpoint to force cookie name reflection
2. Execute arbitrary JavaScript in the authenticated page context
3. Enable unauthorized interactions with sensitive site features

## Instructions

### Step 1: Prepare the Redirect

**Context**: Ensure the malicious cookie is set and then initiate a redirect to the target endpoint.

From the XSS context or console, execute:

```javascript
window.top.location.href = 'https://www2.petersons.af.mil/nssi/core/dot_stu_reg/Registration.aspx';
```

### Step 2: Observe Reflection and Execution

**Context**: The endpoint loads and reflects the first cookie name (e.g., 'zzz<script>alert(document.domain)</script>') unsanitized in the HTML, triggering the script.

Load the page and watch for execution.

**Expected Output**: Alert dialog displaying the document domain (e.g., www2.petersons.af.mil), confirming XSS.

### Step 3: Validate Impact

**Context**: Confirm execution occurs in the authenticated context by replacing alert with more invasive payloads (e.g., keylogging or form submission).

Test with enhanced payload in cookie: 'zzz<script>document.body.innerHTML += \"<h1>XSS Triggered\"</h1>\"</script>'

Reload and observe page modification.

**Expected Output**: Visible changes or actions on the page.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- reflected-xss
