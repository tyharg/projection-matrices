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
				m = form.cleaned_data['rows']
				n = form.cleaned_data['cols']

				num_array = list(numbers)
				
				A = np.matrix(num_array)
				A = A.reshape(int(m),int(n))

				#Calculate projection matrix step by step, plan to add show-work feature.
				At = A.getT()
				AtA = np.matmul(At,A)
				AtAi = AtA.getI()
				AAtAI = np.matmul(A, AtAi)
				AAtAIAt = np.matmul(AAtAI, At)
				
				#Matrix specifications
				P = AAtAIAt
				P_rows = P.shape[0]
				P_cols = P.shape[1]
				
				

				#Parallel arrays hold numerator and denominators
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
				
				#Zip arrays for template rendering
				P_zip = zip(P_numr, P_dnmr) 


				#Valid output response
				valid_output = True
				print(P)
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

			#Invalid output response: something went wrong within the calculation
			except:
				out = ' Perhaps your matrix rows are linearly dependent?'
				
				valid_output = False
				return render(request, 'orthproj_output.html', {
				'page_name': page_name,
				'section': section,
				'out': out,
				'valid_output': valid_output,
				})
		#Invalid output: something went wrong before the calculation
		else:
			valid_output = False
			out = ' Check your matrix input values.'
			
			return render(request, 'orthproj_output.html', {
				'page_name': page_name,
				'section': section,
				'out': out,
				'valid_output': valid_output,
				})
			
	#Render form
	else:
		form = numberForm()

		return render(request, 'orthproj.html', {
		'page_name': page_name,
		'section': section,
		'form': form,
		
		

		
		
		})
