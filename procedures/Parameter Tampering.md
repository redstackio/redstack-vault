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

2.Go to your cart and proceed to checkout.

3.While proxying with Burp Suite , fill all the billing details and proceed to pay via preferred payment gateway like paypal.

4.Now go to Burp Proxy and find the correct request with item amount and shipping charge.

5.Alter the shipping charge to 0 and amount to 1 and forward the request.

6.Turn off the intercept and go to the browser to observe the tampered price at the paypay gateway.

## Platforms

- Web

## Tags

- [[Parameter Tampering]]
- [[Web Applications]]
