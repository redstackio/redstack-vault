---
tags:
  - gitlab
  - snippets
  - sensitive-data
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - GitLab
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: e0a7faaf-d386-4904-9d35-499c154b47be
created_at: '2025-12-14T17:32:10.404Z'
updated_at: '2025-12-14T17:32:10.405Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Private-Snippet-in-GitLab-Project

## Summary

This procedure creates a private snippet within a GitLab project, storing sensitive information that can later be disclosed via the API vulnerability.

## Description

To demonstrate the impact of the GitLab API flaw, create a snippet marked as private in a public project, including mock sensitive data like API tokens. This step relies on the UI and assumes the project has snippets enabled. The snippet ID will be used in exploitation steps.

## Requirements

1. Project with snippets enabled
2. GitLab UI access
3. Sensitive data to store (e.g., test tokens)

## Defense

Defensive measures and detection strategies:

- Disable snippets in public projects
- Enforce snippet visibility audits and private-only policies for sensitive data

## Objectives

1. Store sensitive information in a private snippet
2. Obtain snippet ID for targeting
3. Simulate real-world misconfiguration

## Instructions

### Step 1: Create Snippet

**Context**: Use the project snippets interface to add a new private entry.

In the project, click Snippets > New Snippet. Set title e.g., "Secret snippet", mark as Private, and enter content like "API_TOKEN=supersecret" in the file body. Create the snippet.

> Verify the snippet appears as private in the list, accessible only to the owner.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[snippets]]
- [[sensitive-data]]
