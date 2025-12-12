SMALL_BUSINESS = 'Small Business'
STARTUP = 'Startup'
CORPORATE = 'Corporate'

TYPE_CHOICES = [
        (SMALL_BUSINESS, 'Small Business'),
        (STARTUP, 'Startup'),
        (CORPORATE, 'Corporate'),
    ]


REQUIRED_FIELDS = {
            SMALL_BUSINESS: ["number_of_employees", "annual_revenue"],
            STARTUP: ["founders", "funding_stage"],
            CORPORATE: ["departments", "global_branches"],
        }
