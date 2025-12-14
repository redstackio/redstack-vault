---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - information-disclosure
  - debug-mode
  - web-vulnerability
  - credentials-leak
type: procedure
tools: []
tactics:
  - '[[Collection]]'
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:25:17.297Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
  - '[[Gather Victim Host Information]]'
---
# Detect-Debug-Mode-Information-Disclosure

## Summary

This procedure involves manually testing a web application to detect if debug mode is enabled in production, leading to the disclosure of sensitive information such as usernames, passwords, API keys, and configuration details. It exploits common misconfigurations in frameworks like Django where DEBUG=True exposes internal data via error pages or debug outputs.

## Description

In production web applications, enabling debug mode (e.g., DEBUG=True in Django settings) can inadvertently reveal sensitive backend information during error conditions. Attackers perform manual testing by accessing the site and triggering errors, such as invalid requests, to observe verbose outputs. The target environment is typically a publicly accessible web app using a server-side framework. Expected outcomes include extraction of credentials for potential unauthorized access or lateral movement. Prerequisites include only basic web access; no specialized tools are needed, making this accessible to beginners.

## Requirements

1. Publicly accessible web application URL.
2. Ability to send HTTP requests (browser or curl, though manual).
3. Knowledge of common error-triggering inputs (e.g., invalid form data).

## Defense

Defensive measures and detection strategies:

- Disable debug mode in all production configurations (set DEBUG=False).
- Implement error handling to sanitize outputs and log sensitive exposures.
- Use web application firewalls (WAF) to detect anomalous error requests.
- Regularly audit configuration files and monitor for debug keywords in logs.

## Objectives

1. Identify misconfigured debug settings exposing sensitive data.
2. Collect credentials and API keys for further exploitation.
3. Assess the application's security posture through passive observation.

## Instructions

### Step 1: Access the Web Application

**Context**: Begin by navigating to the target web application's main URL to establish a baseline interaction and look for any immediate indicators of verbose logging.

Open a web browser and visit the site's homepage. Interact normally with features like search, login, or API endpoints if exposed.

> No specific command; use browser dev tools to inspect responses for any unusual headers or content.

### Step 2: Trigger Error Conditions

**Context**: Intentionally cause server-side errors to elicit debug outputs, such as stack traces or configuration dumps.

Submit invalid data to forms (e.g., malformed login credentials) or access non-existent pages (e.g., append /nonexistent/ to the URL). Alternatively, send requests with invalid parameters to API endpoints.

For example, in a browser:

- Enter invalid search query or cause a 500 error.
- Check the error page for details like database queries, env variables, or creds.

> Observe for phrases like "DEBUG: True" or exposed vars in the HTML/JSON response.

### Step 3: Extract and Validate Sensitive Data

**Context**: Review the debug output for actionable information and verify its sensitivity.

Copy any revealed data (e.g., usernames: admin/password:secret, API_KEY=abc123). Test if the data is real by attempting low-risk uses, like checking if an API key works in a separate request.

> Success is confirmed if credentials enable access to internal systems or further recon.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection
- [[Discovery]] Discovery

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials
- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[information-disclosure]]
- [[debug-mode]]
- [[web-vulnerability]]
- [[credentials-leak]]
