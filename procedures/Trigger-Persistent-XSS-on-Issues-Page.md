---
id: proc-gitlab-trigger-xss-issues-page
tags:
  - xss
  - trigger
  - token-exfiltration
  - gitlab
type: procedure
tools: []
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
  - '[[Cloud Instance Metadata API]]'
updated_at: '2025-12-14T03:16:31.006Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Cloud Instance Metadata API]]'
---
# Trigger-Persistent-XSS-on-Issues-Page

## Summary

This procedure triggers the persistent XSS by rendering the project's Issues page, executing the injected javascript: URI in the victim's browser to leak the API token and enable account takeover.

## Description

Once the payload is stored, viewing the Issues page (/projects/:id/issues) renders the malicious URI as a link. Browser handling of javascript: schemes executes the code, accessing client-side data like window.gon.api_token for exfiltration, potentially leading to unauthorized project access and data exposure.

## Requirements

1. Victim access to the public project Issues page.
2. Injected payload in the custom issue tracker.
3. Victim's browser must support javascript: URI execution.

## Defense

Defensive measures and detection strategies:

- Escape or neutralize javascript: URIs in rendered links.
- Content Security Policy (CSP) to block inline JS execution.
- Monitor for anomalous JS alerts or network requests from Issues pages.

## Objectives

1. Execute arbitrary JS in victim's context.
2. Exfiltrate sensitive credentials like API tokens.
3. Achieve account takeover and lateral movement.

## Instructions

### Step 1: Direct Victim to Issues Page

**Context**: Lure the victim to the vulnerable endpoint.

Share the project URL and instruct to click "Issues" or directly link to /projects/:id/issues.

### Step 2: Render the Page

**Context**: Load the page to display the injected link.

The Issues page fetches and renders the custom tracker configuration, including the Project URL as a clickable element.

**Expected Output**: Malicious link visible on the page.

### Step 3: Execute Payload

**Context**: Trigger JS via interaction or auto-load.

Clicking the link (or if auto-executing) runs the javascript: code, e.g., alerting or sending window.gon.api_token to an attacker endpoint.

**Expected Output**: JS execution; token leaked via alert or fetch request.

**Success Indicators**:
- JS runs in victim's browser.
- API token captured by attacker.
- Follow-on API abuse possible.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Cloud Instance Metadata API]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[token-exfiltration]]
