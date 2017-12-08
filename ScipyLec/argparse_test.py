#! encoding = utf8
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='test argparse')
    parser.add_argument('--input', type=str,
                        help='input path', dest='inputfile')
    # parser.add_argument('--')
    args = parser.parse_args()

    print('input args:{}'.format(args.inputfile))
