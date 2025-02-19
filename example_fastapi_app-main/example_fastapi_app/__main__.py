import asyncio
import ipaddress
import argparse
from argparse import ArgumentParser
from fastapi import FastAPI
from fastapi.params import Body, Path
from hypercorn.config import Config
from hypercorn.asyncio import serve

rest_api = FastAPI()

persons_list = []

class person:
    def __init__(self, name, age, description):
        self.name == name
        self.age == age
        self.description == description

    def __eq__(self, other):
        return self.name == other.name

@rest_api.post('/person')
def create_record(name: str = Body(...),
                  age: int = Body(...),
                  description: str = Body(...)):  # TODO: Refactor this
    persons_list.append(person(name, age, description))


@rest_api.get('/person/{name}')
def get_record(name: str = Path(...)):
    return persons_list[persons_list.index(person(name, None, None))]


@rest_api.delete('/person/{name}')
def remove_record(name: str = Path(...),
                  age: int = Body(None),
                  description: str = Body(None)):
    new_person = person(name, age, description)

    persons_list.pop(persons_list.index(new_person))


@rest_api.put('/person/{name}')
def update_record(name: str = Path(...),
                  age: int = Body(None),
                  description: str = Body(None)):
    remove_record(name, age, description)

    persons_list.append(person(name, age, description))




if __name__ == '__main__':
    parser = ArgumentParser(
        description="Example fastapi backend")
    parser.add_argument("--server-ip",
                        dest="ip",
                        type=str,
                        required=False,
                        default="127.0.0.1",
                        help="Define the ip that the api server will listen to.")
    parser.add_argument("--server-port",
                        dest="port",
                        type=int,
                        required=False,
                        default=8080,
                        help="Define the port that the api server will listen to.")
    options = parser.parse_args()

    # Validate ip and port
    ipaddress.ip_address(options.ip)

    if not (1 <= options.port <= 65535):
        raise ValueError(f"port number {options.port} is not in the allowed range for ports (1 to 65535)")

    # Run hypercorn server
    config = Config()
    config.bind = [f"{options.ip}:{str(options.port)}"]
    asyncio.run(serve(rest_api, config))