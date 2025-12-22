---
id: 123e4567-e89b-12d3-a456-426614174001
name: Access-Slack-Account-Preferences
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:53.320Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - xss
  - slack
  - web
commands: []
platforms:
  - Web
tools: []
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Access-Slack-Account-Preferences

## Summary

This procedure outlines how to navigate to Slack's account preferences page, specifically targeting the highlight words feature, as a prerequisite for exploiting the stored XSS vulnerability.

## Description

In the context of testing Slack's web application, accessing the account preferences page via the browser allows interaction with user-configurable settings. The page at `https://<workspace>.slack.com/account/preferences?updated_highlight_words=1` loads the highlight words textarea, which is vulnerable to stored XSS due to improper sanitization. This step requires an authenticated session and sets up the environment for payload injection. Expected outcomes include visibility of the input field, enabling subsequent exploitation.

## Requirements

1. Valid Slack user account credentials for authentication
2. Web browser with JavaScript enabled
3. Internet access to the Slack web application

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls to limit preferences modifications
- Monitor for unusual navigation patterns to preferences endpoints
- Use client-side CSP to restrict script execution on preference pages

## Objectives

1. Gain access to the vulnerable highlight words configuration
2. Verify the textarea input is present and editable
3. Prepare for payload injection without triggering alerts

## Instructions

### Step 1: Authenticate and Navigate

**Context**: Log in to Slack and directly access the preferences page to avoid intermediate menus.

No specific command required; use browser navigation:

- Log in at `https://<workspace>.slack.com`
- Navigate to `https://<workspace>.slack.com/account/preferences?updated_highlight_words=1`

> This URL parameter triggers the highlight words section. Successful access shows the preferences interface.

### Step 2: Verify Page Load

**Context**: Confirm the highlight words textarea is loaded and ready for input.

Inspect the page source or visually check for the textarea element.

> Look for `<textarea>` tag associated with highlight words. If present, proceed to injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[slack]]
- [[web]]
