---
id: cbc7312a-e829-4716-acdb-d99131149213
name: bbqsql
type: tool
verified: false
created_at: '2019-08-28T21:17:37.778539+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# bbqsql

## Overview

Blind SQL injection can be a pain to exploit. When the available tools work they work well, but when they don’t you have to write something custom. This is time-consuming and tedious. BBQSQL can help you address those issues.BBQSQL is a blind SQL injection framework written in Python. It is extreme

## Description

Blind SQL injection can be a pain to exploit. When the available tools work they work well, but when they don’t you have to write something custom. This is time-consuming and tedious. BBQSQL can help you address those issues.BBQSQL is a blind SQL injection framework written in Python. It is extremely useful when attacking tricky SQL injection vulnerabilities. BBQSQL is also a semi-automatic tool, allowing quite a bit of customization for those hard to trigger SQL injection findings. The tool is built to be database agnostic and is extremely versatile. It also has an intuitive UI to make setting up attacks much easier. Python gevent is also implemented, making BBQSQL extremely fast.Similar to other SQL injection tools you provide certain request information.Must provide the usual information:



URL



HTTP Method



Headers



Cookies



Encoding methods



Redirect behavior



Files



HTTP Auth



Proxies



Then specify where the injection is going and what syntax we are injecting.






