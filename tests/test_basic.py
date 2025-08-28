import subprocess
import sys


def test_fibonacci_output():
    # Run the fibonacci_demo.py script
    result = subprocess.run([sys.executable, "fibonacci_demo.py"], capture_output=True, text=True)
    output = result.stdout.strip().split()
    expected = ["0","1","1","2","3","5","8","13","21","34"]
    assert output[:10] == expected
