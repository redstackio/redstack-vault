---
id: fd1f5484-36d8-4e40-9baa-0ff495e05cf3
name: Insecure Deserialisation(Modify Serial Data Types)
type: procedure
verified: true
submitted: true
created_at: '2020-08-17T18:07:08.224478+00:00'
updated_at: '2023-05-26T01:07:26.748997+00:00'
platforms:
- Web
tags:
- '[[Insecure Deserialisation]]'
- '[[Web Applications]]'
---

# Insecure Deserialisation(Modify Serial Data Types)

**Status**: ✓ Verified

## Summary

An attacker will exploit the datatype present in the serialised PHP object to access the unexpected data. 

## Description

# Description

An attacker will exploit the datatype present in the serialised PHP object to access the unexpected data.

# 

# Instructions

# 

1. Login to the application with the credentials.







![4edd1ff1-f80b-49b5-9bcb-0debbee0a282.png]()





2. Intercept the request and send the request to the repeater tab . select the session cookie and navigate to *decoder *tab on the burpsuite.







![94792cc1-0609-4a22-9dea-93559ccde69d.png]()







3. Change the access token in the session cookie to integer 0 and replace the datatype label from s to i. 

The modified object looks like this :



*O:4:"User":2:{s:8:"username";s:13:"administrator";s:12:"access_token";i:0;}*



![1839bb7f-17d1-4f11-9a50-b52b9adf5e43.png]()





4.. Base64 and URL-encode the object. Copy the URL-encoded string to your clipboard





![9ff692d3-6f98-4c6f-9408-1eeecad21447.png]()





5. Replace the session cookie value with the modified value from step 4 and send the request from repeater tab to the server.Observe that the response contains the admin interface.





![ed9b97bd-b410-4bff-ba90-50504a936413.png]()



## Platforms

- Web

## Tags

- [[Insecure Deserialisation]]
- [[Web Applications]]


