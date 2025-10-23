---
id: f817a0d2-6f1f-49f3-a29e-19760314ccb1
name: Price Tampering In E-commerce Applications
type: procedure
verified: true
submitted: true
created_at: '2020-08-04T19:24:11.462445+00:00'
updated_at: '2023-05-26T15:56:13.268534+00:00'
platforms:
- Web
tags:
- '[[Parameter Tampering]]'
- '[[Web Applications]]'
---

# Price Tampering In E-commerce Applications

**Status**: ✓ Verified

## Summary

If price parameter with a value is observed in the request, it can be modified by intercepting the request to purchase the product for a lower value. 

## Description

# Description

If price parameter with a value is observed in the request, it can be modified by intercepting the request to purchase the product for a lower value.

# 

# Instructions





1. Wallet amount in the screenshot is 1000 and price of each quantity is 250







![11af8631-69c8-4d2b-bab6-567b17e1ba04.jpg](_assets/images/Mash/11af8631-69c8-4d2b-bab6-567b17e1ba04.jpg)









2. Enter the quantity as 1





![970db0af-84e1-4e32-ac58-ba998d9c661a.jpg](_assets/images/Mash/970db0af-84e1-4e32-ac58-ba998d9c661a.jpg)















3. Intercept the request and modify the price parameter to any other value. Here it is modified to 50 instead of 250.









![54e9b46d-550d-4812-afd7-76bde3d9abf5.jpg](_assets/images/Mash/54e9b46d-550d-4812-afd7-76bde3d9abf5.jpg)













4. After forwarding the request, the order is placed successfully









![a86e78d0-b9da-4ccc-b0e8-716819ca37e3.jpg](_assets/images/Mash/a86e78d0-b9da-4ccc-b0e8-716819ca37e3.jpg)











5. Click on Home and observe that the product is booked for a value lower than the actual one. Wallet amount is reduced by 50.







![ce859728-a308-46a4-9571-42a6927c5d96.jpg](_assets/images/Mash/ce859728-a308-46a4-9571-42a6927c5d96.jpg)









## Platforms

- Web

## Tags

- [[Parameter Tampering]]
- [[Web Applications]]


