---
tags:
  - xss-trigger
  - embed-generation
  - infogram
  - javascript-execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:14.293Z'
sub_techniques: []
id: 6f746b3a-745f-4538-8a13-eaca64b78f0f
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Generate-Infogram-Share-Embed-to-Trigger-XSS

## Summary

This procedure generates the embed code for an Infogram project, which reflects the malicious title unsanitized into HTML attributes and text, enabling JavaScript execution when the embed is loaded on an external page.

## Description

The share feature produces an iframe or script-based embed snippet that includes the project title directly in HTML without escaping, e.g., in data-title attributes and <a> tag content. For a payload like '<script>alert(1);</script>', this results in executable code on the embedding site. This exploits the reflected XSS in the embed generation. Prerequisites: a project with malicious title. Expected outcome: embed code that triggers XSS on load.

## Requirements

1. Infogram project with malicious title from prior step
2. Access to the project's share interface
3. A test HTML page or third-party site to embed and verify

## Defense

Defensive measures and detection strategies:

- Encode all dynamic content in embeds (e.g., use htmlspecialchars for titles)
- Validate embed usage and monitor for anomalous script executions
- Audit share features for input sanitization gaps

## Objectives

1. Produce exploitable embed code with reflected payload
2. Demonstrate XSS execution in embedding context
3. Highlight brand trust erosion potential

## Instructions

### Step 1: Access Share Feature

**Context**: Open the sharing options for the malicious project.

In the project editor or dashboard, click the 'Share' button and select 'Embed' or 'Get Code'.

### Step 2: Generate Embed Snippet

**Context**: Retrieve the HTML code containing the unsanitized title.

Choose the embed option; the generated code will include lines like <a href='https://infogram.com/d08ad077-3490-4241-b9a9-057da53e2e7d'><script>alert(1);</script></a> and data-title="<script>alert(1);</script>". Copy the full snippet.

### Step 3: Test Embed for XSS

**Context**: Load the embed in a separate page to trigger execution.

Create a simple HTML file (e.g., test.html) with <body> containing the embed code, open it in a browser, and observe the alert dialog.

> Success is confirmed by the JavaScript alert firing, proving XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-trigger]]
- [[embed-generation]]
