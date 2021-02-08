import asyncio
import logging
from libgenesis import Libgen
import json


async def test():
    # creat a Libgen object with return result limit set to 50
    lg = Libgen(result_limit=50)
    # search Libgen
    result = await lg.search('japan history')

    ids = [*result]
    print(ids[0], json.dumps(result[ids[0]], indent=4))
    # download the first result and print the path
    # file = await lg.download(result[ids[0]]['mirrors']['main'])
    # print(file)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(test())
    except KeyboardInterrupt:
        logging.error("KeyboardInterruption: Task Terminated!")
