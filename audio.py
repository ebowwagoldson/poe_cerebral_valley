import fal_client

class AudioProcessor:
    def __init__(self, fal_client):
        self.fal_client = fal_client

    async def generate_speech(self, text):
        handler = await self.fal_client.submit(
            "fal-ai/metavoice-v1",
            arguments={
                "text": text,
                "audio_url": "https://cdn.themetavoice.xyz/speakers/bria.mp3"
            },
        )

        log_index = 0
        async for event in handler.iter_events(with_logs=True):
            if isinstance(event, fal_client.InProgress):
                new_logs = event.logs[log_index:]
                for log in new_logs:
                    print(log["message"])
                log_index = len(event.logs)

        result = await handler.get()
        return result["audio"]["url"]