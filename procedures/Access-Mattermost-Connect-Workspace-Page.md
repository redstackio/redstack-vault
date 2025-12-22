---
id: 123e4567-e89b-12d3-a456-426614174000
tags:
  - web
  - navigation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques: []
updated_at: '2025-12-13T23:52:39.144Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
---
# Access-Mattermost-Connect-Workspace-Page

## Summary

This procedure navigates to the Mattermost customer portal's connect-workspace page, serving as the entry point for accessing the vulnerable workspace creation functionality.

## Description

In the context of testing for self-XSS in Mattermost's customer portal, this initial step involves using a web browser to reach https://customers.mattermost.com/cloud/connect-workspace. No authentication is required for this public-facing page, and it redirects or loads the interface for workspace management. The expected outcome is successful page load without barriers, setting up for further interaction with the creation form.

## Requirements

1. Web browser with JavaScript enabled
2. Internet access to the public Mattermost domain
3. No prior credentials or sessions needed

## Defense

Defensive measures and detection strategies:

- Monitor access logs to the customer portal for unusual patterns
- Implement rate limiting on page loads to prevent automated scraping

## Objectives

1. Gain access to the workspace connection interface
2. Verify public accessibility of the portal
3. Prepare for navigation to the creation screen

## Instructions

### Step 1: Open Web Browser and Navigate

**Context**: Launch a browser and directly access the target URL to begin the attack chain.

No command required; manually enter the URL in the browser address bar: https://customers.mattermost.com/cloud/connect-workspace

> The page should load, displaying workspace connection options. If redirected, follow to the main portal.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web]]
- [[navigation]]
