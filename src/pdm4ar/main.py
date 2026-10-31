import argparse
import os
import logging

import contracts
from zuper_commons import ZLogger
from zuper_commons.text import remove_escapes

from pdm4ar.exercises_def import logger
from pdm4ar.exercises_def.ex14 import get_exercise14
from pdm4ar.exercises_def.structures import ExerciseEvaluator, out_dir


def run_exercise(configs: list[str] | None = None):
    ex = get_exercise14(configs)
    evaluator = ExerciseEvaluator(exercise=ex)

    out_main = out_dir("14")

    ZLogger("reprep").setLevel(logging.WARNING)  # suppress annoying messages from reprep

    perf, report = evaluator.evaluate()

    report_file = os.path.join(out_main, "index.html")
    report.to_html(report_file)
    result_str = remove_escapes(str(perf))
    logger.info(f"\n<<<<<\n{result_str}\n>>>>>")
    logger.info(f"Report written to {report_file}")


def _setup_args():
    parser = argparse.ArgumentParser(description="Multi-robot warehouse goal collection (PDM4AR exercise 14)")
    parser.add_argument(
        "-c",
        "--config",
        nargs="+",
        help="scenario(s) to run, e.g. config_3.yaml (default: all public scenarios)",
    )
    return parser.parse_args()


def main():
    contracts.disable_all()
    args = _setup_args()
    run_exercise(configs=args.config)


if __name__ == "__main__":
    main()
