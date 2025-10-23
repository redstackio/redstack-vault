---
id: 4dbd112f-2d56-4a0d-b2b5-500f1bdc604b
type: code
language: TypeScript
verified: false
created_at: '2023-04-06T03:56:43.795878+00:00'
updated_at: '2023-04-10T20:24:52.287178+00:00'
---

# Code Snippet 4dbd112f

**Language**: TypeScript

```typescript
import { Component, OnInit } from '@angular/core';
import { DomSanitizer } from '@angular/platform-browser';

@Component({
  selector: 'my-app',
  template: `
    <h4>An untrusted URL:</h4>
    <p><a class="e2e-dangerous-url" [href]="dangerousUrl">Click me</a></p>
    <h4>A trusted URL:</h4>
    <p><a class="e2e-trusted-url" [href]="trustedUrl">Click me</a></p>
  `,
})
export class App implements OnInit {
  dangerousUrl: string;
  trustedUrl: any;

  constructor(private sanitizer: DomSanitizer) {}

  ngOnInit() {
    this.dangerousUrl = 'javascript:alert("Hi there")';
    this.trustedUrl = this.sanitizer.bypassSecurityTrustUrl(this.dangerousUrl);
  }
}
```


