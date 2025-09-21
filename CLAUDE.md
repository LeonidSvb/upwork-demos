# Upwork Project Assistant - Claude Coding Guidelines

# Core Principles

## Simplicity First
- Always prefer simple solutions over complex ones
- Avoid over-engineering or premature optimization
- Choose straightforward implementations that are easy to understand and maintain

## DRY (Don't Repeat Yourself)
- Avoid duplication of code whenever possible
- Before writing new functionality, check for similar existing code
- Refactor common patterns into reusable utilities or components

## Environment Awareness
- Write code that works consistently across different environments: dev, test, prod
- Use environment variables for configuration differences
- Avoid hardcoding values that might differ between environments

## Focused Changes
- Only make changes that are requested or directly related to the task at hand
- Be confident that changes are well understood and necessary
- Avoid scope creep or tangential improvements unless explicitly requested

# Upwork-Specific Guidelines

## Proposal Generation
- Always use real data when creating proposals
- Proposals must be specific and address client requirements
- Include realistic time and cost estimates
- Demonstrate understanding of client's problem

## MVP-First Approach
- Focus on core functionality first
- Avoid overcomplication in initial stages
- Propose phased implementation with quick results
- Clearly define what's included in MVP vs future iterations

## Client Communication
- Write clearly and professionally
- Use structured format for proposals
- Include testing and validation plans
- Always offer demonstration or trial period

## Time Estimation
- Add 20-30% buffer to base estimates
- Account for communication and revision time
- Break large tasks into measurable milestones
- Provide time ranges rather than fixed deadlines

# File Organization

## Agent Files
- Store agents in separate files with clear names
- Document input and output for each agent
- Use consistent structure across all agents

## Templates
- Keep proposal templates separate
- Version successful templates
- Adapt for specific project categories

## Analysis Results
- Save project analyses for future reference
- Structure by project types
- Mark successful and unsuccessful proposals

# Data and Testing

## No Fake Data in Production
- Use only real examples from Upwork
- Test with actual project requirements
- Validate proposals before submission

## Quality Checks
- Check grammar and spelling
- Validate technical details
- Ensure alignment with client requirements
- Verify competitive pricing

# Batch Processing

## Project Analysis
- Analyze multiple projects simultaneously
- Use common patterns for similar projects
- Automate repetitive analysis parts

## Proposal Generation
- Create base templates for common project types
- Batch adapt for specific requirements
- Use variables for personalization

# Performance Metrics

## Track Success
- Monitor proposal acceptance rate
- Analyze rejection reasons
- Optimize approach based on data
- Document best practices