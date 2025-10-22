---
id: ee333deb-0625-4120-ab1a-966689311475
name: SSRF To Access Back-end Systems
type: procedure
verified: true
submitted: true
created_at: '2020-08-17T14:33:17.543551+00:00'
updated_at: '2023-05-26T01:09:22.075933+00:00'
platforms:
- Web
tags:
- '[[SSRF]]'
- '[[Web Applications]]'
---

# SSRF To Access Back-end Systems

**Status**: ✓ Verified

## Summary

An attacker can exploit the SSRF vulnerability to access application's back-end systems. These back-end systems have internal IPs not reachable to the application's users. 

## Description

# Description

An attacker can exploit the SSRF vulnerability to access application's back-end systems. These back-end systems have internal IPs not reachable to the application's users.

# Instructions

1.Navigate to product , click on* check stock*. Intercept the request using BurpSuite and send the request to *intruder* tab. Change the stopckapi parameter to *http://192.168.0.1:8080/admin*

2.In the burp intruder tab, highlight the last octet of the IP and then click on *add *to add the octet for bruteforcing the last octet.

3.Navigate to *payloads *tab in the bur intruder tab and change the payload type to* numbers *and enter " 1" in the *to *field and "255" in the *from *filed . Choose *step *in the below option and start attack. A new window will be opened.

4. Observe the status in the now opened attack window. Check the response of the 200 status code . The response shows the admin interface. 

## Platforms

- Web

## Tags

- [[SSRF]]
- [[Web Applications]]
