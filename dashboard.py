import tkinter as tk
from tkinter import ttk
import json
import asyncio
import websockets
import threading

class Dashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Device Monitoring Dashboard")
        self.geometry("800x600")  

        self.filter_frame = tk.Frame(self)
        self.filter_frame.pack(fill=tk.BOTH, expand=False)

        self.status_label = tk.Label(self.filter_frame, text="Filter by Status:")
        self.status_label.pack(side=tk.LEFT, padx=10)
        
        self.status_combobox = ttk.Combobox(self.filter_frame, values=["All", "Online", "Offline"])
        self.status_combobox.set("All")
        self.status_combobox.pack(side=tk.LEFT, padx=10)
        
        self.filter_button = tk.Button(self.filter_frame, text="Filter", command=self.filter_devices)
        self.filter_button.pack(side=tk.LEFT, padx=10)
        
        self.device_frame = tk.Frame(self)
        self.device_frame.pack(fill=tk.BOTH, expand=True)

        self.device_listbox = tk.Listbox(self.device_frame, selectmode=tk.SINGLE)
        self.device_listbox.pack(fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.device_frame, orient=tk.VERTICAL)
        self.device_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.device_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.device_count_label = tk.Label(self)
        self.device_count_label.pack(pady=10)

        self.devices = []  

        self.websocket_thread = threading.Thread(target=self.start_websocket)
        self.websocket_thread.daemon = True
        self.websocket_thread.start()

    def start_websocket(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            loop.run_until_complete(self.websocket_handler())
        except websockets.exceptions.WebSocketException as e:
            self.handle_websocket_error(str(e))

    async def websocket_handler(self):
        try:
            async with websockets.connect('ws://localhost:8000/ws/devices/') as websocket:
                await websocket.send(json.dumps({'action': 'get_devices'}))
                while True:
                    response = await websocket.recv()
                    devices = json.loads(response)
                    self.devices.append(devices)
                    self.display_devices()
        except websockets.exceptions.WebSocketException as e:
            self.handle_websocket_error(str(e))
            
    def handle_websocket_error(self, error_message):
        print(f"WebSocket Error: {error_message}")

    def filter_devices(self):
        selected_status = self.status_combobox.get()
        if selected_status == "All":
            self.display_devices()
        else:
            filtered_devices = [device for device in self.devices if device['status'] == selected_status]
            self.display_devices(filtered_devices)

    def display_devices(self, devices=None):
        self.device_listbox.delete(0, tk.END)
        devices_to_display = devices or self.devices
        for device in devices_to_display:
            device_name = device['device_name']
            status = device['status']
            last_update_time = device['last_update_time']
            device_info = f"Device Name: {device_name}, Status: {status}, Last Update Time: {last_update_time}"
            self.device_listbox.insert(tk.END, device_info)

       
        device_count = len(devices_to_display)
        self.device_count_label.config(text=f"Total Devices: {device_count}")

if __name__ == "__main__":
    dashboard = Dashboard()
    dashboard.mainloop()
