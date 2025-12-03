# Kata Ideas

These are katas that are designed to practice AI Assited Engineering. Goal is to provide problem(s), with defined technical contraints, that allow practitioners to re-run the kata using different AI Assisted engineering approaches. More advanced practitioners may choose to alter the technical constraints for their own growth, but our goal is focused on the learning of AI Assisted Engineering.

To ensure there is confidense created within the practicitioners of AI Assisted Engineering, we should ensure where able to illustrate the ability to use these tools in Enterprise Grade Applications, with solid engineering fundementals and without a reduction in code quality.

## Kata guidelines

- Define a concise learning objective and expected skill gains.
- The bare bones repo should be the baseline for every Kata's starting point. Try not to compound katas (e.g. don't make Kata B dependant on completing Kata A) 
- Keep scenarios scoped and realistic to encourage incremental progress.
- 

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
  * Awesome Copilot
  * ...
* Issue/Plan tracking
  * Default issue tracking as defined by Prompt approach and tool choice
  * Beads
  * ...

## Potential Katas

### IaC Kata

A kata to have the practitioner to create the IaC required to deploy the repo into Azure. A stretch goal on this one would be to also construct the DevOps pipelines to deploy the IaC. An alternitive of a stretch goal would be to have a follow up kata, that is dependant on this kata to implement the IaC pipeline.

Challenge points would come from implementing the IaC after previous kata challenges are done. e.g. After a backend API is added, and/or database layer created, include VNet security, Managed Identities, etc. 

Keep in mind, if you want buy in from Pro-Devs on HVE, you need to enforse the AI Agents can work in a pro-dev application implementation, that comes with all the bells of whistles of an Enterprise Grade application. Django, by itself, doesn't provide that.

### Account creation

A kata to build out the features required to allow a user to create an Account within the system. As there is a paywall to create an account, payment processing could be a requirement for this kata. 

While Django has code behind capability and therefore could have direct database and application function built there, we want to make sure we're following engineering fundementals and account creation creation done via a backend API. Barebones repo currently has no backend API.

This could also be a challenge point. e.g. implement with only Django, vs implement with a backend API. 

### Free Tools Development

Currently the free tools page only has a single tool available. So each one of the free tools can theoritically become their own kata. The tools listed are:

* Retirement Planner Card
* Mortgage Calculator Card
* Loan Payoff Calculator Card
* Budget Planner Card
* Savings Goal Tracker Card

Should make the requirements on these fairly light to allow for the exploration of AI Assisted requirements and planning.

### Pro Dashboard

There be blank bits in these files where a Dashboard should be. Perhaps a kata to create one? I'm guessing we'll want some actual pro features before we have things to display in a dashboard, so perhaps the inclusion of dashboard widgets should be apart of the Pro-Features kata(s)?

### Pro-Features developed

Pro features being behind a paywall, let's make something worth paying for. Stressing a seperation of concerns between frontend and backend functionality would be prudent here. As a client will generally not appretiate the core of the business logic to be sitting in a code behind page of the Web App, a backend API for these features should be a part of challenge.

Potential Pro Features to implement:

1.  **Automated Transaction Categorization**: Auto-tag imported transactions using keyword matching or ML, with user-defined custom rules.
2.  **Investment Portfolio Rebalancing**: Calculate specific buy/sell orders needed to return a portfolio to its target asset allocation.
3.  **Net Worth History & Forecasting**: Visual tracking of assets vs. liabilities over time, including Monte Carlo simulations for future growth.
4.  **Subscription Manager**: Detect recurring payments from transaction history and alert on
