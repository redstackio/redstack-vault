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



![f4fce536-afd3-4858-88e9-0ad9626a03c3.png]()





2.In the burp intruder tab, highlight the last octet of the IP and then click on *add *to add the octet for bruteforcing the last octet.





![f98f61d2-98b1-4ffd-890a-af5003c867df.png]()







3.Navigate to *payloads *tab in the bur intruder tab and change the payload type to* numbers *and enter " 1" in the *to *field and "255" in the *from *filed . Choose *step *in the below option and start attack. A new window will be opened.



![080ffa87-2c1f-4a25-abbe-b4f4c466eb5b.png]()







4. Observe the status in the now opened attack window. Check the response of the 200 status code . The response shows the admin interface. 





![9cc0808c-430c-4cc0-847a-c56ad479c782.png]()





## Platforms

- Web

## Tags

- [[SSRF]]
- [[Web Applications]]


