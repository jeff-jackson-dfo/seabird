#!/usr/bin/env python

""" Check the rules
"""

from importlib import resources
import json
import re
import seabird


def test_load_available_rules():
    """Try to read all available rules

    https://github.com/castelao/seabird/issues/7
    """
    rules_dir = "rules"

    # Locate the rules directory inside the seabird package
    rules_root = resources.files(seabird).joinpath(rules_dir)

    # List JSON rule files, excluding refnames.json
    rule_files = [
        p.name
        for p in rules_root.iterdir()
        if p.is_file() and re.match(r"^(?!refnames).*\.json$", p.name)
    ]

    for rule_file in rule_files:
        print(f"loading rule: {rule_file}")

        # Load JSON content
        with rules_root.joinpath(rule_file).open("r", encoding="utf-8") as f:
            rule = json.load(f)

        assert isinstance(rule, dict)
        assert len(rule) > 0
