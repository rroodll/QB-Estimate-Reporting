# QB-Estimate-Reporting

Management and reporting of resource estimates for quantum algorithms

## Features

This package describes in detail the data structure that has been accepted by the QB working group to detail how a Resource Estimate should be reported. It also includes
code to load this data structure from a JSON file and a notebook that demostrates how to use the code and the data structure.

---

## Installation and Environment Setup

It is recommended that conda be used to manage the environment. A setup.py file is included to facilitate this.
Change directory to the location of setup.py, then perform the following commands.

- Create and activate the environment:

        on Windows use:
        conda create -n <Environment Name> "python>=3.8,<=3.11.5"
        on Mac use:
        conda create -n <Environment Name> python'>=3.8,<=3.11.5'

        conda activate <Environment Name>

- Install the package

        pip install .

- If you are working as a developer (for all platforms and shells):

        on Windows use:
        pip install -e .[dev]
        on Mac use:
        pip install -e ."[dev]"

---

## Overview of Examples Included as Jupyter Notebooks

Notebooks showcasing features are organized as follows in the /qb_reporting directory.

## Disclaimer

DISTRIBUTION STATEMENT A. Approved for public release: distribution unlimited.

© 2023 MASSACHUSETTS INSTITUTE OF TECHNOLOGY

    Subject to FAR 52.227-11 – Patent Rights – Ownership by the Contractor (May 2014)
    SPDX-License-Identifier: BSD-2-Clause

This material is based upon work supported by the Under Secretary of Defense for Research and Engineering under Air Force Contract No. FA8702-15-D-0001. Any opinions, findings, conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the Under Secretary of Defense for Research and Engineering.

A portion of this research was sponsored by the United States Air Force Research Laboratory and the United States Air Force Artificial Intelligence Accelerator and was accomplished under Cooperative Agreement Number FA8750-19-2-1000. The views and conclusions contained in this document are those of the authors and should not be interpreted as representing the official policies, either expressed or implied, of the United States Air Force or the U.S. Government. The U.S. Government is authorized to reproduce and distribute reprints for Government purposes notwithstanding any copyright notation herein.

The software/firmware is provided to you on an As-Is basis
