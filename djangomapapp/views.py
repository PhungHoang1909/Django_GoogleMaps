from django.shortcuts import render

def map_view(request):
    marker_data = [
        {'name': 'Location 1', 'lat': 10.808883, 'lng': 106.685039},
        {'name': 'Location 2', 'lat': 10.807669, 'lng': 106.691269},
        {'name': 'Location 3', 'lat': 10.779168, 'lng': 106.673643},
        {'name': 'Location 4', 'lat': 10.795280, 'lng': 106.735505},
        {'name': 'Location 5', 'lat': 10.804531, 'lng': 106.672297},
        # Add more marker data as needed
    ]
    return render(request, 'map.html', {'marker_data': marker_data})
