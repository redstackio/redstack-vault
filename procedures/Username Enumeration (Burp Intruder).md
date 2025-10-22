---
id: ac1e05a8-6f1f-43a0-945a-1d3f2b5ef28f
name: Username Enumeration (Burp Intruder)
type: procedure
verified: true
submitted: true
created_at: '2020-09-01T14:26:44.992618+00:00'
updated_at: '2023-05-26T18:49:36.290206+00:00'
platforms:
- Web
tags:
- '[[Enumeration]]'
- '[[Web Applications]]'
---

# Username Enumeration (Burp Intruder)

**Status**: ✓ Verified

## Summary

Description An attacker brute forces the username field to identify the correct username of the application Instructions 1. Login to the account using random(invalid) username and password.Intercept the login request using burp proxy tab 

## Description

Description

An attacker brute forces the username field to identify the correct username of the application

Instructions

1. Login to the account using random(invalid) username and password.Intercept the login request using burp proxy tab

2. Observe that the response says invalid username.

3. Send the login request from the sitemap to the burp intruder

4.From the positions tab under intruder tab , slect attack type to sniper . Make sure to add only username for the payload position and clear the rest of the paramters.

5.Under payloads tab, select payload type *simple list and paste the list of usernames . The list can be obtained from[ https://github.com/danielmiessler/SecLists/tree/master/Usernames/Name](https://github.com/danielmiessler/SecLists/tree/master/Usernames/Names)s. Click on start attack to start the attack*

6.When the attack finishes , observe the responses in the attack window. 

7.Observe that all the length columns are same except for one of the entries which has 3266 lenght compared to 3264 for others. Make a note of the username.

8. Use the username from above step and a random password to login. 

9.Observe that the server throws an invalid password error. Username has been successfully enumerated. Similar steps from tehabove can be followed to identify the correct password for the username *austin*

## Platforms

- Web

## Tags

- [[Enumeration]]
- [[Web Applications]]
