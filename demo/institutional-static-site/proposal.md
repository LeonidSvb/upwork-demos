# Upwork Proposal - Front-End Developer for Static Institutional Website

## Screening Questions Answers

### 1. Can you confirm you can execute a static build exactly as specified — with no reinterpretation or added elements?

**Yes, absolutely.** I understand this project requires disciplined execution, not creative interpretation. I will build exactly what is specified in your documentation—no additional features, no design "improvements," no personal preferences injected into the code. Every element will be implemented according to your specifications with zero deviation.

I have created a demonstration specifically for this proposal that shows my ability to follow strict requirements: a clean, text-based institutional site with semantic HTML5, minimal CSS, no frameworks, and WCAG 2.1 AA compliance.

**Demo:** [View Static Site Demo](./index.html)

### 2. Provide one example of a site you built using only HTML, CSS, and minimal JS (no frameworks).

**Example:** The institutional website demo I've created for this proposal demonstrates exactly this approach:

**Technical Stack:**
- Pure HTML5 with semantic elements
- Vanilla CSS (no preprocessors, no frameworks)
- Minimal vanilla JavaScript for keyboard navigation enhancement
- Zero external dependencies
- No build tools required

**Features Implemented:**
- 4 pages with consistent structure
- Semantic HTML5 (header, nav, main, article, section, footer)
- Proper heading hierarchy (h1-h4)
- WCAG 2.1 AA accessibility
- JSON-LD schema markup (Organization + Breadcrumb)
- Keyboard navigation with focus indicators
- Skip-to-content link
- ARIA landmarks for screen readers
- Monochrome color scheme with high contrast
- Responsive design without media query libraries
- Left-aligned, text-focused layout

**File Size:**
- HTML: ~3KB per page
- CSS: ~4.5KB total
- JS: ~1.2KB total

This demonstrates my ability to write clean, standards-compliant code without relying on frameworks or external libraries.

### 3. Briefly describe how you ensure WCAG 2.1 AA accessibility (keyboard nav, headings, contrast, ARIA).

**My WCAG 2.1 AA Implementation Process:**

**Keyboard Navigation:**
- All interactive elements (links, buttons, form inputs) accessible via Tab/Shift+Tab
- Visible focus indicators with 2-3px solid outline and offset
- Skip-to-content link for bypassing navigation
- Logical tab order following visual flow
- No keyboard traps

**Heading Hierarchy:**
- Single h1 per page (page title)
- Proper nesting without skipping levels (h1→h2→h3→h4)
- Headings describe content sections accurately
- Validation with document outline tools

**Color Contrast:**
- Minimum ratio 4.5:1 for normal text (14pt and below)
- Minimum ratio 3:1 for large text (18pt+ or 14pt bold)
- I use WebAIM Contrast Checker or browser DevTools
- For this project's monochrome scheme: black text (#000) on white background (#FFF) = 21:1 ratio (exceeds requirements)

**ARIA Implementation:**
- Landmark roles: banner, navigation, main, contentinfo
- aria-label for navigation regions ("Main navigation", "Breadcrumb")
- aria-current="page" for current page links
- aria-required="true" for required form fields
- Only when semantic HTML isn't sufficient
- ARIA doesn't replace semantic HTML—it supplements it

**Testing:**
- Manual keyboard testing (unplug mouse, navigate entire site)
- Screen reader testing (NVDA on Windows, VoiceOver on Mac)
- Automated tools: axe DevTools, WAVE, Lighthouse accessibility audit
- Color contrast checking for all text/background combinations

### 4. How do you validate JSON-LD schema markup before deployment?

**My JSON-LD Validation Process:**

**1. Google Rich Results Test**
- URL: https://search.google.com/test/rich-results
- Primary validation tool for checking Google recognition
- Shows preview of how schema appears in search results
- Identifies errors and warnings

**2. Schema.org Validator**
- URL: https://validator.schema.org/
- Official schema validation
- Checks syntax and structure against schema.org specifications
- Validates proper @context, @type, and required properties

