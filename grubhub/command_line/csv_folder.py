import aiofiles


async def ensure_csv_folder_exists(csv_folder):
    if await aiofiles.os.path.exists(csv_folder) is False:
        await aiofiles.os.makedirs(csv_folder)
