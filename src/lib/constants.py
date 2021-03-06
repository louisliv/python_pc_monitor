CONSTANTS ={
    "buttons": [
        {
            "name": "connect",
            "title": "Connect",
            "method": "handle_connect",
            "toggle": True
        },
        {
            "name": "save_config",
            "title": "Save Configuration",
            "method": "handle_set_config",
            "toggle": False
        }
    ],
    "text_fields_sections": [
        {
            "title": "General Settings",
            "text_fields": [
                {
                    "id": "refresh", 
                    "label": "Refresh Data Interval (Millis)"
                }
            ]
        },
        {
            "title": "Server Connection",
            "text_fields": [
                {
                    "id": "ip", 
                    "label": "IP"
                },
                {
                    "id": "port", 
                    "label": "Port"
                }
            ]
        },
        {
            "title": "Open Hardware Monitor Name Settings",
            "text_fields": [
                {
                    "id": "cpu_load", 
                    "label": "CPU Load (%)"
                },
                {
                    "id": "cpu_fan", 
                    "label": "CPU Fan (RPM)"
                },
                {
                    "id": "gpu_load", 
                    "label": "GPU Load (%)"
                },
                {
                    "id": "gpu_fan", 
                    "label": "GPU Fan (RPM)"
                },
                {
                    "id": "gpu_temp", 
                    "label": "GPU Temperature (C)"
                },
                {
                    "id": "cpu_temp", 
                    "label": "CPU Temperature (C)"
                },
                {
                    "id": "total_vram", 
                    "label": "Total VRAM (MB)"
                },
                {
                    "id": "used_vram", 
                    "label": "Used VRAM (MB)"
                },
                {
                    "id": "available_ram", 
                    "label": "Available RAM (GB)"
                },
                {
                    "id": "used_ram", 
                    "label": "Used RAM (GB)"
                }
            ]
        }
    ]
}