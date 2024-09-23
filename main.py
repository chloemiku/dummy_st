import os
import subprocess


# Streamlit app code
if __name__ == "__main__":
    script_path = os.path.abspath(__file__)
    subprocess.run(["streamlit", "run", "ui.py"])