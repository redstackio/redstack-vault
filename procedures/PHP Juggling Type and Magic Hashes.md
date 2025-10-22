---
id: 840e23fe-cb30-40b6-83a6-b3b3718d8e56
name: PHP Juggling Type and Magic Hashes
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:40.705716+00:00'
updated_at: '2023-04-06T03:56:40.730275+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Subvert Trust Controls|T1553 - Subvert Trust Controls]]'
sub_techniques:
- '[[Code Signing|T1553.002 - Code Signing]]'
- '[[Install Root Certificate|T1553.004 - Install Root Certificate]]'
tags:
- '[[Example vulnerable code]]'
- '[[PHP Juggling type and magic hashes]]'
- '[[Type Juggling]]'
commands:
- '[[Comparing two strings]]'
- '[[Retrieve value of $cookie[''hmac'']]]'
- '[[Setting a cookie]]'
---

# PHP Juggling Type and Magic Hashes

## Summary

PHP Juggling Type and Magic Hashes is a technique used by attackers to bypass authentication mechanisms. The vulnerability lies in the weak comparison operators used in PHP, which can be manipulated to coerce the comparison of two different data types. Attackers can use this technique to create a h

## Description

# Description

PHP Juggling Type and Magic Hashes is a technique used by attackers to bypass authentication mechanisms. The vulnerability lies in the weak comparison operators used in PHP, which can be manipulated to coerce the comparison of two different data types. Attackers can use this technique to create a hash that appears to be equivalent to a valid password hash, allowing them to bypass authentication mechanisms. This technique can be used to gain unauthorized access to sensitive systems and data.

To exploit this vulnerability, attackers typically use a tool or script to generate a hash that appears to be equivalent to a valid password hash. They then use this hash to bypass the authentication mechanism and gain access to the target system or data. This technique can be used to target any system that uses PHP and is vulnerable to weak comparison operators.

## Requirements

1. Access to the target system

1. Knowledge of PHP Juggling Type and Magic Hashes technique

1. Tools or scripts to generate equivalent hash

## Defense

1. Use strong comparison operators instead of weak comparison operators in PHP code

1. Implement multi-factor authentication to reduce the risk of unauthorized access

1. Regularly monitor and review logs for suspicious activity

## Objectives

1. Bypass authentication mechanisms

1. Gain unauthorized access to sensitive systems and data

# Instructions

1. This function validates a cookie by checking if the HMAC value in the cookie matches the hash of the username and expiration time concatenated with a key. It also checks if the expiration time has passed. The function returns true if the cookie is valid, false otherwise.

**Code**: [[function validate_cookie($cookie, $key) {
    $has]]

> The function takes two arguments: $cookie, which is an associative array containing the cookie data, and $key, which is a string used to generate the HMAC value. The function first calculates the hash of the username and expiration time concatenated with the key using the hash_hmac function. It then checks if the HMAC value in the cookie matches the calculated hash using a loose comparison. If the HMAC value does not match, the function returns false. The function then converts the expiration time in the cookie to an integer using intval and checks if it has passed using the time function. If the expiration time has passed, the function returns false. Otherwise, the function returns true to indicate that the cookie is valid.

2. Use this command to extract cookies from a website.

**Code**: [[$cookie]]

> This command takes no arguments. It will extract all the cookies from the website and store them in the $cookie variable for further use in the script.

**Command** ([[Setting a cookie]]):

```bash
document.cookie = 'username=John Doe'
```

3. To generate a Zero-like hash string, use the following command:

`zeroHash = hashlib.sha256(b'0').hexdigest()`

This will generate a hash string that has a similar structure to a zero value.

To calculate the HMAC of a message using the Zero-like hash string, use the following command:

`hmacHash = hmac.new(key, msg, hashlib.sha256).hexdigest()`

Where `key` is the secret key, `msg` is the message to be hashed, and `hashlib.sha256` is the hashing algorithm to be used.

**Code**: [[$cookie['hmac']]]

> The `data` field contains the value of the `hmac` cookie, which is used to authenticate the user. By generating a Zero-like hash string, we can make it more difficult for an attacker to guess the correct HMAC value. The `instruction` field provides the commands to generate a Zero-like hash string and calculate the HMAC using this hash string. The `explain` field provides additional information about the purpose of the Zero-like hash string and how it can improve security.

**Command** ([[Retrieve value of $cookie['hmac']]]):

```bash
$cookie['hmac']
```

4. Use the comparison operator '==' to check if two strings are equal.

**Code**: [["0e768261251903820937390661668547" == "0"]]

> The '==' operator compares two strings and returns a boolean value of true if they are equal, and false if they are not. In this example, the string "0e768261251903820937390661668547" is being compared to the string "0". Since these two strings are not equal, the comparison will return false.

**Command** ([[Comparing two strings]]):

```bash
"0e768261251903820937390661668547" == "0"
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Subvert Trust Controls|T1553 - Subvert Trust Controls]]

### Sub-Techniques

- [[Code Signing|T1553.002 - Code Signing]]
- [[Install Root Certificate|T1553.004 - Install Root Certificate]]

## Commands Used

- [[Comparing two strings]]
- [[Retrieve value of $cookie['hmac']]]
- [[Setting a cookie]]

## Tags

- [[Example vulnerable code]]
- [[PHP Juggling type and magic hashes]]
- [[Type Juggling]]
