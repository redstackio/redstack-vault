---
id: 7e8b2a12-f5b6-43ac-98d0-e47c96d92b2b
name: Reflected XSS With Most Tags & Attributes Blocked
type: procedure
verified: true
submitted: true
created_at: '2020-08-27T09:13:27.032958+00:00'
updated_at: '2023-05-26T01:15:43.470598+00:00'
platforms:
- Web
tags:
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Reflected XSS]]'
- '[[Web Applications]]'
---

# Reflected XSS With Most Tags & Attributes Blocked

**Status**: ✓ Verified

## Summary

Descritpion Most of the applications block few tags and attributes in getting executed in JS . This can be bypassed by testing all the available tags and attributes in HTML context using burp intruder tab. Then with the accepted tags and attributes , a malicious payload can be crafted. Instructions

## Description

# Descritpion

Most of the applications block few tags and attributes in getting executed in JS . This can be bypassed by testing all the available tags and attributes in HTML context using burp intruder tab. Then with the accepted tags and attributes , a malicious payload can be crafted.

# Instructions

1.Inject a standard XSS payload such as: `<img src=1 onerror=alert(document.cookie)>`

2. Observe that this payload gets blocked. Now we need to find an allowed tag.

3.With your browser proxying traffic through Burp Suite, use the search function in the lab. Send the resulting request to Burp Intruder

4.Replace the value of the search term with: `<> `Place the cursor between the angle brackets and click "Add §" twice, to create a payload position. The value of the search term should now look like: `<§§>`

5.Use XSS cheat sheet and click on *copy tags to clipboard* to copy all the available tags .

6.Paste the copied tags from the above step in the *payloads *tab of the burp intruder and then click on *start attack*.

7.Observe that all payloads caused an HTTP 400 response, except for the `body` payload, which caused a 200 response as it is the only allowed tag.

8. Now back to the Positions tab in Burp Intruder, replace search term with: `<body%20=1>. Click on *add* to add the payload positio`n.

9.Use XSS cheat sheet and click on *copy events to clipboard*  to copy all the available attributes.

10.Paste the copied events from the above step in the *payloads *tab of the burp intruder and then click on *start attack*.

11Observe that all payloads caused an HTTP 400 response, except for the `onresize`payload, which caused a 200 response as it is the only allowed event.

12. Following the is the final payload with the tag and attribute accepted by the application. Craft an exploit with the paylaod and load it in the browser . A response can be seen with a alert popup visible. 

*`<iframe src="https://your-lab-id.web-security-academy.net/?search=%22%3E%3Cbody%20onresize=alert(document.cookie)%3E" onload=this.style.width='100px'*>`

## Platforms

- Web

## Tags

- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Reflected XSS]]
- [[Web Applications]]
