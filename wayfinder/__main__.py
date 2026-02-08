import argparse


def main() -> int:
    args = _arg_parser().parse_args()
    try:
        args.func(args)
    except Exception as e:
        print("[!]", e)
        return 1


def _arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="waypoint: helping csv files find their way")
    subparsers = parser.add_subparsers(dest="command", required=True)
    _import_parser(subparsers)
    return parser


def _import_parser(subparsers) -> None:
    import_parser = subparsers.add_parser(
        "import", help="validate CSVs and generate a report")
    import_parser.add_argument(
        "inputs", nargs="+", help="one or more csv files to validated")
    import_parser.add_argument(
        "--schema", required=True, help="schema to validate the files against")
    import_parser.add_argument("--output-dir", default=".",
                               help="output directory for the validated files")
    import_parser.add_argument(
        "--report-dir", default=".",
        help="output directory for the generated report")


if __name__ == '__main__':
    main()
