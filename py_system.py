import os
import sys
import argparse
# add description

ap = argparse.ArgumentParser(description='test_250',
                            prog='asshole',
                             usage='nothing to say',
                             epilog='the floor of help')

ap.add_argument('-ig', '--ignore',nargs=3, help='在 %(prog)s 传入图片文件')
args = vars(ap.parse_args())
print(args)