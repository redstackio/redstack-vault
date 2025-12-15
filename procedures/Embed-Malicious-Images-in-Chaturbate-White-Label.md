---
id: proc-embed-images-white-label-001
tags:
  - embedding
  - white-label
  - proxy-trigger
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
updated_at: '2025-12-14T17:26:48.941Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Embed-Malicious-Images-in-Chaturbate-White-Label

## Summary

This procedure embeds img tags pointing to attacker PHP scripts in Chaturbate White Label HTML, causing the asset proxy to rewrite and fetch the malicious URLs upon page load.

## Description

Chaturbate White Labels allow HTML customization in profiles or homepages. By inserting <img> sources to slow.php, big.php, etc., the proxy (camo.stream.highwebmedia.com) intercepts and proxies the requests, hashing paths like /hash/attacker/slow.php, initiating the DoS without direct access.

## Requirements

1. Active Chaturbate White Label account
2. Hosted PHP scripts ([[procedures/Create-Slow-Response-PHP-Script]] etc.)
3. HTML editing access in dashboard

## Defense

Defensive measures and detection strategies:

- Sanitize HTML in White Labels for external img srcs
- Proxy validation of image content-types and sizes
- Log and alert on proxy fetches to unknown domains

## Objectives

1. Trigger proxy fetches automatically on page views
2. Obfuscate attack via URL hashing
3. Enable passive DoS activation

## Instructions

### Step 1: Access White Label Editor

**Context**: Log in and navigate to HTML sections.

No command; go to Chaturbate White Label dashboard > Homepage intro or Verified profile HTML.

> Expected output: Editor opens for HTML input.

### Step 2: Insert img Tags

**Context**: Embed sources to trigger fetches.

Add to HTML:

```html
<img src="http://attacker/slow.php" alt="">
<img src="http://attacker/big.php" alt="">
<img src="http://attacker/big_valid.php" alt="">
```

> Expected output: Save and view page; inspect network for proxy URLs like https://camo.stream.highwebmedia.com/4854b41b7c19a74ff2007dced08a28a6b67459a8/attacker.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- embedding
- chaturbate
