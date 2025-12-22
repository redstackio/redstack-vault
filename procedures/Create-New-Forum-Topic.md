---
tags:
  - xss
  - initial-access
  - shopify
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
impact_level: low
detection_risk: low
sub_techniques: []
id: 421436e8-f8ea-49bb-b14c-04e74acf03fc
created_at: '2025-12-14T03:16:08.160Z'
updated_at: '2025-12-14T03:16:08.160Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-New-Forum-Topic

## Summary

This procedure outlines navigating to the Shopify Discussion Forums and initiating the creation of a new topic, serving as the entry point for injecting malicious payloads in subsequent steps.

## Description

In the context of exploiting stored XSS in Shopify's forums, this step establishes access to the topic creation interface. The forums are hosted at ecommerce.shopify.com/shopify-discussion, and creating a topic requires a user account. This procedure assumes basic web navigation and form interaction, with no advanced tools needed. Expected outcome is a loaded form ready for payload input, enabling the attack chain to proceed without alerting defenses.

## Requirements

1. Valid Shopify account (signup is free and quick)
2. Web browser with JavaScript enabled
3. Internet access to ecommerce.shopify.com

## Defense

Defensive measures and detection strategies:

- Require account verification for forum access to limit anonymous postings
- Monitor for unusual topic creation rates from new accounts
- Implement rate limiting on topic submissions

## Objectives

1. Access the topic creation form
2. Prepare for payload injection
3. Establish a persistent attack vector in the forums

## Instructions

### Step 1: Navigate to Forums

**Context**: Locate the discussion section to begin topic creation.

No command required; use browser to visit https://ecommerce.shopify.com/shopify-discussion and click 'New Topic' or equivalent button.

> Browser loads the forum index; look for the 'Create Topic' option in the navigation or sidebar.

### Step 2: Initiate Topic Creation

**Context**: Open the form for entering title and message.

Click the 'New Topic' button to load the creation form.

> Form appears with fields for title, message body, and optional tags/categories.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[shopify]]
- [[web]]
