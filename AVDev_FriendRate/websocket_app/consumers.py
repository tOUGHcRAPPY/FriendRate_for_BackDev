import asyncio

import pyaudio
from channels.generic.websocket import AsyncWebsocketConsumer

active_clients = []


class AudioSenderConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.microphone_enabled = True

    async def connect(self):
        self.user = self.scope["user"]
        if self.user.is_authenticated:
            await self.accept()
        else:
            await self.close()

    async def disconnect(self, close_code):
        if self.user.id in active_clients:
            active_clients.remove(self.user.id)

    async def receive(self, text_data):
        if text_data == "mute":
            self.microphone_enabled = False
        elif text_data == "unmute":
            self.microphone_enabled = True
        else:
            # Здесь можно обрабатывать другие данные или команды
            pass

        # Здесь будет код для обработки и отправки аудио-данных с учетом состояния микрофона
        if self.microphone_enabled:
            await self.send_audio_data()  # Отправка аудио, если микрофон включен
        else:
            pass  # Микрофон отключен, пропускаем запись и отправку аудио

    async def send_audio_data(self):
        # Это примерный код, который отправляет аудио-данные по WebSocket соединению
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16,
                        channels=1,
                        rate=44100,
                        input=True,
                        frames_per_buffer=1024)

        while True:
            if not self.microphone_enabled:
                break

            data = stream.read(1024)
            await self.send(data)

        stream.stop_stream()
        stream.close()
        p.terminate()


class AudioReceiverConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        if self.user.is_authenticated:
            await self.accept()
        else:
            await self.close()

    async def disconnect(self, close_code):
        if self.user.id in active_clients:
            active_clients.remove(self.user.id)

    async def receive(self, text_data):
        pass  # Здесь будет код для обработки и воспроизведения аудио-данных
