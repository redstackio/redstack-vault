---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
tags:
  - takeover-demo
  - phishing-hosting
  - subdomain-takeover
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:51:10.437Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Demonstrate Subdomain Takeover by Hosting Content

## Summary

This procedure validates the takeover by publishing custom content on the controlled blog and confirming it appears on the original subdomain.

## Description

Post-takeover, the attacker edits the Tumblr blog to host arbitrary content, such as a phishing page or defacement. Visiting blog.snapchat.com then displays the new content, like 'Hello Snapchat - Jake Reynolds', proving full control and potential for brand damage or user deception.

## Requirements

1. Control of the claimed Tumblr account
2. Web browser to edit and test
3. Propagation time for DNS changes (typically quick for Tumblr)

## Defense

Defensive measures and detection strategies:

- Implement certificate pinning or HSTS to detect subdomain mismatches
- Monitor traffic to subdomains for anomalous content or referrers
- Use content security policies (CSP) to restrict hosted content

## Objectives

1. Confirm resolution to attacker-controlled blog
2. Display custom content to simulate impact (e.g., phishing)
3. Highlight risks like misinformation on official-looking subdomains

## Instructions

### Step 1: Publish Custom Content

**Context**: Update the Tumblr blog with demonstration content.

In the Tumblr editor, create a post with title 'Hello Snapchat - Jake Reynolds' and publish.

> Content is now live on the claimed domain.

### Step 2: Validate on Subdomain

**Context**: Access the original subdomain to verify takeover.

Visit http://blog.snapchat.com/ in a browser.

> The page loads the new Tumblr blog, confirming successful takeover.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[takeover-demo]]
- [[phishing-hosting]]
