---
id: uuid-identify-vuln
tags:
  - xss
  - recon
  - web-vuln
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:16:31.426Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify Vulnerable Email Parameter on Acronis Thank-You Page

## Summary

This procedure involves inspecting the Acronis newsletter thank-you page to identify the 'email' parameter that is reflected without sanitization, enabling potential XSS attacks.

## Description

The Acronis site at https://cz.acronis.com/dekujeme-za-odber-novinek-produktu-disk-director/ processes newsletter subscriptions and reflects the 'email' query parameter directly into the HTML response. This lack of output encoding allows attackers to inject malicious scripts. The procedure targets public-facing web applications built on PHP/WordPress stacks where user inputs are not properly escaped. Expected outcome is confirmation of reflection, setting the stage for payload testing.

## Requirements

1. Web browser with inspect element capability
2. Access to the public internet and the target URL
3. Basic knowledge of URL query parameters and HTML inspection

## Defense

Defensive measures and detection strategies:

- Implement content security policy (CSP) to restrict script execution
- Use output encoding libraries like htmlspecialchars in PHP for all user inputs
- Monitor for anomalous query parameters in web logs

## Objectives

1. Confirm reflection of the email parameter in page content
2. Identify lack of sanitization for XSS potential
3. Gather details for crafting targeted payloads

## Instructions

### Step 1: Access and Inspect the Page

**Context**: Navigate to the thank-you page and append a test email to observe reflection.

Visit the URL with a sample parameter: https://cz.acronis.com/dekujeme-za-odber-novinek-produktu-disk-director/?user=OK&oktosend=&email=test@example.com

Inspect the page source (right-click > View Page Source) and search for 'test@example.com' to see if it's echoed verbatim in HTML.

> If reflected without &lt; or &gt; encoding, the parameter is vulnerable to XSS.

### Step 2: Analyze Reflection Point

**Context**: Determine exact location of reflection to plan injection.

Use browser developer tools (F12 > Elements tab) to locate where the email value appears, typically in a paragraph or input field. Note any surrounding HTML tags that could be broken with payload.

> Successful analysis reveals direct insertion, e.g., <p>Thank you, test@example.com!</p> without escaping.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[recon]]
- [[web-vuln]]
