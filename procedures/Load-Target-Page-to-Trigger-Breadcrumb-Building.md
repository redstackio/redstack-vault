---
id: proc-load-page-breadcrumb
tags:
  - dom-injection
  - breadcrumb-xss
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/document-ready-bindbreadcrumb]]'
  - '[[commands/qstring-myk-check]]'
  - '[[commands/referrer-home-check]]'
  - '[[commands/get-search-page-name]]'
  - '[[commands/inject-referrer-breadcrumb]]'
  - '[[commands/get-kbsfdchostname]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:28:20.720Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Load-Target-Page-to-Trigger-Breadcrumb-Building

## Summary

This procedure navigates to the target page on kb.informatica.com, triggering the bindBreadCrumb JavaScript function to process the malicious referrer and inject it unescaped into the DOM as a breadcrumb link.

## Description

Upon loading the page with 'myk=xxx', the document.ready event calls bindBreadCrumb(), which validates conditions like non-empty myk, absence of /home.aspx in referrer, empty CoveoSearchUrl cookie, and referrer matching //search.informatica.com. It then creates an <li> element with innerHTML set to '<a href="' + document.referrer + '" ... >Search Results</a>', appending it to #DynamicBreadcrumb. This injects the payload into the href, setting up for execution.

## Requirements

1. Malicious referrer already set from prior step.
2. Target page accessible via HTTPS.
3. JavaScript execution enabled in browser.

## Defense

Defensive measures and detection strategies:

- Escape all dynamic content inserted into HTML attributes using libraries like DOMPurify.
- Validate and sanitize document.referrer before use, rejecting suspicious patterns.

## Objectives

1. Execute bindBreadCrumb to build the vulnerable breadcrumb.
2. Inject the payload into the DOM without breaking the page.
3. Confirm injection via DOM inspection.

## Instructions

### Step 1: Navigate to Target with Malicious Referrer

**Context**: Load the page to fire the ready event and call bindBreadCrumb.

**Command** ([[commands/document-ready-bindbreadcrumb]]):
```javascript
$(document).ready(function(){ bindBreadCrumb(); });
```

> This automatically triggers on page load, initializing breadcrumb construction. Expected output: bindBreadCrumb function executes.

### Step 2: Validate myk Parameter

**Context**: Check for non-empty 'myk' to proceed with referrer processing.

**Command** ([[commands/qstring-myk-check]]):
```javascript
if(qString('myk')!=''){ /* process referrer */ }
```

> Branches into referrer handling if myk is present. Expected output: Condition true, proceeds to next checks.

### Step 3: Check Referrer for Home Page Exclusion

**Context**: Skip if referrer contains /home.aspx.

**Command** ([[commands/referrer-home-check]]):
```javascript
var previousUrl = document.referrer.toLowerCase(); if(previousUrl.indexOf('/home.aspx')>-1){ /* skip */ } else { /* proceed */ }
```

> Ensures malicious referrer is used. Expected output: Proceeds if no /home.aspx.

### Step 4: Retrieve Search Page Name from Cookie

**Context**: Fallback to referrer if cookie empty.

**Command** ([[commands/get-search-page-name]]):
```javascript
var varCoveoSearchResultPageName = fnGetSearchPageName(); if(varCoveoSearchResultPageName !=""){ /* use cookie */ } else { /* use referrer */ }
```

> Calls helper to parse CoveoSearchUrl cookie. Expected output: Empty if no cookie, falls back.

### Step 5: Inject Referrer into Breadcrumb

**Context**: Build and append the vulnerable link.

**Command** ([[commands/inject-referrer-breadcrumb]]):
```javascript
var varDocumentReferrer = document.referrer; if(varDocumentReferrer !=""){ if(varDocumentReferrer.toLowerCase().indexOf(fnGetKBSFDCHostName())!=-1){ var li = document.createElement('li'); strChild = '<a href="' + varDocumentReferrer + '" style="color:#999 !important;" >Search Results</a>'; li.innerHTML = strChild; document.getElementById('DynamicBreadcrumb').appendChild(li); } }
```

> Appends the injected element. Expected output: New <a> in DOM with malicious href.

### Step 6: Verify Hostname Match

**Context**: Ensure referrer matches expected domain.

**Command** ([[commands/get-kbsfdchostname]]):
```javascript
function fnGetKBSFDCHostName(){ if(document.location.href.indexOf('kb.informatica.com')>-1){ return '//search.informatica.com'; } }
```

> Returns matching hostname. Expected output: '//search.informatica.com'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/document-ready-bindbreadcrumb]]
- [[commands/qstring-myk-check]]
- [[commands/referrer-home-check]]
- [[commands/get-search-page-name]]
- [[commands/inject-referrer-breadcrumb]]
- [[commands/get-kbsfdchostname]]

## Tools Used


## Tags

- dom-injection
- breadcrumb-xss
