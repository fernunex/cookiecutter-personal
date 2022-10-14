import subprocess

MESSAGE_COLOR = "\x1b[0;34m"
PACKAGE_COLOR = "\x1b[1;33m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR}Almost done!")
print(f"Initializing a git repository...{RESET_ALL}")

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])

print(f"{MESSAGE_COLOR}The beginning of your destiny is defined now! Create and have fun!{RESET_ALL}")

# Creating environment with conda
create_environment = "{{cookiecutter.create_environment}}"
if create_environment == "Yes":
    print(f"{PACKAGE_COLOR}Conda is installing some packages...{RESET_ALL}")
    subprocess.call(['conda', 'env', 'create', '--file','environment.yml'])
else:
    print(f"{PACKAGE_COLOR}The environment was not create.{RESET_ALL}")