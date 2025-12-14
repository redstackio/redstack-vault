---
id: proc-uuid-4
name: Deliver-and-Execute-CSRF-Attack-on-Victim
tags:
  - csrf
  - delivery
  - exploitation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:22.545Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Deliver-and-Execute-CSRF-Attack-on-Victim

## Summary

This procedure involves sending the malicious HTML to a victim who is logged into onpatient.com, resulting in the unauthorized addition of an album to their account upon page load.

## Description

The crafted HTML form is delivered via email, phishing link, or hosted page. When the victim visits it while authenticated, their browser uses the active session cookie to submit the POST request, bypassing CSRF protections. The server adds the album and returns a success response with the new ID, achieving account manipulation like spam or further phishing.

## Requirements

1. Malicious HTML file prepared
2. Method to deliver to victim (e.g., email, social engineering)
3. Victim must be logged in to onpatient.com

## Defense

Defensive measures and detection strategies:

- Deploy anti-phishing training and email filters
- Monitor account for suspicious actions like bulk album adds
- Use multi-factor authentication and session timeouts

## Objectives

1. Induce victim to load the malicious page
2. Leverage victim's session for forged request
3. Confirm exploitation via album addition and response

## Instructions

### Step 1: Host or Send the HTML

**Context**: Make the form accessible to the victim.

Upload form-csrf.html to a web server or attach to an email with a enticing subject like "Check this photo album!".

> Include a link: <a href="http://attacker.com/form-csrf.html">View Album</a>.

### Step 2: Verify Execution

**Context**: Check the victim's account post-visit.

After victim interaction, log in as attacker or monitor to see the 'hacking' album in victim's photos.

> Expected: Server response includes new album ID, e.g., {"id": 12345}.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[delivery]]
- [[exploitation]]
