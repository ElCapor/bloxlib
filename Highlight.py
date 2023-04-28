from .instance import Instance
from .Camera import Vector3
from .Exploit import roblox
class Highlight(Instance):
    def __init__(self, otherType=0) -> None:
        super().__init__(otherType)
    def SetFillColor(self, newColor : Vector3): #placeholder until i add color3
        NewMemoryRegion = roblox.Program.allocate(100)
        NewMemAddress = NewMemoryRegion
        struct = roblox.Program.allocate(12)
        InstanceAddress = Highlight.getAddress() #Change This
        FunctionAddress = Highlight.GetPropertyDescriptor("FillColor").GetSet().Set()
        roblox.Program.write_float(struct, newColor.x)
        roblox.Program.write_float(struct + 4, newColor.y)
        roblox.Program.write_float(struct + 8, newColor.z)
        HexArray = ''
        MovIntoEcxOp = 'B9' + roblox.hex2le(roblox.d2h(InstanceAddress))
        PushOPX = '68' +  roblox.hex2le(roblox.d2h(struct))
        CallOp = 'E8' + roblox.hex2le(roblox.calcjmpop(roblox.d2h(FunctionAddress),roblox.d2h(NewMemAddress + 10)))
        StoreOp = 'A3' + roblox.hex2le(roblox.d2h(NewMemAddress + 0x30))
        RetOp = 'C3'
        HexArray = MovIntoEcxOp +  PushOPX  + CallOp + StoreOp + RetOp
        roblox.Program.write_bytes(NewMemAddress,bytes.fromhex(HexArray),roblox.gethexc(HexArray))
        roblox.Program.start_thread(NewMemAddress)
        returnValue = roblox.DRP(NewMemAddress + 0x30)
        roblox.Program.free(NewMemAddress)
        return returnValue


__all__ = ["Highlight"]