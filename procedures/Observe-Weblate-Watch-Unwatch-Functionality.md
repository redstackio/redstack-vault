---
id: proc-weblate-observe-watch-001
tags:
  - recon
  - web
  - csrf
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:27:23.341Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Observe-Weblate-Watch-Unwatch-Functionality

## Summary

This procedure involves inspecting the Watch/Unwatch feature on Weblate project pages to understand the underlying HTTP requests and identify potential security weaknesses, such as missing CSRF protections.

## Description

In a Weblate instance like hosted.weblate.org, project pages include a Watch/Unwatch button that toggles subscription to project updates and notifications. Legitimate interactions send a POST request with a CSRF token, but direct endpoint access reveals inadequate validation. This reconnaissance step is crucial for confirming the vulnerability before exploitation, targeting Django-based web applications. Expected outcomes include capturing request details and verifying token non-enforcement.

## Requirements

1. Access to a Weblate instance with authentication
2. Browser with developer tools (e.g., Chrome DevTools)
3. Knowledge of a target project slug (e.g., 'androbd')

## Defense

Defensive measures and detection strategies:

- Enable comprehensive web application firewall (WAF) rules to monitor unusual POST patterns to admin endpoints
- Implement strict CSRF token validation on all state-changing actions
- Log and alert on direct endpoint accesses without tokens

## Objectives

1. Capture legitimate watch/unwatch request details
2. Identify endpoints vulnerable to CSRF
3. Confirm action success without token for exploitation planning

## Instructions

### Step 1: Navigate to Project Page

**Context**: Locate the Watch/Unwatch interface to prepare for inspection.

Visit a project page, such as https://hosted.weblate.org/projects/androbd/, and ensure you are authenticated.

**Expected Output**: Project dashboard loads with Watch/Unwatch button visible in the top-right.

### Step 2: Interact and Inspect Request

**Context**: Trigger the action to observe network traffic and token usage.

Click the Watch/Unwatch button and open the browser's Network tab in developer tools to capture the POST request to /accounts/watch/<project>/ or /accounts/unwatch/<project>/.

**Expected Output**: Request details show POST method with CSRF token in the form data (e.g., csrfmiddlewaretoken: <value>).

### Step 3: Test Direct Access

**Context**: Verify if the endpoint enforces the token by bypassing it.

Directly enter the URL https://hosted.weblate.org/accounts/watch/androbd/ in the browser address bar while authenticated.

**Expected Output**: Action succeeds, updating subscription without prompting for or validating a token.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[web]]
- [[csrf]]
