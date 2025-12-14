---
id: proc-uuid-1
tags:
  - gitlab
  - export
  - recon
type: procedure
tools:
  - '[[tools/GitLab]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:56:03.869Z'
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
# Export-GitLab-Project-with-Discussions

## Summary

This procedure exports a GitLab project containing merge request discussions to obtain the project.json file, which includes Note objects vulnerable to manipulation for XSS injection.

## Description

In the context of exploiting persistent XSS in GitLab, this initial step involves creating or selecting a project with discussions and exporting it to access the serialized Note data. The export process reveals the structure of Note objects, including note_html and cached_markdown_version fields, analyzed from GitLab's CacheMarkdownField concern. This sets up the attack by providing a modifiable JSON file without triggering immediate security checks.

## Requirements

1. Authenticated GitLab account with project creation and export permissions
2. A project with at least one merge request containing discussions
3. Access to GitLab UI via web browser

## Defense

Defensive measures and detection strategies:

- Monitor export activities for unusual patterns in project data
- Implement rate limiting on project exports/imports
- Audit logs for export requests from user accounts

## Objectives

1. Obtain project.json with Note objects for manipulation
2. Identify cache invalidation logic flaws
3. Prepare data for XSS payload injection

## Instructions

### Step 1: Create or Select Project

**Context**: Ensure the project has merge request discussions to include Note objects in the export.

Log in to GitLab and navigate to a project. If needed, create a merge request and add a discussion note.

### Step 2: Initiate Export

**Context**: Trigger the export to generate the archive with project.json.

In the project settings, select 'Export project' and wait for the download link. Download the .tar.gz archive.

**Expected Output**: Archive file containing project.json with discussions array.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/GitLab]]

## Tags

- [[tools/GitLab]]
- [[export]]
- [[recon]]
