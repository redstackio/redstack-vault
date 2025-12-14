---
tags:
  - origin-validation
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
impact_level: high
detection_risk: medium
sub_techniques: []
id: 05929641-53bc-4a97-9c43-0e939c6b8147
created_at: '2025-12-13T23:56:04.001Z'
updated_at: '2025-12-13T23:56:04.001Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Check for Broken Origin Validation in Embedded Apps

## Summary

This procedure involves analyzing pages and documentation to identify broken origin validation in Shopify embedded apps, confirming that origins are verified based on the logged-in store, enabling iframing and message posting on own stores.

## Description

The attack scenario targets Shopify's embedded apps where origin validation relies on the shopOrigin of the current logged-in shop. This allows attackers to iframe apps on their own stores and post malicious messages, setting up for further exploitation like XSS. The procedure requires access to Shopify documentation and a test store. Expected outcomes include confirmation of the vulnerability for chaining with other attacks.

## Requirements

1. Access to Shopify documentation and a test store
2. Basic understanding of web origin policies
3. No special tools required

## Defense

Defensive measures and detection strategies:

- Implement strict origin checks beyond logged-in shop
- Monitor for unusual iframe and postMessage activities in logs

## Objectives

1. Identify broken origin validation
2. Confirm potential for malicious message posting
3. Set foundation for XSS exploitation

## Instructions

### Step 1: Analyze Documentation

**Context**: Review Shopify embedded app documentation to understand origin validation mechanisms.

> Check how shopOrigin is set and verified.

### Step 2: Test on Own Store

**Context**: Set up an iframe of an embedded app on your own store and attempt to post messages.

> Confirm that messages are accepted based on logged-in shop origin.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- origin-validation
- shopify
