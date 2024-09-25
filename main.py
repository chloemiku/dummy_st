# import os
# import subprocess
#
# import ui as ui
#
# # Streamlit app code
# if __name__ == "__main__":
#     script_path = os.path.abspath(__file__)
#     ui_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ui.py")
#
#     subprocess.run(["streamlit", "run", ui_path])

import os
import subprocess
import sys

# Get the current directory of the bundled executable or script
if getattr(sys, 'frozen', False):
    # This is where PyInstaller bundles everything
    bundle_dir = sys._MEIPASS
else:
    # When running locally without PyInstaller
    bundle_dir = os.path.dirname(os.path.abspath(__file__))

ui_script_path = os.path.join(bundle_dir, "ui.py")

if __name__ == "__main__":
    subprocess.run(["streamlit", "run", ui_script_path])