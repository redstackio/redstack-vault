---
id: proc-uuid-002
tags:
  - xss
  - javascript-execution
  - trigger
  - slack
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
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:36.167Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-Execution-by-Viewing-Slack-Integration-Details

## Summary

This procedure triggers the execution of a stored XSS payload in Slack's integrations by having a victim view the affected integration details page. The lack of output encoding causes the browser to interpret and run the malicious JavaScript, allowing arbitrary code execution in the victim's authenticated session.

## Description

Once the payload is stored from the injection procedure, any user viewing the integration details on slack.com will have the payload rendered in their browser. This executes JavaScript, such as alerting or sending requests to an attacker-controlled server, as demonstrated in the proof-of-concept video. The attack relies on social engineering to lure victims to the page and targets the web platform's rendering mechanism. Outcomes include access to session cookies, DOM manipulation, or data exfiltration from the Slack workspace.

## Requirements

1. Stored payload from prior injection in the target integration
2. Victim with authenticated access to the Slack workspace
3. Method to direct the victim to view the integration (e.g., link sharing)

## Defense

Defensive measures and detection strategies:

- Apply output encoding to all stored data displayed in HTML contexts
- Implement browser-based protections like XSS auditors or strict CSP headers
- Log and alert on unusual JavaScript execution or outbound requests from Slack pages
- Educate users on phishing links related to workspace integrations

## Objectives

1. Execute arbitrary JavaScript in the victim's browser context
2. Collect sensitive data like session tokens or workspace information
3. Maintain persistence or escalate to further attacks

## Instructions

### Step 1: Share Integration Details

**Context**: Direct the victim to the integration details page to load the stored payload.

Send a link to the integration via Slack message, email, or notification, e.g., 'Check out this new integration: https://slack.com/customize/integration-details'.

> The victim must be logged in for the session context to be available.

### Step 2: Load the Page

**Context**: When the victim accesses the page, the server retrieves and displays the unsanitized payload.

No command needed; the browser automatically renders the HTML, executing the JS from the payload 'http://jeroldcamacho.com/%5Ex1s1s/slack.com.txt'.

> Expected output: JavaScript runs, e.g., network request to the attacker's domain or console alert, as per the POC video.

### Step 3: Verify Execution

**Context**: Monitor for signs of successful execution from the attacker's side.

Check server logs for incoming requests from the victim's IP or observe effects like stolen cookies being exfiltrated.

> Success is confirmed if JS executes without errors in the browser dev tools.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[javascript-execution]]
- [[slack]]
