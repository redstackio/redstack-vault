---
id: f4f47150-536e-41ff-92a6-aaebb71b233f
name: parsero
type: tool
verified: false
created_at: '2019-08-28T21:17:36.557598+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# parsero

## Overview

Parsero is a free script written in Python which reads the Robots.txt file of a web server and looks at the Disallow entries. The Disallow entries tell the search engines what directories or files hosted on a web server mustn’t be indexed. For example, “Disallow: /portal/login” means that the conte

## Description

Parsero is a free script written in Python which reads the Robots.txt file of a web server and looks at the Disallow entries. The Disallow entries tell the search engines what directories or files hosted on a web server mustn’t be indexed. For example, “Disallow: /portal/login” means that the content on www.example.com/portal/login it’s not allowed to be indexed by crawlers like Google, Bing, Yahoo… This is the way the administrator have to not share sensitive or private information with the search engines.But sometimes these paths typed in the Disallows entries are directly accessible by the users without using a search engine, just visiting the URL and the Path, and sometimes they are not available to be visited by anybody… Because it is really common that the administrators write a lot of Disallows and some of them are available and some of them are not, you can use Parsero in order to check the HTTP status code of each Disallow entry in order to check automatically if these directories are available or not.Also, the fact the administrator write a robots.txt, it doesn’t mean that the files or directories typed in the Dissallow entries will not be indexed by Bing, Google, Yahoo… For this reason, Parsero is capable of searching in Bing to locate content indexed without the web administrator authorization. Parsero will check the HTTP status code in the same way for each Bing result.






