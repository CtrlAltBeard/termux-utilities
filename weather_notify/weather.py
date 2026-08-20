#!/usr/bin/env python3
import requests
import json
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

console = Console()

def interpret_weather_code(code):
    """Convert WMO weather codes to human-readable descriptions"""
    weather_codes = {
        0: "☀️ Clear sky",
        1: "🌤️ Mainly clear",
        2: "⛅ Partly cloudy",
        3: "☁️ Overcast",
        45: "🌫️ Foggy",
        48: "🌫️ Depositing rime fog",
        51: "🌦️ Light drizzle",
        53: "🌧️ Moderate drizzle",
        55: "🌧️ Dense drizzle",
        61: "🌧️ Slight rain",
        63: "🌧️ Moderate rain",
        65: "⛈️ Heavy rain",
        71: "❄️ Slight snow",
        73: "❄️ Moderate snow",
        75: "❄️ Heavy snow",
        77: "❄️ Snow grains",
        80: "🌧️ Slight rain showers",
        81: "🌧️ Moderate rain showers",
        82: "⛈️ Violent rain showers",
        85: "❄️ Slight snow showers",
        86: "❄️ Heavy snow showers",
        95: "⛈️ Thunderstorm",
        96: "⛈️ Thunderstorm with slight hail",
        99: "⛈️ Thunderstorm with heavy hail",
    }
    return weather_codes.get(code, f"Unknown (code: {code})")

def get_temp_color(temp):
    """Return color based on temperature"""
    if temp < -5:
        return "blue"
    elif temp < 5:
        return "cyan"
    elif temp < 15:
        return "green"
    elif temp < 25:
        return "yellow"
    else:
        return "red"

def get_wind_direction(degrees):
    """Convert wind degrees to compass direction"""
    directions = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
                 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
    index = round(degrees / 22.5) % 16
    return directions[index]

def get_uv_color(uv):
    """Return color based on UV index"""
    if uv < 3:
        return "green"
    elif uv < 6:
        return "yellow"
    elif uv < 8:
        return "orange"
    else:
        return "red"

