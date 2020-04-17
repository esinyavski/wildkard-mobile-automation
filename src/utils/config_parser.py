import os
import json

from dataclasses import dataclass

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "../../config.json")


@dataclass
class ConfigPhone:
    country: str
    number: str
    full_number: str = None


@dataclass
class Config:
    platformName: str
    platformVersion: str
    deviceName: str
    udid: str
    xcodeOrgId: str
    xcodeSigningId: str
    bundleId: str
    appiumUrl: str
    main_phone: ConfigPhone
    waiting_time: int


def parse_config() -> Config:
    with open(CONFIG_PATH) as file:
        config = json.load(file)
        return Config(
            platformName=config['platformName'],
            platformVersion=config['platformVersion'],
            deviceName=config['deviceName'],
            udid=config['udid'],
            xcodeOrgId=config['xcodeOrgId'],
            xcodeSigningId=config['xcodeSigningId'],
            bundleId=config['bundleId'],
            appiumUrl=config['appiumUrl'],
            main_phone=ConfigPhone(number=config['main_phone']['number'],
                                   full_number=config['main_phone']['full_number'],
                                   country=config['main_phone']['country']),
            waiting_time=config['waiting_time']
        )
