import asyncio

async def auth_user():
    await asyncio.sleep(2)
    print("User authenticated")

async def fetch_profile():
    await asyncio.sleep(1)
    print("Profile loaded")

async def main():         # run both together
    await asyncio.gather( #key line
        auth_user(),
        fetch_profile()
    )
asyncio.run(main())