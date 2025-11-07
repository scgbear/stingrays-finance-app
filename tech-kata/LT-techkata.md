# Tech Kata: Stingrays Finance App

**Duration:** 30 minutes  
**Difficulty:** Intermediate  
**Technologies:** Django, Python, HTML/CSS, JavaScript

## Overview

Welcome to the Stingrays Finance App coding kata! This exercise challenges you to enhance a Django-based financial web application by implementing core features that will make it functional and discoverable. You'll be working with a pre-configured Django project structure and are encouraged to use AI coding assistants to accelerate your development.

## Prerequisites

- Basic knowledge of Django framework
- Understanding of Python web development
- Familiarity with HTML/CSS
- Git workflow knowledge

## Setup Instructions

1.1 **Initial Setup**

   
   ```bash
   npm install
   ```

   Ensure npm install executes sucessfully

1.2 **Initial Setup**

   
   ```bash
   ./start.sh
   ```

   Ensure the application runs successfully before proceeding with the tasks.

2. **Project Structure Overview**
   - `apps/core/`: Core application functionality
   - `apps/pro/`: Professional features and dashboard
   - `templates/`: HTML templates
   - `static/`: CSS and static assets
   - `StingraysFinance/`: Main Django project configuration

## Tasks

### Task 1: Investment Calculator Implementation (15 minutes)

**Objective:** Implement a functional investment calculator with backend logic to power the existing frontend interface.

**Requirements:**

- Create backend logic for compound interest calculations
- Ensure proper data validation and error handling
- Connect the frontend to the backend functionality

**Acceptance Criteria:**

- [ ] Users can input initial investment amount, interest rate, and time period
- [ ] Backend calculates compound interest accurately
- [ ] Results are displayed in a user-friendly format
- [ ] Form validation prevents invalid inputs
- [ ] Error handling for edge cases (negative values, etc.)

**Technical Specifications:**

- Use Django views and models as appropriate
- Implement proper form handling
- Add unit tests for calculation logic
- Follow Django best practices for URL routing

### Task 2: SEO-Optimized Blog System (15 minutes)

**Objective:** Build an integrated blog system to drive organic traffic through search engine optimization. (Note: Libraries like Wagtail can be used)

**Requirements:**

- Create a blog model and admin interface
- Implement blog listing and detail pages
- Add SEO-friendly features (meta tags, structured URLs, sitemap)
- Ensure responsive design integration

**Acceptance Criteria:**

- [ ] Admin can create, edit, and publish blog posts
- [ ] Blog posts have SEO-friendly URLs (slugs)
- [ ] Meta descriptions and title tags are automatically generated
- [ ] Blog listing page shows published posts with pagination
- [ ] Individual blog post pages are properly formatted
- [ ] Basic search functionality for blog posts

**SEO Features to Implement:**

- URL slug generation from post titles
- Meta description and keywords fields
- Open Graph tags for social media sharing
- XML sitemap generation
- Internal linking suggestions

## Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [SEO Best Practices](https://developers.google.com/search/docs)
- Investment Calculation Formulas: Compound Interest = P(1 + r/n)^(nt)

---

**Good luck! Remember to leverage AI coding assistants to maximize your productivity within the 30-minute timeframe.**
