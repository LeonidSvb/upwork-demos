# 🚀 Project Setup Guide - Core Principles & Structure

Complete guide for setting up marketing automation projects using Claude Code.

## 📋 Core Principles

### 1. File Organization
- **kebab-case** for all file names
- Functional grouping over arbitrary folders
- Related materials stay together
- Clear hierarchy with meaningful names

### 2. Documentation Standards
- **English only** for all documentation
- Consistent markdown with emoji headers
- Practical examples included
- Concise but actionable content

### 3. Client-Centric Structure
- Each client gets dedicated folder in `CLIENTS/`
- Standardized but flexible templates
- Clear separation of client vs. internal materials

## 🏗️ Essential Directory Structure

### Core Directories (Required for all projects)

```
project-root/
├── CLIENTS/                    # Client-specific materials
│   ├── _templates/            # Setup templates (this file)
│   └── [client-name]/         # Individual client folders
├── KNOWLEDGE/                 # Centralized knowledge base
│   ├── FRAMEWORKS/           # Strategy frameworks & scoring
│   ├── SOURCES/              # Source materials & research
│   └── TEMPLATES/            # Reusable content templates
├── TOOLS/                    # Technical infrastructure
│   ├── scripts/              # Automation scripts
│   ├── CHANGELOG.md          # Technical change history
│   └── package.json          # Dependencies
├── CLAUDE.md                 # Claude Code memory & commands
├── PROJECT-REPORT.md         # Client-facing progress reports
└── README.md                 # Project overview
```

### Optional Directories (Based on client needs)

```
├── AGENTS/                   # AI automation agents
│   ├── _templates/          # Agent creation templates
│   ├── content-repurposer/  # Content transformation
│   └── youtube-processor/   # Video processing
├── TRAINING/                # Learning & onboarding materials
│   ├── quick-start.md       # Getting started
│   ├── progress-tracker.md  # Learning progress
│   └── reference/           # Quick references
└── Valuable_Assets/         # Legacy organization (migrate to KNOWLEDGE/)
```

## 📁 Client Folder Template

### Standard Client Structure
```
CLIENTS/[client-name]/
├── brand-pack.md           # Brand guidelines & voice
├── strategist-pack.md      # Content strategy & frameworks
├── demos/                  # Screenshots & results
│   ├── before-after/      # Transformation examples
│   └── results/           # Performance metrics
└── call-transcripts/      # Client meeting records
```

### Brand Pack Template (`brand-pack.md`)
```markdown
# 🎨 [Client Name] Brand Pack

## Brand Identity
- **Company**: [Full company name]
- **Industry**: [Primary industry/niche]
- **Target Audience**: [Key demographics]

## Voice & Tone
- **Brand Voice**: [Professional/Casual/Technical/etc.]
- **Key Messages**: [Core value propositions]
- **Avoid**: [Things to avoid in content]

## Visual Identity
- **Colors**: [Primary brand colors]
- **Fonts**: [Typography preferences]
- **Logo Usage**: [Logo guidelines]

## Content Guidelines
- **Content Pillars**: [Main content themes]
- **Posting Schedule**: [Frequency and timing]
- **Hashtag Strategy**: [Relevant hashtags]
```

### Strategy Pack Template (`strategist-pack.md`)
```markdown
# 📊 [Client Name] Content Strategy

## Strategic Overview
- **Goals**: [Primary objectives]
- **KPIs**: [Success metrics]
- **Timeline**: [Project phases]

## Content Framework
- **Content Types**: [Blog, video, social, etc.]
- **Distribution Channels**: [Where content goes]
- **Repurposing Strategy**: [How content transforms]

## ICE Scoring System
[Use framework from KNOWLEDGE/FRAMEWORKS/]

## Implementation Plan
- **Phase 1**: [Initial setup]
- **Phase 2**: [Content production]
- **Phase 3**: [Optimization]
```

## ⚙️ Technical Setup

### CLAUDE.md Configuration
Essential commands and memory for Claude Code:

