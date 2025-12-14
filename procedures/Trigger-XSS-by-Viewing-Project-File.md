---
tags:
  - xss
  - execution
  - browser
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:03.658Z'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
id: 38d98e66-bf09-4899-ab58-09cba8d239d5
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger XSS by Viewing Project File

## Summary

This procedure executes the stored XSS payload by rendering the project file containing the malicious emoji reference in a web browser, leading to JavaScript execution in the viewer's context.

## Description

When the README.md file is viewed, GitLab's markdown renderer calls emoji_image_tag, inserting the unescaped img tag with the onerror payload. This executes alert(location) or more dangerous code like session theft. The attack affects any authenticated or public user viewing the file, demonstrating the stored nature of the XSS in a collaborative environment like GitLab.

## Requirements

1. Web browser access to the GitLab instance
2. URL to the project file (e.g., /group/project/-/blob/main/README.md)
3. No CSP blocking inline scripts (common in GitLab setups)

## Defense

Defensive measures and detection strategies:

- Patch GitLab to version fixing CVE (escape src in emoji_image_tag)
- Monitor browser console for onerror events and alerts
- Use browser extensions or proxies to detect XSS payloads

## Objectives

1. Execute the injected JavaScript in the victim's browser
2. Demonstrate impact like data exfiltration or hijacking
3. Validate the full exploit chain

## Instructions

### Step 1: Navigate to File

**Context**: Load the project file URL in a browser to trigger rendering.

**Command** (Browser):
Enter URL like https://gitlab.example.com/xss_target/test-project/-/blob/main/README.md.

> Expected output: Page loads with rendered markdown, emoji img tag inserted.

### Step 2: Observe Execution

**Context**: The onerror event fires due to invalid src, running the payload.

**Command** (Passive):
View the page; no input needed.

> Expected output: Alert dialog with current URL; inspect element shows injected img tag.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Web-Browser]]

## Tags

- xss
- trigger
