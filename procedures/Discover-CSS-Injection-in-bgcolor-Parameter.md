---
tags:
  - css-injection
  - discovery
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:57.205Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: eb3b0f74-419e-4ce1-9301-4ace428fa687
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Discover-CSS-Injection-in-bgcolor-Parameter

## Summary

This procedure identifies a CSS injection vulnerability in the bgcolor parameter of the Chaturbate /embed/admin/ endpoint by testing payloads that alter page styling, confirming insufficient input sanitization.

## Description

The attack targets the /embed/admin/ endpoint where the bgcolor parameter is reflected into inline CSS without proper validation. By URL-encoding a payload like `%7D*%7Bbackground:red`, attackers close the existing style rule (e.g., body{background:...}) and inject new rules applying to all elements (*). This allows arbitrary CSS execution, setting the stage for side-channel attacks. The target environment is the public-facing Chaturbate web application, requiring only browser access. Expected outcomes include visual confirmation of injection via style changes, enabling further exploitation like token leakage.

## Requirements

1. Web browser or HTTP client for accessing the endpoint
2. Knowledge of URL encoding for payloads
3. Access to the public Chaturbate domain

## Defense

Defensive measures and detection strategies:

- Implement strict whitelisting for CSS values in bgcolor (e.g., only hex colors)
- Encode or escape user input in CSS contexts to prevent rule closure
- Monitor for anomalous CSS payloads in access logs

## Objectives

1. Confirm arbitrary CSS execution via style alteration
2. Validate lack of sanitization in the parameter
3. Establish foundation for escalation to information disclosure

## Instructions

### Step 1: Craft and Access Test Payload

**Context**: Construct a URL with an encoded payload to close the CSS rule and apply a detectable style change, such as a red background.

Access the following URL in a browser:

```url
https://chaturbate.com/embed/admin/?bgcolor=%7D*%7Bbackground:red&tour=nvfS&disable_sound=0&campaign=iNSGX
```

> This payload decodes to `}*{background:red}`, injecting after the existing body style. If successful, the page elements turn red, indicating injection. No command-line tool is needed; observe the rendered page.

### Step 2: Verify Injection

**Context**: Check for the style change to ensure the payload executed without blocking.

Inspect the page source or visually confirm the background color shift.

> Expected output: All elements (* selector) have a red background, overriding default styles. If no change occurs, try variations like `%7Dbody%7Bbackground:blue%7D` to test specificity.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[css-injection]]
- [[web-vuln]]
