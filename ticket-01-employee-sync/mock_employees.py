MOCK_EMPLOYEES = [
    # --- Engineering (4) ---
    {
        "type": "Employee",
        "attributes": {
            "id": {"label": "ID", "value": 1},
            "first_name": {"label": "Vorname", "value": "Max"},
            "last_name": {"label": "Nachname", "value": "Mustermann"},
            "email": {"label": "E-Mail", "value": "max@techstart.de"},
            "department": {
                "label": "Abteilung",
                "value": {"attributes": {"name": "Engineering"}}
            },
            "position": {"label": "Position", "value": "Senior Developer"},
            "hire_date": {"label": "Eintrittsdatum", "value": "2023-06-01"},
            "status": {"label": "Status", "value": "active"}
        }
    },
    {
        "type": "Employee",
        "attributes": {
            "id": {"label": "ID", "value": 2},
            "first_name": {"label": "Vorname", "value": "Anna"},
            "last_name": {"label": "Nachname", "value": "Weber"},
            "email": {"label": "E-Mail", "value": "anna@techstart.de"},
            "department": {
                "label": "Abteilung",
                "value": {"attributes": {"name": "Engineering"}}
            },
            "position": {"label": "Position", "value": "Junior Developer"},
            "hire_date": {"label": "Eintrittsdatum", "value": "2025-01-15"},
            "status": {"label": "Status", "value": "active"}
        }
    },
    {
        "type": "Employee",
        "attributes": {
            "id": {"label": "ID", "value": 3},
            "first_name": {"label": "Vorname", "value": "Tom"},
            "last_name": {"label": "Nachname", "value": "Fischer"},
            "email": {"label": "E-Mail", "value": "tom@techstart.de"},
            "department": {
                "label": "Abteilung",
                "value": {"attributes": {"name": "Engineering"}}
            },
            "position": {"label": "Position", "value": "DevOps Engineer"},
            "hire_date": {"label": "Eintrittsdatum", "value": "2024-03-01"},
            "status": {"label": "Status", "value": "active"}
        }
    },
    {
        "type": "Employee",
        "attributes": {
            "id": {"label": "ID", "value": 4},
            "first_name": {"label": "Vorname", "value": "Sarah"},
            "last_name": {"label": "Nachname", "value": "Klein"},
            "email": {"label": "E-Mail", "value": "sarah@techstart.de"},
            "department": {
                "label": "Abteilung",
                "value": {"attributes": {"name": "Engineering"}}
            },
            "position": {"label": "Position", "value": "QA Engineer"},
            "hire_date": {"label": "Eintrittsdatum", "value": "2024-07-01"},
            "status": {"label": "Status", "value": "active"}
        }
    },
    # --- Marketing (3) ---
    {
        "type": "Employee",
        "attributes": {
            "id": {"label": "ID", "value": 5},
            "first_name": {"label": "Vorname", "value": "Lisa"},
            "last_name": {"label": "Nachname", "value": "Schmidt"},
            "email": {"label": "E-Mail", "value": "lisa@techstart.de"},
            "department": {
                "label": "Abteilung",
                "value": {"attributes": {"name": "Marketing"}}
            },
            "position": {"label": "Position", "value": "Marketing Manager"},
            "hire_date": {"label": "Eintrittsdatum", "value": "2023-09-01"},
            "status": {"label": "Status", "value": "active"}
        }
    },
    {
        "type": "Employee",
        "attributes": {
            "id": {"label": "ID", "value": 6},
            "first_name": {"label": "Vorname", "value": "Jonas"},
            "last_name": {"label": "Nachname", "value": "Braun"},
            "email": {"label": "E-Mail", "value": "jonas@techstart.de"},
            "department": {
                "label": "Abteilung",
                "value": {"attributes": {"name": "Marketing"}}
            },
            "position": {"label": "Position", "value": "Content Specialist"},
            "hire_date": {"label": "Eintrittsdatum", "value": "2024-11-01"},
            "status": {"label": "Status", "value": "active"}
        }
    },
    {
        "type": "Employee",
        "attributes": {
            "id": {"label": "ID", "value": 7},
            "first_name": {"label": "Vorname", "value": "Nina"},
            "last_name": {"label": "Nachname", "value": "Hoffmann"},
            "email": {"label": "E-Mail", "value": "nina@techstart.de"},
            "department": {
                "label": "Abteilung",
                "value": {"attributes": {"name": "Marketing"}}
            },
            "position": {"label": "Position", "value": "SEO Manager"},
            "hire_date": {"label": "Eintrittsdatum", "value": "2025-02-01"},
            "status": {"label": "Status", "value": "inactive"}
        }
    },
    # --- HR (2) ---
    {
        "type": "Employee",
        "attributes": {
            "id": {"label": "ID", "value": 8},
            "first_name": {"label": "Vorname", "value": "Laura"},
            "last_name": {"label": "Nachname", "value": "Krüger"},
            "email": {"label": "E-Mail", "value": "laura@techstart.de"},
            "department": {
                "label": "Abteilung",
                "value": {"attributes": {"name": "HR"}}
            },
            "position": {"label": "Position", "value": "HR Operations Lead"},
            "hire_date": {"label": "Eintrittsdatum", "value": "2022-04-01"},
            "status": {"label": "Status", "value": "active"}
        }
    },
    {
        "type": "Employee",
        "attributes": {
            "id": {"label": "ID", "value": 9},
            "first_name": {"label": "Vorname", "value": "David"},
            "last_name": {"label": "Nachname", "value": "Neumann"},
            "email": {"label": "E-Mail", "value": "david@techstart.de"},
            "department": {
                "label": "Abteilung",
                "value": {"attributes": {"name": "HR"}}
            },
            "position": {"label": "Position", "value": "Recruiter"},
            "hire_date": {"label": "Eintrittsdatum", "value": "2024-06-01"},
            "status": {"label": "Status", "value": "active"}
        }
    },
    # --- Finance (2) ---
    {
        "type": "Employee",
        "attributes": {
            "id": {"label": "ID", "value": 10},
            "first_name": {"label": "Vorname", "value": "Michael"},
            "last_name": {"label": "Nachname", "value": "Wagner"},
            "email": {"label": "E-Mail", "value": "michael@techstart.de"},
            "department": {
                "label": "Abteilung",
                "value": {"attributes": {"name": "Finance"}}
            },
            "position": {"label": "Position", "value": "Finance Manager"},
            "hire_date": {"label": "Eintrittsdatum", "value": "2023-01-15"},
            "status": {"label": "Status", "value": "active"}
        }
    },
    {
        "type": "Employee",
        "attributes": {
            "id": {"label": "ID", "value": 11},
            "first_name": {"label": "Vorname", "value": "Julia"},
            "last_name": {"label": "Nachname", "value": "Becker"},
            "email": {"label": "E-Mail", "value": "julia@techstart.de"},
            "department": {
                "label": "Abteilung",
                "value": {"attributes": {"name": "Finance"}}
            },
            "position": {"label": "Position", "value": "Accountant"},
            "hire_date": {"label": "Eintrittsdatum", "value": "2023-08-01"},
            "status": {"label": "Status", "value": "inactive"}
        }
    },
    # --- Sales (1) ---
    {
        "type": "Employee",
        "attributes": {
            "id": {"label": "ID", "value": 12},
            "first_name": {"label": "Vorname", "value": "Patrick"},
            "last_name": {"label": "Nachname", "value": "Müller"},
            "email": {"label": "E-Mail", "value": "patrick@techstart.de"},
            "department": {
                "label": "Abteilung",
                "value": {"attributes": {"name": "Sales"}}
            },
            "position": {"label": "Position", "value": "Account Executive"},
            "hire_date": {"label": "Eintrittsdatum", "value": "2024-09-01"},
            "status": {"label": "Status", "value": "active"}
        }
    },
]