def get_weather(city):
    try:
        # Using Open-Meteo API (free, no API key needed)
        geo_url = "https://geocoding-api.open-meteo.com/v1/search"
        params = {"name": city, "count": 1, "language": "en", "format": "json"}

        # Get city coordinates
        geo_response = requests.get(geo_url, params=params)
        geo_data = geo_response.json()

        if not geo_data.get('results'):
            console.print(f"[red]❌ City '{city}' not found.Try again![/red]")
            return

        city_info = geo_data['results'][0]
        latitude = city_info['latitude']
        longitude = city_info['longitude']
        city_name = city_info['name']
        country = city_info.get('country', 'Unknown')
        admin1 = city_info.get('admin1', '')

        # Get detailed weather data
        weather_url = "https://api.open-meteo.com/v1/forecast"
        weather_params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,weathercode,windspeed_10m,wind_direction_10m,pressure_msl,cloud_cover,visibility",
            "daily": "weathercode,temperature_2m_max,temperature_2m_min,precipitation_sum,windspeed_10m_max,uv_index_max",
            "timezone": "auto"
        }

        weather_response = requests.get(weather_url, params=weather_params)
        weather_data = weather_response.json()

        # Extract current weather
        current = weather_data['current']
        current_time = datetime.fromisoformat(current['time'])
        current_temp = current['temperature_2m']
        current_feels_like = current['apparent_temperature']
        current_humidity = current['relative_humidity_2m']
        current_wind = current['windspeed_10m']
        current_wind_dir = current['wind_direction_10m']
        current_code = current['weathercode']
        current_pressure = current['pressure_msl']
        current_cloud = current['cloud_cover']
        current_visibility = current['visibility']
        current_precip = current['precipitation']

        # Extract tomorrow's forecast (index 1)
        daily = weather_data['daily']
        tomorrow_date = daily['time'][1]
        tomorrow_temp_max = daily['temperature_2m_max'][1]
        tomorrow_temp_min = daily['temperature_2m_min'][1]
        tomorrow_wind = daily['windspeed_10m_max'][1]
        tomorrow_code = daily['weathercode'][1]
        tomorrow_precip = daily['precipitation_sum'][1]
        tomorrow_uv = daily['uv_index_max'][1]

        wind_dir = get_wind_direction(current_wind_dir)
        visibility_km = current_visibility / 1000 if current_visibility else 0
        temp_color = get_temp_color(current_temp)
        uv_color = get_uv_color(tomorrow_uv)

        # ═══════════════════════════════════════════════════════════
        # LOCATION HEADER
        # ═══════════════════════════════════════════════════════════
        location_text = Text()
        location_text.append("📍 ", style="bold cyan")
        location_text.append(f"{city_name}", style="bold white")
        location_text.append(f", {admin1}", style="dim")
        location_text.append(f"\n   {country}", style="dim cyan")
        location_text.append(f" • {latitude:.2f}°, {longitude:.2f}°", style="dim")

        console.print()
        console.print(Panel(location_text, border_style="cyan", expand=False))

        # ═══════════════════════════════════════════════════════════
        # CURRENT WEATHER TABLE
        # ═══════════════════════════════════════════════════════════
        current_table = Table(title="🌡️  CURRENT WEATHER", title_style="bold yellow")
        current_table.add_column("Metric", style="cyan", width=20)
        current_table.add_column("Value", style="white")

        current_table.add_row("Condition", interpret_weather_code(current_code))

        temp_text = Text(f"{current_temp}°C", style=temp_color)
        current_table.add_row("Temperature", temp_text)

        feels_text = Text(f"{current_feels_like}°C", style=temp_color)
        current_table.add_row("Feels Like", feels_text)

        humidity_text = Text(f"{current_humidity}%", style="blue")
        current_table.add_row("Humidity", humidity_text)

        wind_text = Text(f"{current_wind} km/h {wind_dir} 🧭", style="green")
        current_table.add_row("Wind", wind_text)

        current_table.add_row("Pressure", f"{current_pressure} hPa")
        current_table.add_row("Cloud Cover", f"{current_cloud}%")
        current_table.add_row("Visibility", f"{visibility_km:.1f} km")

        if current_precip > 0:
            precip_text = Text(f"{current_precip} mm", style="blue")
            current_table.add_row("Precipitation", precip_text)

        current_table.add_row("Time", f"[dim]{current_time.strftime('%H:%M')}[/dim]")

        console.print(current_table)

        # ═══════════════════════════════════════════════════════════
        # TOMORROW'S FORECAST TABLE
        # ═══════════════════════════════════════════════════════════
        tomorrow_table = Table(title=f"📅 TOMORROW'S FORECAST ({tomorrow_date})", title_style="bold yellow")
        tomorrow_table.add_column("Metric", style="cyan", width=20)
        tomorrow_table.add_column("Value", style="white")

        tomorrow_table.add_row("Condition", interpret_weather_code(tomorrow_code))

        tomorrow_high_text = Text(f"{tomorrow_temp_max}°C", style=get_temp_color(tomorrow_temp_max))
        tomorrow_low_text = Text(f"{tomorrow_temp_min}°C", style=get_temp_color(tomorrow_temp_min))
        tomorrow_table.add_row("High / Low", f"{tomorrow_high_text} / {tomorrow_low_text}")

        tomorrow_wind_text = Text(f"{tomorrow_wind} km/h", style="green")
        tomorrow_table.add_row("Max Wind", tomorrow_wind_text)

        if tomorrow_precip > 0:
            tomorrow_precip_text = Text(f"{tomorrow_precip} mm", style="blue")
            tomorrow_table.add_row("Precipitation", tomorrow_precip_text)

        uv_text = Text(f"{tomorrow_uv}", style=uv_color)
        tomorrow_table.add_row("UV Index", uv_text)

        console.print(tomorrow_table)
        console.print()

    except requests.exceptions.RequestException as e:
        console.print(f"[red]❌ Error fetching weather data: {e}[/red]")
    except KeyError as e:
        console.print(f"[red]❌ Error parsing weather data: {e}[/red]")

if __name__ == "__main__":
    city_input = console.input("[bold cyan]Enter city name: [/bold cyan]")
    get_weather(city_input)
