---
id: proc-create-document-nextcloud
tags:
  - nextcloud
  - document-creation
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
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:39.550Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Document-in-Nextcloud

## Summary

This procedure creates a new office document in Nextcloud using the web interface, preparing it for sharing and collaborative editing in Collabora Online.

## Description

Nextcloud's file management allows users to create new documents directly, which can then be opened in the integrated Collabora Online editor. This step is essential for delivering the stored XSS payload via collaborative features, as the document serves as the vector for the session where user names are displayed.

## Requirements

1. Authenticated Nextcloud account with file creation permissions
2. Collabora Online integration enabled in the Nextcloud instance
3. Web browser access

## Defense

Defensive measures and detection strategies:

- Restrict document creation to verified users
- Log all document creation events for anomaly detection
- Scan uploaded or created files for malicious content, though this targets metadata

## Objectives

1. Generate a shareable document for collaborative use
2. Ensure compatibility with Collabora Online editing
3. Position the document for payload delivery

## Instructions

### Step 1: Navigate to Files Section

**Context**: Access the main file management area in Nextcloud.

Log in and click on the "Files" app from the top menu.

> Expected: File list view loads.

### Step 2: Initiate New Document

**Context**: Use the creation tools to start a new office file.

Click the "+" or "New" button and select "Office document" or similar (e.g., Text document).

> Expected: Collabora Online editor opens with a blank document.

### Step 3: Save the Document

**Context**: Persist the document in the file system.

Enter a name for the document (e.g., "test.docx") and save it.

> Expected: Document appears in the files list; can be reopened in Collabora.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[nextcloud]]
- [[document-creation]]
