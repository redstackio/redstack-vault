---
tags:
  - iframe-inspection
  - parameter-discovery
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:12.992Z'
sub_techniques: []
id: 7925b2c5-8615-4dcf-a12d-de6f5bb22376
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inspect-Cashier-Iframe-Source

## Summary

This procedure uses browser developer tools to locate and examine the cashier iframe's src attribute, revealing the exposed PIN parameter for IDOR exploitation.

## Description

The iframe with id='cashiercont' contains a src URL to https://cashier.binary.com/login.asp with parameters like PIN (account ID), Password (hash), Secret, and Action=DEPOSIT. Inspection identifies the lack of validation, allowing client-side tampering.

## Requirements

1. Loaded deposit flow from attacker session
2. Browser with developer tools (e.g., Chrome DevTools)
3. Basic knowledge of HTML inspection

## Defense

Defensive measures and detection strategies:

- Avoid exposing authentication parameters in client-side code
- Use postMessage or secure tokens for iframe communication
- Implement CSP to restrict iframe modifications

## Objectives

1. Locate the iframe element in the DOM
2. Extract and understand src parameters
3. Identify PIN as modifiable account reference

## Instructions

### Step 1: Open Developer Tools

**Context**: Access inspection interface.

Right-click the page and select "Inspect" or press F12 to open DevTools.

### Step 2: Locate Iframe Element

**Context**: Find the vulnerable iframe.

In the Elements tab, search for <iframe id="cashiercont">.

### Step 3: Examine SRC Attribute

**Context**: Reveal parameters for modification.

Expand the iframe node and copy the src value, noting PIN=<ATTACKER_ID>, Password=..., Secret=..., Action=DEPOSIT.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[iframe-inspection]]
- [[parameter-discovery]]
