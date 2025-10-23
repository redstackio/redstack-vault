---
id: d719ca64-527b-4789-a71d-8bc9a5fa0666
name: Web Cache Poisoning With an Unkeyed Header
type: procedure
verified: true
submitted: true
created_at: '2020-08-18T15:53:49.105443+00:00'
updated_at: '2023-05-26T01:23:39.090333+00:00'
platforms:
- Web
tags:
- '[[Web Applications]]'
- '[[web cache posioning]]'
---

# Web Cache Poisoning With an Unkeyed Header

**Status**: ✓ Verified

## Summary

An attacker may be able to eploit the weak implementation of web cache where the application server handles input from an unkeyed header in an unsafe way. 

## Description

# Description

An attacker may be able to eploit the weak implementation of web cache where the application server handles input from an unkeyed header in an unsafe way.



# Instructions



1.With Burp running, load the website's home page. In Burp, go to "Proxy" > "HTTP history" and observe the requests and responses in the HTTP History. Find the GET request for the home page and send it to Burp Repeater.





![f72d7216-0bcd-4ad9-a422-ac00bac14ef5.png]()







2.Add a cache-buster query parameter, such as ?cb=1234.







![91895faf-8870-4bb9-946e-f988c3850682.png]()





3.Add the X-Forwarded-Host header to dynamically generate an absolute URL for importing a JavaScript file stored at /resources/js/tracking.js.







![57c21e83-b8cf-4da4-82ee-cfb0e8568524.png]()





4.Replay the request and observe the response which contains the header *X-Cache: hit*





![942f29be-8b30-4911-98bf-1709c61d2d5a.png]()





5.Change the file name to match the path used by the vulnerable response: /resources/js/tracking.js





![3348886b-c0d6-4999-8c41-56d681db4225.png]()





6.In the body, enter the payload alert(document.cookie).Keep sending the request every few seconds to re-poison the cache until the victim is affected





![15da7eaf-d20b-4763-85b6-c34cba404314.png]()







## Platforms

- Web

## Tags

- [[Web Applications]]
- [[web cache posioning]]


