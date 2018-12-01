from catkin_pkg.packages import find_package_paths

import cppcheck


def prepare_arguments(parser):
    parser.add_argument('-e', '--enable', action='append',
        choices=[
            'all', 'warning', 'style', 'performance', 'portability', 'information', 'unusedFunction', 'missingInclude'
        ],
        help='cppcheck check options'
    )
    parser.add_argument('-q', '--quiet', action='store_true', default=False, help='Only print when there is an error')

    return parser


def run_cppcheck(args):
    enable_checks = args.enable
    quiet = args.quiet

    # TODO(nnarain): Get workspace root from catkin...
    package_paths = find_package_paths('.')

    cppcheck.check(package_paths, enable_checks)


description = dict(
    verb='cppcheck',
    description='Run cppcheck on catkin packages',
    main=run_cppcheck,
    prepare_arguments=prepare_arguments
)
