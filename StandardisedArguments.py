"""
Functions which help standardise how commandline arguments are structured

"""
import argparse


def create_basic_parser(description):
    """
    Creates a basic argument parser with in and out arguments

    description:- the description to pass to the argument parser
    Return value:- an argparse parser object
    """
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--out', nargs=1, required=True, help="The directory to output results to.")
    parser.add_argument('--input', nargs='+', required=True, help="A path to process.")
    return parser


def add_api_arguments(parser):
    """
    Adds extra arguments to a parser for when accessing APIs

    parser:- an argparse parser object to add the arguments to
    Return value:- the parser object that was passed in
    """
    parser.add_argument('--api_url', nargs=1, required=True, help="The base api url to use.")
    parser.add_argument('--api_key',
                        nargs=1,
                        required=True,
                        help="The token, or key, to send with api calls.")
    parser.add_argument('--api_key_header',
                        nargs=1,
                        required=True,
                        help="The header name to send the key as, eg x-token, or Authorization")
    return parser

def add_sql_server_arguments(parser):
    """
    Adds extra arguments to a parser for when accessing SQL Server databases

    parser:- an argparse parser object to add the arguments to
    Return value:- the parser object that was passed in
    """
    parser.add_argument('--sql_server', nargs=1, required=True, help='the sql server to connect to')
    parser.add_argument('--sql_username', nargs=1, required=True, help='the user to connect as')
    parser.add_argument('--sql_password', nargs=1, required=True, help='the password to use')
    parser.add_argument('--sql_database', nargs=1, required=True, help='the db to access')
    return parser

def add_crypto_arguments(parser):
    """
    Adds extra arguments to a parser for when using cryptography

    parser:- an argparse parser object to add the arguments to
    Return value:- the parser object that was passed in
    """
    parser.add_argument('--crypto_key', nargs=1, required=True, help='The encryption key to use')
    return parser

def add_azure_storage_arguments(parser):
    """
    Adds extra arguments to a parser for when using azure blob storage

    parser:- an argparse parser object to add the arguments to
    Return value:- the parser object that was passed in
    """
    parser.add_argument('--storage_account_name',
                        nargs=1,
                        required=True,
                        help='the storage account name')
    parser.add_argument('--storage_account_key',
                        nargs=1,
                        required=True,
                        help='the key to access the account')
    parser.add_argument('--storage_container_name',
                        nargs=1,
                        required=True,
                        help='the container to sync')
    return parser
