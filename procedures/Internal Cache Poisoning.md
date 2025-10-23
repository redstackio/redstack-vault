---
id: daf338a5-0783-4751-a995-9010d4112755
name: Internal Cache Poisoning
type: procedure
verified: true
submitted: true
created_at: '2020-09-03T17:49:18.390332+00:00'
updated_at: '2023-05-26T01:16:11.065879+00:00'
platforms:
- Web
tags:
- '[[Web Applications]]'
- '[[web cache posioning]]'
---

# Internal Cache Poisoning

**Status**: ✓ Verified

## Summary

Few applications implement internal cache techniques. Caching can be implemented on small fragments of the response instead on the whole response. An attacker can try to exploit this implementation by poisoning these internal cache pages. 

## Description

# Description

Few applications implement internal cache techniques. Caching can be implemented on small fragments of the response instead on the whole response. An attacker can try to exploit this implementation by poisoning these internal cache pages.

# Instructions







1. Acces the application's home page with burp running and proxying the requests.





![ba95eb1a-1579-477c-a00a-180a20b7010a.png]()





2.Identify the GET / request from the HTTP History and send the request to the repeater tab. Notice that the server accpets X-Forwarded-Host header by sending a request to the server with the header.



![39fce276-99f0-42f1-b3c3-4aaaf78593d0.png]()





3.Modify the X-forwarded-Host header value to that of exploit server where you will be hosting the malicious code.





![e762d5eb-dfe5-4ceb-b858-0bed5a61360e.png]()



4.Keep sending the request to the server until  the canonical link element , analytics.js and geolacate.js is posined with exploit server host.





![3228fb5c-69ef-4731-9b90-a0179c69b051.png]()







5. Craft a malicoious JS adn host it on the exploit server to serve to the victim . When the victim access the internally poisoned cache , the maclicious code hosted on the server gets executed .





![939faeee-1552-4652-9a65-8e0224120a84.png]()

















## Platforms

- Web

## Tags

- [[Web Applications]]
- [[web cache posioning]]


