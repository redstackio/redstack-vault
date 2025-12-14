---
tags:
  - xss
  - gitlab
  - issue
type: procedure
tools:
  - '[[tools/GitLab-CI-CD]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: low
detection_risk: medium
sub_techniques: []
id: dbd1a16c-c9cb-4249-a428-97fa70abb484
created_at: '2025-12-13T23:52:43.681Z'
updated_at: '2025-12-13T23:52:43.681Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Issue-with-SVG-Reference-in-Title

## Summary

This procedure creates a GitLab issue whose title embeds a reference to the malicious SVG using <svg><use xlink:href>, allowing the SVG to load when the issue is referenced in tooltips.

## Description

GitLab permits SVG in issue titles without full sanitization. The <use> element with xlink:href points to the raw SVG URL, pulling in the foreignObject payload. This sets up the trap for tooltip rendering.

## Requirements

1. GitLab project with write access
2. Raw URL of the malicious SVG from previous step

## Defense

Defensive measures and detection strategies:

- Sanitize issue titles to strip SVG and xlink:href attributes
- Block external SVG loads in user-generated content
- Audit issues for embedded media

## Objectives

1. Plant the SVG payload in an issue title
2. Enable loading via issue references
3. Prepare for tooltip-based exploitation

## Instructions

### Step 1: Access Issue Creation

**Context**: Navigate to the GitLab project issues.

Use the GitLab UI to create a new issue.

### Step 2: Set Malicious Title

**Context**: Input the SVG reference as the title.

Set title to: <svg><use xlink:href="https://gitlab.com/username/project/-/raw/master/xss.svg#xss"/></svg>

Submit the issue.

**Expected Output**: Issue created (e.g., #1) with the title containing the embedded SVG reference.

### Step 3: Verify Title Rendering

**Context**: Check if the title displays the SVG.

View the issue; the title should render the SVG inline without breaking.

**Expected Output**: SVG visible in title.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/GitLab-CI-CD]]

## Tags

- xss
- gitlab
