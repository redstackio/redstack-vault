---
id: 985f6f9a-e74b-4599-97be-098cbff0f055
name: Inject-XSS-Payload-into-LocaleID-Parameter
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:12.736Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
tags:
  - xss
  - payload-injection
  - web
platforms:
  - Web
commands:
  - '[[commands/send-xss-payload-to-locale-change-endpoint]]'
tools: []
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

# Inject-XSS-Payload-into-LocaleID-Parameter

## Summary

This procedure crafts and sends a malicious GET request to the Locale-Change endpoint on teavana.com, injecting a JavaScript payload into the LocaleID parameter to exploit the lack of validation and escaping before the '_CA' suffix.

## Description

The vulnerability stems from the LocaleID parameter being reflected unescaped into a JavaScript string in the response. By injecting a payload like 'eas%27;alert(1);//dasdsan_CA', the attacker breaks out of the string using a closing quote and semicolon, executes alert(1), and comments out the rest. This occurs on the Demandware platform, and the attack requires prior session establishment. Expected outcome is payload reflection leading to execution upon page load.

## Requirements

1. HTTP client (e.g., curl, Burp Suite)
2. Knowledge of URL encoding (%27 for ')
3. Established session from initial site access

## Defense

Defensive measures and detection strategies:

- Validate and sanitize LocaleID parameter inputs
- Escape output in JavaScript contexts
- Implement Web Application Firewall (WAF) rules for XSS patterns
- Log and monitor requests to /Locale-Change endpoint

## Objectives

1. Deliver XSS payload via LocaleID
2. Achieve reflection without sanitization
3. Enable JavaScript breakout and execution

## Instructions

### Step 1: Craft the Malicious Request

**Context**: Modify the LocaleID to include the payload before '_CA' to inject into the JS string.

**Command** ([[commands/send-xss-payload-to-locale-change-endpoint]]):
```bash
curl -X GET "https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Locale-Change?LocaleID=eas%27;alert(1);//dasdsan_CA" -v
```

> This sends the GET request; verbose (-v) shows headers and response. The payload uses URL-encoded quote to close the JS string, injects alert(1), and comments out the suffix.

### Step 2: Analyze Response

**Context**: Inspect the response for reflection.

Use browser or curl output to view the HTML/JS.

> Look for: var uri = 'https:///on/demandware.store/Sites-StarbucksCA-Site/eas';alert(1);//dasdsan_CA/Home-Show'; confirming breakout.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/send-xss-payload-to-locale-change-endpoint]]

## Tools Used


## Tags

- [[xss]]
- [[payload-injection]]
- [[web]]
