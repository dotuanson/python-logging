import logging
from Package import module


def main():
    logging.basicConfig(level=logging.INFO)
    logging.info('Started')
    module.do_something()
    logging.info('Finished')


if __name__ == '__main__':
    main()
