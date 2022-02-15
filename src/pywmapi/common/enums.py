from enum import Enum


class Platform(str, Enum):
    pc = "pc"
    xbox = "xbox"
    ps4 = "ps4"
    switch = "switch"


class Language(str, Enum):
    en = "en"
    ru = "ru"
    ko = "ko"
    de = "de"
    fr = "fr"
    pt = "pt"
    zh_hans = "zh-hans"
    zh_hant = "zh-hant"
    es = "es"
    it = "it"
    pl = "pl"


class OrderType(str, Enum):
    sell = "sell"
    buy = "buy"


class IncludeOption(str, Enum):
    item = "item"


class WeaponType(str, Enum):
    shotgun = "shotgun"
    rifle = "rifle"
    pistol = "pistol"
    melee = "melee"
    zaw = "zaw"
    kitgun = "kitgun"


class IconFormat(str, Enum):
    land = "land"
    port = "port"
