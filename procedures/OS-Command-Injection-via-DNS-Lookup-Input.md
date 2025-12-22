---
id: 7f0997b7-3ce7-4cd3-9022-dd526dd04c15
name: OS-Command-Injection-via-DNS-Lookup-Input
type: procedure
verified: true
submitted: true
created_at: '2020-07-28T16:52:08.361140+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Unix Shell]]'
sub_techniques: []
tags:
  - injection
  - os-command-injection
  - owasp
  - owasp-top-10
  - web-applications
commands:
  - '[[commands/curl-os-command-injection-test]]'
platforms:
  - Web
tools: []
validated: true
---

# OS-Command-Injection-via-DNS-Lookup-Input

## Summary

This procedure demonstrates how to exploit an OS command injection vulnerability in a web application's DNS lookup feature by injecting arbitrary operating system commands through an unsanitized input field, allowing execution of server-side commands such as ping for confirmation.

## Description

OS command injection occurs when user-supplied input is improperly sanitized and passed to system shell commands, enabling attackers to execute arbitrary OS commands on the server. In this scenario, a web form intended for DNS lookups (e.g., querying domain information) concatenates user input directly into a backend command like `dnslookup <input>`. By appending command separators like `||` or `;`, an attacker can chain additional commands, such as a ping with a delay to confirm execution without needing to see output directly. This technique targets web applications vulnerable to OWASP Top 10 injection flaws, typically on Linux/Unix servers running the backend. Success is indicated by server-side effects like network delays or reflected command output in responses. Prerequisites include direct access to the vulnerable input field, often via a browser or proxy tool.

## Requirements

1. Access to a web application with a DNS lookup or similar input field that executes system commands (e.g., `nslookup` or `dig`).
2. Knowledge of the target's URL and input mechanism (GET parameter or POST form).
3. Basic understanding of shell command separators (`||`, `;`, `&`).
4. Optional: A proxy like Burp Suite for intercepting and modifying requests.

## Defense

Defensive measures and detection strategies:

- Input validation and sanitization: Whitelist allowed characters and avoid direct shell execution.
- Use parameterized APIs or libraries (e.g., Python's `subprocess` with shell=False) instead of string concatenation.
- Web Application Firewall (WAF) rules to block common injection patterns like `||`, `;`, or command names (e.g., `ping`, `id`).
- Application logging: Monitor for anomalous delays or unexpected command executions in server logs.
- Least privilege: Run web processes with minimal permissions to limit impact of injected commands.

## Objectives

1. Identify and confirm the OS command injection vulnerability in the DNS lookup input.
2. Execute a benign test command (e.g., ping) to validate server-side execution.
3. Demonstrate potential for more destructive commands if the vulnerability is exploitable.

## Instructions

### Step 1: Identify the Vulnerable DNS Lookup Input

**Context**: Locate the input field in the web application that performs DNS lookups, as this field likely passes user input directly to a system command without sanitization. This step sets up the attack surface by understanding the normal flow.

Inspect the form or URL parameter (e.g., `?host=example.com`) using browser developer tools or a proxy to confirm how input is submitted.

**Expected Output**: Normal DNS resolution output, such as IP addresses or domain records, confirming the endpoint works as intended.

### Step 2: Test for OS Command Injection Using a Separator

**Context**: Append a command separator to the legitimate input to attempt chaining a secondary command. The `||` operator ignores the original command if it succeeds and executes the injected one, allowing blind testing without visible output.

Use the following command to simulate the injection via curl, assuming a GET-based endpoint (adjust URL and method as needed for POST forms):

**Command** ([[commands/curl-os-command-injection-test]]):
```bash
curl "http://target.com/dns?host=example.com || ping -c 10 127.0.0.1"
```

> This sends a request where the backend might execute `dnslookup "example.com || ping -c 10 127.0.0.1"`, running the ping command 10 times, which introduces a noticeable delay (about 40 seconds total) if successful. Replace `http://target.com/dns?host=` with the actual endpoint. If using a browser, enter the payload directly in the input field.

**Expected Output**: A response delay of approximately 40 seconds, or partial command output (e.g., ping statistics) reflected in the HTTP response body if the application echoes results.

### Step 3: Verify Success and Escalate if Needed

**Context**: Confirm injection by observing effects and test a simple command like `id` to retrieve user context, indicating the privilege level of execution.

Repeat the injection with a revealing command:

**Command** ([[commands/curl-os-command-injection-test]]):
```bash
curl "http://target.com/dns?host=example.com ; id"
```

> The `;` separator chains commands unconditionally. Look for output like `uid=33(www-data) gid=33(www-data)` in the response, confirming execution under the web server's user.

**Expected Output**: Command output (e.g., user ID details) in the response, or error messages indicating partial execution.

### Step 4: Clean Up and Document

**Context**: Avoid leaving traces and note variations for different separators (`&&`, `|`) or OS-specific commands (e.g., `dir` on Windows).

No specific command needed; review logs or responses for artifacts.
