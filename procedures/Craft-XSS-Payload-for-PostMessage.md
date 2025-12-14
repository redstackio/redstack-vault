---
tags:
  - xss
  - dom-xss
  - postmessage
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/alert-document-domain]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 79ff5a0a-85ef-42c9-82c9-6f439ec21134
created_at: '2025-12-13T23:56:20.064Z'
updated_at: '2025-12-13T23:56:20.064Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft XSS Payload for PostMessage

## Summary

This procedure crafts a JSON payload exploiting insecure postMessage handlers by injecting a JavaScript URI into the 'followUpUrl' field to execute arbitrary code.

## Description

By mimicking a legitimate 'mktoResponse' structure, the payload tricks the event listener into processing a malicious followUpUrl, leading to XSS via location.href assignment. This is effective for demonstrating execution in the target's domain context.

## Requirements

1. Knowledge of the target's JSON structure from prior analysis
2. Ability to send postMessage from a controlled page
3. Browser for testing

## Defense

Defensive measures and detection strategies:

- Validate all fields in incoming messages
- Sanitize URLs before assigning to location.href
- Implement CSP to block javascript: URIs

## Objectives

1. Create payload triggering XSS
2. Execute script like alert(document.domain)
3. Verify execution in target context

## Instructions

### Step 1: Construct JSON Payload

**Context**: Build the payload matching the expected structure.

Create the JSON object with 'mktoResponse' containing a 'followUpUrl' set to 'javascript:alert(document.domain);//'.

```json
{"mktoResponse":{"for":"mktoFormMessage0","error":false,"data":{"formId":"1013","followUpUrl":"javascript:alert(document.domain);//","aliId":17144124}}}
```

> This payload sets location.href to execute [[commands/alert-document-domain]].

### Step 2: Test Payload Locally

**Context**: Verify the payload's structure and potential execution.

Simulate the event listener in a test environment to ensure the JSON parses correctly and triggers the redirect.

> Expected alert showing the document domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used

- [[commands/alert-document-domain]]

## Tools Used



## Tags

- [[xss]]
- [[payload-crafting]]
