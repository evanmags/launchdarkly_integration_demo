from textwrap import dedent
import woodchipper
from cats.database import get_random

from fastapi import Response

logger = woodchipper.get_logger(__name__)


def do_stuff():
    logger.info("Meow Meow")
    return Response(get_random())


def do_other_stuff():
    logger.info("Party Time")
    return Response("https://www.youtube.com/watch?v=dQw4w9WgXcQ")


def do_not_do_stuff():
    logger.info("Nothing Special Happened")
    return Response("Nothing Special Happened")
