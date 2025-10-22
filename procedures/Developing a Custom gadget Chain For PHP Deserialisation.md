---
id: abb7cd92-05b9-4038-9d86-a08b052f9b2b
name: Developing a Custom gadget Chain For PHP Deserialisation
type: procedure
verified: true
submitted: true
created_at: '2020-08-31T17:05:19.859611+00:00'
updated_at: '2023-05-26T01:08:11.282719+00:00'
platforms:
- Web
tags:
- '[[deserialization]]'
- '[[Web Applications]]'
---

# Developing a Custom gadget Chain For PHP Deserialisation

**Status**: ✓ Verified

## Summary

Attacker might be able to craft a custom gadget by carefully observing the source code to identify longer gadget chains. Then it can lead to high severity attacks. 

## Description

# Description

Attacker might be able to craft a custom gadget by carefully observing the source code to identify longer gadget chains. Then it can lead to high severity attacks.

# Instructions

# 

1.Login to the account with the details provided. Observe that the session contains a serialised PHP object . 

# 

# 

2. From the site-map observe the file `/cgi-bin/libs/CustomTemplate.php`

3.Get the source code of the file `/cgi-bin/libs/CustomTemplate.php by submitting the request to the server.Observe that `__wakeup() magic method for a CustomTemplate will create a new Product by referencing the default_desc_type and desc from the CustomTemplate__wakeup() magic method for a CustomTemplate will create a new Product by referencing the default_desc_type and desc from the CustomTemplate. Also there is a defaultmap() which has get() method will be invoked to read an attribute which doesnt exist .

4.Navigate back to home page request from the sitemap and copy the session cookie value.

5. Decode the session cookie using burp decoder

6. Craft a custom gadget with the below values . This gadget will delete the marale.txt from the server.

*CustomTemplate->default_desc_type = "rm /home/carlos/morale.txt";
CustomTemplate->desc = DefaultMap;
DefaultMap->callback = "exec*

Base64 and URL-encode the object using burp decoder.

*O:14:"CustomTemplate":2:{s:17:"default_desc_type";s:26:"rm /home/carlos/morale.txt";s:4:"desc";O:10:"DefaultMap":1:{s:8:"callback";s:4:"exec";}}*

7.Copy the url encoded value to session cookie parameter value and send the request to the server . Observe that the request has been accpeted and the file has been successfully deleted

## Platforms

- Web

## Tags

- [[deserialization]]
- [[Web Applications]]
