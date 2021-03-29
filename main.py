# simulation of using yaml
import argparse
import os
from defaults import _C as cfg

def main():
    parser = argparse.ArgumentParser(description="YAML parser")
    parser.add_argument(
            "--config-file",
            default="./setting.yaml",
            metavar="FILE",
            help="path to config file",
            )
    # this makes sure you can use commond like
    # python main.py --config-file setting.yaml MODEL.ARCH PSP
    parser.add_argument(
        "opts",
        help="Modify config options using the command-line",
        default=None,
        nargs=argparse.REMAINDER,
    )
    args = parser.parse_args()
    cfg.merge_from_file(args.config_file)
    cfg.merge_from_list(args.opts)
    cfg.freeze()

    print(cfg.MODEL.ARCH)

if __name__ == "__main__":
    main()