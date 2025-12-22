---
id: proc-002
tags:
  - xss
  - shopify
  - web
  - url-capture
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-13T23:52:55.594Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Capture-Signed-Preview-URL

## Summary

This procedure captures the signed URL generated after initiating app listing creation, which includes a signature parameter for previewing changes without full authentication.

## Description

During the Shopify app listing creation, a redirect occurs to a URL with a ?signature parameter. This URL allows previewing the listing as if shared with another user. Capturing it enables simulation of victim access in an isolated session, crucial for testing XSS without alerting the attacker account.

## Requirements

1. Active session in Shopify Partners dashboard
2. Completion of listing initiation from prior step
3. Clipboard or note-taking for URL storage

## Defense

Defensive measures and detection strategies:

- Expire signed URLs quickly (e.g., short TTL)
- Log and monitor usage of signed preview URLs for anomalies

## Objectives

1. Obtain reusable URL for victim simulation
2. Preserve signature for unauthenticated preview access
3. Enable isolated testing of injected payload

## Instructions

### Step 1: Initiate Listing Creation

**Context**: Trigger the redirect that generates the signed URL.

After selecting 'Create listing', allow the page to redirect.

> Expected: Browser navigates to a new URL with signature.

### Step 2: Copy Full URL

**Context**: Extract the complete URL including query parameters.

Right-click address bar or use Ctrl+L to select, then copy the entire URL (e.g., https://apps.shopify.com/preview?signature=abc123).

> Expected: URL stored, ready for incognito use.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[shopify]]
- [[web]]
