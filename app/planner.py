def plan_task(user_input: str):
    """
    Break the user request into simple workflow steps.
    """
    return [
        f"Understand the request: {user_input}",
        "Break the task into smaller steps",
        "Prepare a structured response"
    ]
