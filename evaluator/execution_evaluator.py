import os
import subprocess
import tempfile



def execute_test_script(code):
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            test_file = os.path.join(
                tmpdir, 'test_agent.py'
            )
            with open(
                    test_file, 'w',encoding="utf-8"
            ) as f:
                f.write(code)
            result = subprocess.run(
                ["pytest",
                test_file,
                "-v"],
                capture_output=True,
                text=True,
                timeout=60,
            )

        return {
            "status":
                "PASS" if result.returncode == 0 else "FAIL",
            "stdout":
                result.stdout,
            "stderr":
                result.stderr
        }
    except Exception as e:
        return {
            "status":
                "ERROR",
            "error":
            str(e),
        }