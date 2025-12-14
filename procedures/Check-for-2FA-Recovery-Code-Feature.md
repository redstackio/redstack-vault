---
id: proc-002
tags:
  - 2fa
  - recovery-code
  - business-logic
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:24:47.482Z'
skill_level: beginner
impact_level: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Check-for-2FA-Recovery-Code-Feature

## Summary

This procedure inspects the 2FA settings UI for the presence of a recovery code feature in a TOTP-only configuration, identifying gaps that could lead to user lockout in applications with incomplete 2FA implementations.

## Description

During security testing of web-based authentication systems, such as Legal Robot's during a 2FA rollout, this step involves manually exploring the settings page for recovery or backup code options. These codes serve as a fallback if the authenticator app is lost. The absence for TOTP users indicates a business logic oversight, as the feature exists for other methods. This is performed post-TOTP enablement to assess completeness.

## Requirements

1. Account configured with TOTP-only 2FA
2. Access to the 2FA management interface
3. Browser developer tools for UI inspection if needed

## Defense

Defensive measures and detection strategies:

- Conduct UI/UX audits to ensure all 2FA paths include recovery options
- Log access attempts to recovery features for anomaly detection
- Use penetration testing to validate 2FA fallback mechanisms

## Objectives

1. Locate any recovery code generation or display elements
2. Confirm unavailability for TOTP setups
3. Document the UI inconsistency for reporting

## Instructions

### Step 1: Navigate to 2FA Settings

**Context**: Return to the security or 2FA section after enabling TOTP.

No command; click through the menu to the relevant page.

> Expected: Settings page loads with TOTP status shown.

### Step 2: Search for Recovery Options

**Context**: Scan for links, buttons, or modals related to 'Recovery Codes', 'Backup', or 'Lost Access'.

No command; interact with UI elements manually.

> Expected: No such feature visible, or a disabled/missing section.

### Step 3: Inspect UI Elements

**Context**: Use browser inspect tools to check for hidden or conditional recovery code elements tied to 2FA type.

No command; right-click and inspect HTML for relevant IDs/classes.

> Expected: Code reveals conditional rendering absent for TOTP.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[2fa]]
- [[recovery-code]]
- [[business-logic]]
