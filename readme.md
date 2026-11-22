# Daily Report Bot (n8n Workflow)

An automated **n8n** workflow that collects daily progress updates through a form submission, formats them into a structured `daily_report` message, and sends the summary via email using SMTP[cite: 2, 10, 11].

## Features

- **Form Trigger (`On form submission`)**: Captures daily updates including name, learning notes, project work, time spent, challenges, and tomorrow's plan[cite: 10, 11].
- **Report Formatting (`Edit Fields`)**: Combines and formats the form fields into a clean `daily_report` text output[cite: 2, 10, 11].
- **Automated Email Delivery (`Send an Email`)**: Sends the formatted report via SMTP (configured with Gmail SMTP on port `465` with SSL/TLS)[cite: 2, 10, 11].

## Workflow Architecture

```text
[On form submission] ---> [Edit Fields (daily_report)] ---> [Send an Email (SMTP)]