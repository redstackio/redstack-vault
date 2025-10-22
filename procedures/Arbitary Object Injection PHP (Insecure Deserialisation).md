---
id: 72516c05-f75a-4a74-a5d0-c0abc1277b25
name: Arbitary Object Injection PHP (Insecure Deserialisation)
type: procedure
verified: true
submitted: true
created_at: '2020-09-05T08:01:55.427702+00:00'
updated_at: '2023-05-26T18:24:39.715885+00:00'
platforms:
- Web
tags:
- '[[Insecure Deserialisation]]'
- '[[Web Applications]]'
---

# Arbitary Object Injection PHP (Insecure Deserialisation)

**Status**: ✓ Verified

## Summary

Descritpiion An attacker will be able to create instances of arbitrary classes whihc will then ivnoke the functions to execute the arbitrary code on the server. Instrcutions 1. With burp running and intercepting the requests , Login to the account. Notice that the session cookie contains the serial

## Description

# Descritpiion

An attacker will be able to create instances of arbitrary classes whihc will then ivnoke the functions to execute the arbitrary code on the server. 

# Instrcutions

1. With burp running and intercepting the requests , Login to the account. Notice that the session cookie contains the serialised object.

2. From the sitemap, notice the application referes the* `libs/CustomTemplate.ph*p and send the request to the server.`

3.Submit the request to the server by appending ~ operator at the end of the file name to fetch the source code.

4.Notice that CustomTemplate class contains destruct() magic method.This will invoke the *`unlink()*` method on the *`lock_file_pat*h` attribute, which will delete the file on this path

5.Use burp decoder to contruct a serialised PHP data in the following way.This object will create a CustomTemplate object with the lock_file_path set to `/*home/carlos/morale.tx`*t

*`O:14:"CustomTemplate":1:{s:14:"lock_file_path";s:23:"/home/carlos/morale.txt";*}`

6.Change the session cookie value from step1 to the value from decoder and send the request to the server.

7.The method destruct() wil be invoked and will delete the file from the server.

## Platforms

- Web

## Tags

- [[Insecure Deserialisation]]
- [[Web Applications]]
