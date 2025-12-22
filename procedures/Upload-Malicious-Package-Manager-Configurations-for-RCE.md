---
id: 13a7433a-0722-43a1-9683-13a04987daaa
name: Upload-Malicious-Package-Manager-Configurations-for-RCE
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:41.118450+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
  - '[[techniques/Ingress Tool Transfer|T1105 - Ingress Tool Transfer]]'
  - >-
    [[techniques/Command and Scripting Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques:
  - >-
    [[techniques/Command and Scripting Interpreter/Unix Shell|T1059.004 - Unix
    Shell]]
tags:
  - '[[tags/Configuration Files]]'
  - '[[tags/Exploits]]'
  - '[[tags/Upload Insecure Files]]'
  - rce
  - file-upload
  - npm
  - composer
commands:
  - '[[commands/npm-run-prepare]]'
  - '[[commands/composer-install]]'
platforms:
  - Linux
  - Web
tools: []
validated: true
---

# Upload-Malicious-Package-Manager-Configurations-for-RCE

## Summary

This procedure exploits insecure file upload vulnerabilities in web applications to upload malicious configuration files for package managers like NPM or Composer. By embedding arbitrary commands in lifecycle hooks such as 'prepare' or 'pre-command-run', attackers can achieve remote code execution (RCE) when the server processes the uploaded package, such as during an automatic install or build step.

## Description

In web applications with vulnerable file upload features that do not properly validate or sanitize uploads, attackers can upload JSON configuration files (package.json for NPM or composer.json for Composer) containing malicious scripts in predefined hook sections. These hooks execute automatically during package installation or explicit runs, allowing command execution on the server. For example, the NPM 'prepare' hook runs before publishing and on local installs, while Composer's 'pre-command-run' executes before any command. This technique targets development or CI/CD environments where uploaded packages are installed without scrutiny, leading to RCE. It is particularly effective against PHP or Node.js-based applications with loose upload controls. Success results in arbitrary command execution, enabling file creation, data exfiltration, or further compromise.

## Requirements

1. Authenticated or unauthenticated access to a file upload endpoint that accepts .json files without MIME type or content validation.
2. The target server must use NPM or Composer to process uploaded packages (e.g., via a build script, plugin installer, or admin panel).
3. Server-side execution environment supporting shell commands (typically Linux/Unix with bash access).
4. Knowledge of the upload directory or path where the server will process the file.

## Defense

- Implement strict file type validation, including content scanning for executable scripts in JSON files using tools like ClamAV or custom parsers.
- Restrict uploads to non-executable extensions and sandbox package installations in isolated environments.
- Monitor for anomalous file uploads and installations via logging (e.g., audit npm/composer commands) and use web application firewalls (WAF) to block suspicious JSON payloads.
- Regularly scan dependencies and configurations for malicious hooks during CI/CD pipelines.

## Objectives

1. Achieve remote code execution on the target server via package manager hooks.
2. Demonstrate compromise by creating proof-of-concept files or exfiltrating data.
3. Establish persistence or escalate privileges through subsequent commands in the hook.

## Instructions

### Step 1: Craft Malicious NPM package.json

**Context**: Create a package.json file with a malicious 'prepare' script that executes an arbitrary command when NPM processes the package. This hook runs automatically during 'npm install' or can be triggered explicitly.

Embed the following code snippet into a package.json file, customizing the command as needed (e.g., replace '/bin/touch /tmp/pwned.txt' with a reverse shell or data exfil command).

**Code** ([[codes/NPM-Package-JSON-Prepare-Script]]):

```js
"scripts": {
    "prepare" : "/bin/touch /tmp/pwned.txt"
}
```

> This adds a 'prepare' script to the JSON. Save it as package.json in your working directory. The command executes shell code directly, so ensure it aligns with the target's environment (e.g., use 'cmd /c' on Windows).

### Step 2: Upload the Malicious package.json

**Context**: Use the vulnerable file upload functionality to place the package.json on the server. This step assumes a web form or API endpoint for uploads; use tools like Burp Suite to bypass any weak restrictions.

Navigate to the upload endpoint (e.g., /upload.php) and submit the package.json file. If authentication is required, use valid credentials. Verify the upload succeeds by checking server responses or accessing the uploaded file path.

**Expected Output**: HTTP 200 OK or success message confirming upload, with the file accessible at a predictable path (e.g., /uploads/package.json).

### Step 3: Trigger NPM Hook Execution

**Context**: Execute the NPM command that triggers the 'prepare' hook, either by interacting with an admin panel that installs packages or by exploiting a feature that runs 'npm install' on uploads.

If direct access is available, run the following in the directory containing the uploaded package.json:

**Command** ([[commands/npm-run-prepare]]):

```bash
npm run prepare
```

> Alternatively, if the application auto-installs, simply trigger the install process (e.g., via a build button). This executes the hook, running the embedded command.

**Expected Output**: No direct output from the hook, but verify success by checking if /tmp/pwned.txt was created (e.g., via a subsequent enumeration step or log review).

### Step 4: Craft Malicious Composer composer.json

**Context**: Similarly, create a composer.json with a 'pre-command-run' hook for PHP/Composer environments. This executes before any Composer command, providing RCE on install.

Embed the following code snippet into a composer.json file, customizing the command.

**Code** ([[codes/Composer-JSON-Pre-Command-Run-Hook]]):

```js
"scripts": {
    "pre-command-run" : [
    "/bin/touch /tmp/pwned.txt"
    ]
}
```

> Save as composer.json. The array format allows multiple commands if needed.

### Step 5: Upload and Trigger Composer Hook

**Context**: Upload the composer.json and trigger installation to execute the pre-hook.

Upload via the same endpoint as Step 2, then trigger:

**Command** ([[commands/composer-install]]):

```bash
composer install
```

> This runs 'composer install' on the uploaded file, firing the pre-command-run hook.

**Expected Output**: Composer output indicating successful install, with the command executed (verify /tmp/pwned.txt existence).
