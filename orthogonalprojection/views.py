from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import numberForm

import numpy as np
import fractions
import djfractions




	

def get_digits(request):
	out = None
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = numberForm(request.POST)
		# check whether it's valid:
		if form.is_valid():

			
			
			numbers = form.cleaned_data['numbers']

			

			print(form.cleaned_data['rows'])
			print(form.cleaned_data['cols'])
			
			m = form.cleaned_data['rows']
			n = form.cleaned_data['cols']
			
			totalvals = m * n

			num_array = list(numbers)
			
			
			A = np.matrix(num_array)
			A = A.reshape(int(m),int(n))

			At = A.getT()
			AtA = np.matmul(At,A)
			AtAi = AtA.getI()
			AAtAI = np.matmul(A, AtAi)
			AAtAIAt = np.matmul(AAtAI, At)
			
			out = AAtAIAt.tolist()
			
			np.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})
			print(out)
			
			row = int(m)
			
			
			
			return render(request, 'orthproj.html', {
			'num_array': num_array,
			'out': out,
			'row': row,
			'table': AAtAIAt
			
			})
			
			
	else:
		form = numberForm()

		return render(request, 'orthproj.html', {'form': form})