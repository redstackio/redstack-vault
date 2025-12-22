---
id: proc-initiate-malicious-bulk-import-ui
tags:
  - bulk-import
  - ui-exploit
  - injection
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:14.607Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
  - '[[Exploit Public-Facing Application]]'
---
# Initiate-Malicious-Bulk-Import-via-UI

## Summary

This procedure triggers the bulk import in GitLab UI using the ngrok-tunneled mock API URL and API token, causing GitLab to query the mock for malicious import_source and template_name, leading to command injection during archive validation.

## Description

In the GitLab web interface, start a group import specifying the ngrok URL as the source, authenticate with the API token, select the mocked group/project, set no parent namespace, and name the destination. This invokes the ProjectPipeline, passing uncontrolled params to Projects::CreateService and ultimately the vulnerable validator.

## Requirements

1. Valid GitLab session as maintainer
2. Ngrok URL and API token ready
3. BulkImports feature enabled

## Defense

Defensive measures and detection strategies:

- Sanitize all import parameters in transformers (e.g., block shell chars)
- Require admin approval for bulk imports
- Log and alert on import_source containing paths with metacharacters

## Objectives

1. Start the import pipeline with malicious source
2. Trigger GraphQL queries to mock API
3. Execute the injection in validator after timeout

## Instructions

### Step 1: Navigate to Import UI

**Context**: Access the bulk import interface.

**Instructions**: Log in to GitLab, go to New > New group > Import group tab.

### Step 2: Configure and Start Import

**Context**: Enter details to initiate payload delivery.

**Instructions**: Paste ngrok URL (e.g., https://abc123.ngrok.io), API token, select source group from mock, set 'No parent' for destination, enter new group name (e.g., 'imported'), click 'Import group'. Optional: Proxy through Burp on 8080 for interception.

> Import job starts; monitor logs for progress.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Unix Shell]] Unix Shell
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- bulk-import
- ui-exploit
