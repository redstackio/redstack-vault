---
tags:
  - xss
  - viewer
  - rendering
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:25.116Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: fc080240-8709-4915-a38b-4f1b1038c024
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# View-File-in-Repository-Blob-Viewer

## Summary

This procedure navigates to the uploaded malicious YAML file in GitLab's repository blob viewer, triggering the rendering process via swagger-ui that injects the unsanitized HTML payload.

## Description

GitLab's file viewer at paths like /-/blob/master/ automatically detects and renders OpenAPI YAML files using an outdated swagger-ui, which incorporates a vulnerable DOMPurify library. This step exploits that by simply accessing the URL, causing the browser to process the malicious content. Prerequisites: The file must be uploaded previously. Expected outcomes: Malicious HTML is injected into the DOM, setting up for XSS execution.

## Requirements

1. Access to the GitLab repository URL
2. Web browser with JavaScript enabled
3. Victim or self as viewer (affects any authenticated user viewing the file)

## Defense

Defensive measures and detection strategies:

- Patch GitLab to disable or update swagger-ui rendering for YAML files
- Implement client-side sanitization checks or disable JS in viewers
- Log and alert on views of OpenAPI files from untrusted sources
- Use WAF rules to block known DOMPurify bypass patterns

## Objectives

1. Trigger rendering of the malicious YAML
2. Inject unsanitized HTML into the browser DOM
3. Prepare for JavaScript execution

## Instructions

### Step 1: Construct the Viewer URL

**Context**: Build the exact URL to the blob viewer.

Format: https://gitlab.com/{username}/{repo}/-/blob/{branch}/{filename}, e.g., https://gitlab.com/username/repo/-/blob/master/openapi.yaml.

### Step 2: Access the URL in Browser

**Context**: Load the page to initiate rendering.

Open the URL in a web browser. The swagger-ui will parse and display the YAML, processing the 'description' field and injecting the payload.

### Step 3: Inspect for Injection

**Context**: Verify the payload is active.

Use browser dev tools (F12) to check the DOM for injected elements like svg or iframe.

**Expected Output**: Swagger UI interface loads with embedded malicious HTML visible in elements inspector.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- viewer
- rendering
