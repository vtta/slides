#!/usr/bin/env python3

import argparse
import os


def new(args):
    cmd = 'cp template/"{}"/template.md "{}".md'.format(
        args.template, args.name)
    print('+', cmd)
    if not args.dry_run:
        os.system(cmd)


def build(args):
    cmd = 'tpage --include_path=template/"{}" "{}".md > "{}".html'.format(
        args.template, args.name, args.name)
    print('+', cmd)
    if not args.dry_run:
        os.system(cmd)


def show(args):
    cmd = 'open "{}".html'.format(args.name)
    print('+', cmd)
    if not args.dry_run:
        os.system(cmd)


def main():
    templates = []
    for (dirpath, dirnames, filenames) in os.walk('./template'):
        templates.extend(dirnames)
        break

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d',
        '--dry-run',
        action='count',
        default=0,
        help='only run script logic, not execute final command')
    subparsers = parser.add_subparsers(title='subcommands',
                                       description='valid subcommands',
                                       help='additional help')

    subcmd_new = subparsers.add_parser('new',
                                       help='create a new placeholder slide')
    subcmd_new.add_argument('name',
                            type=str,
                            help='file name you want for the new slide')
    subcmd_new.add_argument(
        '-t',
        '--template',
        choices=templates,
        default=templates[0],
        help='template to use when building, possible values: remaek, simple')
    subcmd_new.set_defaults(func=new)

    subcmd_build = subparsers.add_parser('build', help='build the slide')
    subcmd_build.add_argument('name',
                              type=str,
                              help='file name of the slide you want to build')
    subcmd_build.add_argument(
        '-t',
        '--template',
        choices=templates,
        default=templates[0],
        help='template to use when building, possible values: remaek, simple')
    subcmd_build.set_defaults(func=build)

    subcmd_show = subparsers.add_parser('show', help='view the built slide')
    subcmd_show.add_argument('name',
                             type=str,
                             help='file name of the slide you want to show')
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()