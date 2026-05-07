#!/usr/bin/env python3
"""Simple todo CLI tool."""

import json
import sys
from pathlib import Path

TODO_FILE = Path("todos.json")


def load_todos():
    if TODO_FILE.exists():
        return json.loads(TODO_FILE.read_text())
    return []


def save_todos(todos):
    TODO_FILE.write_text(json.dumps(todos, indent=2, ensure_ascii=False))


def cmd_add(text):
    todos = load_todos()
    todos.append({"id": len(todos) + 1, "text": text, "done": False})
    save_todos(todos)
    print(f"Added: {text}")


def cmd_list():
    todos = load_todos()
    if not todos:
        print("No todos.")
        return
    for t in todos:
        status = "✓" if t["done"] else " "
        print(f"  [{status}] {t['id']}. {t['text']}")


def cmd_done(task_id):
    todos = load_todos()
    for t in todos:
        if t["id"] == task_id:
            t["done"] = True
            save_todos(todos)
            print(f"Done: {t['text']}")
            return
    print(f"Todo {task_id} not found.")


def main():
    if len(sys.argv) < 2:
        print("Usage: todo.py <add|list|done> [args]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: todo.py add <text>")
            sys.exit(1)
        cmd_add(" ".join(sys.argv[2:]))
    elif command == "list":
        cmd_list()
    elif command == "done":
        if len(sys.argv) < 3:
            print("Usage: todo.py done <id>")
            sys.exit(1)
        try:
            cmd_done(int(sys.argv[2]))
        except ValueError:
            print("ID must be a number.")
            sys.exit(1)
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
