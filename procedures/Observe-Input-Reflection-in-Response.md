---
id: proc-uuid-002
tags:
  - xss
  - input-reflection
type: procedure
tools:
  - '[[tools/Browser]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:53.620Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Observe-Input-Reflection-in-Response

## Summary

This procedure tests for direct reflection of user input from the serial parameter in the server's HTML response, confirming lack of output encoding that enables XSS attacks.

## Description

By submitting a simple invalid serial like "test123" and inspecting the page source, this step verifies if the input is echoed back verbatim into the HTML. In the target ASP application, the serial is reflected without HTML entity encoding, creating an opportunity for script injection. Prerequisites include access to the endpoint from the previous procedure.

## Requirements

1. Web browser with inspect element capability
2. Prior access to the verification endpoint
3. Knowledge of basic HTML source inspection

## Defense

Defensive measures and detection strategies:

- Apply HTML output encoding to all user inputs in responses
- Scan for reflection patterns in application code
- Log and alert on suspicious input lengths or characters

## Objectives

1. Verify unencoded reflection of serial input
2. Document the exact location of reflection in the response
3. Assess potential for script insertion

## Instructions

### Step 1: Submit Test Input

**Context**: Provide an invalid serial to check for echo in the response.

Use [[tools/Browser]] to modify and submit the URL:

```url
http://www.grouplogic.com/files/glidownload/verify3.asp?version=CC1100x7660&serial=test123
```

> Inspect the response source; expect to see "test123" reflected directly, e.g., in a <p> tag without &lt; or &gt; escaping.

### Step 2: Inspect Response

**Context**: Analyze the HTML to confirm reflection point.

Right-click and select "View Page Source" in the browser.

> Look for the serial value echoed back, confirming no encoding.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser]]

## Tags

- [[xss]]
- [[input-reflection]]
