---
id: c2aef0ba-375e-4fd2-8f43-a4c7a4360b64
name: sqlsus
type: tool
verified: false
created_at: '2019-08-28T21:17:19.149478+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# sqlsus

## Overview

sqlsus is an open source MySQL injection and takeover tool, written in perl.Via a command line interface, you can retrieve the database(s) structure, inject your own SQL queries (even complex ones), download files from the web server, crawl the website for writable directories, upload and control a

## Description

sqlsus is an open source MySQL injection and takeover tool, written in perl.Via a command line interface, you can retrieve the database(s) structure, inject your own SQL queries (even complex ones), download files from the web server, crawl the website for writable directories, upload and control a backdoor, clone the database(s), and much more…

Whenever relevant, sqlsus will mimic a MySQL console output.sqlsus focuses on speed and efficiency, optimizing the available injection space, making the best use (I can think of) of MySQL functions.

It uses stacked subqueries and an powerful blind injection algorithm to maximize the data gathered per web server hit.

Using multi-threading on top of that, sqlsus is an extremely fast database dumper, be it for inband or blind injection.If the privileges are high enough, sqlsus will be a great help for uploading a backdoor through the injection point, and takeover the web server.It uses SQLite as a backend, for an easier use of what has been dumped, and integrates a lot of usual features (see below) such as cookie support, socks/http proxying, https.
