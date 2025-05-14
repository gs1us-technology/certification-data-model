#!/usr/bin/env python3

import sys
import json
from pyld import jsonld
from jsonschema import validate, Draft202012Validator
from deepdiff import DeepDiff

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <jsonld-file>")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename) as f:
        doc = json.load(f)
  
    doc.pop("@context", None)
    doc.pop("$schema", None)

    with open("./docs/cert_schema.json") as f:
        schema = json.load(f)

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(doc), key=lambda e: e.path)
    if errors:
        for err in errors:
            print(f"❌ Error at {list(err.path)}: {err.message}")
        exit(-1)
    else:
        print("✅ Example document is Valid against schema")

    with open("./docs/cert_context.json") as f:
        context = json.load(f)

    # Expand and flatten
    expanded = jsonld.expand(
        doc,
        options={"expandContext": context["@context"]}
    )    

    print(json.dumps(expanded, indent=2))

    compacted = jsonld.compact(expanded, context)
    compacted.pop("@context", None)

    diff = DeepDiff(compacted, doc, ignore_order=True)  # Set ignore_order=False if order matters

    if diff:
        print("❌ Differences found:")
        print(diff.pretty())
        print(json.dumps(compacted, indent=2))
        exit(-1)
    else:
        print("✅ JSON documents are equal.")

except Exception as e:
    print(f"Error: {e}")
    sys.exit(2)
