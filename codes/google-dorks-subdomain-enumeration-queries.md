---
id: 4bb6eed2-0654-4ef4-a76e-e57404428a01
type: code
language: text
verified: true
created_at: '2023-04-06T03:56:25.425808+00:00'
updated_at: '2023-04-10T20:25:37.764859+00:00'
platforms:
  - Web
tags:
  - reconnaissance
  - google-dorks
  - subdomain-enumeration
validated: true
---

# google-dorks-subdomain-enumeration-queries

## Code

```text
site:*.domain.com -www
site:domain.com filetype:pdf
site:domain.com inurl:'&'
site:domain.com inurl:login,register,upload,logout,redirect,redir,goto,admin
site:domain.com ext:php,asp,aspx,jsp,jspa,txt,swf
site:*.*.domain.com
```

## Description

This code snippet is a collection of Google Dork queries for comprehensive subdomain enumeration and asset discovery. Copy-paste each line into the Google search bar sequentially to gather subdomains, files, and vulnerable URLs during passive reconnaissance. It combines basic and advanced operators to build a full picture of the target's web presence.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| domain.com | Target domain to replace in all queries | example.com |

## Usage

Use in a reconnaissance phase of red teaming or pentesting. Start with subdomain queries, then move to file and URL searches. Script these into a browser automation tool (e.g., Selenium) for efficiency, or manually execute. Cross-reference results with tools like Sublist3r for validation. Ideal for scoping engagements where direct DNS queries are restricted.

## Detection

- Unusual search patterns from IP addresses (Google logs may flag high-volume dork usage).
- No direct network indicators since it's passive, but correlate with subsequent scans on discovered subdomains.
- Monitor for automated browser traffic to google.com from recon tools.

## Related

- [[procedures/Subdomain-Enumeration-with-Google-Dorks]]
- [[tools/Google-Search]] (if formalized as a tool)
