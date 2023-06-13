from .Exploit import roblox
from .GetSetImpl import GetSetImpl
from .offsets import property_descriptor_offsets
class PropertyDescriptor:
	def __init__(self, Address) -> None:
		self.addr = Address
	def GetAddress(self) -> int:
		return self.addr
	def GetName(self) -> str:
		addr = self.GetAddress()
		return roblox.ReadNormalString(roblox.DRP(addr + property_descriptor_offsets["name"]))
	def GetReturnValue(self) -> str:
		return roblox.ReadInstaceString(roblox.DRP(self.GetAddress() + property_descriptor_offsets["returnType"])+0x4)
	def GetSecurity(self) -> int:
		return roblox.Program.read_int(self.addr + property_descriptor_offsets["security"])
	def SetSecurity(self, new_security) -> None:
		roblox.Program.write_int(self.addr + property_descriptor_offsets["security"], new_security)
	def GetSet(self):
		return GetSetImpl(roblox.DRP(self.addr + property_descriptor_offsets["GetSet"]))
	
__all__ = ["PropertyDescriptor"]