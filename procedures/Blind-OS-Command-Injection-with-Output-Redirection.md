---
id: 011c74d7-5e91-485e-8a33-d50c70ca2108
name: Blind-OS-Command-Injection-with-Output-Redirection
type: procedure
verified: true
submitted: true
created_at: '2020-08-30T18:31:31.868887+00:00'
updated_at: '2023-05-26T01:29:31.504897+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Unix Shell]]'
sub_techniques: []
tags:
  - '[[tags/injection]]'
  - '[[tags/os command injection]]'
  - '[[tags/owasp]]'
  - '[[tags/owasp top 10]]'
  - '[[tags/Web Applications]]'
commands:
  - '[[commands/submit-feedback-with-injection]]'
  - '[[commands/retrieve-output-file]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Blind-OS-Command-Injection-with-Output-Redirection

## Summary

This procedure exploits a blind OS command injection vulnerability in a web application, such as a feedback form, where direct output is not visible. By redirecting the output of an injected command to a web-accessible file, the attacker can later retrieve and view the results, enabling reconnaissance like identifying the current user or system details without immediate feedback from the application.

## Description

Blind OS command injection occurs when user input is passed to system shell commands without proper sanitization, allowing arbitrary command execution. In blind scenarios, the application does not echo the command output, making exploitation challenging. This technique uses output redirection (e.g., > filename) to write results to a file in a directory accessible via the web server, such as /var/www/images/. The attacker first submits an injected payload via a vulnerable parameter (e.g., email field in a POST request), then accesses the file through another endpoint (e.g., an image loader GET request). This is common in PHP or similar web apps running on Linux/Unix systems with misconfigured input validation. The procedure assumes a Linux target and uses tools like Burp Suite for request interception and manipulation. Success reveals system information, which can lead to further exploitation like privilege escalation or data exfiltration.

## Requirements

1. Access to a vulnerable web application with a blind OS command injection point, such as a feedback form that executes system commands on input (e.g., email parameter piped to a mail command).
2. Burp Suite or equivalent proxy tool to intercept and modify HTTP requests.
3. Knowledge of the web server's directory structure, particularly a writable web-accessible path like /var/www/images/ (common on Apache/Nginx setups).
4. Network access to the target application, typically over HTTP/HTTPS on port 80/443.
5. Basic understanding of shell redirection and Linux commands.

## Defense

Defensive measures and detection strategies:

- Input validation and sanitization: Use whitelisting for parameters and avoid direct shell execution (e.g., use safe APIs like mail() in PHP without system calls).
- Web Application Firewall (WAF): Rules to detect injection patterns like ||, ;, > in inputs.
- Logging and monitoring: Enable application logs for command executions and monitor file system for unexpected writes in web directories (e.g., via file integrity monitoring tools like OSSEC).
- Least privilege: Run web server processes with minimal permissions to prevent file writes outside intended directories.
- Output encoding: Ensure no direct command output is reflected, but implement proper error handling to avoid blind exploitation.

## Objectives

1. Inject a command that redirects output to a web-readable file without triggering visible errors.
2. Retrieve the file contents to confirm command execution and gather system information.
3. Validate the vulnerability for further exploitation, such as injecting more complex commands.

## Instructions

### Step 1: Intercept and Prepare Feedback Submission

**Context**: Identify the vulnerable endpoint, typically a POST request to a feedback or contact form. Use a proxy to capture the legitimate request and forward it to a repeater for modification. This step ensures you can inject without disrupting normal flow.

**Tool**: Use [[tools/Burp-Suite]] to intercept traffic.

> Navigate to the feedback form, fill in details (e.g., name, message), and submit. In Burp, intercept the request and send it to Repeater. Verify the request structure, focusing on the email parameter which is vulnerable to injection.

### Step 2: Inject Command with Output Redirection

**Context**: Modify the email parameter to include a blind injection payload that executes a reconnaissance command (e.g., whoami) and redirects its output to a file in a web-accessible directory. The || separator chains the command without breaking the original execution.

**Command** ([[commands/submit-feedback-with-injection]]):

Use Burp Repeater or curl to send the modified POST request:

```bash
curl -X POST http://target.com/feedback -d "name=Test&email=||whoami>/var/www/images/output.txt|&message=Test" -H "Content-Type: application/x-www-form-urlencoded"
```

> This injects ||whoami>/var/www/images/output.txt| into the email field, assuming the app executes something like system("mail -s feedback $email"). The command runs whoami, redirects output to output.txt, and the pipe | maintains syntax. Send the request and check for a 200 OK response, indicating no immediate error.

**Expected Output**: HTTP 200 OK response from the server, with no visible command output in the body (blind nature).

### Step 3: Intercept Image or File Load Request

**Context**: Locate an endpoint that loads files from the web directory, such as an image viewer GET request with a filename parameter. Intercept this to prepare for retrieval.

**Tool**: Use [[tools/Burp-Suite]] Proxy and Repeater.

> Browse to a page that loads an image (e.g., product image), intercept the GET request in Burp, and send to Repeater. Confirm the URL structure, e.g., /images?filename=product.jpg.

### Step 4: Retrieve the Redirected Output File

**Context**: Modify the filename parameter to point to the injected file, allowing retrieval of the command output via the web server.

**Command** ([[commands/retrieve-output-file]]):

Use Burp Repeater or curl to send the modified GET request:

```bash
curl http://target.com/images?filename=output.txt
```

> Change the filename parameter to output.txt and send. The server will serve the file contents if accessible, revealing the whoami output.

**Expected Output**: HTTP response body containing the system username, e.g., "www-data" or similar, confirming successful injection and redirection.

### Step 5: Cleanup and Validation

**Context**: Verify the exploitation and clean up to avoid detection. Check for additional reconnaissance or escalation.

> If successful, the output file shows the command result. Delete the file if possible (e.g., inject rm /var/www/images/output.txt in a follow-up) to cover tracks. Test with other commands like id or uname -a for more info.

**Expected Output**: Confirmation of system details; no errors in subsequent requests.
