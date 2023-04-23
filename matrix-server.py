import simplematrixbotlib as botlib
from nio import AsyncClient

SERVER_URL = "https://matrix.example.com"
USER_ID = "@shrutibindal:matrix.org"
ACCESS_TOKEN = "..."
ROOM_ID = "https://matrix.to/#/@shrutibindal:matrix.org"

async def main():
    client = AsyncClient(SERVER_URL)
    await client.login(token=ACCESS_TOKEN, device_name="mybot")

    # Join the channel
    await client.room_join(ROOM_ID)

    # Fetch the historical messages
    response = await client.room_messages(
        ROOM_ID,
        limit=100,  # Adjust the limit as needed
        direction="b",
        filter={},
    )

    for event in response["chunk"]:
        # Process each message event here
        print(event)

    # Subscribe to live updates
    since_token = response["end"]
    while True:
        response = await client.sync(since_token=since_token, timeout=30000)
        since_token = response["next_batch"]

        for room_id, room_info in response["rooms"]["join"].items():
            if room_id == ROOM_ID:
                for event in room_info["timeline"]["events"]:
                    # Process each new message event here
                    print(event)





