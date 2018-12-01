
def prepare_arguments(parser):
    parser.add_argument('-r', '--rule', default=None, help='CppCheck rule file')
    return parser


def run_cppcheck(args):
    pass

description = dict(
    verb='cppcheck',
    description='Run cppcheck on catkin packages',
    main=run_cppcheck,
    prepare_arguments=prepare_arguments
)
