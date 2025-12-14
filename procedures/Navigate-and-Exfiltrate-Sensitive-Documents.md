---
id: proc-005
tags:
  - data-exfiltration
  - confidential-documents
  - dod
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:29:57.321Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[T1005.001]]'
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Navigate-and-Exfiltrate-Sensitive-Documents

## Summary

This procedure uses the bypassed access to search, view, and download confidential documents from the DoD application, focusing on aircraft and missile issues.

## Description

With authenticated access achieved, the attacker navigates the application's guest interfaces to query messages and retrieve attachments. Endpoints like /Guest/MessageSearch.aspx and /Guest/MessagesDetails.aspx expose sensitive data without further checks. This leads to exfiltration of classified information. Prerequisites: Successful bypass from prior procedure.

## Requirements

1. Bypassed access to the application
2. Web browser for navigation and downloads
3. Local storage for saving files

## Defense

Defensive measures and detection strategies:

- Implement data loss prevention (DLP) on downloads
- Audit logs for unusual searches and file accesses
- Encrypt sensitive documents and require additional auth for downloads

## Objectives

1. Search for relevant messages
2. View details and attachments
3. Download and exfiltrate data

## Instructions

### Step 1: Search Messages

**Context**: Use the sidebar to access the search functionality and query for sensitive topics.

**Command** (Browser Navigation):

Navigate to /Guest/MessageSearch.aspx and perform searches (e.g., keywords like 'aircraft issues').

> Results display messages related to confidential topics.

### Step 2: View and Download Details

**Context**: Click into search results to access details and attachments.

**Command** (Browser Navigation):

Go to /Guest/MessagesDetails.aspx for selected messages and download documents.

> Files containing aircraft/missile data can be saved locally.

**Expected Output**: Downloaded files with sensitive content, such as PDFs or reports on DoD systems.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Local System]] Data from Local System

### Sub-Techniques

- [[T1005.001]] Web Browser

## Commands Used

- None

## Tools Used

- None

## Tags

- [[data-exfiltration]]
- [[confidential-documents]]
- [[dod]]
