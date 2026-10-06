import flet as ft
import requests

# Set your deployed Vercel URL here
API_URL = "http://127.0.0.1:5000/get-location"  # Change to Vercel URL after deployment

def main(page: ft.Page):
    page.title = "GPS Location Finder"
    page.window_width = 400
    page.window_height = 500
    page.padding = 20

    lat_input = ft.TextField(label="Latitude", placeholder="e.g. 6.9271")
    lon_input = ft.TextField(label="Longitude", placeholder="e.g. 79.8612")
    result_text = ft.Text(size=16, weight=ft.FontWeight.BOLD)

    def fetch_address(e):
        lat = lat_input.value
        lon = lon_input.value

        if not lat or not lon:
            result_text.value = "Please enter both Latitude and Longitude."
            page.update()
            return

        result_text.value = "Fetching address..."
        page.update()

        try:
            response = requests.post(
                API_URL,
                json={"latitude": float(lat), "longitude": float(lon)}
            )
            data = response.json()

            if "address" in data:
                result_text.value = f"Address:\n{data['address']}"
            else:
                result_text.value = f"Error: {data.get('error', 'Unknown error')}"
        except Exception as err:
            result_text.value = f"Failed to reach server: {err}"

        page.update()

    submit_btn = ft.ElevatedButton("Get Location Name", on_click=fetch_address)

    page.add(
        ft.Text("GPS to Address Converter", size=20, weight=ft.FontWeight.BOLD),
        lat_input,
        lon_input,
        submit_btn,
        ft.Divider(),
        result_text
    )

ft.app(target=main)