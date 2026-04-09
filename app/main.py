from planner import plan_task
from executor import execute_steps
from validator import validate_results


def run_workflow(user_input: str):
    steps = plan_task(user_input)
    executed_results = execute_steps(steps)
    final_output = validate_results(executed_results)
    return final_output


if __name__ == "__main__":
    user_query = "Summarize customer support issues"
    output = run_workflow(user_query)
    print(output)
