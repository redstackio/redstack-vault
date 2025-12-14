---
id: proc-uuid-002
tags:
  - xss
  - execution
  - exfiltration
type: procedure
tools: []
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
updated_at: '2025-12-14T03:15:41.435Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-on-Victim-View

## Summary

This procedure exploits the stored XSS by having a victim user access the tainted member book entry, causing the Datatables library to render and execute the injected JavaScript in their authenticated session.

## Description

Once the payload is stored from the injection procedure, any authenticated user viewing the member book will trigger the XSS as Datatables dynamically loads and displays the unsanitized content. This executes in the victim's browser, potentially hijacking their session or stealing sensitive data like cookies. The attack relies on social engineering to lure victims or natural application usage.

## Requirements

1. A victim with authenticated access to the member book feature
2. The injected payload already stored from prior procedure
3. Attacker monitoring for exfiltrated data if payload includes fetch

## Defense

Defensive measures and detection strategies:

- Use server-side rendering with proper escaping for dynamic content
- Implement user permission checks for viewing member book entries
- Log and alert on unexpected script executions or outbound requests from the app

## Objectives

1. Execute the stored JavaScript in a victim's browser context
2. Collect session data or perform actions on behalf of the victim
3. Achieve impacts like account takeover or data theft

## Instructions

### Step 1: Lure or Wait for Victim Access

**Context**: Ensure a victim loads the affected page to trigger rendering.

Share a direct link to the member book via email or in-app notification, or rely on regular user activity to view the feature.

### Step 2: Observe Execution

**Context**: Monitor for payload activation as the victim views the content.

When the victim accesses the member book, Datatables processes the entry, injecting and running the script. For testing, use a benign alert; for real attacks, exfiltrate via network request.

**Expected Output**: Script runs—e.g., alert dialog or HTTP request to attacker server with stolen data.

### Step 3: Verify Impact

**Context**: Confirm successful exploitation by checking exfiltrated data.

Inspect network logs on the attacker server for received cookies or use the stolen session to access the victim's account.

**Expected Output**: Access to victim session or data receipt.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[trigger]]
