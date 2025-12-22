---
id: proc-gitlab-access-grafana
tags:
  - gitlab
  - admin-access
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T00:11:15.945Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
---

# Access-GitLab-Admin-Grafana-Settings

## Summary

This procedure outlines how to navigate to the GitLab admin panel's Grafana dashboard settings, a prerequisite for exploiting the stored XSS vulnerability in the URL input field.

## Description

In GitLab instances, administrators can configure monitoring tools like Grafana via the admin application settings. The Grafana domain URL field is vulnerable to stored XSS because it accepts arbitrary inputs without protocol validation. This procedure assumes admin privileges and direct access to the web interface, targeting Ruby on Rails-based GitLab deployments.

## Requirements

1. Valid GitLab administrator credentials
2. Network access to the GitLab instance (e.g., http://example.gitlab.com)
3. Modern web browser

## Defense

Defensive measures and detection strategies:

- Implement role-based access control to limit admin panel access
- Monitor admin setting changes via audit logs in PostgreSQL or Sidekiq
- Use web application firewalls (WAF) to detect anomalous URL patterns in admin inputs

## Objectives

1. Gain access to the vulnerable configuration page
2. Verify the Grafana settings section is editable
3. Prepare for payload injection without triggering alerts

## Instructions

### Step 1: Log In as Administrator

**Context**: Authenticate to the GitLab instance to access privileged areas.

Navigate to the login page and enter admin credentials.

**Expected Output**: Successful login redirect to the dashboard.

### Step 2: Navigate to Admin Settings

**Context**: Access the application settings section focused on metrics.

From the top menu, go to Admin Area > Settings > General > Metrics and Profiling, or directly visit http://example.gitlab.com/admin/application_settings/metrics_and_profiling#js-grafana-settings.

**Expected Output**: Page loads with the Grafana domain URL field visible and editable.

**Success Indicators**:
- No permission errors
- URL field accepts input

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[gitlab]]
- [[admin-access]]

---
