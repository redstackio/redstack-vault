---
id: 5c0b9508-a2e9-43a0-a90b-6f4cf9abce4e
name: 'DOM XSS Using Web Messages & JSON.parse '
type: procedure
verified: true
submitted: true
created_at: '2020-08-31T14:35:36.746931+00:00'
updated_at: '2023-05-26T01:36:09.708027+00:00'
platforms:
- Web
tags:
- '[[DOM XSS]]'
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
---

# DOM XSS Using Web Messages & JSON.parse 

**Status**: ✓ Verified

## Summary

An attacker will get his payload executed by using the application's JSON.parse . 

## Description

# Description

An attacker will get his payload executed by using the application's JSON.parse .

# Instructions







1.Access the application and right click on the page and select *view page source *







![02a54494-9592-42a3-aa0d-e968bbab85fd.png]()





2.Observe that the page contains an event listener and the message recieved is parsed using JSON.parse







![ba38608c-bc40-447e-933a-66f7da0082cc.png]()





3. Craft a payload in similar way as below



The postmessage() funtion sends a web message to the home page and the event listener onload recieves the message and parses the message using JSON.parse







**Code**: [[<iframe src=https://ac831fff1e627a4780714f27008a00]]







4.Load the payload from the above step in the browser and observe that a alert pop can be seen.





![ac00d351-30f2-4c5d-8f5a-dba2f91f36a1.png]()



## Platforms

- Web

## Tags

- [[DOM XSS]]
- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]


