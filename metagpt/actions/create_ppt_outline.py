import asyncio
from metagpt.actions.action import Action
from metagpt.actions.action_output import ActionOutput

class CreatePPTOutline(Action):
    def __init__(self, topic: str):
        self.topic = topic

    async def run(self) -> ActionOutput:
        outline = await self.generate_outline(self.topic)
        return ActionOutput(outline=outline)

    async def generate_outline(self, topic: str) -> str:
        # Simulate asynchronous outline generation
        await asyncio.sleep(1)
        return f"Outline for {topic}"
