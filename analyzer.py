import re


def analyze_requirement(requirement):

    text = requirement.lower()

    functional_requirements = []
    non_functional_requirements = []
    users = []
    inputs = []
    outputs = []
    missing_information = []
    constraints = []


    # =====================================================
    # USERS / ACTORS
    # =====================================================

    user_keywords = {
        "student": "Student",
        "students": "Student",

        "teacher": "Teacher",
        "teachers": "Teacher",

        "admin": "Administrator",
        "administrator": "Administrator",
        "administrators": "Administrator",

        "customer": "Customer",
        "customers": "Customer",

        "user": "User",
        "users": "User",

        "employee": "Employee",
        "employees": "Employee",

        "manager": "Manager",
        "managers": "Manager"
    }

    for keyword, user in user_keywords.items():

        if re.search(r"\b" + keyword + r"\b", text):

            if user not in users:
                users.append(user)


    # =====================================================
    # FUNCTIONAL REQUIREMENTS
    # =====================================================

    functional_patterns = {

        "summar": "Document/topic summarization",

        "search": "Search functionality",

        "find": "Topic/document search",

        "check": "Information/topic checking",

        "understand": "Content understanding",

        "upload": "PDF/document upload",

        "extract": "Content extraction",

        "download": "Download functionality",

        "view": "Content viewing",

        "login": "User login",

        "register": "User registration",

        "signup": "User registration",

        "notification": "Notification system",

        "notify": "Notification system",

        "report": "Report generation",

        "track": "Tracking functionality",

        "filter": "Filtering functionality"
    }


    for keyword, feature in functional_patterns.items():

        if keyword in text:

            if feature not in functional_requirements:
                functional_requirements.append(feature)


    # =====================================================
    # INPUTS
    # =====================================================

    if any(word in text for word in [
        "pdf",
        "document",
        "file",
        "material"
    ]):

        inputs.append("PDF / document")


    if any(word in text for word in [
        "topic",
        "keyword",
        "query",
        "search"
    ]):

        inputs.append("Topic / search query")


    if any(word in text for word in [
        "user",
        "student",
        "teacher",
        "customer"
    ]):

        inputs.append("User request")


    # =====================================================
    # OUTPUTS
    # =====================================================

    if any(word in text for word in [
        "summar",
        "overview",
        "understand"
    ]):

        outputs.append("Generated summary / overview")


    if any(word in text for word in [
        "search",
        "find",
        "topic",
        "check"
    ]):

        outputs.append("Search result / topic availability")


    if "extract" in text:

        outputs.append("Extracted document content")


    # =====================================================
    # NON-FUNCTIONAL REQUIREMENTS
    # =====================================================

    if any(word in text for word in [
        "secure",
        "security",
        "password",
        "privacy"
    ]):

        non_functional_requirements.append("Security")


    if any(word in text for word in [
        "fast",
        "quick",
        "quickly",
        "performance"
    ]):

        non_functional_requirements.append("Performance")


    if any(word in text for word in [
        "easy",
        "simple",
        "user-friendly",
        "understand"
    ]):

        non_functional_requirements.append("Usability")


    if any(word in text for word in [
        "accurate",
        "accuracy",
        "correct"
    ]):

        non_functional_requirements.append("Accuracy")


    if any(word in text for word in [
        "mobile",
        "responsive"
    ]):

        non_functional_requirements.append("Responsive design")


    # =====================================================
    # CONSTRAINTS
    # =====================================================

    if "pdf" in text:

        constraints.append(
            "The system should support PDF-based document processing."
        )


    # =====================================================
    # MISSING INFORMATION
    # =====================================================

    if not users:

        missing_information.append(
            "The intended user/actor is not clearly specified."
        )


    if any(word in text for word in [
        "pdf",
        "document"
    ]):

        if "upload" not in text:

            missing_information.append(
                "The method for providing the PDF/document is not specified."
            )


    if "summar" in text:

        missing_information.append(
            "The required summary format and level of detail are not specified."
        )


    if "search" in text:

        missing_information.append(
            "The expected search behavior and result format are not specified."
        )


    if "topic" in text:

        missing_information.append(
            "The system behavior when a topic is not found is not specified."
        )


    # =====================================================
    # PRIORITY
    # =====================================================

    if len(functional_requirements) >= 4:

        priority = "High"

    elif len(functional_requirements) >= 2:

        priority = "Medium"

    else:

        priority = "Low"


    # =====================================================
    # RETURN RESULT
    # =====================================================

    return {

        "requirement": requirement,

        "functional_requirements":
            functional_requirements,

        "non_functional_requirements":
            non_functional_requirements,

        "users":
            users,

        "inputs":
            inputs,

        "outputs":
            outputs,

        "missing_information":
            missing_information,

        "constraints":
            constraints,

        "priority":
            priority
    }
