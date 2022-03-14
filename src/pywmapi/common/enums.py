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


class ElementType(str, Enum):
    impact = "impact"
    heat = "heat"
    cold = "cold"
    electricity = "electricity"
    toxin = "toxin"
    magnetic = "magnetic"
    radiation = "radiation"


class ProfileStatus(str, Enum):
    offline = "offline"
    online = "online"
    ingame = "ingame"


class WSType(str, Enum):
    SET_STATUS = "@WS/USER/SET_STATUS"


class AuctionType(str, Enum):
    riven = "riven"
    lich = "lich"
    kubrow = "kubrow"


class Polarity(str, Enum):
    madurai = "madurai"
    vazarin = "vazarin"
    naramon = "naramon"
    zenurik = "zenurik"
    unairu = "unairu"
    penjaga = "penjaga"
    umbra = "umbra"
    aura = "aura"
