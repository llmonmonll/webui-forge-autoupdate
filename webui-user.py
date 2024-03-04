import os
import shutil
import subprocess
import datetime

# Absolute path of the directory where Stable Diffusion WebUI (A1111) is located.
A1111_HOME = r"\absolute\path\to\stable-diffusion-webui"

# Absolute path of the directory where Stable Diffusion WebUI Forge (lllyasviel) is located.
WEB_UI_FORGE = r"\absolute\path\to\Stable Diffusion WebUI Forge (lllyasviel)"

# Absolute path of the directory where Stable Diffusion WebUI Forge (lllyasviel) is located.
WEB_UI = r"\absolute\path\to\Stable Diffusion WebUI Forge (lllyasviel)\webui"


DIR = os.path.join(WEB_UI_FORGE, "system")
GIT_BIN_PATH = os.path.join(DIR, "git", "bin")
PYTHON_PATH = os.path.join(DIR, "python")
PYTHON_SCRIPTS_PATH = os.path.join(DIR, "python", "Scripts")
PY_LIBS_PATH = os.path.join(DIR, "python", "Scripts", "Lib")
PY_SITE_PACKAGES_PATH = os.path.join(DIR, "python", "Scripts", "Lib", "site-packages")
PIP_PATH = os.path.join(DIR, "python", "Scripts")
PIP_INSTALLER_LOCATION = os.path.join(DIR, "python", "get-pip.py")
TRANSFORMERS_CACHE = os.path.join(DIR, "transformers-cache")
LAUNCH_PATH = os.path.join(WEB_UI, "launch.py")

# Set environment variables
os.environ["DIR"] = DIR
os.environ["PATH"] = f"{GIT_BIN_PATH};{PYTHON_PATH};{PYTHON_SCRIPTS_PATH};{os.environ['PATH']}"
os.environ["PY_LIBS"] = f"{PY_LIBS_PATH};{PY_SITE_PACKAGES_PATH}"
os.environ["PY_PIP"] = PIP_PATH
os.environ["SKIP_VENV"] = "1"
os.environ["PIP_INSTALLER_LOCATION"] = PIP_INSTALLER_LOCATION
os.environ["TRANSFORMERS_CACHE"] = TRANSFORMERS_CACHE
os.environ["LAUNCH_PATH"] = LAUNCH_PATH

VENV_DIR = os.path.join(A1111_HOME, "venv")

# === If a backslash is required, use subsequent COMMANDLINE_ARGS. Comment out this COMMANDLINE_ARGS. ===
# COMMANDLINE_ARGS = [
#     "--ckpt-dir", os.path.join(A1111_HOME, "models", "Stable-diffusion"),
#     "--embeddings-dir", os.path.join(A1111_HOME, "embeddings"),      
#     "--hypernetwork-dir", os.path.join(A1111_HOME, "models", "hypernetworks"),
#     "--lora-dir", os.path.join(A1111_HOME, "models", "Lora"),
#     "--theme", "dark"
# ]

# === Use when a backslash is required. Ver.1 (Is there a backslash) ===
COMMANDLINE_ARGS = [
    "--ckpt-dir", os.path.join(A1111_HOME, "models", "Stable-diffusion").replace("\\", "/"),
    "--embeddings-dir", os.path.join(A1111_HOME, "embeddings").replace("\\", "/"),      
    "--hypernetwork-dir", os.path.join(A1111_HOME, "models", "hypernetworks").replace("\\", "/"),
    "--lora-dir", os.path.join(A1111_HOME, "models", "Lora").replace("\\", "/"),
    "--theme", "dark"
]

# === Use when a backslash is required. Ver.2 (Is there a forward slash) ===
# COMMANDLINE_ARGS = [
#     "--ckpt-dir", os.path.join(A1111_HOME, "models", "Stable-diffusion").replace("/", "\\"),
#     "--embeddings-dir", os.path.join(A1111_HOME, "embeddings").replace("/", "\\"),      
#     "--hypernetwork-dir", os.path.join(A1111_HOME, "models", "hypernetworks").replace("/", "\\"),
#     "--lora-dir", os.path.join(A1111_HOME, "models", "Lora").replace("/", "\\"),
#     "--theme", "dark"
# ]

COMMANDLINE_ARGS_STR = " ".join(COMMANDLINE_ARGS)

def run_bat_file(file_path):
    subprocess.Popen([file_path], shell=True)

def set_environment_variables():
    os.environ["VENV_DIR"] = VENV_DIR
    os.environ["COMMANDLINE_ARGS"] = COMMANDLINE_ARGS_STR

def set_console_title(title):
    os.system(f"title {title}")

def backup_self():
    current_file = os.path.abspath(__file__)
    new_file = current_file.replace(".py", ".py.bak")
    shutil.copyfile(current_file, new_file)

# Function to perform a git pull
def git_pull(directory):
    try:
        # Run a git pull
        subprocess.run(["git", "-C", directory, "pull"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Update succeeded")
    except subprocess.CalledProcessError:
        print("Git pull failed. Perform the pull again after a hard reset.")
        # Hard reset and run git pull again
        subprocess.run(["git", "-C", directory, "reset", "--hard"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(["git", "-C", directory, "pull"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def monday_message():
    print("Today is Monday; Update Stable diffusion webui forge...")

def main():
    set_console_title("Stable Diffusion WebUI Forge")  # Setting the title
    backup_self()  # Self-replication of backup files
    set_environment_variables()  # Setting environment variables
    today = datetime.datetime.now().weekday()  # Monday: 0, Tuesday: 1, ... , Sunday: 6
    if today == 0:  # Monday
        monday_message()  # Monday's message
        git_pull(WEB_UI)
        os.chdir(WEB_UI)
        # run_bat_file("update.bat")
        os.system(os.path.join(WEB_UI, "webui.bat"))
    else:
        os.system(os.path.join(WEB_UI, "webui.bat"))
if __name__ == "__main__":
    main()
