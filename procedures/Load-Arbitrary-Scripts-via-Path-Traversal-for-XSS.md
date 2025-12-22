---
tags:
  - xss
  - javascript
  - exploit
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: afeb5bec-c72c-4445-8e3a-4377c33eaa9b
created_at: '2025-12-14T03:16:30.877Z'
updated_at: '2025-12-14T03:16:30.877Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Load Arbitrary Scripts via Path Traversal for XSS

## Summary

This procedure exploits confirmed path traversal in GoCD's URL routing to load and execute arbitrary JavaScript files from unexpected locations, enabling reflected or stored XSS attacks that compromise user browsers.

## Description

Once path traversal is validated, attackers can direct the routing to serve user-uploaded or misconfigured JavaScript files (e.g., from /js/ directories or prior uploads). GitHub Pages' static nature limits server controls, allowing HTTP responses to include these scripts without validation. In an attack scenario, a victim visiting the crafted URL executes the JS in their context, potentially leading to session hijacking, data theft, or further phishing. Outcomes include successful script injection, as demonstrated by payload execution like alerts or DOM changes.

## Requirements

1. Confirmed vulnerable paths from prior reconnaissance.
2. Web browser with console for monitoring script execution.
3. Optional: Access to upload malicious JS if stored XSS is targeted (e.g., via another vector).

## Defense

Defensive measures and detection strategies:

- Enforce script-src directives in CSP to restrict external or traversed script sources.
- Sanitize all URL paths server-side, rejecting any .. or %2F sequences.
- Deploy WAF rules to flag and block traversal attempts in real-time.

## Objectives

1. Load unintended JavaScript via traversed paths.
2. Execute arbitrary code in the browser for XSS.
3. Compromise user security on GoCD sites.

## Instructions

### Step 1: Target Potential Script Locations

**Context**: Use the traversal to point to directories likely containing JS files, such as root or user-upload areas.

Navigate to a crafted URL like:

```plaintext
https://www.go.cd/user/upoad/..%2F..%2Fjs/malicious.js
```

> If malicious.js exists (e.g., uploaded via another flaw), it loads as a script tag. Inspect network tab to confirm 200 OK response and script content.

### Step 2: Trigger XSS Execution

**Context**: Embed the traversal in a context where the loaded script runs, such as an img src or script tag in reflected responses.

Test with a payload that includes the traversal in a script-loading attribute:

```plaintext
https://docs.go.cd/current/user/upoad/..%2F..%2Fpath/to/payload.js
```

> Monitor browser console for execution (e.g., if payload.js contains alert('XSS')). Screenshots of alerts or console errors confirm success.

### Step 3: Validate Impact

**Context**: Simulate user compromise by checking for data access or persistence.

After loading, attempt actions like cookie access via console:

```javascript
console.log(document.cookie);
```

> Expected: Script runs with site privileges, exposing session data if stored XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- javascript
- path-traversal
