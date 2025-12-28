#!/usr/bin/python3
"""
Task 0 - Simple Template Rendering
Generates personalized invitation files based on a template and attendee list.
"""

import os


def generate_invitations(template, attendees):
    """
    Generates invitation files using a string template and a list of attendees.

    Args:
        template (str): Template text containing placeholders.
        attendees (list): List of dictionaries with attendee information.

    Behavior:
        - Validates input types
        - Handles empty template
        - Handles empty attendee list
        - Replaces missing data with "N/A"
        - Writes output_X.txt files sequentially
    """

    # 1️⃣ **Check input types**
    if not isinstance(template, str):
        print("Error: template should be a string.")
        return

    if not isinstance(attendees, list) or \
       not all(isinstance(item, dict) for item in attendees):
        print("Error: attendees should be a list of dictionaries.")
        return

    # 2️⃣ **Check for empty template**
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # 3️⃣ **Check for empty list**
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # 4️⃣ **Process each attendee**
    for index, person in enumerate(attendees, start=1):
        # Replace missing data with "N/A"
        name = person.get("name", "N/A") or "N/A"
        event_title = person.get("event_title", "N/A") or "N/A"
        event_date = person.get("event_date", "N/A") or "N/A"
        event_location = person.get("event_location", "N/A") or "N/A"

        # Replace placeholders
        filled_template = (
            template.replace("{name}", str(name))
                    .replace("{event_title}", str(event_title))
                    .replace("{event_date}", str(event_date))
                    .replace("{event_location}", str(event_location))
        )

        # File name
        output_filename = f"output_{index}.txt"

        # 5️⃣ **Write output file**
        try:
            with open(output_filename, "w") as f:
                f.write(filled_template)

        except Exception as e:
            print(f"Error writing to file {output_filename}: {e}")
            return
