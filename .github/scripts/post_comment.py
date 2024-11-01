#!/usr/bin/env python3

from github_utils import gh_post_pr_comment
from gitutils import get_git_remote_name, get_git_repo_dir, GitRepo

def parse_args():
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("pr_num", type=int)
    return parser.parse_args()

import torch

class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.x = torch.Tensor([0, 0, 0])
        self.numbers = torch.nn.Parameter(self.x)

    def forward(self):
        return torch.sum(self.numbers)

def main():
    args = parse_args()
    repo = GitRepo(get_git_repo_dir(), get_git_remote_name())
    org, project = repo.gh_owner_and_name()

    model = Model()
    model.load_state_dict(torch.load("weights.pt"))
    gh_post_pr_comment(org, project, args.pr_num, f"The sum is: {model().item()}")


if __name__ == "__main__":
    main()
