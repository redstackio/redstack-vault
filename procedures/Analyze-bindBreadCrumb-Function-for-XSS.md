---
tags:
  - xss
  - code-review
  - javascript
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '[TIMESTAMP]'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:31.692Z'
sub_techniques: []
id: f977d35f-dc3d-4c71-9018-d8a8337fbcbd
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Analyze-bindBreadCrumb-Function-for-XSS

## Summary

This procedure involves reviewing the JavaScript code of the bindBreadCrumb function on kb.informatica.com to detect DOM-based XSS vulnerabilities stemming from unencoded insertions of user-controlled values like document.referrer into HTML attributes.

## Description

The bindBreadCrumb function executes after document load via $(document).ready and constructs breadcrumb links using insecure string concatenations, such as strChild = '<a href="' + varDocumentReferrer + '" style="color:#999 !important;" >Search Results</a>';. Without proper escaping, this allows JavaScript injection in href attributes when varDocumentReferrer is controlled, leading to execution on user interactions like mouseover. This targets pages like /solution/4/Pages/17377.aspx and requires code review tools or manual inspection.

## Requirements

1. Access to the target's JavaScript source code (via browser dev tools or download)
2. Knowledge of JavaScript and DOM manipulation
3. Browser developer tools for inspection

## Defense

Defensive measures and detection strategies:

- Implement output encoding for HTML attributes (e.g., using DOMPurify or manual escaping)
- Validate and sanitize inputs like document.referrer before insertion
- Use Content Security Policy (CSP) to restrict inline scripts and eval
- Monitor for anomalous referrer patterns in logs

## Objectives

1. Identify vulnerable code patterns in bindBreadCrumb
2. Confirm sources of untrusted data (document.referrer, document.URL, etc.)
3. Assess potential for JavaScript injection in href

## Instructions

### Step 1: Locate and Inspect JavaScript

**Context**: Access the JavaScript file containing bindBreadCrumb and search for the function definition.

Inspect the code around $(document).ready(function(){ bindBreadCrumb(); }); to find assignments using varDocumentReferrer = document.referrer;

### Step 2: Identify Insecure Concatenations

**Context**: Scan for string building in anchor tags without encoding.

Look for patterns like strChild = '<a href="' + varDocumentReferrer + '" ... >Search Results</a>'; and note lack of escaping for quotes or event handlers.

### Step 3: Document Vulnerable Points

**Context**: List all affected variables and locations.

Note insertions of document.URL, varCoveoSearchResultPageURL, varDocumentReferrer, and varStaticCoveoSearchResultPageURL into href attributes.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[code-review]]
- [[JavaScript]]
