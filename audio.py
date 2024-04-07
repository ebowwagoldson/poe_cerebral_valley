import asyncio
import fal_client

text = "The HTTP 404 Not Found response status code indicates that the server cannot find the requested resource. Links that lead to a 404 page are often called broken or dead links and can be subject to link rot."

async def synthesize_speech():
    handler = await fal_client.submit_async(
        "fal-ai/metavoice-v1",
        arguments={
            "text": text,
            "audio_url": "https://cdn.themetavoice.xyz/speakers/bria.mp3"  
        },
    )

    result = await handler.get()
    audio_url = result["audio_url"]["url"]
    print(f"Synthesized speech audio URL: {audio_url}")
    return audio_url

asyncio.run(synthesize_speech())