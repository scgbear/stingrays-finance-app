# Kata Ideas

## Kata guidelines

- Define a concise learning objective and expected skill gains.
- The bare bones repo should be the baseline for every Kata's starting point. Try not to compound katas (e.g. don't make Kata B dependant on completing Kata A) 
- Keep scenarios scoped and realistic to encourage incremental progress.
- Goal is to provide a problem, with defined technical contraints, that allow the practitioner to re-run the kata using different AI Assisted engineering approaches. More advanced practitioners may choose to alter the technical constraints for their own growth, but our goal is focused on the learning of AI Assisted Engineering.

## Kata variances

One of the value adds of a code kata is the ability to stay within a specific problem and create variance in the implementation by defining alternate rules for running the kata multiple times. Since these kata's are focused on learning HVE and AI Assisted Engineering practices the variances should be not within the problem space but with the approach taken. The variances that should be targetted are:

* Tool choice:
  * GitHub Copilot
  * Claude Code
  * OpenAI's CODEX
  * ...
* Prompting approaches
  * Raw tools, no packaged set of pre-built prompts/modes/instructions
  * HVE-Core
  * Spec-Kit
  * Hybrid
* Issue/Plan tracking
  * Default issue tracking as defined by Prompt apprach and tool choice
  * Beads
  * ...

## Potential Katas

### IaC Kata

A kata to have the practitioner to create the IaC required to deploy the repo into Azure. A stretch goal on this one would be to also construct the DevOps pipelines to deploy the IaC. An alternitive of a stretch goal would be to have a follow up kata, that is dependant on this kata to implement the IaC pipeline.

### Account creation

A kata to build out the features required to allow a user to create an Account within the system. As there is a paywall to create an account, payment processing could be a requirement for this kata. Engineering fundementals would also have this paywall and account creation done via a backend API. Barebones repo currently has no backend API.

### Free Tools Development

Currently the free tools page only has a single tool available. So each one of the free tools can theoritically become their own kata. The tools listed are:

* Retirement Planner Card
* Mortgage Calculator Card
* Loan Payoff Calculator Card
* Budget Planner Card
* Savings Goal Tracker Card

Should make the requirements on these fairly light to allow for the exploration of AI Assisted requirements and planning.

### Pro Dashboard

There be blank bits in these files where a Dashboard should be. Perhaps a kata to create one? I'm guessing we'll want some actual pro features before we have things to display in a dashboard...

### Pro-Features developed

Pro features being behind a paywall, let's make something worth paying for. This would presumably be where an backend API starts to get more features created for it and the complexity of design starts to better mirror what our clients would expect.  
