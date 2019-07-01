import argparse
import getpass

from api import run_webserver 


class PasswordRetriever(argparse.Action):
    def __call__(self, parser, namespace, values, opts):
        if values is None:
            values = getpass.getpass()
        setattr(namespace, self.dest, values)


def start_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('run', help='Run a webserver at specified port')

    parser.add_argument(
        '-pwd',
        help='Specify the password',
        nargs='?',
        dest='password',
        action=PasswordRetriever
    )

    parser.add_argument(
        '-p', '--port', 
        help='Specify thw webserver port',
        type=int
    )
    parser.add_argument(
        '-e', '--environment',
        help='Specify the environment which the application in running on',
        choices=['dev', 'staging', 'prod']
    )

    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        '-v', '--verbose',
        help='Specify whether is running on verbose mode or not'
    )
    group.add_argument(
        '-q', '--quiet',
        help='Specify whether is running on quiet mode or not'
    )

    args = parser.parse_args()

    port = args.port if args.port else 8080
    env = args.environment if args.environment else 'dev'

    if args.run:
        print('Serving a webserver at port {}...'.format(port))
        print('Running on: {} environment'.format(env))
        print('Using the password: {}'.format(args.password))
        
        run_webserver(port)
    else:
        print('No command has been sent.')
