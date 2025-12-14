---
id: proc-intercept-aura-burp
tags:
  - burp-suite
  - intercept
  - aura
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T17:31:43.140Z'
skill_level: intermediate
impact_level: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-Modify-Aura-Request-Burp

## Summary

Intercept a legitimate POST request to the Salesforce Aura endpoint using Burp Suite and prepare it in Repeater for payload modification to exploit access control flaws.

## Description

The Aura framework in Salesforce handles client-server interactions; by intercepting the request from the registration page, attackers can analyze and alter it to invoke unauthorized actions like querying ContentDocument records, bypassing BAC.

## Requirements

1. Burp Suite Professional or Community edition
2. Target Salesforce instance accessible
3. Browser proxied through Burp

## Defense

Defensive measures and detection strategies:

- Validate all Aura action parameters server-side
- Log and alert on unusual request modifications (e.g., via SIEM integration)
- Use Salesforce Shield to monitor API abuse

## Objectives

1. Capture the original Aura execution request
2. Forward to Repeater for safe modification
3. Identify payload structure for exploitation

## Instructions

### Step 1: Enable Interception in Burp

**Context**: Start capturing traffic from the browser.

No command; in Burp Proxy > Intercept tab, turn on interception.

> Browse to registration page; halt on POST to /s/sfsites/aura.

### Step 2: Forward to Repeater

**Context**: Send the intercepted request to Repeater for analysis.

No command; right-click the request in Proxy history and select "Send to Repeater".

> Inspect headers (e.g., Content-Type: application/json) and message payload containing aura.ApexAction.execute.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[tools/Burp-Suite]]
- [[intercept]]
