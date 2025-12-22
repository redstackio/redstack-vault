---
id: uuid-trigger-xss
tags:
  - xss-trigger
  - document-view
  - link-click
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:20.005Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Access-Swiftype-Document-Details-to-Trigger-XSS

## Summary

This procedure navigates to the Swiftype document list and details page, then triggers the stored XSS by clicking the vulnerable 'View on your site' link, executing the injected JavaScript payload.

## Description

Once the payload is stored, any user with access (admin or viewer) can trigger it by viewing the document details at https://app.swiftype.com/engines/<engine>/document_types/<type>/documents/<id>. The 'url' field is rendered as an href without encoding, allowing javascript: URIs to execute on click. This step demonstrates the client-side impact, such as alert popups or session theft via more advanced payloads. Prerequisites: Injected document and login as an authorized user.

## Requirements

1. Login credentials for Swiftype account (admin/viewer role)
2. Engine ID, document type, and external_id from injection step
3. Web browser to access the app UI

## Defense

Defensive measures and detection strategies:

- Sanitize all user-controlled fields before rendering in HTML attributes
- Use Content Security Policy (CSP) to block inline JavaScript execution
- Audit document views for anomalous behavior (e.g., unexpected alerts)
- Role-based access controls to limit who can view API documents

## Objectives

1. Locate and access the injected document in the UI
2. Trigger payload execution via link interaction
3. Demonstrate potential for broader client-side attacks

## Instructions

### Step 1: Navigate to Document List

**Context**: View the list of documents to find the injected one.

Visit https://app.swiftype.com/engines/123/document_types/test/documents#q=&page=1 and search for external_id v1uyQZNg2vE.

> Expected output: Document listed with title and other fields.

### Step 2: Open Document Details

**Context**: Access the details page where the vulnerable link is rendered.

Click on the document ID to load https://app.swiftype.com/engines/123/document_types/test/documents/v1uyQZNg2vE.

> Expected output: Details page loads with 'View on your site' link showing the malicious URL.

### Step 3: Trigger the XSS

**Context**: Interact with the link to execute the payload.

Click the 'View on your site' link, which executes javascript:alert(1).

> Expected output: Browser alert dialog appears, confirming XSS execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss-trigger
- document-view
- link-click
