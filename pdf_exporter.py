# File: pdf_exporter.py
#
# Copyright (c) 2023 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions
# and limitations under the License.


import datetime

from fpdf import FPDF


class PDF(FPDF):
    def get_date_str(self):
        return datetime.datetime.now().strftime("%B %d, %Y, %I:%M%p")

    def write_title(self, title):
        # Logo
        # self.image('logo_pb.png', 10, 8, 33)
        # Arial bold 15
        self.set_font("Arial", "B", 16)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, "{t} - {d}".format(t=title, d=self.get_date_str()), 0, 0, "C")
        # Line break
        self.ln(10)

    def write_worbookname(self, name):
        self.ln(10)
        self.set_font("Arial", "U", 15)
        self.cell(40, 10, name)
        self.ln(10)

    def write_phase(self, phase):
        self.ln(10)
        self.set_font("Arial", "B", 14)
        self.cell(40, 10, phase)
        self.ln(10)

    def write_task_name(self, taskname):
        self.ln(5)
        self.set_font_size(13)
        self.set_font("Arial")
        self.cell(10)
        self.cell(40, 10, taskname)
        self.ln(5)

    def write_section(self, title, text):
        self.ln(5)
        self.set_font("Arial", "B", 12)
        self.cell(20)
        self.cell(40, 10, "- {t}:".format(t=title))
        self.ln(10)
        self.set_font_size(11)
        self.set_font("Arial")
        self.cell(20)
        self.multi_cell(150, 5, text)
        self.ln(3)

    def write_actions(self, actions):
        if not actions:
            return
        self.set_font("Arial", "B", 12)
        self.cell(20)
        self.cell(40, 10, "- Actions:")
        self.ln(7)
        self.set_font_size(11)
        self.set_font("Arial")
        self.cell(20)
        for action in actions:
            self.cell(40, 10, action)
            self.ln(7)
            self.cell(20)
        self.ln(3)

    def write_playbooks(self, playbooks):
        if not playbooks:
            return
        self.set_font("Arial", "B", 12)
        self.cell(20)
        self.cell(40, 10, "- Playbooks:")
        self.ln(7)
        self.set_font_size(11)
        self.set_font("Arial")
        self.cell(20)
        for playbook in playbooks:
            self.cell(40, 10, playbook["playbook"])
            self.ln(7)
            self.cell(20)
        self.ln(3)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font("Arial", "I", 8)
        # Page number
        self.cell(0, 10, "Page " + str(self.page_no()), 0, 0, "C")