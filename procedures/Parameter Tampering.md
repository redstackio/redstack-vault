---
id: a6e2d7b8-13a9-4a3b-b21b-ffacb242c445
name: Parameter Tampering
type: procedure
verified: true
submitted: true
created_at: '2020-08-23T17:16:02.852469+00:00'
updated_at: '2023-05-26T01:24:18.902855+00:00'
platforms:
- Web
tags:
- '[[Parameter Tampering]]'
- '[[Web Applications]]'
---

# Parameter Tampering

**Status**: ✓ Verified

## Summary

An attacker will manipulate the parameters of the application to bypass application's buisness logic. 

## Description

# Description

An attacker will manipulate the parameters of the application to bypass application's buisness logic.

# Instructions



1.Visit vulnerable domain and open the product you want to buy and add it in the cart.







![9c408bdc-3a80-457a-ab22-dc30e9a1921b.png]()





2.Go to your cart and proceed to checkout.





![003f5cfb-45cf-4811-bbb7-01d68e3460dc.png]()







3.While proxying with Burp Suite , fill all the billing details and proceed to pay via preferred payment gateway like paypal.







![540cf90b-564d-44d1-8069-e1fd8e3f4495.png]()







4.Now go to Burp Proxy and find the correct request with item amount and shipping charge.





![afb50ea2-a7d9-41ce-b9d4-a661eb3fdb1f.png]()







5.Alter the shipping charge to 0 and amount to 1 and forward the request.





![470cb466-9fc2-4839-a13d-e161b0ac7fa3.png]()









6.Turn off the intercept and go to the browser to observe the tampered price at the paypay gateway.





![e5e68d98-dc82-4bed-a27b-0e73e61f70d6.png]()



## Platforms

- Web

## Tags

- [[Parameter Tampering]]
- [[Web Applications]]


