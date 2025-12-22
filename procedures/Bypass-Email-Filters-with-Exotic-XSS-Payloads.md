---
id: 30e1c192-d4dc-4eda-8230-1a3275962777
name: Bypass-Email-Filters-with-Exotic-XSS-Payloads
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:42.636755+00:00'
updated_at: '2023-04-10T20:21:50.226603+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
techniques:
  - >-
    [[techniques/Obfuscated Files or Information|T1027 - Obfuscated Files or
    Information]]
  - '[[techniques/Data Obfuscation|T1001 - Data Obfuscation]]'
sub_techniques: []
tags:
  - '[[tags/Bypass email filter]]'
  - '[[tags/Cross Site Scripting]]'
  - '[[tags/Filter Bypass and exotic payloads]]'
commands:
  - '[[commands/Validate-Email-Format-with-XSS]]'
platforms:
  - Web
  - Email
tools: []
validated: true
---

# Bypass-Email-Filters-with-Exotic-XSS-Payloads

## Summary

This procedure demonstrates how to craft exotic email payloads that embed XSS scripts to bypass email content filters. By disguising malicious JavaScript within malformed email addresses, attackers can deliver payloads that execute on vulnerable web applications, such as contact forms or email clients with rendering flaws, enabling cross-site scripting attacks to steal session data or perform other malicious actions.

## Description

Email filters often scan for known malicious patterns like script tags or suspicious JavaScript, but they may overlook payloads hidden in email address fields, especially if the format appears superficially valid. This technique leverages obfuscation by embedding XSS payloads (e.g., SVG onload events) within the local-part of an email address, followed by a dummy domain. When processed by a vulnerable application, the payload can trigger execution. This is particularly effective against web-based email systems or forms that insert user input without proper sanitization. The approach aligns with defense evasion tactics by obfuscating the malicious intent, allowing delivery of payloads for command and control or data exfiltration. Success depends on the target's filter rules and input handling; test iteratively to refine the payload.

## Requirements

1. Access to an email sending interface or API (e.g., SMTP server, web form).
2. Knowledge of the target's email filter rules and potential XSS sinks (e.g., reflected in email previews).
3. A testing environment to validate payload execution without triggering alerts.
4. Basic JavaScript understanding for payload customization.

## Defense

- Implement content security policies (CSP) to block inline scripts and SVG execution.
- Sanitize all email inputs, especially address fields, using allowlists for valid characters.
- Use advanced email gateways with behavioral analysis to detect anomalous payloads.
- Enable logging and monitoring for unusual JavaScript execution in email processing contexts.

## Objectives

1. Evade email content filters by obfuscating XSS payloads in email addresses.
2. Deliver executable JavaScript to exploit cross-site scripting vulnerabilities.
3. Establish potential command and control or data collection via executed scripts.

## Instructions

### Step 1: Craft the Exotic XSS Payload

**Context**: Begin by creating a JavaScript snippet that tests for XSS execution, such as triggering a confirm dialog. Embed this within an email address structure to mimic a valid format while bypassing filter regex patterns that expect standard local-part@domain syntax.

**Code** ([[codes/XSS-Payload-in-Email-Address]]):

```javascript
"><svg/onload=confirm(1)>"@x.y
```

> This payload uses a closing tag (">) to break out of any quoting, followed by an SVG element with an onload handler that executes confirm(1) to verify XSS. The "@x.y suffix simulates an email domain. Customize the onload action for real attacks, e.g., sending data to an attacker-controlled server.

### Step 2: Validate Email Format for Bypass

**Context**: Test if the crafted payload passes basic email validation without alerting filters. This step ensures the obfuscated string is accepted as an "email" while hiding the malicious intent. Use a simple validation tool or script to check format compliance.

**Command** ([[commands/Validate-Email-Format-with-XSS]]):

```bash
node -e "console.log(/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(process.argv[1]))" "\"><svg/onload=confirm(1)>"@x.y
```

> This Node.js one-liner uses a basic regex to validate the email format. If it returns true, the payload is structurally valid and likely to bypass simple filters. Expected output: true (indicating format acceptance). If false, adjust the payload to fit the regex while preserving XSS functionality. Why: This confirms the evasion potential before deployment.

### Step 3: Deliver and Test the Payload

**Context**: Send the payload via an email form or API to a test target. Monitor for execution, such as the confirm dialog popping up, to verify bypass and exploitation success. Use a proxy to inspect requests and responses.

**Instructions**: Submit the payload as the "from" or "to" field in a contact form or email composer. For example, in a web form, enter the full payload string. If using an API, include it in the JSON body under email fields.

> Expected output: The target application processes the email, renders the field, and executes the JavaScript (e.g., confirm dialog appears). Success criteria: No filter rejection, and XSS triggers without errors. Decision point: If blocked, try variations like URL-encoding parts of the payload or using different event handlers (e.g., onerror instead of onload).
