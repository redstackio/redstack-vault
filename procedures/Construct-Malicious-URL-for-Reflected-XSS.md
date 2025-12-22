---
tags:
  - xss
  - payload-construction
  - url-injection
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:31.052Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: d1af8db4-9df1-4431-bd8f-d78041c7b592
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Construct-Malicious-URL-for-Reflected-XSS

## Summary

This procedure involves crafting a malicious URL by injecting a JavaScript payload into the 'city' GET parameter of Uber's careers page, exploiting insufficient input validation to enable reflected XSS.

## Description

In this attack scenario, the target is the public-facing web application at www.uber.com/careers/list/. The 'city' parameter is reflected back into the HTML without proper encoding, allowing an attacker to close an existing script tag and inject a new one. The payload `</script><script>alert("xss by pavanw3b")</script>` is appended to a base value like 'allicg', with additional junk like 'fupaiiz' to maintain parameter integrity. This leads to arbitrary JavaScript execution when the URL is loaded, potentially enabling phishing, site defacement, or credential theft in a real attack.

## Requirements

1. Knowledge of the target URL structure (www.uber.com/careers/list/)
2. Basic understanding of HTML and JavaScript for payload crafting
3. Text editor or browser address bar for URL construction

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding (e.g., HTML entity encoding) for all user-controlled parameters
- Use Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous JavaScript payloads in web logs

## Objectives

1. Create a functional malicious URL that injects and reflects JavaScript
2. Ensure the payload evades basic sanitization
3. Prepare for delivery to a victim via phishing or social engineering

## Instructions

### Step 1: Identify Base Parameter

**Context**: Start with the legitimate 'city' parameter value from the target page, such as 'allicg'.

No command required; manually note the base value.

> Expected output: Base string 'allicg' ready for injection.

### Step 2: Append JavaScript Payload

**Context**: Inject the payload to break out of any existing script context and execute new code.

Manually construct: `city=allicg</script><script>alert('xss by pavanw3b')</script>fupaiiz`.

> Explanation: The `</script><script>` closes and reopens a script tag, allowing execution of the alert. The junk suffix 'fupaiiz' helps avoid breaking the URL.

### Step 3: Build Full URL

**Context**: Combine with other query parameters to form the complete malicious URL.

Full URL: `https://www.uber.com/careers/list/?city=allicg</script><script>alert('xss by pavanw3b')</script>fupaiiz&country=all&keywords=&subteam=all&team=all`.

> Expected output: A copy-paste ready URL for the next step.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- payload-crafting
