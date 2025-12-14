---
id: 123e4567-e89b-12d3-a456-426614174004
name: Visit-ZenTao-Issue-Details-Page
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.876Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - gitlab
  - zentao
  - xss-trigger
commands: []
platforms:
  - Web
tools:
  - '[[tools/GitLab]]'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Visit-ZenTao-Issue-Details-Page

## Summary

This procedure accesses the ZenTao issue details page in GitLab, causing it to fetch and render malicious data from the configured server, injecting HTML elements.

## Description

Visiting the specific URL triggers an API call to the malicious ZenTao server, which responds with JSON containing unencoded HTML in the 'id' field and javascript: URLs in 'url', setting up the XSS without immediate execution.

## Requirements

1. Configured malicious ZenTao integration
2. Victim or attacker browser session
3. Issue ID like 'story-1' prepared on mock server

## Defense

Defensive measures and detection strategies:

- Encode all API response fields before rendering
- Implement input validation for external integrations
- Monitor outbound requests to unknown domains

## Objectives

1. Fetch malicious JSON payload
2. Render injected HTML on page
3. Display clickable elements for XSS

## Instructions

### Step 1: Construct URL

**Context**: Build the issue details URL for the project.

No command; use format https://gitlab.example.com/user1/project1/-/integrations/zentao/issues/story-1.

> Replace with actual project path and issue ID.

### Step 2: Load Page

**Context**: Visit the URL to trigger fetch.

No command; enter URL in browser.

> Expected: Page loads with breadcrumb showing injected <img> or links.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/GitLab]]

## Tags

- [[tools/GitLab]]
- [[tools/ZenTao]]
- [[xss-trigger]]
