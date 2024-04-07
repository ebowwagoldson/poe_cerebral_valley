from __future__ import annotations

import os
import fastapi_poe as fp
from video_maker import VideoMaker

POE_ACCESS_KEY = os.getenv("POE_ACCESS_KEY")

bot = VideoMaker()
app = fp.make_app(bot, POE_ACCESS_KEY)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)