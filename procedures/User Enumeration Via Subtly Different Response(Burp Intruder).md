---
id: 34a353fa-c241-448c-91cc-38d990537d00
name: User Enumeration Via Subtly Different Response(Burp Intruder)
type: procedure
verified: true
submitted: true
created_at: '2020-09-01T15:28:11.573734+00:00'
updated_at: '2023-05-26T18:09:38.131345+00:00'
tags:
- '[[Enumeration]]'
- '[[Web Applications]]'
---

# User Enumeration Via Subtly Different Response(Burp Intruder)

**Status**: ✓ Verified

## Summary

Descritpion Some times brute forcing doesnt give the desired results. A detailed analysis of the responses of the brute force attack is needed to identify the subtle differences in the resposne. Instructions 1. Login to the account using random username and password 

## Description

# Descritpion

Some times brute forcing doesnt give the desired results. A detailed analysis of the responses of the brute force attack is needed to identify the subtle differences in the resposne.

# Instructions

1. Login to the account using random username and password

2. From the proxy tab, under HTTP History , identify the login request and send the request to the intruder tab.

3.From the positions tab, slect attack type to sniper

4. Select the username from the *positions *tab and click on *add *to the username parameter value to the payload position

5.Use the provided the list of usernames provided or use any username paylaods from [*https://github.com/danielmiessler/SecLists/tree/master/Usernames/Name](https://github.com/danielmiessler/SecLists/tree/master/Usernames/Names)s and pate them in the paylaod tab*

6.Click on *options *tab ,under *grep-extract* , click *add *. Scroll down in the response.

7. Identify the *invalid username or password*. Highlight the text .

8.Click on ok to start the attack.

9. When the attack finishes , notice the additional column which shows the error message.On closer analysis of error messages , the hihlighted response contains a typo error meesage. It doent have the full stop at the end of the error message invalid username or password Make a note of the username *accounting*

10.Repeat the same steps 3 to 9 for the password filed . 

11. Use the username  and passwords identified from steps 9 and 10 to login.

12. Observe that the login is successful

## Tags

- [[Enumeration]]
- [[Web Applications]]
