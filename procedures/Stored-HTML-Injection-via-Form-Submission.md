---
id: 4417ce3e-a88e-4801-ac81-01fd5bd6686f
name: Stored-HTML-Injection-via-Form-Submission
type: procedure
verified: true
submitted: true
created_at: '2020-07-27T17:11:46.410466+00:00'
updated_at: '2023-05-26T18:41:27.082450+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - '[[tags/HTML Injection]]'
  - '[[tags/injection]]'
  - '[[tags/stored HTML injection]]'
  - '[[tags/Web Applications]]'
commands:
  - '[[commands/netcat-windows-listen-verbose]]'
tools:
  - '[[tools/Netcat]]'
platforms:
  - Web
skill_level: beginner
impact_level: high
detection_risk: medium
validated: true
---

# Stored-HTML-Injection-via-Form-Submission

## Summary

This procedure demonstrates how to perform a stored HTML injection attack by submitting malicious HTML code through a vulnerable web form. The injected code, such as an iframe, is stored on the server and served to unsuspecting users, causing their browsers to load attacker-controlled content. This can lead to further exploitation like session hijacking, data exfiltration, or drive-by downloads when victims access the page.

## Description

Stored HTML injection occurs when user input is not properly sanitized and is embedded directly into HTML pages without escaping. Unlike reflected injections, the malicious code persists in the database or file system and executes every time the page is loaded by any user. In this scenario, the target web application has a form (e.g., a comment or profile field) that accepts input and displays it without validation. The attacker injects an iframe tag pointing to their controlled server, which can serve JavaScript or other payloads to interact with the victim's browser. This technique is commonly used in web applications to achieve client-side execution and is mapped to MITRE ATT&CK technique T1059.007 (JavaScript for Automation). Prerequisites include identifying a vulnerable input field and setting up an attacker server to host the malicious content.

## Requirements

1. Access to a vulnerable web application with a stored input field (e.g., comment box, user profile).
2. Attacker-controlled server (IP and port accessible from the victim's network) to host the iframe content.
3. Netcat or similar listener tool installed on the attacker machine to capture connections or data.
4. Basic knowledge of HTML and web traffic interception (optional, for verification).

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization using libraries like DOMPurify or OWASP ESAPI to escape HTML entities.
- Use Content Security Policy (CSP) headers to restrict iframe sources and script execution (e.g., frame-ancestors 'self').
- Monitor for anomalous network traffic from web servers to internal/external IPs not matching expected patterns.
- Employ Web Application Firewalls (WAF) to detect and block HTML tags in user inputs.
- Regularly scan stored content for malicious patterns using automated tools like grep or security scanners.

## Objectives

1. Inject persistent malicious HTML into the web application.
2. Cause victim browsers to load attacker-controlled content upon page access.
3. Establish a connection or exfiltrate data via the loaded iframe.
4. Verify successful injection and execution through listener output.

## Instructions

### Step 1: Identify Vulnerable Input Field

**Context**: Locate a form field in the web application that accepts user input and stores it for display to other users without proper sanitization. This could be a comment section, forum post, or profile bio.

Inspect the page source or use developer tools to confirm that input is reflected as raw HTML when submitted.

### Step 2: Prepare the Malicious Payload

**Context**: Craft the HTML injection payload using an iframe to load content from your attacker server. This payload will be executed in the victim's browser context when the page is accessed.

Use the following payload structure, substituting your server details:

Reference: [[codes/HTML-Iframe-Injection-Payload]]

### Step 3: Submit the Payload

**Context**: Enter the payload into the vulnerable form and submit it to store the injection on the server.

Navigate to the form, paste the payload into the text box, and click submit. Ensure no client-side validation blocks the HTML tags.

### Step 4: Set Up Listener on Attacker Machine

**Context**: Start a listener to capture any connections or requests triggered by the iframe loading in the victim's browser. This verifies execution and allows further interaction.

**Command** ([[commands/netcat-windows-listen-verbose]]):
```cmd
nc.exe -lvp $_PORT
```

> This command starts Netcat in listening mode on the specified port (e.g., 9999). Replace $_PORT with your chosen port. Expected output includes a confirmation message like "listening on [any] 9999 ...". Keep this running before accessing the injected page.

### Step 5: Trigger and Verify Execution

**Context**: Access the page containing the stored injection as a victim user to trigger the payload. Monitor the listener for incoming connections.

Log in as or simulate a different user and navigate to the page displaying the injected content. Observe the Netcat window for incoming requests or data from the victim's browser loading the iframe.

**Expected Output**: In the Netcat listener, you should see a connection from the victim's IP, potentially including HTTP requests or data if the loaded page is configured to send it back.

> Example listener output:
> listening on [any] 9999 ...
> connect to [192.168.43.183] from (victim_ip) [port] at (timestamp)

