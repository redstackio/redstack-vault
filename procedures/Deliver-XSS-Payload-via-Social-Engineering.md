---
tags:
  - phishing
  - social-engineering
  - delivery
type: procedure
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1566.001]]'
updated_at: '2025-12-14T17:28:20.493Z'
sub_techniques: []
id: b3b3df57-6f94-4a69-817e-57d109492512
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.001]]'
---
# Deliver-XSS-Payload-via-Social-Engineering

## Summary

This procedure delivers the malicious Twitter intent URL to the victim through social engineering to induce clicking and trigger the XSS chain.

## Description

Rely on phishing-like tactics to send the crafted URL, disguising it as a legitimate request to favorite a tweet. The victim must click to proceed to the intent page, setting up the referer bypass.

## Requirements

1. Communication channel with victim (email, chat, etc.)
2. Crafted URL
3. Plausible pretext for interaction

## Defense

Defensive measures and detection strategies:

- User training on link verification
- Email filters for suspicious URLs
- Browser warnings for shortened links

## Objectives

1. Gain victim interaction
2. Direct to malicious URL
3. Initiate attack chain

## Instructions

### Step 1: Prepare Message

**Context**: Craft a convincing lure.

Write message: "Please favorite this: [malicious URL]".

### Step 2: Send to Victim

**Context**: Transmit via chosen channel.

Deliver the message and monitor for clicks.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1566.001]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
