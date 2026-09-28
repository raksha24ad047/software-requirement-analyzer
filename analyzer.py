def analyze_requirement(requirement):
    text = requirement.lower()

    functional_requirements = []
    non_functional_requirements = []
    users = []
    inputs = []
    outputs = []
    missing_information = []

    # Functional requirement detection
    functional_keywords = {
        "login": "User login",
        "register": "User registration",
        "signup": "User registration",
        "search": "Search functionality",
        "notification": "Notification system",
        "notify": "Notification system",
        "payment": "Payment processing",
        "upload": "File upload",
        "download": "File download",
        "report": "Report generation",
        "dashboard": "Dashboard",
        "booking": "Booking functionality",
        "track": "Tracking functionality"
    }

    for keyword, feature in functional_keywords.items():
        if keyword in text and feature not in functional_requirements:
            functional_requirements.append(feature)

    # User/actor detection
    user_keywords = {
        "student": "Student",
        "teacher": "Teacher",
        "admin": "Administrator",
        "administrator": "Administrator",
        "customer": "Customer",
        "user": "User",
        "employee": "Employee",
        "manager": "Manager"
    }

    for keyword, user in user_keywords.items():
        if keyword in text and user not in users:
            users.append(user)

    # Non-functional requirement detection
    if any(word in text for word in ["secure", "security", "password"]):
        non_functional_requirements.append("Security")

    if any(word in text for word in ["fast", "quick", "performance"]):
        non_functional_requirements.append("Performance")

    if any(word in text for word in ["easy", "simple", "user-friendly"]):
        non_functional_requirements.append("Usability")

    if any(word in text for word in ["mobile", "responsive"]):
        non_functional_requirements.append("Responsive design")

    # Input detection
    if any(word in text for word in ["name", "email", "password", "details"]):
        inputs.append("User-provided information")

    # Output detection
    if any(word in text for word in ["display", "show", "report", "notification"]):
        outputs.append("Information displayed to the user")

    # Missing information detection
    if not users:
        missing_information.append("User/actor is not clearly specified.")

    if not functional_requirements:
        missing_information.append(
            "Specific system functionality is not clearly specified."
        )

    if "notification" in text or "notify" in text:
        missing_information.append(
            "Notification timing and delivery method should be specified."
        )

    # Priority
    priority = "High" if len(functional_requirements) >= 3 else "Medium"

    return {
        "requirement": requirement,
        "functional_requirements": functional_requirements,
        "non_functional_requirements": non_functional_requirements,
        "users": users,
        "inputs": inputs,
        "outputs": outputs,
        "missing_information": missing_information,
        "priority": priority
    }
