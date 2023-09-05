#!/usr/bin/python3

java_version = None

# Read the text file and search for lines starting with "Java_version="
with open('file.txt', 'r') as file:
    for line in file:
        if line.strip().startswith('Java_version='):
            # Extract the Java version information after the equals sign
            java_version = line.split('=')[1].strip()

# Get the Java version installed on your system
import subprocess
import re

version = subprocess.check_output(['java', '-version'], stderr=subprocess.STDOUT)

java_sys_version = re.search(r'"[0-9\._]*"', version.decode().split("\r")[0]).group().replace('"', '')

if java_version:
    print("Found Java version in the file:", java_version)
    if java_version == java_sys_version:
        print("Java and Python versions are the same.")
    else:
        print("Java and Python versions are different.")
        print("Python version:", java_sys_version)
else:
    print("Java version not found in the file.")

