from telethon.sync import TelegramClient
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import DeleteHistoryRequest
from telethon.tl.types import InputPeerChannel, InputPeerChat, InputPeerUser
import asyncio


# Isi dengan API ID dan API Hash kamu
api_id = 'xxxxx'
api_hash = 'xxxxxx'
phone_number = '+62xxxx'

client = TelegramClient('session_name', api_id, api_hash, connection_retries=5, timeout=30)

async def main():
    await client.start(phone_number)

    dialogs = await client.get_dialogs()

    for dialog in dialogs:
        entity = dialog.entity
        if dialog.is_channel:
            if getattr(entity, 'left', False):
                print(f'Berhasil keluar dari channel: {entity.title}')
            else:
                print(f'Keluar channel: {entity.title}')
                try:
                    await client(LeaveChannelRequest(channel=InputPeerChannel(entity.id, entity.access_hash)))
                except Exception as e:
                    print(f'Error keluar channel: {e}')

            print(f'hapus chat history in channel: {entity.title}')
            try:
                await client(DeleteHistoryRequest(peer=InputPeerChannel(entity.id, entity.access_hash), max_id=0, just_clear=False, revoke=True))
            except Exception as e:
                print(f'Error hapus chat history: {e}')

        elif dialog.is_group:
            if getattr(entity, 'left', False):
                print(f'Sudah pergi keluar group: {entity.title}')
            else:
                print(f'keluwar group: {entity.title}')
                try:
                    await client(LeaveChannelRequest(channel=InputPeerChat(entity.id)))
                except Exception as e:
                    print(f'Error keluar group: {e}')

            print(f'Menghapus riwayat obrolan di grup: {entity.title}')
            try:
                await client(DeleteHistoryRequest(peer=InputPeerChat(entity.id), max_id=0, just_clear=False, revoke=True))
            except Exception as e:
                print(f'Error menghapus riwayat obrolan di grup: {e}')

        elif dialog.is_user:
            print(f'Menghapus riwayat obrolan dengan pengguna: {entity.username or entity.phone}')
            try:
                await client(DeleteHistoryRequest(peer=InputPeerUser(entity.id, entity.access_hash), max_id=0, just_clear=False, revoke=True))
            except Exception as e:
                print(f'Error menghapus riwayat obrolan dengan pengguna: {e}')

with client:
    client.loop.run_until_complete(main())
