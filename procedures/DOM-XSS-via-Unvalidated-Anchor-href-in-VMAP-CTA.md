---
tags:
  - dom-xss
  - vmap
  - cta-link
type: procedure
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:55.274Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: d1daf99b-27f4-4f46-a9f9-c2893ce50666
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# DOM-XSS-via-Unvalidated-Anchor-href-in-VMAP-CTA

## Summary

This procedure targets a potential DOM XSS in the updateCallToAction function by injecting a javascript: URL into the tw:cta_open_url field of a VMAP file loaded by the player.

## Description

The player parses VMAP files from whitelisted domains and sets an anchor's href to the ctaLink (tw:cta_open_url) without javascript: validation. If an attacker hosts a malicious VMAP on a allowed domain like twimg.com, clicking the CTA executes the payload. Full PoC limited by hosting, but demonstrates supply-chain risk in ad integrations.

## Requirements

1. Ability to host a VMAP XML file on a whitelisted Twitter domain
2. Access to the Amplify player
3. Basic XML crafting skills

## Defense

Defensive measures and detection strategies:

- Validate all URLs in VMAP against protocol whitelists excluding javascript:
- Scan hosted VMAP files for malicious content before serving
- Disable or sandbox CTA links in player configurations

## Objectives

1. Inject and execute JS via ad metadata
2. Highlight third-party content risks
3. Enable phishing or redirection attacks

## Instructions

### Step 1: Craft Malicious VMAP

**Context**: Create VMAP XML with injected CTA URL.

Example VMAP snippet:

```xml
<Extensions>
  <tw:cta_open_url>javascript:alert(1)</tw:cta_open_url>
</Extensions>
```

Host on whitelisted domain.

### Step 2: Load VMAP in Player

**Context**: Configure player to use the malicious VMAP.

Access player URL with VMAP reference (specific param depends on loader).

### Step 3: Trigger CTA

**Context**: Interact with the call-to-action element.

Click the anchor to execute href.

> Payload runs in current context on click.

**Expected Output**: Alert on CTA interaction.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[dom-xss]]
- [[vmap]]
- [[twitter]]
