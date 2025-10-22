---
id: bfd75c6c-7fcc-4555-9ef4-cac655b11845
name: dumpzilla
type: tool
verified: false
created_at: '2019-08-28T21:17:28.370737+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# dumpzilla

## Overview

Dumpzilla application is developed in Python 3.x and has as purpose extract all forensic interesting information of Firefox, Iceweasel and Seamonkey browsers to be analyzed. Due to its Python 3.x developement, might not work properly in old Python versions, mainly with certain characters. Works und

## Description

Dumpzilla application is developed in Python 3.x and has as purpose extract all forensic interesting information of Firefox, Iceweasel and Seamonkey browsers to be analyzed. Due to its Python 3.x developement, might not work properly in old Python versions, mainly with certain characters. Works under Unix and Windows 32/64 bits systems. Works in command line interface, so information dumps could be redirected by pipes with tools such as grep, awk, cut, sed… Dumpzilla allows to visualize following sections, search customization and extract certain content.

Cookies + DOM Storage (HTML 5).

User preferences (Domain permissions, Proxy settings…).

Downloads.

Web forms (Searches, emails, comments..).

Historial.

Bookmarks.

Cache HTML5 Visualization / Extraction (Offline cache).

visited sites “thumbnails” Visualization / Extraction .

Addons / Extensions and used paths or urls.

Browser saved passwords.

SSL Certificates added as a exception.

Session data (Webs, reference URLs and text used in forms).

Visualize live user surfing, Url used in each tab / window and use of forms.

Dumpzilla will show SHA256 hash of each file to extract the information and finally a summary with totals.

Sections which date filter is not possible: DOM Storage, Permissions / Preferences, Addons, Extensions, Passwords/Exceptions, Thumbnails and Session
