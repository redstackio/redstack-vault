---
url: 'https://chromewebstore.google.com/detail/h1-triage-wizard/...'
tags:
  - browser-extension
  - triage
  - hackerone
type: tool
verified: false
platforms:
  - Chrome Browser Extension
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T00:11:09.480Z'
id: dfa80db3-c410-4faf-8cb1-dccff62df13c
validated: true
submitted: true
---
# H1-Triage-Wizard-Chrome-Extension

**Status**: Unverified

## Overview

The H1 Triage Wizard is a Chrome extension for HackerOne users to streamline vulnerability report triaging, including a beta questionnaire modal. It is used here to demonstrate HTML injection vulnerabilities leading to stored XSS.

## Description

This extension integrates with HackerOne.com to provide context menus for report analysis, loading stored questionnaire responses into modals. A flaw in its JavaScript allows unsanitized HTML interpolation via .replace(), enabling XSS attacks that could compromise user data integrity in the browser.

## Features

- Feature 1: Context menu for 'View Triage Questionnaire (Beta)'
- Feature 2: Interpolation of stored responses into HTML templates
- Feature 3: Integration with HackerOne report pages for seamless triaging

## Installation

### Requirements

- Google Chrome browser
- Access to Chrome Web Store

### Install Commands

No CLI install; use browser UI:

1. Visit Chrome Web Store
2. Search "H1 Triage Wizard"
3. Click "Add to Chrome"

## Basic Usage

Enable in chrome://extensions/ and right-click on HackerOne reports to access features.

### Common Options

| Option | Description |
|--------|-------------|
| Enable/Disable | Toggle in extensions page |
| Permissions | Grants access to hackerone.com domains |

## Examples

### Example 1: Basic Usage

Right-click a report on hackerone.com and select triage option.

### Example 2: Advanced Usage

Pre-populate questionnaire responses via extension storage, then trigger modal to observe injections.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Presence in chrome://extensions/
- Network requests to hackerone.com with extension headers
- Console logs from buildTriageQuestionnaireModal function

## Related Procedures


## Related Tools


## References

- HackerOne Report: https://hackerone.com/reports/1874260
- Chrome Web Store listing
