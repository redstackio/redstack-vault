---
tags:
  - xssi
  - token-leak
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: c7a050f7-ae34-4b45-a13f-b609cac1d05a
created_at: '2025-12-11T06:10:40.535Z'
updated_at: '2025-12-11T06:10:40.535Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Set Up Malicious Site for XSSI Token Leak

## Summary

This procedure sets up a malicious website that exploits XSSI by including a vulnerable PayPal JavaScript file to expose sensitive security challenge tokens used in reCAPTCHA implementations.

## Description

The attack involves creating a webpage that loads the PayPal JS file cross-site, allowing the leakage of tokens due to missing XSSI protections. This is targeted at web environments using JavaScript for CAPTCHA challenges, leading to potential token capture for further exploitation.

## Requirements

1. Web server to host the malicious site.
2. Knowledge of the vulnerable PayPal JS endpoint.
3. JavaScript capabilities to capture leaked data.

## Defense

Defensive measures and detection strategies:

- Implement XSSI protections like prefixing JS with while(1); or similar.
- Monitor for unauthorized script inclusions from third-party domains.

## Objectives

1. Expose sensitive tokens via XSSI.
2. Prepare for token leakage upon victim visit.
3. Enable subsequent account compromise steps.

## Instructions

### Step 1: Create Malicious HTML

**Context**: Craft an HTML page that includes the vulnerable script.

Create an index.html with:

```html
<script src="https://vulnerable.paypal.js.endpoint"></script>
<script>
// Capture exposed tokens here, e.g., via overriding functions or parsing globals
console.log(window.exposedToken); // Example capture
// Send to attacker server
</script>
```

> This includes the PayPal JS and attempts to access leaked variables.

### Step 2: Host the Site

**Context**: Deploy the site on a server accessible to the victim.

Host the HTML on a web server, ensuring it's publicly accessible.

> Verify by visiting the site and checking console for leaked data.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[xssi]]
- [[token-leak]]
