---
id: c506ef11-6f25-43d7-9ce1-7adac0780f01
name: pdfid
type: tool
verified: false
created_at: '2019-08-28T21:17:32.768913+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# pdfid

## Overview

This tool is not a PDF parser, but it will scan a file to look for certain PDF keywords, allowing you to identify PDF documents that contain (for example) JavaScript or execute an action when opened. PDFiD will also handle name obfuscation.The idea is to use this tool first to triage PDF documents,

## Description

This tool is not a PDF parser, but it will scan a file to look for certain PDF keywords, allowing you to identify PDF documents that contain (for example) JavaScript or execute an action when opened. PDFiD will also handle name obfuscation.The idea is to use this tool first to triage PDF documents, and then analyze the suspicious ones with my pdf-parser.An important design criterium for this program is simplicity. Parsing a PDF document completely requires a very complex program, and hence it is bound to contain many (security) bugs. To avoid the risk of getting exploited, I decided to keep this program very simple (it is even simpler than pdf-parser.py).






