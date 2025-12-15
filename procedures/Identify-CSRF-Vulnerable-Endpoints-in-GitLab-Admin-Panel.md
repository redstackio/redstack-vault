---
id: 123e4567-e89b-12d3-a456-426614174001
name: Identify CSRF Vulnerable Endpoints in GitLab Admin Panel
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:57.419Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Drive-by Compromise]]'
sub_techniques: []
tags:
  - csrf
  - gitlab
  - recon
commands: []
platforms:
  - Web
  - GitLab
tools: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---

# Identify CSRF Vulnerable Endpoints in GitLab Admin Panel

## Summary

This procedure involves inspecting GitLab's admin panel to identify endpoints for pausing and resuming CI/CD runners that lack CSRF protection, allowing forged requests from external sources.

## Description

In GitLab, the admin panel provides endpoints to manage CI/CD runners, such as pausing or resuming them. Testing reveals that the URLs /admin/runners/:runner_id/resume and /admin/runners/:runner_id/pause do not validate CSRF tokens, enabling attackers to perform state-changing actions via cross-site requests. This is typically discovered by reviewing network requests during normal admin operations or by directly testing POST requests without tokens. The procedure assumes access to a GitLab instance for testing and focuses on confirmation of the vulnerability.

## Requirements

1. Access to a GitLab instance with admin privileges for testing
2. Web browser developer tools (e.g., Chrome DevTools) to inspect requests
3. Knowledge of the runner ID (obtainable from the admin runners list)

## Defense

Defensive measures and detection strategies:

- Implement CSRF token validation on all state-changing admin endpoints
- Use SameSite cookies and monitor for anomalous runner status changes in logs
- Educate admins on phishing risks and verifying unexpected runner actions

## Objectives

1. Confirm lack of CSRF protection on runner management endpoints
2. Document vulnerable URLs for exploitation planning
3. Assess potential impact on CI/CD workflows

## Instructions

### Step 1: Access Admin Panel and List Runners

**Context**: Log in as an admin and navigate to the runners management section to obtain runner IDs.

Go to http://{gitlab_instance}/admin/runners in your browser. Note the ID of a target runner from the list.

**Expected Output**: List of runners with their IDs visible.

### Step 2: Test Endpoint Without CSRF Token

**Context**: Send a POST request to the resume or pause endpoint without including a CSRF token to verify if the action succeeds.

Use browser dev tools or a tool like curl to simulate the request. For example, in dev tools console or via a simple script:

Replace {gitlab_instance} and {runner_id} with actual values, and ensure you are authenticated (cookies/session active).

**Expected Output**: Server responds with success (e.g., 200 OK) and runner status updates in the panel.

### Step 3: Confirm Vulnerability

**Context**: Repeat for both pause and resume endpoints to ensure consistency.

Check the admin panel to verify the status change occurred without intentional action.

**Expected Output**: Unauthorized status change confirms CSRF vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[gitlab]]
- [[recon]]