**3. Google Search Console**
- After deployment, monitor in Search Console
- Check "Enhancements" section for schema issues
- Identifies errors Google encounters when crawling
- Shows which pages successfully implement schema

**4. Manual Code Review**
- Verify proper JSON syntax (commas, quotes, brackets)
- Confirm @context uses https://schema.org
- Check @type matches intended schema type
- Validate all required properties are present
- Ensure nested schemas are properly structured

**5. Browser DevTools**
- Inspect page source to verify JSON-LD is present
- Check that script type is "application/ld+json"
- Confirm JSON is valid (no syntax errors in console)

**Example from my demo:**
```json
{
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "Institutional Website Demo",
    "url": "https://example.com",
    "description": "..."
}
```

Validated with Rich Results Test before including in demo.

---

## Proposal Summary

I am a disciplined front-end developer who excels in environments where precision and specification adherence matter more than creative freedom. Your project's strict requirements align perfectly with my development approach.

**What I Bring:**
- **Discipline:** I follow specifications exactly without adding or removing elements
- **Clean Code:** Semantic, readable, maintainable code structure
- **Standards Expertise:** Deep understanding of HTML5, WCAG 2.1, and web standards
- **Attention to Detail:** Every element serves its specified purpose
- **No Assumptions:** I ask clarifying questions rather than interpreting requirements

**Deliverables I Will Provide:**
- 12-page static site matching your exact specifications
- Semantic HTML5 throughout
- Minimal CSS with monochrome styling
- Essential-only vanilla JavaScript
- WCAG 2.1 AA accessibility compliance
- JSON-LD schema markup (Organization, Breadcrumb, document schema)
- Lighthouse report showing 90+ scores (mobile and desktop)
- Accessibility validation documentation
- Completed Developer Checklist
- Pre-Deployment Verification Form
- Complete ZIP archive of all code
- Deployment to your hosting environment

**Timeline:** 5-7 days as specified

**Approach:**
1. Receive and review all specifications and content
2. Build site structure following your exact layout requirements
3. Implement accessibility features per WCAG 2.1 AA
4. Add JSON-LD schema markup
5. Test thoroughly (validators, Lighthouse, keyboard, screen readers)
6. Complete all documentation
7. Submit for your validation
8. Make any specification-compliant adjustments
9. Deploy to your hosting

I understand this is not a creative project. It is an execution project. I will deliver exactly what you have specified—nothing more, nothing less.

**Questions for You:**
- Will specifications be provided as a written document, wireframes, or both?
- Do you have hosting credentials ready, or will those be provided during the project?
- Are there specific Lighthouse performance targets beyond 90+ for mobile and desktop?

I look forward to executing your institutional website with precision and discipline.

**Demonstration of my work for this project:** The demo site in this folder showcases exactly the type of disciplined, standards-compliant development you require.

---

## Cover Letter for Upwork

I have built a demonstration specifically for your project: a clean, standards-compliant static institutional website with semantic HTML5, minimal CSS, and WCAG 2.1 AA accessibility.

**Demo:** [Link to demo]

This demonstrates exactly what you need:
- Semantic HTML5 with proper document structure
- Vanilla CSS with monochrome styling
- Minimal JavaScript for keyboard enhancement
- WCAG 2.1 AA compliance
- JSON-LD schema markup
- No frameworks, no libraries, no external dependencies
- Clean, readable code

I have answered all four screening questions in detail within my full proposal.

**Key Points:**
- I can confirm I will execute exactly as specified with zero deviation
- The demo I created uses only HTML, CSS, and minimal JS
- I implement WCAG 2.1 AA through keyboard nav, proper headings, high contrast, and ARIA
- I validate JSON-LD using Google Rich Results Test and Schema.org validator

I thrive in environments where discipline and precision matter more than creativity. Your specifications-driven approach aligns perfectly with my development methodology.

Timeline: 5-7 days as specified

I look forward to executing your institutional website with the precision and standards compliance it requires.

Please review the demonstration and my detailed answers to your screening questions.

Best regards