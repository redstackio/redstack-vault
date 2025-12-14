---
id: proc-uuid-3
tags:
  - xss
  - url-construction
  - iframe
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
updated_at: '2025-12-14T03:15:10.456Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Construct-Iframe-URL-with-XSS-Payload

## Summary

This procedure builds the full URL for the Zomato widget endpoint, injecting the encoded XSS payload into 'language_id' while including necessary parameters to ensure the widget loads.

## Description

Combine the vulnerable endpoint with the payload and widget options like city_id=276, theme=blue. This URL, when loaded in an iframe, triggers the XSS. Scenario: Attacker prepares for embedding in a phishing page. Outcomes: Functional URL that delivers the exploit without alerting filters.

## Requirements

1. Encoded payload from previous step
2. Zomato widget documentation for parameters
3. URL builder or text editor

## Defense

Defensive measures and detection strategies:

- Validate parameter lengths and formats server-side
- Block requests with excessive encoding or suspicious patterns
- Use referrer checks to restrict iframe embedding

## Objectives

1. Integrate payload seamlessly
2. Maintain widget usability for stealth
3. Validate URL syntax

## Instructions

### Step 1: Assemble Base URL

**Context**: Start with endpoint and required params.

Base: `https://www.zomato.com/widgets/res_search_widget.php?city_id=276`

> city_id=276 is for a specific city like Delhi; adjust as needed.

### Step 2: Inject Payload and Options

**Context**: Add language_id with payload and UI params.

Full URL: `https://www.zomato.com/widgets/res_search_widget.php?city_id=276&language_id=%22%7D%27)%3Balert(document.domain)%3Bconsole.log(%27&theme=blue&hideCitySearch=on&hideResSearch=on&sort=popularity`

> Test by pasting into browser; widget should load with alert on payload trigger.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[iframe]]
