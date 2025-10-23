---
id: 36b17e39-2824-4c69-982e-2a8539657d38
name: Reflected DOM XSS
type: procedure
verified: true
submitted: true
created_at: '2020-08-23T18:03:15.781222+00:00'
updated_at: '2023-05-26T18:39:04.335999+00:00'
platforms:
- Web
tags:
- '[[Reflected DOMXSS]]'
- '[[Web Applications]]'
---

# Reflected DOM XSS

**Status**: ✓ Verified

## Summary

Descritpion In reflected DOM xss, the server side process the payload from a request and the payload gets reflected in the response. Instructions 1. Enter the text xss in the search box as shown below. 

## Description

Descritpion

In reflected DOM xss, the server side process the payload from a request and the payload gets reflected in the response.



Instructions





1. Enter the text xss in the search box as shown below.







![b19eed62-1efb-49b7-901f-985f0b8b603d.png]()





2.Intercept the request using burpsite.





![50b9cff3-e22f-4fe1-a9af-2778681cc85c.png]()







3. observe the response reflects the search term *xss *in the body.





![45f687bc-b7c9-405a-b34b-2664cdc5bd22.png]()





4.Use the developer tools in chrome browser to identify the searchresults.js. It can be seen that the JS file eval() function call .





![45e18c0f-61e6-4222-8c27-134a6a92dbc1.png]()







5. Observe that the search term in the application doesnot escape the'\' in the JSON response.







![fa92622f-1975-4279-9f9d-6766f1f014a5.png]()







6. Enter the payload ***\"-alert(1)*}// in the search field **





![0d7ba3c4-e641-4635-b320-6343dd8a0319.png]()







6. Payload gets executed and a alert(1) can be seen.





![144556f8-f131-49db-9cb2-8cdfef409164.png]()



## Platforms

- Web

## Tags

- [[Reflected DOMXSS]]
- [[Web Applications]]


