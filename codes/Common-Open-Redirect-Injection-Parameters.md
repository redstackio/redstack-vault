---
id: f562e9b7-53b1-4a05-970d-52d50fb6c96d
name: Common-Open-Redirect-Injection-Parameters
type: code
language: text
verified: true
created_at: '2023-04-06T03:56:31.851982+00:00'
updated_at: '2023-04-10T20:23:05.600527+00:00'
platforms:
  - Web
tags:
  - injection-parameters
  - open-redirect
validated: true
---

# Common-Open-Redirect-Injection-Parameters

## Code

```text
/{payload}
?next={payload}
?url={payload}
?target={payload}
?rurl={payload}
?dest={payload}
?destination={payload}
?redir={payload}
?redirect_uri={payload}
?redirect_url={payload}
?redirect={payload}
/redirect/{payload}
/cgi-bin/redirect.cgi?{payload}
/out/{payload}
/out?{payload}
?view={payload}
/login?to={payload}
?image_url={payload}
?go={payload}
?return={payload}
?returnTo={payload}
?return_to={payload}
?checkout_url={payload}
?continue={payload}
?return_path={payload}
```

## Description

This code snippet provides a comprehensive list of common URL parameters and paths used by web applications for redirection. Replace {payload} with a malicious URL (e.g., http://evil.com) to test for open redirection vulnerabilities. It serves as a reference for enumerating injection points during vulnerability assessment.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| {payload} | Malicious or test URL to inject for redirection | http://evil.com/phish |

## Usage

Use this list in conjunction with tools like curl or Burp Suite to append parameters to target URLs and test redirects. For example, in a procedure like [[procedures/Open-URL-Redirection-via-Injection-Parameters]], iterate through each entry to identify vulnerable endpoints. This is typically used during web application penetration testing to map redirect behaviors.

## Detection

- Web logs showing unusual Location headers pointing to external domains.
- WAF alerts on unvalidated redirect parameters.
- Browser warnings for unexpected navigations from trusted sites.

## Related

- [[procedures/Open-URL-Redirection-via-Injection-Parameters]]
