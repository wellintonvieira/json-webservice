import random
from django.http import JsonResponse

def random_numbers(request):
	if request.method == "GET":
		numbers = random.sample(range(1, 60), 6)
		numbers.sort()
		return JsonResponse({"key": numbers})
		