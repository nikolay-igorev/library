import argparse

import lib
import lib.entity
import lib.repository
import lib.service
import lib.storage.json


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "command", choices=["list", "add", "delete", "change-status", "search"]
    )
    return parser


if __name__ == "__main__":
    args = get_parser().parse_args()

    storage = lib.storage.json.JSONStorage("./database.json")
    repository = lib.repository.Books(storage)
    service = lib.service.ConsoleService(repository)

    match args.command:
        case "list":
            service.handle_list()
        case "delete":
            service.handle_delete()
        case "search":
            service.handle_search()
        case "add":
            service.handle_add()
        case "change-status":
            service.handle_change_status()
