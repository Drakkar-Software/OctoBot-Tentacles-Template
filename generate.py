# MIT License
#
# Drakkar-Software OctoBot-Tentacles-Template
# Copyright (c) Drakkar-Software.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import json
import logging
import os


def parse_package(package_content):
    description_pos = package_content.find("$tentacle_description")
    if description_pos > -1:
        description_begin_pos = package_content.find("{")
        description_end_pos = package_content.find("}") + 1
        description_raw = package_content[description_begin_pos:description_end_pos]
        description = json.loads(description_raw)
        description_list[description["name"]] = description


def read_package(path):
    for file_name in os.listdir(path):
        if file_name.endswith(".py"):
            with open("{0}/{1}".format(path, file_name), "r") as package:
                parse_package(package.read())
                logging.info("Reading tentacle {0}...".format(package))
        else:
            file_name = "{0}/{1}".format(path, file_name)
            if os.path.isdir(file_name) and not path.startswith('.'):
                read_package(file_name)


if __name__ == '__main__':
    description_list = {}
    package_list_file = "tentacles_list.json"

    # Foreach folder (not hidden)
    for root_dir in os.listdir(os.getcwd()):
        if os.path.isdir(root_dir) and not root_dir.startswith('.'):
            read_package(root_dir)

    # Create package list file
    with open(package_list_file, "w") as package_list:
        package_list.write(json.dumps(description_list))

    logging.info("Generation complete")
