---
id: 5eebb632-cba1-4e01-94cb-3ea0bd540fc0
name: HTTP Request Smuggling To Perform Web Cache Deception
type: procedure
verified: true
submitted: true
created_at: '2020-08-18T14:22:22.651619+00:00'
updated_at: '2023-05-26T18:10:27.854878+00:00'
platforms:
- Web
tags:
- '[[http request smuggling]]'
- '[[Web Applications]]'
- '[[web cache deception]]'
---

# HTTP Request Smuggling To Perform Web Cache Deception

**Status**: ✓ Verified

## Summary

For this kind og attack to happen, the application's front end server doesn't support chunked encoding and the front end server is caching static resources making it possible to perform web cache deception by ssmuggling request to the back-end. 

## Description

# Description

For this kind og attack to happen, the application's front end server doesn't support chunked encoding and the front end server is caching static resources making it possible to perform web cache deception by ssmuggling request to the back-end.

# Instructions



1. Login to the application using credentials.





![c044e05d-b11c-4861-a6b6-e3112ab1eade.png]()







2. Click "Account Details" on the top right, and observe that the response doesn't have any anti-caching headers







![ca4ffb70-44b3-427b-b9b9-2ce9c3a7c638.png]()





3.Smuggle a request to fetch the API key:



Add following to the request from step 2:



0

GET /apikey HTTP/1.1

x-ignore: X



![c53ccfeb-089f-44df-a698-2c7b3d494d55.png]()



4. Repeat this request a few times, then load the home page in an incognito browser window.

Use the Search function on the Burp menu to see if the phrase "Your API Key" has appeared in any static resources. If it hasn't, repeat the POST requests, force-reload the browser window, and re-run the search.





![be869ca7-321f-4bb8-85ef-fd0b1069477d.png]()





5. Observe the apikey in the following which is fetced by smuggling request.







![718c6297-bfae-4fe5-ac19-eabf68b12f72.png]()



## Platforms

- Web

## Tags

- [[http request smuggling]]
- [[Web Applications]]
- [[web cache deception]]


