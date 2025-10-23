---
id: f2d65daa-f252-42c5-abe2-34ad50700ab0
name: 'XPath Injection Through Search '
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T16:17:37.677420+00:00'
updated_at: '2023-05-26T01:26:27.854062+00:00'
platforms:
- Web
tags:
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
- '[[xml]]'
---

# XPath Injection Through Search 

**Status**: ✓ Verified

## Summary

An attacker will craft an XML query through XPath to maliciously exfilitrate the sensitive information from application's server . 

## Description

# Description

 An attacker will craft an XML query through XPath to maliciously exfilitrate the sensitive information from application's server .

# 

# Instructions

# 

1.Observe the url with two parameters with user controlled data. 



![787d258b-3186-4082-9b29-fa64bf61f3dd.PNG](_assets/images/Mash/787d258b-3186-4082-9b29-fa64bf61f3dd.PNG)



2.Try to generate an error message to enumerate the application's server information through injecting *single quote *after the* action *in url.





![bd55b6f6-070c-4746-a5d3-a75d516fa5f2.PNG](_assets/images/Mash/bd55b6f6-070c-4746-a5d3-a75d516fa5f2.PNG)





3.An error message can be observed in the response page which reveals Xpath being in use for querying data.







![ffb5480b-7086-4e40-aa54-259775ad00bb.PNG](_assets/images/Mash/ffb5480b-7086-4e40-aa54-259775ad00bb.PNG)









4. Construct a XML query through XPath to reveal password information from backend files and insert in the url aas shown below .



*Payload  :  ')]/password | a[contains(a,'*





![50eb1ea8-c1d5-44e5-b925-828765544591.PNG](_assets/images/Mash/50eb1ea8-c1d5-44e5-b925-828765544591.PNG)





5. Submitting the request with* payload w*ill reveal sensitive information.* *







![2d9026c1-8d0c-48ad-9da0-47acb9357eec.PNG](_assets/images/Mash/2d9026c1-8d0c-48ad-9da0-47acb9357eec.PNG)















## Platforms

- Web

## Tags

- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
- [[xml]]


