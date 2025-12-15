---
id: proc-uuid-1
tags:
  - csrf
  - web
  - testing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:57.690Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Flickr-Account-Deletion-Feature

## Summary

This procedure involves accessing and testing Flickr's account deletion form to observe its functionality and security features, serving as the initial step in identifying potential vulnerabilities like CSRF.

## Description

In the context of Flickr's transition from Yahoo authentication to SmugMug's login flow, this procedure tests the deletion endpoint at https://www.flickr.com/account/delete. It requires an authenticated session and uses browser tools to inspect the form, revealing the absence of modern protections. Expected outcomes include confirmation of form accessibility and basic submission behavior, setting the stage for deeper analysis.

## Requirements

1. Authenticated Flickr account via https://identity.flickr.com/
2. Web browser with developer console (e.g., Chrome DevTools)
3. Internet access to Flickr services

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing forms
- Monitor for anomalous deletion requests from unusual referers
- Use same-site cookie policies to mitigate cross-site requests

## Objectives

1. Verify access to the account deletion form
2. Observe form submission mechanics
3. Identify initial security gaps

## Instructions

### Step 1: Authenticate and Access Form

**Context**: Log in to establish a session and navigate to the target page.

Open a web browser and go to https://identity.flickr.com/ to log in with valid credentials. Once authenticated, visit https://www.flickr.com/account/delete to load the deletion form.

### Step 2: Inspect Form Elements

**Context**: Use developer tools to examine the HTML structure for security features.

Right-click the form and select "Inspect Element." Look for input fields, especially hidden ones for tokens. Check the action URL and method (should be POST to /account/delete).

### Step 3: Test Submission

**Context**: Simulate a deletion without completing it to understand the flow.

Fill in any required fields (e.g., confirmation text) and submit the form. Observe the network request in the DevTools Network tab for headers and payloads.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web]]
- [[testing]]
