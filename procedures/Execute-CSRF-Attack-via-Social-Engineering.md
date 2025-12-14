---
id: 123e4567-e89b-12d3-a456-426614174003
name: Execute-CSRF-Attack-via-Social-Engineering
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:15.450Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Drive-by Compromise]]'
sub_techniques: []
tags:
  - csrf
  - social-engineering
  - drive-by
platforms:
  - Web
commands: []
tools: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---

# Execute CSRF Attack via Social Engineering

## Summary

This procedure outlines delivering crafted CSRF PoC pages to authenticated administrators through social engineering, resulting in unauthorized execution of state-changing actions in Concrete CMS 5.7.3.1.

## Description

With PoC HTML pages ready, the attack relies on tricking victims into visiting the malicious site while their session is active. This drive-by compromise forces submissions to endpoints like user group management or translation saves, potentially chaining with other vulns like stored XSS for greater impact. The scenario targets web admins in a PHP environment, with outcomes including system configuration changes or data loss.

## Requirements

1. Hosted malicious HTML pages accessible via URL
2. Knowledge of victim's email or communication channels for phishing
3. Active authenticated session on the target CMS for the victim

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens universally and validate on all POSTs
- Use anti-phishing training and URL scanners
- Log and alert on suspicious admin actions (e.g., sudden file deletions)

## Objectives

1. Lure victim to malicious page for automatic form submission
2. Achieve unauthorized actions like enabling registration or deleting files
3. Verify impact through application state changes

## Instructions

### Step 1: Prepare Delivery Mechanism

**Context**: Set up a way to direct the victim to the PoC page without suspicion.

Host the HTML on a server (e.g., via GitHub Pages or simple HTTP) and craft a phishing email or link disguised as a legitimate update or report.

### Step 2: Distribute the Link

**Context**: Use social engineering to get the admin to click and load the page.

Send an email like "Review this urgent dashboard update: [malicious-link]" to the target admin, ensuring they are logged into the CMS.

### Step 3: Monitor and Confirm Execution

**Context**: Observe the results of the forced submission.

Check the CMS for changes (e.g., files deleted, groups modified) or use server logs to confirm the POST request originated from the malicious referrer.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[social-engineering]]
- [[drive-by]]
