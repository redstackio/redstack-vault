---
id: 515625a2-4285-4906-9272-9a48bd2ff44e
name: Web Cache Posioning Unknown Header (Param Miner)
type: procedure
verified: true
submitted: true
created_at: '2020-08-20T02:49:23.019761+00:00'
updated_at: '2023-05-26T18:39:20.246310+00:00'
platforms:
- Web
tags:
- '[[Web Applications]]'
- '[[web cache posioning]]'
---

# Web Cache Posioning Unknown Header (Param Miner)

**Status**: ✓ Verified

## Summary

Param Miner is an burp extension that can be used to identify the secret/hidden parameters. Its mostly useful in identifying the web cache poisoning vulnerabilities. 

## Description

# Description

 Param Miner is an burp extension that can be used to identify the secret/hidden parameters. Its mostly useful in identifying the web cache poisoning vulnerabilities.

# Instructions

1. With burp *intercept off* and burp running , browse the application to log all the requests in *http history* tab. Identify the GET request of the homepage and send the request to *repeater *tab.

2.Right click on the request in the repeater tab and select "Guess headers"  ( Param Miner need to be enabled for this option to be shown).Param miner will identify the hidden parameter *x-host* header. Add the identified paramter to the request in the repeater tab and also add cache buster in the *GET* request url.

3.Send the modified request to the server. Observe that the value in x-host header is used to dynamically generate an url for importing the javascript file.

4.Craft a payload with *document.cookie *.

5. Modify the* x-host* header parameter to the exploit crafted in step 4. Observe that modified x-host header is being reflected in the response to generate an url for importing java script as in step 3.

6.Keep sending the request to server until *x-cache : hit* is observed in the response headers. Observe the vary header in the response is used to specify the user-agent as part of the cache key. We need to identify the victim's user agent to target.

Paste the following payload in the commnet section of the application to interact with attacker's server.

*payload  <img src="https://your-exploit-server-id.web-security-academy.net/foo" />*

7. Access the server logs of the exploit to identify the victim's user-agent and copy the useragent to clip board.

8.Modify the request by replacing the user-agent with the victim's user-agent and remove the cache buster from the GET url. Keep sending the request to the sever until *x-cache : hit* is observed in the response which confirms the cache being poisoned . Victim access the application while the cache is poisoned.

## Platforms

- Web

## Tags

- [[Web Applications]]
- [[web cache posioning]]
