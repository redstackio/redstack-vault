---
tags:
  - configuration
  - jira
  - jql
type: procedure
tools:
  - '[[tools/atlasboard]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T03:16:30.368Z'
sub_techniques: []
id: 6c78daa3-b0b3-42a8-88b4-bfb3050c2373
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Configure-JIRA-Integration

## Summary

This procedure configures the Atlasboard dashboard to connect to a JIRA server, specifying the server URL and JQL query to fetch issues that will later be used to display the vulnerable 'blockers' widget.

## Description

Editing the dashboard JSON file links Atlasboard to JIRA, pulling issue data including summaries. The 'blockers' widget in the integrated package fails to sanitize these summaries, setting up the XSS vector. Requires access to a JIRA instance and knowledge of project keys for JQL. Outcome: Dashboard ready to query and render JIRA data.

## Requirements

1. Access to JIRA instance with API connectivity
2. Valid JIRA project key and JQL syntax knowledge
3. Text editor for JSON configuration
4. Integrated Atlassian package from prior steps

## Defense

Defensive measures and detection strategies:

- Validate JIRA API configurations for least privilege
- Monitor outbound connections from dashboards to issue trackers
- Sanitize all external data feeds in custom widgets

## Objectives

1. Establish connection between Atlasboard and JIRA
2. Define query for fetching relevant issues
3. Ensure configuration supports vulnerable widget rendering

## Instructions

### Step 1: Edit Dashboard Configuration

**Context**: Update the example dashboard JSON to include JIRA details.

**Command** (Manual Edit):
No CLI command; use a text editor to modify 'packages/atlassian/dashboards/example1.json'.

> Set 'jira_server' to your instance URL (e.g., 'https://your-jira.atlassian.net') and 'jql' to a query like 'project = "YOUR-PROJECT" ORDER BY priority DESC'. Add authentication if needed (e.g., basic auth or token). Expected output: Valid JSON with connection params.

### Step 2: Validate Configuration

**Context**: Test the JQL in JIRA to ensure issues are retrievable.

**Command** (JIRA UI Test):
Access JIRA's issue search and run the JQL query.

> Confirm issues return without errors. Expected output: List of matching issues in JIRA.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/atlasboard]]

## Tags

- [[configuration]]
- [[jira]]
- [[jql]]
