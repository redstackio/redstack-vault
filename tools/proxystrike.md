---
id: 121e43d4-6652-449c-933f-38d4f5d7b025
name: ProxyStrike
type: tool
verified: false
created_at: '2019-08-28T21:17:32.642546+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# ProxyStrike

## Overview

ProxyStrike is an active Web Application Proxy. It’s a tool designed to find vulnerabilities while browsing an application. It was created because the problems we faced in the pentests of web applications that depends heavily on Javascript, not many web scanners did it good in this stage, so we cam

## Description

ProxyStrike is an active Web Application Proxy. It’s a tool designed to find vulnerabilities while browsing an application. It was created because the problems we faced in the pentests of web applications that depends heavily on Javascript, not many web scanners did it good in this stage, so we came with this proxy.Right now it has available Sql injection and XSS plugins. Both plugins are designed to catch as many vulnerabilities as we can, it’s that why the SQL Injection plugin is a Python port of the great DarkRaver “Sqlibf”.The process is very simple, ProxyStrike runs like a proxy listening in port 8008 by default, so you have to browse the desired web site setting your browser to use ProxyStrike as a proxy, and ProxyStrike will analyze all the paremeters in background mode. For the user is a passive proxy because you won’t see any different in the behaviour of the application, but in the background is very active. :)Some features:

Plugin engine (Create your own plugins!)

Request interceptor

Request diffing

Request repeater

Automatic crawl process

Http request/response history

Request parameter stats

Request parameter values stats

Request url parameter signing and header field signing

Use of an alternate proxy (tor for example ;D )

Sql attacks (plugin)

Server Side Includes (plugin)

Xss attacks (plugin)

Attack logs

Export results to HTML or XML
