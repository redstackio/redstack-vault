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





![1cb593eb-c020-4359-97f9-857dae6a2324.png](_assets/images/Mash/1cb593eb-c020-4359-97f9-857dae6a2324.png)





2. From the sitemap, notice the application referes the* `libs/CustomTemplate.ph*p and send the request to the server.`







![5444762a-8ae2-48a5-82c2-7da90f71869c.png](_assets/images/Mash/5444762a-8ae2-48a5-82c2-7da90f71869c.png)





3.Submit the request to the server by appending ~ operator at the end of the file name to fetch the source code.





![e5f6f1dc-73aa-43f2-a66c-e01ff6ef6f89.png](_assets/images/Mash/e5f6f1dc-73aa-43f2-a66c-e01ff6ef6f89.png)





4.Notice that CustomTemplate class contains destruct() magic method.This will invoke the *`unlink()*` method on the *`lock_file_pat*h` attribute, which will delete the file on this path





![14099a83-0428-4453-9256-407ef7e140d7.png](_assets/images/Mash/14099a83-0428-4453-9256-407ef7e140d7.png)





5.Use burp decoder to contruct a serialised PHP data in the following way.This object will create a CustomTemplate object with the lock_file_path set to `/*home/carlos/morale.tx`*t



*`O:14:"CustomTemplate":1:{s:14:"lock_file_path";s:23:"/home/carlos/morale.txt";*}`



![398e0c35-f789-41f7-a7c6-0dffa90f4621.png](_assets/images/Mash/398e0c35-f789-41f7-a7c6-0dffa90f4621.png)







6.Change the session cookie value from step1 to the value from decoder and send the request to the server.





![821775c3-6221-4e29-877b-82a4197be59e.png](_assets/images/Mash/821775c3-6221-4e29-877b-82a4197be59e.png)





7.The method destruct() wil be invoked and will delete the file from the server.









## Platforms

- Web

## Tags

- [[Insecure Deserialisation]]
- [[Web Applications]]


