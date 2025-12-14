---
id: proc-uuid-002
tags:
  - xss
  - payload-crafting
  - javascript
  - discourse
type: procedure
tools: []
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
updated_at: '2025-12-14T03:46:37.877Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Malicious-Image-URL-for-XSS

## Summary

This procedure details crafting a malformed image URL that exploits the Discourse markdown parser's lack of quote escaping to inject an onerror JavaScript handler, enabling arbitrary code execution on render.

## Description

The payload uses a single quote to prematurely close the src attribute in the generated <img> tag, followed by injected attributes like onerror=alert(1), and terminates with // to comment out trailing content. A .png extension is appended to maintain the appearance of a valid image URL. This targets web browsers viewing Discourse posts, with prerequisites being knowledge of the vulnerability from prior identification. Expected outcomes include successful JS execution, such as alerts or script loading via $.getScript for further compromise.

## Requirements

1. Understanding of HTML attribute injection
2. Test environment for payload validation (e.g., local HTML file simulating parser output)
3. JavaScript knowledge for payload customization

## Defense

Defensive measures and detection strategies:

- Sanitize all URLs by escaping quotes and restricting attribute injection
- Employ HTML entity encoding for user inputs in markdown
- Use browser extensions or WAF rules to detect onerror patterns

## Objectives

1. Create a functional XSS payload for Discourse image links
2. Ensure payload evades basic validation by mimicking valid URLs
3. Test for execution of arbitrary JS, like data exfiltration

## Instructions

### Step 1: Base URL Construction

**Context**: Start with a legitimate-looking base URL to avoid immediate flagging.

Choose a host and path: http://example.com/path/to/image

> This forms the src value up to the injection point.

### Step 2: Inject Breakout and Attribute

**Context**: Add the single quote to close src and inject onerror.

Append 'onerror=alert(1);// to the URL: http://example.com/path/to/image'onerror=alert(1);//

> The quote closes src="...image'", then adds onerror="alert(1)//".

### Step 3: Append Extension and Test

**Context**: Finalize to look like an image and validate.

Add .png: http://example.com/path/to/image'onerror=alert(1);//.png

Use in markdown: ![test](payload-url) and render in a browser.

> Expected output: Alert box on image load failure, confirming execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[payload-crafting]]
- [[JavaScript]]
