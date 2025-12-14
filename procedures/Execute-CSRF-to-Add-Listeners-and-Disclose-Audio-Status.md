---
tags:
  - csrf
  - disclosure
  - web
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:29.589Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: d0bf3a6e-3d51-4491-a506-6bb3672379e3
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute-CSRF-to-Add-Listeners-and-Disclose-Audio-Status

## Summary

This procedure executes the CSRF attack by tricking victims into loading the malicious page, resulting in unauthorized addition to VK.com listener lists and disclosure of private group audio tracks.

## Description

Once the malicious page is crafted, this step involves social engineering to direct victims to it while they are logged into VK.com. The forged request exploits the session to add the victim's user ID to a target listener list and retrieve the current audio broadcast from a private group, revealing sensitive content. Outcomes include collected user IDs and song details for further attacks.

## Requirements

1. Hosted malicious page from previous procedure
2. Method to distribute link (e.g., email, social media)
3. Victim with active VK.com session

## Defense

Defensive measures and detection strategies:

- Log and alert on listener additions from unexpected sources
- Implement rate limiting on audio status requests
- Use WAF rules to detect CSRF patterns in request logs

## Objectives

1. Add victim to private listener list without consent
2. Retrieve and exfiltrate private audio status
3. Collect disclosed user IDs for enumeration

## Instructions

### Step 1: Distribute Malicious Link

**Context**: Use phishing to lure the victim to the hosted page.

Send the URL of the malicious HTML via a convincing message, e.g., "Check out this audio playlist." Ensure the victim is logged into VK.com.

**Expected Output**: Victim visits the page, triggering the form submission.

### Step 2: Monitor Exploitation Results

**Context**: Observe the effects on the target group or use a proxy to capture responses.

After victim interaction, check the private group for new listeners or use dev tools to log the response containing audio details.

**Expected Output**: Response JSON with song title, artist, and added user ID.

### Step 3: Validate Disclosure

**Context**: Confirm the private content was revealed.

Compare disclosed audio against known private group broadcasts to verify success.

**Expected Output**: Sensitive data like "Current song: [Private Track] by [Artist]" and user ID.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[disclosure]]
- [[web]]
