# Company & Approval API Project

A production-ready REST API built with Django and Django REST Framework (DRF) for managing companies of three types (Small Business, Startup, Corporate) with a complete approval workflow, dynamic field validation based on company type, role-based permissions, unified clean response format, interactive Swagger documentation, and 100% test coverage.

## Features

- Company management with three distinct types
- Dynamic validation of company_details JSON field based on company type
- Full generic approval system — companies remain inactive until approved
- All GET endpoints return exactly this unified format:
```json
{
  "data": { ... },
  "approval": { ... } | null
}



Company Type Validation Rules

Company Type,Required fields in company_details
Small Business,"number_of_employees, annual_revenue"
Startup,"founders, funding_stage"
Corporate,"departments, global_branches"

Example Requests
Small Business
{
  "name": "Cairo Coffee Shop",
  "type": "Small Business",
  "company_details": {
    "number_of_employees": 8,
    "annual_revenue": 850000.00
  }
}

Startup
{
  "name": "NileTech",
  "type": "Startup",
  "company_details": {
    "founders": "Mohamed Ahmed, Sara Ali, Omar Khaled",
    "funding_stage": "Series A"
  }
}

Corporate

{
  "name": "Egypt International Group",
  "type": "Corporate",
  "company_details": {
    "departments": ["HR", "Finance", "IT", "Operations", "Legal"],
    "global_branches": 32
  }
}

Quick Start

git clone https://github.com/mohamedhamednour/approval-system
cd company-approval-api

python -m venv .venv
source .venv/bin/activate          # Linux/macOS
# .venv\Scripts\activate           # Windows

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  
python manage.py runserver


API Documentation (Live & Interactive)

Swagger UI → http://127.0.0.1:8000/swagger/




Running Tests

pytest -v


Project Structure

company_approval_api/
├── companies/       
├── approvals/         
├── users/            
├── shared/

