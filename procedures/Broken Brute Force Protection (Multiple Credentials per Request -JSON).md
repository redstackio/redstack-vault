---
id: aba85d85-1216-4bc0-a6f3-95fa8e161543
name: Broken Brute Force Protection (Multiple Credentials per Request -JSON)
type: procedure
verified: true
submitted: true
created_at: '2020-09-05T07:38:30.933941+00:00'
updated_at: '2023-05-26T15:55:46.530834+00:00'
platforms:
- Web
tags:
- '[[broken authentication]]'
- '[[Web Applications]]'
---

# Broken Brute Force Protection (Multiple Credentials per Request -JSON)

**Status**: ✓ Verified

## Summary

Few applications uses JSON format to submit credentials to the server).If they are no validation checks on the user controlled fileds of the JSON , an attacker can manipulate those fileds and gain unthorised access to the victim's account. 

## Description

# Description

Few applications uses JSON format to submit credentials to the server).If they are no validation checks on the user controlled fileds of the JSON , an attacker can manipulate those fileds and gain unthorised access to the victim's account.

# Instructions





1.With burp running and intercepting requests , Login to the account with given credentials. Intercept the login request and notice that the POST login request uses JSON format to submit the credentials.









![1934c0f2-5ccc-4a90-9e65-4a44c2bdf16c.png](_assets/images/Mash/1934c0f2-5ccc-4a90-9e65-4a44c2bdf16c.png)







2.Notice the error with incorrect credentials.





![40aa646d-7b06-4faa-96db-04f98c950521.png](_assets/images/Mash/40aa646d-7b06-4faa-96db-04f98c950521.png)







3. Identify the POST request from the HTTP History and send the request to the repeater.







![5fa57cbd-47f6-4431-a7ec-14942787bd99.png](_assets/images/Mash/5fa57cbd-47f6-4431-a7ec-14942787bd99.png)







4.From the repeater tab, for the password field in JSON format , copy the list of passwords (Use this to get the payloads : [*https://github.com/danielmiessler/SecLists/tree/master/Payload](https://github.com/danielmiessler/SecLists/tree/master/Payloads)s ) and submit the request.*





![7513440a-ec73-44ef-8cd1-ae5e0b2be886.png](_assets/images/Mash/7513440a-ec73-44ef-8cd1-ae5e0b2be886.png)





5.Notice the 302 response . Right click and select *copy url* to copy the response request.





![d7c7e64b-8f04-482c-bfa9-37b55fed84ae.png](_assets/images/Mash/d7c7e64b-8f04-482c-bfa9-37b55fed84ae.png)







6.Load the url in the browser and notice that login was successful





![774ae365-c045-4987-9155-2c0b6a1c1a3a.png](_assets/images/Mash/774ae365-c045-4987-9155-2c0b6a1c1a3a.png)



## Platforms

- Web

## Tags

- [[broken authentication]]
- [[Web Applications]]


