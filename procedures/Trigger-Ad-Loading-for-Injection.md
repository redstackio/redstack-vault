---
id: proc-uuid-2
tags:
  - ads
  - script-loading
  - injection-trigger
type: procedure
tools:
  - '[[tools/Eval-Villain]]'
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
updated_at: '2025-12-14T00:11:15.771Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Ad-Loading-for-Injection

## Summary

This procedure loads the crafted URL in a browser to trigger third-party ad scripts, which inject the vulnerable URL into JavaScript via document.write, setting up the XSS execution.

## Description

Ad providers like lijit.com load pwt.js on the page, calling displayCreative that uses document.write to embed the page URL in single-quoted strings. The malicious URL causes an escape during this injection. This occurs in a standard web browsing environment, leading to payload readiness. Prerequisites: Crafted URL from prior procedure and Eval Villain installed.

## Requirements

1. Firefox browser with Eval Villain extension active.
2. Stable internet connection for ad fetches.
3. Crafted URL ready.

## Defense

Defensive measures and detection strategies:

- Implement ad blockers or CSP to restrict third-party script behaviors.
- Log and audit document.write calls in ad integrations.
- Escape all dynamic URLs in client-side scripts.

## Objectives

1. Initiate ad script execution with the malicious URL.
2. Ensure injection occurs without page breakage.
3. Prepare for observation of escaped payload.

## Instructions

### Step 1: Navigate to Crafted URL

**Context**: Load the page to start ad requests.

Enter https://www.urbandictionary.com/define.php?term=#asdf'-alert(document.domain)-'asdf in Firefox.

> Page renders with definition content; ads begin loading asynchronously.

### Step 2: Enable Monitoring

**Context**: Activate the extension to track script injections.

Ensure Eval Villain is enabled via browser extensions menu.

> Extension icon active; ready to log dangerous function calls.

### Step 3: Wait for Ad Load

**Context**: Allow time for external ad scripts to fetch and execute.

Pause for 10-30 seconds or until ads visibly appear.

> Console may show network requests to lijit.com; no errors indicate successful load.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Eval-Villain]]

## Tags

- [[ads]]
- [[JavaScript]]
- [[document-write]]
