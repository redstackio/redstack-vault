---
tags:
  - xss
  - execution
  - cookie-theft
type: procedure
tools:
  - '[[tools/Firefox-Browser]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 6c9fbd93-6b99-4bf3-b434-e8dc1302f72e
created_at: '2025-12-13T09:01:26.568Z'
updated_at: '2025-12-13T09:01:26.568Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Execute Reflected XSS via Browser to Steal Cookies

## Summary

This procedure executes a crafted XSS payload by loading a malicious URL in a browser, triggering JavaScript to steal and display session cookies.

## Description

By visiting the crafted URL in a browser while logged in, the reflected payload executes in the victim's context, potentially allowing attackers to hijack sessions. This targets web applications with unsanitized reflections, such as the Zomato OAuth endpoint, and can lead to client-side attacks like cookie exfiltration.

## Requirements

1. A web browser like [[tools/Firefox-Browser]]
2. Crafted malicious URL from prior steps
3. Victim must be logged into the target site for cookie theft

## Defense

Defensive measures and detection strategies:

- Use HttpOnly flags on cookies to prevent client-side access
- Enable XSS protection in browsers and servers
- Log and alert on suspicious URL accesses with encoded payloads

## Objectives

1. Trigger XSS execution in the browser
2. Exfiltrate cookie data via JavaScript
3. Demonstrate session hijacking potential

## Instructions

### Step 1: Load the Crafted URL

**Context**: Visit the URL to activate the reflected payload.

Open [[tools/Firefox-Browser]] and navigate to: https://auth2.zomato.com/oauth2/fallbacks/error?error=xss&error_description=xsssy&error_hint=%3Cmarquee%20loop%3d1%20width%3d0%20onfinish%3dco%5Cu006efirm(document.cookie)%3EXSS%3C%2fmarquee%3E

> The page will load and the marquee will trigger the onfinish event.

### Step 2: Observe Payload Execution

**Context**: Confirm the JavaScript runs and displays cookies.

Watch for a confirm dialog popup showing the contents of document.cookie.

> If logged in, this will include session cookies, enabling hijacking.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Firefox-Browser]]

## Tags

- [[xss]]
- [[Execution]]
