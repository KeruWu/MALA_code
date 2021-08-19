import argparse
import subprocess


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-fig", type=int, choices=[1,2,3,4,5], required=True,
                        help='Figure number in the paper')
    parser.add_argument("-subfig", type=str, choices=['a', 'b', 'c', 'd'],
                        help="Subfigure panel in the figure")
    return parser

cmd_dict = {
    (1, 'a') : ["python", "utils/MALA_only.py", "-target", "perturbed", "-init", "warm", "-dependency", "dimension", "-plot", "acc"],
    (1, 'b') : ["python", "utils/MALA_only.py", "-target", "perturbed", "-init", "warm", "-dependency", "dimension", "-plot", "mix"],
    (1, 'c') : ["python", "utils/MALA_only.py", "-target", "perturbed", "-init", "bad", "-dependency", "dimension", "-plot", "acc"],
    (1, 'd') : ["python", "utils/MALA_only.py", "-target", "perturbed", "-init", "bad", "-dependency", "dimension", "-plot", "mix"],
    (2, 'a') : ["python", "utils/ULA_MALA.py", "-plot", "acc"],
    (2, 'b') : ["python", "utils/ULA_MALA.py", "-plot", "mix"],
    (3, 'a') : ["python", "utils/MALA_only.py", "-target", "perturbed", "-init", "warm", "-dependency", "condition", "-plot", "acc"],
    (3, 'b') : ["python", "utils/MALA_only.py", "-target", "perturbed", "-init", "warm", "-dependency", "condition", "-plot", "mix"],
    (4, 'a') : ["python", "utils/MALA_only.py", "-target", "original", "-init", "warm", "-dependency", "dimension", "-plot", "acc"],
    (4, 'b') : ["python", "utils/MALA_only.py", "-target", "original", "-init", "warm", "-dependency", "dimension", "-plot", "mix"],
    (4, 'c') : ["python", "utils/MALA_only.py", "-target", "original", "-init", "bad", "-dependency", "dimension", "-plot", "acc"],
    (4, 'd') : ["python", "utils/MALA_only.py", "-target", "original", "-init", "bad", "-dependency", "dimension", "-plot", "mix"],
    (5, 'a') : ["python", "utils/MALA_only.py", "-target", "original", "-init", "warm", "-dependency", "condition", "-plot", "acc"],
    (5, 'b') : ["python", "utils/MALA_only.py", "-target", "original", "-init", "warm", "-dependency", "condition", "-plot", "mix"],
}

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    cmd = cmd_dict[(args.fig, args.subfig)]
    subprocess.run(cmd)