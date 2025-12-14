---
id: proc-host-malicious-swf-webpage
tags:
  - social-engineering
  - malicious-webpage
  - flash-exploit
type: procedure
tools:
  - '[[tools/Adobe-Flash-SWF]]'
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
updated_at: '2025-12-14T17:29:56.779Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Host-Malicious-Webpage-with-SWF-for-Vimeo-OAuth-Bypass

## Summary

This procedure involves creating and hosting a webpage that embeds a malicious Adobe Flash SWF file to exploit Vimeo's OAuth vulnerabilities, tricking a logged-in victim into initiating the cross-domain policy bypass and token theft.

## Description

The attack relies on social engineering to direct the victim to a controlled webpage. The page embeds an SWF that requires the victim to be authenticated in Vimeo with Flash enabled. This step sets up the initial access vector for the Flash-based CSRF and cross-domain exploit, targeting the /oauth/authorize endpoint. Expected outcome: Victim's browser executes the SWF, loading the permissive policy without suspicion.

## Requirements

1. Web server to host HTML and SWF files (e.g., Apache/Nginx)
2. Victim logged into Vimeo account
3. Adobe Flash Player enabled in browser (tested on Firefox 46, Chrome 50, IE 11)
4. Public URL for the webpage

## Defense

Defensive measures and detection strategies:

- Disable Adobe Flash globally or prompt user approval for SWF execution
- Monitor for unexpected Flash loads from untrusted domains
- Implement Content Security Policy (CSP) to restrict Flash embedding
- Educate users on phishing links and Flash risks

## Objectives

1. Gain initial access via victim interaction with malicious page
2. Trigger SWF execution in victim's browser
3. Position for subsequent policy loading and token theft

## Instructions

### Step 1: Create HTML Page

**Context**: Build a simple webpage to embed the SWF, disguising it as benign content.

Embed the SWF using object tag:

```html
<!DOCTYPE html>
<html>
<head><title>Vimeo Update</title></head>
<body>
<p>Click to update your Vimeo settings.</p>
<object type="application/x-shockwave-flash" data="malicious.swf" width="1" height="1"></object>
</body>
</html>
```

> This loads the SWF invisibly. Save as vimeoOAuth2Bypass.html.

### Step 2: Host the Page

**Context**: Serve the file publicly to share the link with the victim.

Upload to a hosting service or server, e.g., http://opnsec.com/vimeo/vimeoOAuth2Bypass.html.

> Ensure HTTPS if possible, but HTTP works for Flash. Test load in browser with Flash enabled.

### Step 3: Distribute Link

**Context**: Trick victim into visiting via email/phishing.

Send link: "Check your Vimeo account: [URL]".

> Victim opens link; SWF executes if logged in.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Adobe-Flash-SWF]]

## Tags

- social-engineering
- malicious-webpage
- flash-exploit
