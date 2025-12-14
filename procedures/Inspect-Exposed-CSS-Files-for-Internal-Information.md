---
id: proc-uuid-5678
tags:
  - information-disclosure
  - css-exposure
  - sass
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-retrieve-css]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Software]]'
updated_at: '2025-12-14T03:16:08.046Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Software]]'
---
# Inspect-Exposed-CSS-Files-for-Internal-Information

## Summary

This procedure involves accessing and analyzing publicly available CSS files that have not been properly compiled or minified, revealing internal development details such as original SASS code, source maps, comments, and versioning information. It is primarily used in reconnaissance phases to gather non-public insights about a target's development practices without requiring authentication or advanced exploitation.

## Description

In web applications, CSS files are often served in production after compilation and minification to remove development artifacts. However, misconfigurations can lead to serving raw, unprocessed files, exposing sensitive comments, style guides, build metadata, and even hints about the technology stack. This procedure targets such exposures by directly requesting the stylesheet URL, downloading the content, and inspecting it for actionable intelligence. The attack scenario applies to any public-facing website where asset paths are guessable or documented. Expected outcomes include identification of internal notes that could inform further attacks, such as revealing custom class names or debugging information. Prerequisites include basic web access and tools like curl or a browser.

## Requirements

1. Internet connectivity to reach the target website
2. Access to a command-line tool like curl (or a web browser for manual inspection)
3. Knowledge of the target site's asset paths (e.g., /assets/application.css)

## Defense

Defensive measures and detection strategies:

- Ensure all CSS files are compiled, minified, and stripped of comments/source maps before deployment using build tools like Webpack or Gulp
- Implement web application firewalls (WAF) to monitor and block unusual requests to asset paths
- Regularly audit public asset exposure using tools like OWASP ZAP or automated scanners

## Objectives

1. Retrieve unprocessed CSS content from a public endpoint
2. Extract internal development artifacts for reconnaissance
3. Assess potential for further information gathering based on disclosed details

## Instructions

### Step 1: Identify and Request the CSS File

**Context**: Locate the publicly accessible CSS file URL, typically found in the site's HTML source or common asset paths, and fetch it using a simple HTTP request to avoid alerting security systems.

**Command** ([[commands/curl-retrieve-css]]):
```bash
curl https://hackerone.com/assets/application.css -o application.css
```

> This command downloads the CSS file to a local file named application.css. Expected output is the raw file content saved locally, which may include unminified code if the server is misconfigured. Verify the download size and content type (should be text/css).

### Step 2: Analyze the File Contents

**Context**: Inspect the downloaded file for development artifacts. Use a text editor or grep to search for indicators like SASS syntax (e.g., $variables), comments (/* ... */), or source map URLs.

**Command** ([[commands/curl-retrieve-css]] with grep for analysis):
```bash
grep -i "sourceMappingURL" application.css
```

> This searches for source map references, which indicate unprocessed builds. Expected output includes lines with /*# sourceMappingURL=... */, confirming exposure. Manually review for comments containing internal notes or style guides.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Software]]

### Sub-Techniques


## Commands Used

- [[commands/curl-retrieve-css]]

## Tools Used


## Tags

- information-disclosure
- css-exposure
- sass
- reconnaissance
