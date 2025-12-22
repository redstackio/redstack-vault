---
tags:
  - php-object-injection
  - unserialization
type: procedure
tools:
  - '[[tools/Custom-PHP-Script]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/php-exploit-script]]'
platforms:
  - Web
  - Linux
techniques:
  - '[[Command-Line Interface]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques:
  - '[[JavaScript]]'
id: 06fe5c94-ada8-4b32-87ba-3b7d8d69baf5
created_at: '2025-12-13T09:00:28.009Z'
updated_at: '2025-12-13T09:00:28.009Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Perform PHP Object Injection

## Summary

This procedure involves crafting and injecting a serialized PHP object into a vulnerable unserialization endpoint to manipulate application behavior, setting up for further exploits like XXE.

## Description

Using insights from source code, a serialized ConfigFile object with malicious XML is created and base64-encoded. It's uploaded to /api/import_memes_2.0.php via $_FILES['f'], where unserialize() is called without validation, storing it in the session for later triggering.

## Requirements

1. Access to import endpoint
2. Custom PHP script for serialization
3. Knowledge of target classes from source code

## Defense

Defensive measures and detection strategies:

- Avoid unserialize on user input; use JSON instead
- Monitor for unexpected object deserialization in logs

## Objectives

1. Inject arbitrary PHP object
2. Prepare for magic method invocation
3. Enable chained exploitation

## Instructions

### Step 1: Generate Serialized Payload

**Context**: Create the malicious object using a custom script.

Execute [[commands/php-exploit-script]]:

```bash
php exploit.php http://localhost
```

> This generates a base64-encoded serialized array with ConfigFile object.

### Step 2: Upload Payload

**Context**: Send the payload to the import endpoint.

Use curl to upload via multipart form:

```bash
curl -X POST http://target/api/import_memes_2.0.php -F "f=@payload.txt"
```

> Stores the object in $_SESSION['memes'].

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques

- [[JavaScript]]

## Commands Used

- [[commands/php-exploit-script]]

## Tools Used

- [[tools/Custom-PHP-Script]]

## Tags

- [[php-object-injection]]
- [[unserialization]]
