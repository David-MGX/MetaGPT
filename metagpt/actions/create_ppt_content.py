import asyncio
from metagpt.actions.action import Action
from metagpt.actions.action_output import ActionOutput

class CreatePPTContent(Action):
    def __init__(self, topic: str):
        self.topic = topic

    async def run(self) -> ActionOutput:
        content = await self.generate_content(self.topic)
        return ActionOutput(content=content)

    async def generate_content(self, topic: str) -> str:
        # Simulate asynchronous content generation
        await asyncio.sleep(1)
        return f"Content for {topic}"
