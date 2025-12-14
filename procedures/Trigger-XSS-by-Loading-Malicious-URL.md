---
tags:
  - xss-execution
  - browser-trigger
  - javascript
type: procedure
tools:
  - '[[tools/Firefox-Browser]]'
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
updated_at: '2025-12-14T03:16:31.049Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: eae98f5b-01b2-43f9-83c5-bd4192ba526e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-by-Loading-Malicious-URL

## Summary

This procedure triggers the reflected XSS vulnerability by loading the crafted malicious URL in a web browser, resulting in immediate JavaScript execution within the victim's context.

## Description

Targeting the Uber careers page, this step simulates a victim visiting a phishing link. The reflected 'city' parameter executes the injected script on page load, as seen with the alert payload. In a production scenario, this could steal cookies, redirect to fake logins, or deface the page. The attack relies on social engineering to deliver the URL and assumes no browser protections like XSS filters are enabled.

## Requirements

1. Crafted malicious URL from prior procedure
2. Web browser such as Firefox (version 44.0.2)
3. Internet access to the target site

## Defense

Defensive measures and detection strategies:

- Deploy browser-based protections like XSS auditors or extensions (e.g., NoScript)
- Server-side: Sanitize all reflected inputs and use HTTPOnly/Secure flags on cookies
- Log and alert on suspicious script executions via WAF

## Objectives

1. Execute arbitrary JavaScript in the browser
2. Verify vulnerability by observing the alert
3. Demonstrate client-side impact like data exfiltration potential

## Instructions

### Step 1: Open Browser

**Context**: Launch the browser to prepare for URL loading.

Use [[tools/Firefox-Browser]].

> Expected output: Browser window open and ready.

### Step 2: Navigate to Malicious URL

**Context**: Enter the full crafted URL to trigger reflection and execution.

Paste and load: `https://www.uber.com/careers/list/?city=allicg</script><script>alert('xss by pavanw3b')</script>fupaiiz&country=all&keywords=&subteam=all&team=all`.

> Explanation: The page loads normally, but the injected script executes, popping an alert. Check browser console for any errors.

### Step 3: Validate Execution

**Context**: Confirm the XSS fired successfully.

Observe the alert box with 'xss by pavanw3b'.

> Expected output: Alert dialog appears, proving code execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox-Browser]]

## Tags

- xss-trigger
- browser-execution
