import argparse


def create_parser():

    parser = argparse.ArgumentParser()

    parser.add_argument("-u", "--url", dest='url', help="url to scan", type=str)
    parser.add_argument("-p", "--port", dest='port', help="port scan range from 1 to the port entered", type=int)
    parser.add_argument("-s", "--semaphore", dest = 'semaphore', help="the amount of concurrent connections that can be open", type=int)

    return parser


