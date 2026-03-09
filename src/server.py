def run_solver(input_data):
    """
    solver function for CSC770 project.
   
    """

    return {
        "status": "success",
        "message": "solver executed successfully",
        "received_input": input_data,
        "solutions": [
            {"course": "CSC770", "faculty": "Sample Faculty"}
        ]
    }


if __name__ == "__main__":
    sample_input = {
        "courses": ["CSC770"],
        "faculty": ["Sample Faculty"]
    }

    result = run_solver(sample_input)
    print(result)