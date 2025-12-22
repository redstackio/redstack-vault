---
tags:
  - xss
  - stored-xss
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 147ff86a-724b-479d-81c9-7b2bb8019e79
created_at: '2025-12-14T03:16:31.146Z'
updated_at: '2025-12-14T03:16:31.146Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Slack-File-Post

## Summary

This procedure involves navigating to Slack's file post creation endpoint and inserting a malicious JavaScript payload into the title and body fields to enable stored XSS.

## Description

In the context of Slack's file sharing feature, user-supplied content in post titles and bodies is not properly sanitized, allowing attackers with workspace access to inject JavaScript. The payload is stored server-side and later rendered when accessed via public links on www.slack-files.com, executing in the victim's browser. This can lead to client-side attacks like alerts, phishing prompts, or page defacement, though limited by the absence of cookies on the domain.

## Requirements

1. Authenticated access to a Slack workspace via web browser
2. Permission to create file posts in the workspace
3. Knowledge of a basic XSS payload, such as an onerror event handler

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output escaping for all user-controlled fields in file posts
- Use Content Security Policy (CSP) to restrict inline script execution on slack-files.com
- Monitor for anomalous JavaScript payloads in stored content via WAF or backend validation

## Objectives

1. Inject and store malicious JavaScript without triggering client-side validation
2. Prepare content for public exposure to affect unauthenticated users
3. Demonstrate vulnerability in Slack's rendering of user content

## Instructions

### Step 1: Navigate to Creation Endpoint

**Context**: Access the vulnerable form to input the payload.

Open a web browser and go to `https://subdomain.slack.com/files/create/post`, replacing 'subdomain' with your Slack workspace subdomain.

### Step 2: Enter XSS Payload

**Context**: Place the malicious code in fields that will be stored and rendered as HTML.

In both the title and body fields, input the following payload:

```
'><img src=x onerror=alert(10);>'
```

This creates a broken image tag that triggers JavaScript on error, displaying an alert.

### Step 3: Verify Payload Acceptance

**Context**: Ensure the form accepts the input without escaping.

Review the fields to confirm the payload appears unaltered before proceeding to save.

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
- [[stored-xss]]
- [[slack]]
