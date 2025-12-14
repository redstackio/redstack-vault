---
tags:
  - stored-xss
  - shopify
  - admin
  - iframe
  - timeline
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:03.536Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: ba6fb32e-607e-4c77-9006-0b63728089ea
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger Stored XSS in Customer Message

## Summary

This procedure triggers the execution of a stored XSS payload by viewing a malicious customer message in Shopify's admin Timeline, exploiting the lack of iframe sandboxing to run JavaScript in the admin context.

## Description

The core exploitation step in this Shopify stored XSS vulnerability involves clicking a sent message on the customer profile page, which loads email contents in an iframe without the 'sandbox' attribute. Due to recent changes removing this attribute from the email preview, injected scripts (e.g., <script>alert('XSS')</script>) execute freely. This targets the /admin/customers and Timeline features, requiring staff permissions. Outcomes include arbitrary JS execution, potentially leading to session hijacking or data exfiltration.

## Requirements

1. Customer profile open with malicious message present
2. Payload pre-injected via private messaging (e.g., as a customer or compromised account)
3. Admin session active without content security policy (CSP) blocks

## Defense

Defensive measures and detection strategies:

- Re-implement sandbox attributes on all iframes (e.g., sandbox="allow-same-origin")
- Sanitize message contents with HTML entity encoding and JS parsers
- Monitor for JS execution errors or anomalous browser events in admin logs
- Use CSP headers to restrict inline scripts

## Objectives

1. Load the malicious message to execute stored payload
2. Confirm XSS in admin context outside rich text editors
3. Achieve impact like alert or data theft

## Instructions

### Step 1: Locate Malicious Message

**Context**: Identify the stored payload in the customer's communication history.

On the customer profile page, scroll to the Timeline or messages section and locate the sent message containing the injected script.

> Message appears as a clickable item in the activity feed.

### Step 2: Preview and Trigger

**Context**: Load the message contents to activate the unsandboxed iframe.

Click on the sent message to open its preview. The iframe loads the email body, executing the XSS due to missing sandbox.

> Observe execution (e.g., alert dialog or console output); payload runs in the parent admin document context.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[stored-xss]]
- [[shopify]]
- [[admin]]
- [[iframe]]
- [[timeline]]
