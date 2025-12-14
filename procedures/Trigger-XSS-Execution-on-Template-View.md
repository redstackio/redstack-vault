---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - xss
  - execution
  - collection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:08.467Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-Execution-on-Template-View

## Summary

This procedure demonstrates how the stored XSS payload executes when a victim user views the affected template in the Stripo editor, leading to arbitrary JavaScript execution in their authenticated session.

## Description

Once the payload is stored in the Accordion Section Name, any user with access to the template (e.g., via sharing or collaboration) will trigger the XSS upon rendering the block. The script runs in the context of the viewer's session, allowing theft of cookies, form data, or keystrokes. Reported in November 2020 and fixed by December 2020, this relies on social engineering to get victims to interact with the template.

## Requirements

1. Access to the stored template (e.g., shared link or collaborative edit)
2. Victim authentication on Stripo platform
3. Attacker-controlled endpoint for data exfiltration

## Defense

Defensive measures and detection strategies:

- Regular security audits of template rendering code
- User education on avoiding untrusted templates
- Logging and alerting on script execution in editor contexts

## Objectives

1. Execute injected JavaScript in victim browser
2. Collect sensitive data like session tokens
3. Maintain access via hijacked sessions

## Instructions

### Step 1: Share or Access Template

**Context**: Ensure the victim interacts with the template containing the payload.

Share the template link with the target user or invite them to collaborate. Have them open it in their browser while authenticated.

### Step 2: Render Accordion Block

**Context**: The payload triggers upon viewing the Accordion section.

Instruct or wait for the victim to scroll to or expand the Accordion block. The Section Name renders the unsanitized HTML, executing the script.

> For testing, use an alert payload; monitor attacker server for exfiltrated data in real attacks.

### Step 3: Validate Execution

**Context**: Confirm the XSS fired and achieved impact.

Check browser console for errors or use network tab to see requests to attacker domain. Verify stolen data received.

> Expected output: Script runs (e.g., alert or HTTP POST to attacker.com with cookies).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Execution]]
- [[Collection]]