```markdown
# Claude Code Memory - [Project Name]

## Project Context
[Brief project description and client focus]

## Key Commands
- `git status` - Check repository status
- `git add .` - Stage all changes
- `git commit -m "message"` - Commit with Claude attribution
- `update project status` - Add session log to PROJECT-REPORT.md
- `update README weekly` - Update README from PROJECT-REPORT.md
- `generate slack update` - Create casual Slack message

## File Structure Conventions
- Use kebab-case for file names
- Organize by functional areas
- Keep related materials together
- Place documentation at appropriate hierarchy levels

## Development Workflow
- Always read existing files before changes
- Use MultiEdit for multiple file changes
- Follow existing patterns and conventions
- Execute approved plans without asking permission
- Use `claude --dangerously-skip-permissions` for automation
```

### PROJECT-REPORT.md Structure
Client-facing progress tracking:

```markdown
# 📈 [Project Name] - Progress Report

## Executive Summary
[High-level project status and key achievements]

## Value Delivered
- **Content Pieces Created**: [Number]
- **Automation Systems**: [List of systems]
- **Time Saved**: [Estimated hours/week]
- **Performance Improvements**: [Metrics]

## Work Sessions
| Date | Focus | Key Achievements | Impact | Resources |
|------|-------|------------------|--------|-----------|
| [Date] | [Area] | [What was done] | [Business value] | [Links] |

## Next Steps
- [ ] [Priority task 1]
- [ ] [Priority task 2]
- [ ] [Priority task 3]
```

## 🎯 Project-Specific Examples (Colony Spark)

### What Makes This Project Unique
- **Training Component**: Bill's learning journey (TRAINING/ directory)
- **Agent Development**: Custom AI agents (AGENTS/ directory)
- **NetSuite Focus**: Specialized for NetSuite consultants
- **Video Processing**: YouTube content automation

### Adaptable Elements
- **TRAINING/**: Only needed for clients requiring onboarding
- **AGENTS/**: Optional for clients wanting automation
- **Video Processing**: Specific to YouTube content creators
- **Call Transcripts**: Location varies (client vs. internal calls)

### Transferable Principles
- Professional client reporting format
- Automated session logging
- Clear separation: technical logs vs. client reports
- Consistent file naming and organization
- English-only documentation standard

## 🔄 Workflow Automation

### Session Logging
After each work session:
1. Run `update project status` command
2. Add new row to PROJECT-REPORT.md table
3. Include date, focus area, achievements, impact, resources

### Weekly Reporting
1. Run `update README weekly` command
2. Generate executive summary from week's sessions
3. Update stakeholder communications

### Slack Updates
1. Run `generate slack update` command
2. Create casual message from latest session
3. Focus on wins and next steps

## 🚨 Critical Requirements

### Language Compliance
- **ALWAYS write in English** - no exceptions
- Check CLAUDE.md for language requirements
- Translate any non-English content immediately

### Git Practices
- Never commit unless explicitly requested
- Include Claude Code attribution in all commits
- Check git status before and after operations

### File Management
- Prefer editing existing files over creating new ones
- Use MultiEdit for multiple changes to same file
- Follow existing patterns and conventions
- Eliminate duplicate or redundant files

## 🎁 Ready-to-Use Templates

### Quick Client Setup Checklist
- [ ] Create `CLIENTS/[client-name]/` folder
- [ ] Copy and customize `brand-pack.md`
- [ ] Copy and customize `strategist-pack.md`
- [ ] Create `demos/` subfolder
- [ ] Set up `call-transcripts/` if needed
- [ ] Update CLAUDE.md with client context
- [ ] Initialize PROJECT-REPORT.md
- [ ] Add client README to document specific needs

### Copy-Paste Commands
```bash
# Create new client structure
mkdir -p "CLIENTS/[client-name]/demos/before-after"
mkdir -p "CLIENTS/[client-name]/demos/results"
mkdir -p "CLIENTS/[client-name]/call-transcripts"

# Copy templates
cp "CLIENTS/_templates/brand-pack-template.md" "CLIENTS/[client-name]/brand-pack.md"
cp "CLIENTS/_templates/strategist-pack-template.md" "CLIENTS/[client-name]/strategist-pack.md"
```

## 💡 Best Practices

### For Service Providers
- Keep client materials completely separate
- Standardize reporting formats
- Automate repetitive tasks
- Maintain professional documentation

### For Content Creators
- Organize by content type and stage
- Track performance metrics
- Plan repurposing strategies
- Maintain brand consistency

### For Consultants
- Document frameworks and methodologies
- Create reusable templates
- Track client progress systematically
- Maintain knowledge base

---

**Usage**: Reference this guide when setting up new projects. Adapt structure based on client needs while maintaining core organizational principles.