instance_offsets = {
    "name":0x2C,
    "parent":0x3C,
    "childlist":0x30,
    "class_descriptor":0xC,
    "property_descriptor":0x18,
    "event_descriptor":0x78,
    "boundedfunctions":0xD8,
    "new" : "RobloxPlayerBeta.exe+45C060",
    "name_map" : "RobloxPlayerBeta.exe+3A800D8"
}

property_descriptor_offsets = {
    "name": 0x4,
    "returnType" : 0x24,
    "security" : 0x1C,
    "GetSet" : 0x30,
}

bounded_functions_offsets = {
    "name":0x4,
    "security" :0x1C,
    "function" : 0x40
}

__all__ = ["instance_offsets"]