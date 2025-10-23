---
id: 51343a1a-9137-4951-b75b-05b1e3144307
name: PixieWPS
type: tool
verified: false
created_at: '2019-08-28T21:17:19.954739+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# PixieWPS

## Overview

Pixiewps is a tool written in C used to bruteforce offline the WPS pin exploiting the low or non-existing entropy of some APs (pixie dust attack). It is meant for educational purposes only. All credits for the research go to Dominique Bongard.Features: Checksum optimization: it’ll try first for val

## Description

Pixiewps is a tool written in C used to bruteforce offline the WPS pin exploiting the low or non-existing entropy of some APs (pixie dust attack). It is meant for educational purposes only. All credits for the research go to Dominique Bongard.Features:



Checksum optimization: it’ll try first for valid PINs (11’000);



Reduced entropy of the seed from 32 to 25 bits for the C LCG pseudo-random function;



Small Diffie-Hellman keys: don’t need to specify the Public Registrar Key if the same option is used with Reaver.



The program will also try first with E-S0 = E-S1 = 0, then it’ll tries to bruteforce the seed of the PRNG if the –e-nonce option is specificed.






