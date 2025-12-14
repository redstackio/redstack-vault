---
id: proc-uuid-2
tags:
  - xss
  - execution
  - ie-exploit
  - compatibility-mode
type: procedure
tools: []
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
updated_at: '2025-12-14T03:16:37.340Z'
skill_level: low
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-VBScript-XSS-via-IE-Compatibility-Mode

## Summary

This procedure triggers the stored XSS payload by having a victim load the GitLab page in a vulnerable Internet Explorer version, enabling compatibility mode to interpret and execute the vbscript: link as client-side code.

## Description

Once the malicious comment is posted, victims viewing the page in IE 7-10 or IE11 (with compatibility mode enabled) encounter a browser warning about incompatible content. Enabling compatibility mode causes the Markdown renderer to process the vbscript: link, allowing clicks to execute VBScript (equivalent to JavaScript) in the GitLab domain. This can lead to alerts, cookie theft, or other client-side attacks, but only affects IE users who opt into compatibility mode.

## Requirements

1. Victim using Internet Explorer 7-10 or IE11
2. Access to the GitLab page with the injected comment
3. Victim must enable compatibility mode when prompted

## Defense

Defensive measures and detection strategies:

- Block legacy IE usage via browser policies or warnings
- Implement Content Security Policy (CSP) to restrict script execution
- Log and alert on compatibility mode activations in enterprise environments

## Objectives

1. Execute arbitrary code in the victim's browser context
2. Achieve domain-level access for data exfiltration
3. Demonstrate impact through session hijacking potential

## Instructions

### Step 1: Direct Victim to Infected Page

**Context**: Lure the victim to view the GitLab project or issue containing the malicious comment.

**Instructions**: Share the URL via email, chat, or social engineering to encourage the victim to open it in IE.

### Step 2: Enable Compatibility Mode and Interact

**Context**: Upon page load, IE prompts for compatibility mode due to detected issues; enabling it activates the vulnerability.

**Instructions**: When the warning appears, select "Enable compatibility mode." The page reloads, rendering the link. Click the link (e.g., [Click me](vbscript:alert(document.domain))) to execute the payload.

> Successful execution shows an alert with the domain name, confirming XSS in the GitLab context. For real attacks, replace alert with code to exfiltrate cookies via img src or similar.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[ie-exploit]]
- [[vbscript]]
- [[compatibility-mode]]
