---
tags:
  - xss
  - stored-xss
  - html-injection
  - email-exploit
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: dadb78c4-2ef6-4cc6-bc5c-a0e93c36623e
created_at: '2025-12-14T00:11:16.818Z'
updated_at: '2025-12-14T00:11:16.818Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# Craft Malicious HTML Email for XSS Bypass

## Summary

This procedure involves crafting a raw HTML email with encoded tags in <style> elements to bypass the HEY.com HTML sanitizer, allowing injection of arbitrary unsafe HTML such as forms, iframes, or scripts for account compromise.

## Description

The attack exploits a vulnerability where the sanitizer improperly handles encoded closing and opening tags in <style> elements, inserting filtered CSS as HTML. This enables stored XSS when the email is viewed, leveraging the Stimulus framework for actions like auto-submitting forms or executing JavaScript via hCaptcha. The impact includes setting up email forwarding, spoofing login pages for credential theft, or full account takeover.

## Requirements

1. Knowledge of HTML, CSS, and JavaScript for crafting payloads
2. Access to a system for creating text files
3. Understanding of email headers and MIME types

## Defense

Defensive measures and detection strategies:

- Implement robust HTML sanitization that properly escapes encoded tags
- Monitor for unusual email content with encoded sequences
- Use Content Security Policy (CSP) to restrict script execution

## Objectives

1. Bypass the email sanitizer to inject malicious HTML
2. Enable execution of JavaScript or forms upon viewing
3. Achieve account compromise or data exfiltration

## Instructions

### Step 1: Prepare Email Headers and Body

**Context**: Set up the email structure with necessary headers and the malicious <style> tag.

Create the email content with From, To, Subject, MIME-Version, Content-type: text/html, and a <style> tag using escaped sequences like \00003c\000027message-content\00003e to inject forms or iframes.

> This encodes HTML to confuse the sanitizer and allow injection.

### Step 2: Encode Malicious Payload

**Context**: Encode the payload to bypass filtering.

Ensure the <style> contains encoded HTML that, when misinterpreted, injects exploitable elements leveraging Stimulus for auto-submission or hCaptcha for JS execution.

> Test the encoding to confirm it evades sanitization.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Drive-by Compromise]]
- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[xss]]
- [[email-exploit]]
