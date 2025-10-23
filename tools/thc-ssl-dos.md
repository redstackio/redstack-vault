---
id: 535a2404-714d-434a-9164-a12661fd262b
name: thc-ssl-dos
type: tool
verified: false
created_at: '2019-08-28T21:17:41.523281+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# thc-ssl-dos

## Overview

THC-SSL-DOS is a tool to verify the performance of SSL. Establishing a secure SSL connection requires 15x more processing power on the server than on the client. THC-SSL-DOS exploits this asymmetric property by overloading the server and knocking it off the Internet. This problem affects all SSL im

## Description

THC-SSL-DOS is a tool to verify the performance of SSL. Establishing a secure SSL connection requires 15x more processing power on the server than on the client. THC-SSL-DOS exploits this asymmetric property by overloading the server and knocking it off the Internet. This problem affects all SSL implementations today. The vendors are aware of this problem since 2003 and the topic has been widely discussed. This attack further exploits the SSL secure Renegotiation feature to trigger thousands of renegotiations via single TCP connection.






