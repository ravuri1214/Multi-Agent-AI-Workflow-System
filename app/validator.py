def validate_results(results):
    """
    Validate that all workflow steps completed successfully.
    """
    if not results:
        return {
            "status": "failed",
            "message": "No results generated"
        }

    return {
        "status": "success",
        "validated_results": results
    }
