from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.http import JsonResponse

# Create your views here.

def retrieve_bird_api(request):
    api_url = 'https://nuthatch.lastelm.software/v2/birds?page=1&pageSize=100&operator=AND'  # Replace with your API endpoint
    api_key = 'd3c3568f-febc-449d-b5a5-55267be7bb0c'  # Replace with your actual API key

    headers = {
        'accept': 'application/json',
        'API-Key': api_key  # Set the API key in the header as per the curl example
    }

    try:
        # Make the API call
        response = requests.get(api_url, headers=headers)

        # Check if the request was successful
        response.raise_for_status()

        # Parse the response as JSON
        data = response.json()

        if response.status_code == 200:
            data = response.json()  # Parse the JSON response
            birds = data.get('entities', [])  # Get the list of birds
        else:
            birds = []  # Handle the case when the request fails

    # Pass the birds data to the template
        return render(request, 'core/birds.html', {'birds': birds})

        # Return the data as a Django JsonResponse
        return JsonResponse(data, safe=False)

    except requests.exceptions.HTTPError as err:
        return JsonResponse({'error': 'HTTP Error', 'message': str(err)}, status=response.status_code)
    except requests.exceptions.ConnectionError as err:
        return JsonResponse({'error': 'Connection Error', 'message': str(err)}, status=500)
    except requests.exceptions.Timeout as err:
        return JsonResponse({'error': 'Timeout Error', 'message': str(err)}, status=504)
    except requests.exceptions.RequestException as err:
        return JsonResponse({'error': 'Something went wrong', 'message': str(err)}, status=500)