---
tags:
  - xss-execution
  - cookie-theft
  - exploitation
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: f39d4de0-7831-40a0-b4fd-66e01e7a73b4
created_at: '2025-12-14T03:47:23.550Z'
updated_at: '2025-12-14T03:47:23.550Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
---
# Execute XSS Payload via Shared Note Viewer

## Summary

This procedure executes the crafted XSS payload in the Evernote shared note viewer to achieve arbitrary JavaScript execution, demonstrating impacts like session cookie theft and account takeover.

## Description

By accessing the manipulated /client/snv URL, the payload triggers in the 'after-save-note' view, running JS in the context of the victim's session. This can steal cookies, perform unauthorized actions, or install malware. The attack requires tricking a victim into visiting the malicious shared note link.

## Requirements

1. Crafted payload from previous procedure
2. Victim's browser (or self for testing)
3. Evernote shard endpoint (e.g., s1)

## Defense

Defensive measures and detection strategies:

- Browser sandboxing and XSS filters
- Session cookie HttpOnly and Secure flags
- User education on suspicious shared links

## Objectives

1. Trigger payload execution
2. Verify JS runs (e.g., alert or exfil)
3. Assess impact (e.g., data theft)

## Instructions

### Step 1: Prepare POC URL

**Context**: Assemble full exploitation URL.

Use: `https://www.evernote.com/shard/s1/client/snv?view=after-save-note&ionUrl=javascript:alert(document.cookie)//https://www.evernote.com/`.

> URL ready; replace alert with real payload like fetch to attacker server.

### Step 2: Load and Observe Execution

**Context**: Simulate victim access.

Open the URL in a browser logged into Evernote. Watch for JS execution.

> Alert shows cookies; in production, data exfiltrates silently.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Steal Web Session Cookie]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-execution]]
- [[cookie-theft]]
- [[exploitation]]
