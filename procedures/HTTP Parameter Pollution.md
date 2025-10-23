---
id: 2bab2eea-1488-472c-8f69-c90b1afc3439
name: HTTP Parameter Pollution
type: procedure
verified: true
submitted: true
created_at: '2020-08-03T18:05:48.202895+00:00'
updated_at: '2023-05-26T01:24:04.356666+00:00'
platforms:
- Web
tags:
- '[[HPP]]'
- '[[Parameter Pollution]]'
- '[[Web Applications]]'
---

# HTTP Parameter Pollution

**Status**: ✓ Verified

## Summary

If same parameter name is sent in the request with multiple values, application will either accept the first or second occurrence of the parameter. 

## Description

# Description

If same parameter name is sent in the request with multiple values, application will either accept the first or second occurrence of the parameter. 



# Instructions

# 

1. Access the application







![cc26de79-b2c3-477d-a947-5c77aa751d34.png]()





2. Choose any title from the list and click on vote



![440f5245-c14f-4413-b5dc-30a571c58b30.PNG](_assets/images/Mash/440f5245-c14f-4413-b5dc-30a571c58b30.PNG)





3. Vote is casted for the 4th movie which can be observed in the movie parameter in the URL. The value of movie parameter is 4.







![a323841a-c1f6-4c43-be18-aca8e8e55911.PNG](_assets/images/Mash/a323841a-c1f6-4c43-be18-aca8e8e55911.PNG)







4. Use the movie parameter again by adding it at the end of the URL and modify the value to 1. In the below screenshot, it is observed that the vote is casted to 1st movie.









![8e2464b4-093b-4ae0-9b17-d5806b4ff314.PNG](_assets/images/Mash/8e2464b4-093b-4ae0-9b17-d5806b4ff314.PNG)











## Platforms

- Web

## Tags

- [[HPP]]
- [[Parameter Pollution]]
- [[Web Applications]]


