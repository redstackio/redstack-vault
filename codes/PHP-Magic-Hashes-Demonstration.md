---
id: 3bd317d5-339e-41e6-8375-52c26104df49
name: PHP-Magic-Hashes-Demonstration
type: code
language: PHP
verified: true
created_at: '2023-04-06T03:56:40.754770+00:00'
updated_at: '2023-04-06T03:56:40.758731+00:00'
platforms:
  - Web
  - PHP
tags:
  - magic-hashes
  - type-juggling
  - vulnerability-demo
validated: true
---

# PHP-Magic-Hashes-Demonstration

## Code

```php
<?php
var_dump(md5('240610708') == md5('QNKCDZO')); # bool(true)
var_dump(md5('aabg7XSs')  == md5('aabC9RqS'));
var_dump(sha1('aaroZmOk') == sha1('aaK1STfY'));
var_dump(sha1('aaO8zKZF') == sha1('aa3OFF9m'));
?>
```

## Description

This PHP code snippet demonstrates the magic hashes vulnerability by comparing pairs of strings that produce MD5 and SHA1 hashes starting with '0e', which PHP interprets as equal due to loose type juggling with the == operator. It outputs boolean true for equal comparisons despite different inputs, illustrating how attackers can bypass hash-based authentication.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This is a static demonstration; no runtime variables. Strings are hardcoded collision pairs. | N/A |

## Usage

Run this script locally in a PHP environment to verify collision pairs before using them in exploits. For example, save as demo.php and execute `php demo.php`. Outputs: bool(true) for each pair. Integrate pairs into login payloads as shown in [[procedures/Exploit-PHP-Magic-Hashes-for-Authentication-Bypass]]. Useful for training or auditing PHP apps for this flaw.

## Detection

- Review PHP source for == in hash comparisons and weak algos like md5/sha1.
- Enable PHP error logging to catch type juggling anomalies.
- WAF rules for known magic hash strings in POST data (e.g., 'QNKCDZO').
- Application logs showing successful logins with invalid passwords.

## Related

- [[procedures/Exploit-PHP-Magic-Hashes-for-Authentication-Bypass]]
- [[commands/PHP]]
