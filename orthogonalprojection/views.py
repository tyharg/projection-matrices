from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import numberForm

import numpy as np
import fractions

np.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})

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
				
				P = AAtAIAt
				P_rows = P.shape[0]
				P_cols = P.shape[1]
				
				

				
				P_list = [None]*(P_rows * P_cols)
				P_numr = [None]*(P_rows * P_cols)
				P_dnmr = [None]*(P_rows * P_cols)


				counter = 0
				for i in range(P_rows):
					for j in range(P_cols):
						P_list[counter] = (fractions.Fraction(P[i,j]).limit_denominator())
						P_numr[counter] = P_list[counter].numerator
						P_dnmr[counter] = P_list[counter].denominator
						counter += 1
						
				P_list = None
				
				P_zip = zip(P_numr, P_dnmr) 


				print(AAtAIAt)

				
				valid_output = True
				
				
				return render(request, 'orthproj_output.html', {
				'P_rows': P_rows,
				'P_cols': P_cols,
				'P_numr': P_numr,
				'P_dnmr': P_dnmr,
				'P_zip': P_zip,
				'table': P,
				'page_name': page_name,
				'section': section,
				'valid_output': valid_output,
				})
				
				
			except:
				valid_output = False
				out = ' Perhaps your matrix is linearly dependent?'

				return render(request, 'orthproj_output.html', {
				'page_name': page_name,
				'section': section,
				'out': out,
				'valid_output': valid_output,
				})
				
		else:
			valid_output = False
			out = ' Check your matrix input values.'
			
			return render(request, 'orthproj_output.html', {
				'page_name': page_name,
				'section': section,
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