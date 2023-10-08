from enum import Enum


class Platform(Enum):
    pc = "pc"
    xbox = "xbox"
    ps4 = "ps4"
    switch = "switch"


class Language(Enum):
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


class OrderType(Enum):
    sell = "sell"
    buy = "buy"


class IncludeOption(Enum):
    item = "item"


class WeaponType(Enum):
    shotgun = "shotgun"
    rifle = "rifle"
    pistol = "pistol"
    melee = "melee"
    zaw = "zaw"
    kitgun = "kitgun"


class IconFormat(Enum):
    land = "land"
    port = "port"


class ElementType(Enum):
    impact = "impact"
    heat = "heat"
    cold = "cold"
    electricity = "electricity"
    toxin = "toxin"
    magnetic = "magnetic"
    radiation = "radiation"


class ProfileStatus(Enum):
    offline = "offline"
    online = "online"
    ingame = "ingame"


class WSType(Enum):
    SET_STATUS = "@WS/USER/SET_STATUS"


class AuctionType(Enum):
    riven = "riven"
    lich = "lich"
    kubrow = "kubrow"


class Polarity(Enum):
    madurai = "madurai"
    vazarin = "vazarin"
    naramon = "naramon"
    zenurik = "zenurik"
    unairu = "unairu"
    penjaga = "penjaga"
    umbra = "umbra"
    aura = "aura"


class Subtype(Enum):
    # Cetus fishes subtypes
    large = "large"
    medium = "medium"
    small = "small"

    # Fortuna fishes subtypes
    magnificent = "magnificent"
    adorned = "adorned"
    basic = "basic"

    # Special weapons parts subtypes
    blueprint = "blueprint"
    crafted = "crafted"

    # Relics subtypes
    radiant = "radiant"
    flawless = "flawless"
    exceptional = "exceptional"
    intact = "intact"

    # Veiled riven mods subtypes
    revealed = "revealed"
    unrevealed = "unrevealed"
