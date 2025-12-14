---
tags:
  - xss
  - phishing-link
  - mastodon-api
type: procedure
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1566.001]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-13T23:08:55.608Z'
skill_level: intermediate
impact_level: medium
sub_techniques: []
id: e4889886-ed7f-429b-99a7-f8f955b80195
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.001]]'
  - '[[Drive-by Compromise]]'
---
# Send-Malicious-Mastodon-Toot-Link

## Summary

This procedure involves crafting and delivering a Mastodon toot link in IRCCloud that points to a malicious API response containing a javascript: URL, tricking the embed feature into executing XSS.

## Description

The attacker controls a Mastodon instance and configures its API to return JSON with a malicious URL in the toot's 'url' field. Sending the link via IRC message prompts IRCCloud to query the API (/api/v1/statuses/ID), receive the payload, and embed it. This targets web clients with enabled embeds; prerequisites include a running Mastodon server. Expected outcome: Victim's client fetches and processes the malicious JSON, setting up for iframe-based JS execution and cookie theft.

## Requirements

1. Controlled Mastodon instance with API configured for malicious responses
2. Access to send messages in victim's IRC channel
3. Victim's IRCCloud with embeds enabled

## Defense

Defensive measures and detection strategies:

- Block or filter unknown Mastodon domains in IRC clients
- Implement URL sanitization in embed APIs; log suspicious API queries

## Objectives

1. Deliver the phishing-like link to trigger API interaction
2. Ensure JSON payload is returned with javascript: URL
3. Position for embed exploitation

## Instructions

### Step 1: Configure Malicious Mastodon API

**Context**: Set up the server to respond with tainted JSON.

On your Mastodon instance, modify the API endpoint for the toot ID to return JSON like: {"url": "javascript:top.document.body.innerHTML = \"hi your cookie is \" + document.cookie;//"}. Use a fake toot ID like 123456789012345678.

> Test the endpoint directly via browser or curl to confirm JSON output.

### Step 2: Send the Link in IRC

**Context**: Deliver the payload to the victim.

In the IRCCloud channel, type and send: https://sm4.ca/@a/123456789012345678 (replace with your domain/toot).

> Victim must view the message for the client to process the link.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1566.001]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[mastodon-api]]
