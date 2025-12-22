---
id: proc-uuid-001
tags:
  - code-review
  - source-analysis
  - xss
  - discourse
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Ruby
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T03:46:37.911Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Review-Discourse-Onebox-Source-Code-for-Sanitization-Issues

## Summary

This procedure involves analyzing the source code of Discourse's onebox engine to identify sanitization flaws in audio and video parsers, enabling the discovery of XSS vulnerabilities through improper URL handling.

## Description

In a Discourse forum, the onebox engine parses URLs to embed rich content like audio and video players. By reviewing the Ruby source code on GitHub, attackers can spot failures to escape single quotes in URLs, allowing injection of HTML attributes such as onerror handlers. This is similar to a known XSS in the Image parser. The target environment is any Discourse instance using the onebox gem, with expected outcomes including identification of injection points for further exploitation.

## Requirements

1. Access to GitHub repository (public)
2. Basic Ruby and HTML knowledge
3. Browser or text editor for code inspection

## Defense

Defensive measures and detection strategies:

- Implement code reviews with static analysis tools like Brakeman for Ruby apps
- Monitor for anomalous forum posts containing suspicious URLs with quotes
- Use Content Security Policy (CSP) to restrict inline script execution

## Objectives

1. Identify unsanitized URL parsing in audio_onebox.rb and video_onebox.rb
2. Confirm potential for attribute injection leading to XSS
3. Document flaws for reporting or exploitation planning

## Instructions

### Step 1: Access Source Code

**Context**: Locate the relevant files in the Discourse onebox repository to begin analysis.

Navigate to the GitHub repository and open the specific commit files:

- https://github.com/discourse/onebox/blob/394409ca319cc1a1cd31fefa50c9468c990531a3/lib/onebox/engine/audio_onebox.rb
- https://github.com/discourse/onebox/blob/394409ca319cc1a1cd31fefa50c9468c990531a3/lib/onebox/engine/video_onebox.rb

> Search for URL extraction logic, such as template rendering for <audio> or <video> tags.

### Step 2: Analyze URL Handling

**Context**: Check for sanitization of special characters like single quotes in URLs.

Review the code for methods that insert URLs into HTML attributes without escaping. Look for patterns like direct string interpolation in tag attributes.

> Expected finding: No escaping of ' in URLs, allowing closure of attributes and injection of new ones like onerror.

### Step 3: Compare to Known Issues

**Context**: Relate findings to prior vulnerabilities for context.

Cross-reference with the Image parser XSS to validate the pattern of insufficient sanitization.

> Note similarities in parser behavior to strengthen the vulnerability assessment.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[code-review]]
- [[xss-discovery]]
