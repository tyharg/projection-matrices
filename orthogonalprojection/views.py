from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import numberForm

import numpy as np
import fractions


page_name = 'Orthogonal Projection Matrix Calculator '
section = ' - Linear Algebra'



def get_digits(request):

	if request.method == 'POST':
	
		
		form = numberForm(request.POST)

		if form.is_valid():
		
			try:
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
				print(AAtAIAt)
				
				row = int(m)
				
				valid_output = True
				
				
				return render(request, 'orthproj_output.html', {
				'num_array': num_array,
				'out': out,
				'row': row,
				'table': AAtAIAt,
				'page_name': page_name,
				'section': section,
				'valid_output': valid_output,
				})
				
				
			except:
				valid_output = False
				out = 'Something went wrong'

				return render(request, 'orthproj_output.html', {
				'out': out,
				'valid_output': valid_output,
				})
				
		else:
			valid_output = False
			out = 'Something went wrong'
			return render(request, 'orthproj_output.html', {
			'out': out,
			'valid_output': valid_output,
			})
			
			
	else:
		form = numberForm()

		return render(request, 'orthproj.html', {
		'page_name': page_name,
		'section': section,
		'form': form,
		
		

		
		
		})