---
id: proc-uuid-003
name: Craft-and-Deliver-CSRF-PoC
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:49.990Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
  - '[[T1566.001]]'
sub_techniques: []
tags:
  - csrf-poc
  - html-exploit
  - delivery
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[T1566.001]]'
---

# Craft-and-Deliver-CSRF-PoC

## Summary

This procedure generates an HTML-based CSRF proof-of-concept that auto-submits a forged delete request and delivers it to the victim via phishing or direct link.

## Description

Using insights from the intercepted request, the attacker crafts an HTML page with a hidden form and JavaScript to automatically submit a GET request to https://www.█████/mediagallery/delete/id/{victim-album-id}. Burp Suite can assist in generating the PoC. The attack relies on the victim being authenticated; delivery methods include email attachments or malicious links. The target is the web media gallery, with outcomes of ready-to-deploy exploit code.

## Requirements

1. Victim's album ID
2. Text editor or Burp Suite for PoC generation
3. Delivery channel (email, link)

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints
- Educate users on phishing and suspicious links

## Objectives

1. Create functional CSRF exploit
2. Ensure auto-submission without user interaction
3. Deliver to victim effectively

## Instructions

### Step 1: Generate PoC with Burp Suite

**Context**: Use Burp to create the HTML form.

In Burp Suite, right-click the intercepted request and select "Engagement tools > Generate CSRF PoC". Customize to replace {album-id} with victim's ID.

### Step 2: Save and Deliver

**Context**: Host or send the HTML file.

Save as .html and send via email or host on a server, sharing the link with the victim.

**Expected Output**: HTML file with auto-submit script.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript
- [[T1566.001]] Phishing: Spearphishing Attachment

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[csrf-poc]]
- [[html-exploit]]
- [[delivery]]
