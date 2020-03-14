from mirai import Mirai, Image, Plain, MessageChain, Group, Member, Depend
import asyncio
from devtools import debug

authKey = "213we355gdfbaerg"
qq = 208924405

app = Mirai(f"mirai://localhost:8070/ws?authKey={authKey}&qq={qq}")

@app.receiver("GroupMessage")
async def event_gm(app: Mirai, message: MessageChain, group: Group, member: Member):
    if group.id == 655057127:
        debug(message)
        await app.sendGroupMessage(
            group.id,
            [
                Image.fromFileSystem()
            ]
        )

if __name__ == "__main__":
    app.run()