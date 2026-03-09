import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.server import run_solver

"""

def test_run_solver():
    input_data = {
        "courses": ["CSC770"],
        "faculty": ["Sample Faculty"]
    }

    result = run_solver(input_data)

    assert result["status"] == "success"
    assert "solutions" in result
    assert result["received_input"] == input_data


if __name__ == "__main__":
    test_run_solver()
    print("Test passed.")
    
    """
    


def test_run_solver():
    data = {"course": "CSC770"}
    result = run_solver(data)

    assert result["status"] == "success"
    assert "solutions" in result
    assert result["received_input"] == data

    print("Test passed.")

test_run_solver()    